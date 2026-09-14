import json
import unittest
from pathlib import Path

from tools.channel_economics import evaluate, evaluate_batch


FIXTURE = Path(__file__).parents[1] / "fixtures" / "economics" / "channel-scenarios.sample.json"
FIELDS = [
    "net_customer_revenue", "ingredient_cost", "packaging", "labour",
    "payment_processing", "channel_commission", "business_funded_delivery",
    "discounts_promotions", "refunds_cancellations", "variable_waste", "acquisition_cost"
]


def verified_scenario(scenario_id, values):
    return {
        "scenario_id": scenario_id,
        "inputs": {name: {"value": value, "evidence": "VERIFIED_PROJECT"} for name, value in zip(FIELDS, values)},
    }


class ChannelEconomicsTests(unittest.TestCase):
    def load_scenarios(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        return {scenario["scenario_id"]: scenario for scenario in payload["scenarios"]}

    def test_public_reference_and_hypothesis_never_produce_commercial_pass(self):
        scenarios = self.load_scenarios()
        for scenario_id in (
            "marketplace-base-hypothesis",
            "marketplace-high-commission-hypothesis",
            "direct-order-base-hypothesis",
            "direct-order-no-paid-acquisition-hypothesis",
        ):
            result = evaluate(scenarios[scenario_id])
            self.assertEqual(result["status"], "CALCULATED")
            self.assertEqual(result["decision_state"], "DECISION_SUPPORT_ONLY")
            self.assertFalse(result["commercial_pass_eligible"])

    def test_unknown_required_input_is_not_testable(self):
        scenarios = self.load_scenarios()
        result = evaluate(scenarios["unknown-delivery-not-testable"])
        self.assertEqual(result["status"], "NOT_TESTABLE")
        self.assertIn("business_funded_delivery", result["missing_or_unknown"])
        self.assertFalse(result["commercial_pass_eligible"])

    def test_multiple_unknowns_report_deterministically(self):
        scenario = verified_scenario("multiple-unknowns", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["inputs"]["packaging"] = {"value": None, "evidence": "UNKNOWN"}
        scenario["inputs"]["labour"] = {"value": None, "evidence": "UNKNOWN"}
        result = evaluate(scenario)
        self.assertEqual(result["status"], "NOT_TESTABLE")
        self.assertEqual(result["missing_or_unknown"], ["labour", "packaging"])
        self.assertFalse(result["commercial_pass_eligible"])

    def test_invalid_evidence_class_fails_closed(self):
        scenario = verified_scenario("invalid-evidence", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["inputs"]["packaging"]["evidence"] = "ASSUMED_VERIFIED"
        with self.assertRaisesRegex(ValueError, "invalid evidence class"):
            evaluate(scenario)

    def test_unknown_nested_input_keys_fail_closed(self):
        scenario = verified_scenario("nested-override", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["inputs"]["packaging"]["commercial_override"] = True
        with self.assertRaisesRegex(ValueError, "unknown keys for packaging"):
            evaluate(scenario)

        scenario = verified_scenario("nested-note", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["inputs"]["labour"]["annotation"] = "treat as verified"
        with self.assertRaisesRegex(ValueError, "unknown keys for labour"):
            evaluate(scenario)

    def test_zero_revenue_verified_scenario_never_passes(self):
        scenario = verified_scenario("zero-revenue", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        result = evaluate(scenario)
        self.assertEqual(result["contribution_per_order"], "0.00")
        self.assertIsNone(result["contribution_margin_percent"])
        self.assertFalse(result["commercial_pass_eligible"])

    def test_negative_revenue_is_rejected(self):
        scenario = verified_scenario("negative-revenue", [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        with self.assertRaisesRegex(ValueError, "negative net_customer_revenue is not allowed"):
            evaluate(scenario)

    def test_non_finite_numeric_values_are_rejected(self):
        for label, value in (("nan", "NaN"), ("positive-infinity", "Infinity"), ("negative-infinity", "-Infinity")):
            with self.subTest(label=label):
                scenario = verified_scenario(label, [40, 10, value, 5, 1, 0, 5, 0, 0, 0, 2])
                with self.assertRaisesRegex(ValueError, "non-finite numeric value for packaging"):
                    evaluate(scenario)

    def test_rounding_boundary_is_deterministic(self):
        scenario = verified_scenario("rounding-boundary", [10.005, 10.004, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        first = evaluate(scenario)
        second = evaluate(scenario)
        self.assertEqual(first, second)
        self.assertEqual(first["contribution_per_order"], "0.01")
        self.assertEqual(first["contribution_margin_percent"], "0.10")
        self.assertTrue(first["commercial_pass_eligible"])

    def test_all_verified_positive_scenario_can_be_eligible(self):
        scenario = verified_scenario("verified-positive", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        result = evaluate(scenario)
        self.assertEqual(result["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertTrue(result["commercial_pass_eligible"])

    def test_all_verified_negative_scenario_cannot_pass(self):
        scenario = verified_scenario("verified-negative", [20, 10, 2, 6, 1, 3, 4, 0, 0, 0, 1])
        result = evaluate(scenario)
        self.assertLess(float(result["contribution_per_order"]), 0)
        self.assertEqual(result["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertFalse(result["commercial_pass_eligible"])

    def test_duplicate_or_missing_scenario_id_fails_closed(self):
        one = verified_scenario("same", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        two = verified_scenario("same", [41, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        with self.assertRaisesRegex(ValueError, "duplicate scenario_id"):
            evaluate_batch({"scenarios": [one, two]})
        one["scenario_id"] = ""
        with self.assertRaisesRegex(ValueError, "scenario_id is required"):
            evaluate_batch({"scenarios": [one]})

    def test_non_numeric_required_value_identifies_field(self):
        scenario = verified_scenario("bad-number", [40, 10, "abc", 5, 1, 0, 5, 0, 0, 0, 2])
        with self.assertRaisesRegex(ValueError, "invalid numeric value for packaging"):
            evaluate(scenario)

    def test_negative_cost_is_rejected(self):
        scenario = verified_scenario("negative-cost", [40, 10, -1, 5, 1, 0, 5, 0, 0, 0, 2])
        with self.assertRaisesRegex(ValueError, "negative cost input is not allowed for packaging"):
            evaluate(scenario)

    def test_unknown_input_or_scenario_keys_fail_closed(self):
        scenario = verified_scenario("unknown-input", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["inputs"]["mystery_cost"] = {"value": 0, "evidence": "VERIFIED_PROJECT"}
        with self.assertRaisesRegex(ValueError, "unknown economics input keys"):
            evaluate(scenario)
        scenario = verified_scenario("unknown-scenario-key", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        scenario["commercial_override"] = True
        with self.assertRaisesRegex(ValueError, "unknown scenario keys"):
            evaluate(scenario)

    def test_unknown_batch_keys_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "unknown batch keys"):
            evaluate_batch({"scenarios": [], "commercial_override": True})

    def test_empty_batch_is_explicit_and_non_commercial(self):
        result = evaluate_batch({"scenarios": []})
        self.assertEqual(result, {"status": "EMPTY", "commercial_pass_eligible": False, "results": []})

    def test_batch_output_is_sorted_by_scenario_id_and_deterministic(self):
        b = verified_scenario("b-case", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        a = verified_scenario("a-case", [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2])
        first = evaluate_batch({"scenarios": [b, a]})
        reordered_inputs = {k: a["inputs"][k] for k in reversed(list(a["inputs"]))}
        a_reordered = {"scenario_id": "a-case", "inputs": reordered_inputs}
        second = evaluate_batch({"scenarios": [a_reordered, b]})
        self.assertEqual([item["scenario_id"] for item in first["results"]], ["a-case", "b-case"])
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
