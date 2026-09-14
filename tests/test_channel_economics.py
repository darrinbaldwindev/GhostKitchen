import json
import unittest
from pathlib import Path

from tools.channel_economics import evaluate


FIXTURE = Path(__file__).parents[1] / "fixtures" / "economics" / "channel-scenarios.sample.json"


class ChannelEconomicsTests(unittest.TestCase):
    def test_public_reference_and_hypothesis_never_produce_commercial_pass(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        for scenario in payload["scenarios"][:2]:
            result = evaluate(scenario)
            self.assertEqual(result["status"], "CALCULATED")
            self.assertEqual(result["decision_state"], "DECISION_SUPPORT_ONLY")
            self.assertFalse(result["commercial_pass_eligible"])

    def test_unknown_required_input_is_not_testable(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        result = evaluate(payload["scenarios"][2])
        self.assertEqual(result["status"], "NOT_TESTABLE")
        self.assertIn("business_funded_delivery", result["missing_or_unknown"])
        self.assertFalse(result["commercial_pass_eligible"])

    def test_all_verified_positive_scenario_can_be_eligible(self):
        fields = [
            "net_customer_revenue", "ingredient_cost", "packaging", "labour",
            "payment_processing", "channel_commission", "business_funded_delivery",
            "discounts_promotions", "refunds_cancellations", "variable_waste", "acquisition_cost"
        ]
        values = [40, 10, 1, 5, 1, 0, 5, 0, 0, 0, 2]
        scenario = {
            "scenario_id": "verified-positive",
            "inputs": {name: {"value": value, "evidence": "VERIFIED_PROJECT"} for name, value in zip(fields, values)},
        }
        result = evaluate(scenario)
        self.assertEqual(result["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertTrue(result["commercial_pass_eligible"])


if __name__ == "__main__":
    unittest.main()
