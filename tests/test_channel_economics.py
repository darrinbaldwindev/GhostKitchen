import copy
import json
import unittest
from pathlib import Path

from tools.channel_economics import evaluate


FIXTURE = Path(__file__).parents[1] / "fixtures" / "economics" / "channel-scenarios.sample.json"


class ChannelEconomicsTests(unittest.TestCase):
    def load_scenarios(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        return {scenario["scenario_id"]: scenario for scenario in payload["scenarios"]}

    def verified_scenario(self, scenario_id="verified-menu-scenario"):
        values = {
            "net_customer_revenue": 40,
            "ingredient_cost": 10,
            "packaging": 1,
            "labour": 5,
            "payment_processing": 1,
            "channel_commission": 0,
            "business_funded_delivery": 5,
            "discounts_promotions": 0,
            "refunds_cancellations": 0,
            "variable_waste": 0,
            "acquisition_cost": 2,
        }
        return {
            "scenario_id": scenario_id,
            "inputs": {name: {"value": value, "evidence": "VERIFIED_PROJECT"} for name, value in values.items()},
        }

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

    def test_packaging_or_labour_unknown_remains_not_testable(self):
        for field in ("packaging", "labour"):
            scenario = self.verified_scenario(f"unknown-{field}")
            scenario["inputs"][field] = {"value": None, "evidence": "UNKNOWN"}
            result = evaluate(scenario)
            self.assertEqual(result["status"], "NOT_TESTABLE")
            self.assertIn(field, result["missing_or_unknown"])
            self.assertFalse(result["commercial_pass_eligible"])

    def test_all_verified_positive_scenario_can_be_eligible(self):
        result = evaluate(self.verified_scenario())
        self.assertEqual(result["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertTrue(result["commercial_pass_eligible"])

    def test_verified_negative_contribution_never_becomes_commercial_pass(self):
        scenario = self.verified_scenario("verified-negative")
        scenario["inputs"]["ingredient_cost"]["value"] = 45
        result = evaluate(scenario)
        self.assertEqual(result["status"], "CALCULATED")
        self.assertEqual(result["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertLess(float(result["contribution_per_order"]), 0)
        self.assertFalse(result["commercial_pass_eligible"])


if __name__ == "__main__":
    unittest.main()
