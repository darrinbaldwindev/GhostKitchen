#!/usr/bin/env python3
"""Derive and reconcile economics handoff values from evidence packets.

Underlying packet observations are authoritative for arithmetic. Manually supplied
handoff values are reconciliation assertions only and cannot upgrade evidence.
This tool never grants commercial approval.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

TOOLS = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("evidence_packet", TOOLS / "evidence_packet.py")
evidence_packet = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(evidence_packet)
validate_packet = evidence_packet.validate_packet

CENT = Decimal("0.01")
EVIDENCE_RANK = {
    "UNKNOWN": 0,
    "HYPOTHESIS": 1,
    "PUBLIC_REFERENCE": 2,
    "VERIFIED_PROJECT": 3,
}


def _decimal(value: Any, where: str) -> Decimal:
    try:
        parsed = Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{where} must be numeric") from exc
    if not parsed.is_finite():
        raise ValueError(f"{where} must be finite")
    return parsed


def _money(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def _weakest(classes: list[str]) -> str:
    if not classes:
        return "UNKNOWN"
    return min(classes, key=lambda item: EVIDENCE_RANK[item])


def _packaging_derivation(packet: dict[str, Any]) -> dict[str, Any]:
    components = packet["packaging"]["components"]
    total = Decimal("0")
    evidence: list[str] = []
    unresolved: list[str] = []

    for index, component in enumerate(components):
        quantity = component["quantity_used"]
        pack_quantity = component["pack_quantity"]
        price = component["purchase_or_quote_value"]
        evidence.append(component["evidence"])

        if quantity is None or pack_quantity is None or price is None:
            unresolved.append(f"packaging.components[{index}] numeric basis incomplete")
            continue
        pack_quantity_decimal = _decimal(pack_quantity, f"packaging.components[{index}].pack_quantity")
        if pack_quantity_decimal <= 0:
            raise ValueError(f"packaging.components[{index}].pack_quantity must be greater than zero for derivation")
        quantity_decimal = _decimal(quantity, f"packaging.components[{index}].quantity_used")
        price_decimal = _decimal(price, f"packaging.components[{index}].purchase_or_quote_value")
        total += (price_decimal / pack_quantity_decimal) * quantity_decimal

        for field in ("freight_treatment", "gst_treatment"):
            treatment = component[field].strip()
            if not treatment or treatment.upper() == "UNKNOWN":
                unresolved.append(f"packaging.components[{index}].{field} unresolved")

    if unresolved:
        derived_evidence = "UNKNOWN"
        value = None
    else:
        derived_evidence = _weakest(evidence)
        value = _money(total)

    return {
        "value": value,
        "evidence": derived_evidence,
        "unresolved": sorted(set(unresolved)),
    }


def _labour_derivation(packet: dict[str, Any]) -> dict[str, Any]:
    observations = packet["labour"]["observations"]
    rate = packet["labour"]["loaded_hourly_labour_rate"]
    evidence = [rate["evidence"]]
    unresolved: list[str] = []
    active_seconds = Decimal("0")
    abnormal_count = 0

    for index, observation in enumerate(observations):
        evidence.append(observation["evidence"])
        value = observation["active_seconds"]
        if value is None:
            unresolved.append(f"labour.observations[{index}].active_seconds incomplete")
        else:
            active_seconds += _decimal(value, f"labour.observations[{index}].active_seconds")
        if observation["abnormal_or_rework"]:
            abnormal_count += 1

    if rate["value"] is None:
        unresolved.append("labour.loaded_hourly_labour_rate.value incomplete")
    if not rate["scope"].strip():
        unresolved.append("labour.loaded_hourly_labour_rate.scope missing")
    if not rate["source"].strip() or not rate["source_date"].strip():
        unresolved.append("labour.loaded_hourly_labour_rate provenance incomplete")

    if unresolved:
        derived_evidence = "UNKNOWN"
        value = None
    else:
        hourly_rate = _decimal(rate["value"], "labour.loaded_hourly_labour_rate.value")
        value = _money((active_seconds / Decimal("3600")) * hourly_rate)
        derived_evidence = _weakest(evidence)

    return {
        "value": value,
        "evidence": derived_evidence,
        "active_seconds": active_seconds,
        "abnormal_or_rework_observations": abnormal_count,
        "unresolved": sorted(set(unresolved)),
    }


def _reconcile(field: str, supplied: dict[str, Any], derived: dict[str, Any]) -> None:
    supplied_value = supplied["value"]
    supplied_evidence = supplied["evidence"]
    derived_value = derived["value"]
    derived_evidence = derived["evidence"]

    if supplied_value is not None:
        if derived_value is None:
            raise ValueError(f"{field} supplied value cannot be reconciled because derivation is unresolved")
        supplied_money = _money(_decimal(supplied_value, field))
        if supplied_money != derived_value:
            raise ValueError(f"{field} does not match derived value: supplied {supplied_money}, derived {derived_value}")

    if EVIDENCE_RANK[supplied_evidence] > EVIDENCE_RANK[derived_evidence]:
        raise ValueError(
            f"{field} evidence cannot outrank underlying evidence: supplied {supplied_evidence}, derived {derived_evidence}"
        )


def derive_handoff(packet: Any) -> dict[str, Any]:
    structural = validate_packet(packet)
    packaging = _packaging_derivation(packet)
    labour = _labour_derivation(packet)

    handoff = packet["economics_handoff"]
    _reconcile("economics_handoff.packaging_cost_per_order", handoff["packaging_cost_per_order"], packaging)
    _reconcile("economics_handoff.direct_labour_cost_per_order", handoff["direct_labour_cost_per_order"], labour)

    ready = packaging["value"] is not None and labour["value"] is not None
    return {
        "authority": "EVIDENCE_RECONCILIATION_ONLY",
        "commercial_pass_eligible": False,
        "capture_state": structural["capture_state"],
        "handoff_state": "REVIEW_REQUIRED" if ready else "NOT_READY",
        "packaging_cost_per_order": {
            "value": None if packaging["value"] is None else str(packaging["value"]),
            "evidence": packaging["evidence"],
            "unresolved": packaging["unresolved"],
        },
        "direct_labour_cost_per_order": {
            "value": None if labour["value"] is None else str(labour["value"]),
            "evidence": labour["evidence"],
            "active_seconds": str(labour["active_seconds"]),
            "abnormal_or_rework_observations": labour["abnormal_or_rework_observations"],
            "unresolved": labour["unresolved"],
        },
        "note": "Derived handoff values reconcile evidence only; they do not verify evidence truth or grant commercial approval.",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: evidence_handoff.py <packet.json>", file=sys.stderr)
        return 2
    packet = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(derive_handoff(packet), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
