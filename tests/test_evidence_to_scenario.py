import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evidence_to_scenario", ROOT / "tools" / "evidence_to_scenario.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)
bridge = module.bridge


def packet():
    p = json.loads((ROOT / "fixtures" / "evidence" / "representative-order-evidence.template.json").read_text())
    p.update({"concept": "test", "representative_order_id": "order-001", "observation_date": "2026-09-15", "observer": "tester"})
    p["packaging"]["configuration_id"] = "pack-001"
    p["packaging"]["components"][0].update({"component":"container","sku_or_description":"test","quantity_used":1,"pack_quantity":100,"purchase_or_quote_value":20,"freight_treatment":"included","gst_treatment":"included","source":"project","source_date":"2026-09-15","evidence":"VERIFIED_PROJECT"})
    p["packaging"]["pack_time_seconds"].update({"value":25,"source":"project","source_date":"2026-09-15","evidence":"VERIFIED_PROJECT"})
    for h in p["packaging"]["hold_tests"]:
        h.update({"leakage":"NONE","seal_integrity":"PASS","condensation":"LOW","temperature_observation":"recorded","texture_observation":"recorded","presentation":"PASS","overall_result":"PASS"})
    p["labour"]["worker_count"] = 1
    p["labour"]["observations"][0].update({"task":"pack","category":"PACKING","active_seconds":45,"elapsed_seconds":60,"concurrent_work":"NONE","abnormal_or_rework":False,"notes":"","evidence":"VERIFIED_PROJECT"})
    p["labour"]["loaded_hourly_labour_rate"].update({"value":35,"source":"project","source_date":"2026-09-15","scope":"loaded","evidence":"VERIFIED_PROJECT"})
    return p


def request(evidence="HYPOTHESIS"):
    values = {"net_customer_revenue":30,"ingredient_cost":8,"payment_processing":1,"channel_commission":5,"business_funded_delivery":2,"discounts_promotions":1,"refunds_cancellations":0.5,"variable_waste":0.5,"acquisition_cost":2}
    return {"scenario_id":"order-001-direct", "inputs":{k:{"value":v,"evidence":evidence} for k,v in values.items()}}


class EvidenceToScenarioTests(unittest.TestCase):
    def test_end_to_end_uses_derived_packaging_and_labour(self):
        result = bridge(packet(), request())
        self.assertEqual(result["scenario"]["inputs"]["packaging"], {"value":"0.20","evidence":"VERIFIED_PROJECT"})
        self.assertEqual(result["scenario"]["inputs"]["labour"], {"value":"0.44","evidence":"VERIFIED_PROJECT"})
        self.assertEqual(result["calculator_result"]["status"], "CALCULATED")
        self.assertEqual(result["calculator_result"]["decision_state"], "DECISION_SUPPORT_ONLY")
        self.assertFalse(result["commercial_pass_eligible"])
        self.assertEqual(result["correlation"]["representative_order_id"], "order-001")

    def test_caller_cannot_override_derived_fields(self):
        r = request()
        r["inputs"]["packaging"] = {"value":0,"evidence":"VERIFIED_PROJECT"}
        with self.assertRaisesRegex(ValueError, "cannot be supplied or overridden"):
            bridge(packet(), r)

    def test_unresolved_packaging_propagates_unknown_never_zero(self):
        p = packet()
        p["packaging"]["components"][0]["freight_treatment"] = "UNKNOWN"
        result = bridge(p, request())
        self.assertEqual(result["scenario"]["inputs"]["packaging"], {"value":None,"evidence":"UNKNOWN"})
        self.assertEqual(result["calculator_result"]["status"], "NOT_TESTABLE")
        self.assertIn("packaging", result["calculator_result"]["missing_or_unknown"])

    def test_weak_packaging_evidence_is_preserved(self):
        p = packet()
        p["packaging"]["components"][0]["evidence"] = "PUBLIC_REFERENCE"
        result = bridge(p, request())
        self.assertEqual(result["scenario"]["inputs"]["packaging"]["evidence"], "PUBLIC_REFERENCE")

    def test_missing_scenario_id_fails_closed(self):
        r = request()
        r["scenario_id"] = ""
        with self.assertRaisesRegex(ValueError, "scenario_id is required"):
            bridge(packet(), r)

    def test_all_verified_inputs_can_reach_canonical_calculator_but_bridge_never_grants_pass(self):
        result = bridge(packet(), request("VERIFIED_PROJECT"))
        self.assertTrue(result["calculator_result"]["commercial_pass_eligible"])
        self.assertEqual(result["calculator_result"]["decision_state"], "PROJECT_EVIDENCE_READY")
        self.assertFalse(result["commercial_pass_eligible"])


if __name__ == "__main__":
    unittest.main()
