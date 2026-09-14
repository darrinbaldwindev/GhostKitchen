import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evidence_packet", ROOT / "tools" / "evidence_packet.py")
evidence_packet = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(evidence_packet)
validate_packet = evidence_packet.validate_packet


def template_packet():
    return json.loads((ROOT / "fixtures" / "evidence" / "representative-order-evidence.template.json").read_text())


class EvidencePacketValidationTests(unittest.TestCase):
    def test_canonical_template_is_valid_but_incomplete_and_noncommercial(self):
        result = validate_packet(template_packet())
        self.assertEqual(result["authority"], "EVIDENCE_CAPTURE_ONLY")
        self.assertEqual(result["capture_state"], "CAPTURE_INCOMPLETE")
        self.assertFalse(result["commercial_pass_eligible"])
        self.assertGreater(result["evidence_counts"]["UNKNOWN"], 0)

    def test_commercial_pass_promotion_fails_closed(self):
        packet = template_packet()
        packet["commercial_pass_eligible"] = True
        with self.assertRaisesRegex(ValueError, "cannot be commercially pass eligible"):
            validate_packet(packet)

    def test_authority_override_fails_closed(self):
        packet = template_packet()
        packet["authority"] = "COMMERCIAL_APPROVAL"
        with self.assertRaisesRegex(ValueError, "EVIDENCE_CAPTURE_ONLY"):
            validate_packet(packet)

    def test_unknown_nested_key_fails_closed(self):
        packet = template_packet()
        packet["economics_handoff"]["packaging_cost_per_order"]["approved"] = True
        with self.assertRaisesRegex(ValueError, "unknown keys at economics_handoff.packaging_cost_per_order"):
            validate_packet(packet)

    def test_invalid_evidence_class_fails_closed(self):
        packet = template_packet()
        packet["packaging"]["components"][0]["evidence"] = "VERIFIED_BY_AI"
        with self.assertRaisesRegex(ValueError, "invalid evidence class"):
            validate_packet(packet)

    def test_non_finite_measurement_fails_closed(self):
        packet = template_packet()
        packet["packaging"]["pack_time_seconds"]["value"] = float("nan")
        with self.assertRaisesRegex(ValueError, "must be finite"):
            validate_packet(packet)

    def test_invalid_hold_test_set_fails_closed(self):
        packet = template_packet()
        packet["packaging"]["hold_tests"][2]["minutes"] = 30
        with self.assertRaisesRegex(ValueError, "exactly 20, 30 and 40"):
            validate_packet(packet)

    def test_active_labour_cannot_exceed_elapsed_time(self):
        packet = template_packet()
        packet["labour"]["observations"][0]["active_seconds"] = 61
        packet["labour"]["observations"][0]["elapsed_seconds"] = 60
        with self.assertRaisesRegex(ValueError, "cannot exceed elapsed_seconds"):
            validate_packet(packet)

    def test_complete_structure_still_requires_review_and_never_grants_commercial_pass(self):
        packet = template_packet()
        packet["representative_order_id"] = "order-001"
        packet["observation_date"] = "2026-09-14"
        packet["observer"] = "test-observer"
        component = packet["packaging"]["components"][0]
        component.update({
            "component": "container",
            "sku_or_description": "test container",
            "quantity_used": 1,
            "pack_quantity": 100,
            "purchase_or_quote_value": 20.0,
            "source": "project quote",
            "source_date": "2026-09-14",
            "evidence": "VERIFIED_PROJECT",
        })
        packet["packaging"]["pack_time_seconds"].update({
            "value": 25,
            "source": "timed observation",
            "source_date": "2026-09-14",
            "evidence": "VERIFIED_PROJECT",
        })
        for hold in packet["packaging"]["hold_tests"]:
            hold["overall_result"] = "PASS"
        packet["labour"]["worker_count"] = 1
        observation = packet["labour"]["observations"][0]
        observation.update({
            "task": "assemble and pack",
            "category": "PACKING",
            "active_seconds": 45,
            "elapsed_seconds": 60,
            "concurrent_work": "NONE",
            "evidence": "VERIFIED_PROJECT",
        })
        packet["labour"]["loaded_hourly_labour_rate"].update({
            "value": 35.0,
            "source": "project labour basis",
            "source_date": "2026-09-14",
            "scope": "loaded hourly rate",
            "evidence": "VERIFIED_PROJECT",
        })
        packet["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.20,
            "evidence": "VERIFIED_PROJECT",
        }
        packet["economics_handoff"]["direct_labour_cost_per_order"] = {
            "value": 0.44,
            "evidence": "VERIFIED_PROJECT",
        }

        result = validate_packet(packet)
        self.assertEqual(result["capture_state"], "REVIEW_REQUIRED")
        self.assertFalse(result["commercial_pass_eligible"])
        self.assertEqual(result["incomplete_reasons"], [])


if __name__ == "__main__":
    unittest.main()
