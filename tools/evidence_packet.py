#!/usr/bin/env python3
"""Fail-closed validation for representative-order evidence capture packets.

This validator checks structure and evidence labels only. It deliberately does not
certify that supplied evidence is true and never grants commercial approval.
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {"VERIFIED_PROJECT", "PUBLIC_REFERENCE", "HYPOTHESIS", "UNKNOWN"}
TOP_KEYS = {
    "template_version", "authority", "commercial_pass_eligible", "concept",
    "representative_order_id", "observation_date", "observer", "packaging",
    "labour", "economics_handoff",
}
PACKAGING_KEYS = {"configuration_id", "components", "pack_time_seconds", "hold_tests"}
COMPONENT_KEYS = {
    "component", "sku_or_description", "quantity_used", "pack_quantity",
    "purchase_or_quote_value", "freight_treatment", "gst_treatment", "source",
    "source_date", "evidence",
}
MEASUREMENT_KEYS = {"value", "source", "source_date", "evidence"}
HOLD_KEYS = {
    "minutes", "leakage", "seal_integrity", "condensation",
    "temperature_observation", "texture_observation", "presentation", "overall_result",
}
LABOUR_KEYS = {"worker_count", "observations", "loaded_hourly_labour_rate"}
LABOUR_OBSERVATION_KEYS = {
    "task", "category", "active_seconds", "elapsed_seconds", "concurrent_work",
    "abnormal_or_rework", "notes", "evidence",
}
LABOUR_RATE_KEYS = {"value", "source", "source_date", "scope", "evidence"}
HANDOFF_KEYS = {"packaging_cost_per_order", "direct_labour_cost_per_order", "notes"}
HANDOFF_VALUE_KEYS = {"value", "evidence"}


def _exact_keys(obj: dict[str, Any], allowed: set[str], where: str) -> None:
    unknown = set(obj) - allowed
    missing = allowed - set(obj)
    if unknown:
        raise ValueError(f"unknown keys at {where}: {sorted(unknown)}")
    if missing:
        raise ValueError(f"missing keys at {where}: {sorted(missing)}")


def _dict(value: Any, where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{where} must be an object")
    return value


def _list(value: Any, where: str) -> list[Any]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{where} must be a non-empty list")
    return value


def _evidence(value: Any, where: str) -> str:
    if value not in EVIDENCE_CLASSES:
        raise ValueError(f"invalid evidence class at {where}: {value!r}")
    return value


def _nonnegative_number_or_none(value: Any, where: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{where} must be a number or null")
    if not math.isfinite(float(value)):
        raise ValueError(f"{where} must be finite")
    if value < 0:
        raise ValueError(f"{where} must be non-negative")


def validate_packet(packet: Any) -> dict[str, Any]:
    packet = _dict(packet, "packet")
    _exact_keys(packet, TOP_KEYS, "packet")

    if packet["template_version"] != "1.0":
        raise ValueError("unsupported template_version")
    if packet["authority"] != "EVIDENCE_CAPTURE_ONLY":
        raise ValueError("authority must remain EVIDENCE_CAPTURE_ONLY")
    if packet["commercial_pass_eligible"] is not False:
        raise ValueError("evidence packet cannot be commercially pass eligible")

    for field in ("concept", "representative_order_id", "observation_date", "observer"):
        if not isinstance(packet[field], str):
            raise ValueError(f"{field} must be a string")

    evidence_counts: Counter[str] = Counter()
    incomplete_reasons: list[str] = []

    packaging = _dict(packet["packaging"], "packaging")
    _exact_keys(packaging, PACKAGING_KEYS, "packaging")
    if not isinstance(packaging["configuration_id"], str):
        raise ValueError("packaging.configuration_id must be a string")

    components = _list(packaging["components"], "packaging.components")
    for index, raw in enumerate(components):
        where = f"packaging.components[{index}]"
        component = _dict(raw, where)
        _exact_keys(component, COMPONENT_KEYS, where)
        for field in ("component", "sku_or_description", "freight_treatment", "gst_treatment", "source", "source_date"):
            if not isinstance(component[field], str):
                raise ValueError(f"{where}.{field} must be a string")
        for field in ("quantity_used", "pack_quantity", "purchase_or_quote_value"):
            _nonnegative_number_or_none(component[field], f"{where}.{field}")
        evidence = _evidence(component["evidence"], f"{where}.evidence")
        evidence_counts[evidence] += 1
        if evidence == "UNKNOWN" or any(component[f] is None for f in ("quantity_used", "pack_quantity", "purchase_or_quote_value")):
            incomplete_reasons.append(f"{where} incomplete")

    pack_time = _dict(packaging["pack_time_seconds"], "packaging.pack_time_seconds")
    _exact_keys(pack_time, MEASUREMENT_KEYS, "packaging.pack_time_seconds")
    _nonnegative_number_or_none(pack_time["value"], "packaging.pack_time_seconds.value")
    for field in ("source", "source_date"):
        if not isinstance(pack_time[field], str):
            raise ValueError(f"packaging.pack_time_seconds.{field} must be a string")
    pack_time_evidence = _evidence(pack_time["evidence"], "packaging.pack_time_seconds.evidence")
    evidence_counts[pack_time_evidence] += 1
    if pack_time["value"] is None or pack_time_evidence == "UNKNOWN":
        incomplete_reasons.append("packaging.pack_time_seconds incomplete")

    holds = _list(packaging["hold_tests"], "packaging.hold_tests")
    hold_minutes: list[int] = []
    for index, raw in enumerate(holds):
        where = f"packaging.hold_tests[{index}]"
        hold = _dict(raw, where)
        _exact_keys(hold, HOLD_KEYS, where)
        minutes = hold["minutes"]
        if isinstance(minutes, bool) or not isinstance(minutes, int):
            raise ValueError(f"{where}.minutes must be an integer")
        hold_minutes.append(minutes)
        for field in HOLD_KEYS - {"minutes"}:
            if not isinstance(hold[field], str):
                raise ValueError(f"{where}.{field} must be a string")
    if sorted(hold_minutes) != [20, 30, 40]:
        raise ValueError("packaging.hold_tests must contain exactly 20, 30 and 40 minute observations")
    if any(hold["overall_result"] == "UNKNOWN" for hold in holds):
        incomplete_reasons.append("packaging.hold_tests incomplete")

    labour = _dict(packet["labour"], "labour")
    _exact_keys(labour, LABOUR_KEYS, "labour")
    _nonnegative_number_or_none(labour["worker_count"], "labour.worker_count")
    if labour["worker_count"] is None:
        incomplete_reasons.append("labour.worker_count incomplete")

    observations = _list(labour["observations"], "labour.observations")
    for index, raw in enumerate(observations):
        where = f"labour.observations[{index}]"
        observation = _dict(raw, where)
        _exact_keys(observation, LABOUR_OBSERVATION_KEYS, where)
        for field in ("task", "category", "concurrent_work", "notes"):
            if not isinstance(observation[field], str):
                raise ValueError(f"{where}.{field} must be a string")
        if not isinstance(observation["abnormal_or_rework"], bool):
            raise ValueError(f"{where}.abnormal_or_rework must be boolean")
        for field in ("active_seconds", "elapsed_seconds"):
            _nonnegative_number_or_none(observation[field], f"{where}.{field}")
        if observation["active_seconds"] is not None and observation["elapsed_seconds"] is not None:
            if observation["active_seconds"] > observation["elapsed_seconds"]:
                raise ValueError(f"{where}.active_seconds cannot exceed elapsed_seconds")
        evidence = _evidence(observation["evidence"], f"{where}.evidence")
        evidence_counts[evidence] += 1
        if evidence == "UNKNOWN" or observation["active_seconds"] is None or observation["elapsed_seconds"] is None:
            incomplete_reasons.append(f"{where} incomplete")

    rate = _dict(labour["loaded_hourly_labour_rate"], "labour.loaded_hourly_labour_rate")
    _exact_keys(rate, LABOUR_RATE_KEYS, "labour.loaded_hourly_labour_rate")
    _nonnegative_number_or_none(rate["value"], "labour.loaded_hourly_labour_rate.value")
    for field in ("source", "source_date", "scope"):
        if not isinstance(rate[field], str):
            raise ValueError(f"labour.loaded_hourly_labour_rate.{field} must be a string")
    rate_evidence = _evidence(rate["evidence"], "labour.loaded_hourly_labour_rate.evidence")
    evidence_counts[rate_evidence] += 1
    if rate["value"] is None or rate_evidence == "UNKNOWN":
        incomplete_reasons.append("labour.loaded_hourly_labour_rate incomplete")

    handoff = _dict(packet["economics_handoff"], "economics_handoff")
    _exact_keys(handoff, HANDOFF_KEYS, "economics_handoff")
    if not isinstance(handoff["notes"], str):
        raise ValueError("economics_handoff.notes must be a string")
    for field in ("packaging_cost_per_order", "direct_labour_cost_per_order"):
        value = _dict(handoff[field], f"economics_handoff.{field}")
        _exact_keys(value, HANDOFF_VALUE_KEYS, f"economics_handoff.{field}")
        _nonnegative_number_or_none(value["value"], f"economics_handoff.{field}.value")
        evidence = _evidence(value["evidence"], f"economics_handoff.{field}.evidence")
        evidence_counts[evidence] += 1
        if value["value"] is None or evidence == "UNKNOWN":
            incomplete_reasons.append(f"economics_handoff.{field} incomplete")

    for field in ("representative_order_id", "observation_date", "observer"):
        if not packet[field].strip():
            incomplete_reasons.append(f"{field} missing")

    state = "CAPTURE_INCOMPLETE" if incomplete_reasons else "REVIEW_REQUIRED"
    return {
        "authority": "EVIDENCE_CAPTURE_ONLY",
        "commercial_pass_eligible": False,
        "capture_state": state,
        "evidence_counts": {key: evidence_counts.get(key, 0) for key in sorted(EVIDENCE_CLASSES)},
        "incomplete_reasons": sorted(set(incomplete_reasons)),
        "note": "Structural validation does not verify evidence truth or grant calculator/commercial approval.",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: evidence_packet.py <packet.json>", file=sys.stderr)
        return 2
    packet = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(validate_packet(packet), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
