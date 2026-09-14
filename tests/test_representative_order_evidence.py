import copy
import json
import unittest
from pathlib import Path

from tools.representative_order_evidence import validate_record


FIXTURE = Path(__file__).parents[1] / "fixtures" / "evidence" / "representative-order-evidence.template.json"


class RepresentativeOrderEvidenceTests(unittest.TestCase):
    def load_template(self):
        return json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_template_is_valid_capture_only_and_not_handoff_ready(self):
        result = validate_record(self.load_template())
        self.assertEqual(result["status"], "RECORD_VALID")
        self.assertEqual(result["authority"], "EVIDENCE_CAPTURE_ONLY")
        self.assertFalse(result["commercial_pass_eligible"])
        self.assertFalse(result["economics_handoff_ready"])

    def test_authority_cannot_be_promoted(self):
        record = self.load_template()
        record["authority"] = "COMMERCIAL_APPROVAL"
        with self.assertRaisesRegex(ValueError, "authority"):
            validate_record(record)

    def test_commercial_pass_flag_must_remain_false(self):
        record = self.load_template()
        record["commercial_pass_eligible"] = True
        with self.assertRaisesRegex(ValueError, "commercial_pass_eligible"):
            validate_record(record)

    def test_unknown_top_level_keys_fail_closed(self):
        record = self.load_template()
        record["approved_by_ai"] = True
        with self.assertRaisesRegex(ValueError, "unknown top-level keys"):
            validate_record(record)

    def test_invalid_evidence_class_fails_closed(self):
        record = self.load_template()
        record["packaging"]["components"][0]["evidence"] = "TRUST_ME"
        with self.assertRaisesRegex(ValueError, "invalid evidence class"):
            validate_record(record)

    def test_verified_packaging_handoff_requires_verified_support(self):
        record = self.load_template()
        record["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 1.25,
            "evidence": "VERIFIED_PROJECT",
        }
        with self.assertRaisesRegex(ValueError, "verified packaging support"):
            validate_record(record)

    def test_verified_labour_handoff_requires_verified_support(self):
        record = self.load_template()
        record["economics_handoff"]["direct_labour_cost_per_order"] = {
            "value": 2.50,
            "evidence": "VERIFIED_PROJECT",
        }
        with self.assertRaisesRegex(ValueError, "verified labour support"):
            validate_record(record)

    def test_active_seconds_cannot_exceed_elapsed_seconds(self):
        record = self.load_template()
        observation = record["labour"]["observations"][0]
        observation["active_seconds"] = 61
        observation["elapsed_seconds"] = 60
        with self.assertRaisesRegex(ValueError, "active_seconds"):
            validate_record(record)

    def test_duplicate_hold_minutes_fail_closed(self):
        record = self.load_template()
        record["packaging"]["hold_tests"][1]["minutes"] = 20
        with self.assertRaisesRegex(ValueError, "duplicate hold test minutes"):
            validate_record(record)

    def test_fully_supported_record_can_be_handoff_ready_but_not_commercial_pass(self):
        record = self.load_template()
        record.update({
            "concept": "BURGERS_CHICKEN",
            "representative_order_id": "BG-001",
            "observation_date": "2026-09-14",
            "observer": "test-observer",
        })
        component = record["packaging"]["components"][0]
        component.update({
            "component": "burger_box",
            "sku_or_description": "observed-test-sku",
            "quantity_used": 1,
            "pack_quantity": 100,
            "purchase_or_quote_value": 25,
            "freight_treatment": "INCLUDED",
            "gst_treatment": "INCLUDED",
            "source": "project invoice fixture",
            "source_date": "2026-09-14",
            "evidence": "VERIFIED_PROJECT",
        })
        observation = record["labour"]["observations"][0]
        observation.update({
            "task": "assemble and pack",
            "category": "PACKAGING_QA",
            "active_seconds": 90,
            "elapsed_seconds": 120,
            "concurrent_work": "NONE",
            "evidence": "VERIFIED_PROJECT",
        })
        record["labour"]["worker_count"] = 1
        record["labour"]["loaded_hourly_labour_rate"].update({
            "value": 30,
            "source": "project payroll fixture",
            "source_date": "2026-09-14",
            "scope": "loaded direct labour",
            "evidence": "VERIFIED_PROJECT",
        })
        record["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.25,
            "evidence": "VERIFIED_PROJECT",
        }
        record["economics_handoff"]["direct_labour_cost_per_order"] = {
            "value": 0.75,
            "evidence": "VERIFIED_PROJECT",
        }
        result = validate_record(record)
        self.assertTrue(result["economics_handoff_ready"])
        self.assertFalse(result["commercial_pass_eligible"])


if __name__ == "__main__":
    unittest.main()
