import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evidence_handoff", ROOT / "tools" / "evidence_handoff.py")
evidence_handoff = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(evidence_handoff)
derive_handoff = evidence_handoff.derive_handoff


def template_packet():
    return json.loads((ROOT / "fixtures" / "evidence" / "representative-order-evidence.template.json").read_text())


def complete_packet():
    packet = template_packet()
    packet["concept"] = "test-concept"
    packet["representative_order_id"] = "order-001"
    packet["observation_date"] = "2026-09-14"
    packet["observer"] = "test-observer"
    packet["packaging"]["configuration_id"] = "pack-001"

    component = packet["packaging"]["components"][0]
    component.update({
        "component": "container",
        "sku_or_description": "test container",
        "quantity_used": 1,
        "pack_quantity": 100,
        "purchase_or_quote_value": 20.0,
        "freight_treatment": "included in validated landed basis",
        "gst_treatment": "included in validated landed basis",
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
        hold.update({
            "leakage": "NONE",
            "seal_integrity": "PASS",
            "condensation": "LOW",
            "temperature_observation": "recorded",
            "texture_observation": "recorded",
            "presentation": "PASS",
            "overall_result": "PASS",
        })

    packet["labour"]["worker_count"] = 1
    observation = packet["labour"]["observations"][0]
    observation.update({
        "task": "assemble and pack",
        "category": "PACKING",
        "active_seconds": 45,
        "elapsed_seconds": 60,
        "concurrent_work": "NONE",
        "abnormal_or_rework": False,
        "notes": "",
        "evidence": "VERIFIED_PROJECT",
    })
    packet["labour"]["loaded_hourly_labour_rate"].update({
        "value": 35.0,
        "source": "project labour basis",
        "source_date": "2026-09-14",
        "scope": "loaded hourly rate",
        "evidence": "VERIFIED_PROJECT",
    })
    return packet


class EvidenceHandoffTests(unittest.TestCase):
    def test_blank_template_is_not_ready_and_never_commercial(self):
        result = derive_handoff(template_packet())
        self.assertEqual(result["handoff_state"], "NOT_READY")
        self.assertIsNone(result["packaging_cost_per_order"]["value"])
        self.assertIsNone(result["direct_labour_cost_per_order"]["value"])
        self.assertFalse(result["commercial_pass_eligible"])

    def test_verified_packet_derives_expected_values_but_only_requires_review(self):
        packet = complete_packet()
        result = derive_handoff(packet)
        self.assertEqual(result["packaging_cost_per_order"]["value"], "0.20")
        self.assertEqual(result["packaging_cost_per_order"]["evidence"], "VERIFIED_PROJECT")
        self.assertEqual(result["direct_labour_cost_per_order"]["value"], "0.44")
        self.assertEqual(result["direct_labour_cost_per_order"]["active_seconds"], "45")
        self.assertEqual(result["direct_labour_cost_per_order"]["evidence"], "VERIFIED_PROJECT")
        self.assertEqual(result["handoff_state"], "REVIEW_REQUIRED")
        self.assertFalse(result["commercial_pass_eligible"])

    def test_matching_supplied_values_are_reconciliation_only(self):
        packet = complete_packet()
        packet["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.20,
            "evidence": "VERIFIED_PROJECT",
        }
        packet["economics_handoff"]["direct_labour_cost_per_order"] = {
            "value": 0.44,
            "evidence": "VERIFIED_PROJECT",
        }
        result = derive_handoff(packet)
        self.assertEqual(result["handoff_state"], "REVIEW_REQUIRED")

    def test_packaging_value_mismatch_fails_closed(self):
        packet = complete_packet()
        packet["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.21,
            "evidence": "VERIFIED_PROJECT",
        }
        with self.assertRaisesRegex(ValueError, "does not match derived value"):
            derive_handoff(packet)

    def test_labour_value_mismatch_fails_closed(self):
        packet = complete_packet()
        packet["economics_handoff"]["direct_labour_cost_per_order"] = {
            "value": 0.45,
            "evidence": "VERIFIED_PROJECT",
        }
        with self.assertRaisesRegex(ValueError, "does not match derived value"):
            derive_handoff(packet)

    def test_public_reference_component_cannot_be_promoted_to_verified_handoff(self):
        packet = complete_packet()
        packet["packaging"]["components"][0]["evidence"] = "PUBLIC_REFERENCE"
        packet["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.20,
            "evidence": "VERIFIED_PROJECT",
        }
        with self.assertRaisesRegex(ValueError, "cannot outrank underlying evidence"):
            derive_handoff(packet)

    def test_unresolved_freight_blocks_packaging_derivation_and_supplied_value(self):
        packet = complete_packet()
        packet["packaging"]["components"][0]["freight_treatment"] = "UNKNOWN"
        result = derive_handoff(packet)
        self.assertIsNone(result["packaging_cost_per_order"]["value"])
        self.assertEqual(result["packaging_cost_per_order"]["evidence"], "UNKNOWN")
        self.assertEqual(result["handoff_state"], "NOT_READY")

        packet["economics_handoff"]["packaging_cost_per_order"] = {
            "value": 0.20,
            "evidence": "UNKNOWN",
        }
        with self.assertRaisesRegex(ValueError, "cannot be reconciled because derivation is unresolved"):
            derive_handoff(packet)

    def test_zero_pack_quantity_fails_closed(self):
        packet = complete_packet()
        packet["packaging"]["components"][0]["pack_quantity"] = 0
        with self.assertRaisesRegex(ValueError, "must be greater than zero"):
            derive_handoff(packet)

    def test_abnormal_observations_are_retained_in_labour_derivation(self):
        packet = complete_packet()
        packet["labour"]["observations"][0]["abnormal_or_rework"] = True
        result = derive_handoff(packet)
        self.assertEqual(result["direct_labour_cost_per_order"]["abnormal_or_rework_observations"], 1)
        self.assertEqual(result["direct_labour_cost_per_order"]["value"], "0.44")


if __name__ == "__main__":
    unittest.main()
