#!/usr/bin/env python3
"""Bridge representative-order evidence into the canonical GK-010 calculator.

Packaging and labour are derived by evidence_handoff and cannot be supplied by the
caller. The remaining inputs retain channel_economics' strict schema. This bridge
creates no independent commercial authority.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

TOOLS = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, TOOLS / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


evidence_handoff = _load("evidence_handoff", "evidence_handoff.py")
channel_economics = _load("channel_economics", "channel_economics.py")

DERIVED_FIELDS = {"packaging", "labour"}
EXTERNAL_FIELDS = set(channel_economics.REQUIRED) - DERIVED_FIELDS
ALLOWED_REQUEST_KEYS = {"scenario_id", "inputs"}
ALLOWED_ITEM_KEYS = {"value", "evidence"}


def _validate_external_item(field: str, item: Any) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise ValueError(f"{field} must be an object")
    unknown = set(item) - ALLOWED_ITEM_KEYS
    if unknown:
        raise ValueError(f"unknown keys for {field}: {sorted(unknown)}")
    evidence = item.get("evidence", "UNKNOWN")
    if evidence not in channel_economics.ALLOWED_EVIDENCE:
        raise ValueError(f"invalid evidence class for {field}: {evidence}")
    return {"value": item.get("value"), "evidence": evidence}


def bridge(packet: Any, request: Any) -> dict[str, Any]:
    if not isinstance(request, dict):
        raise ValueError("bridge request must be an object")
    unknown_request = set(request) - ALLOWED_REQUEST_KEYS
    if unknown_request:
        raise ValueError(f"unknown bridge request keys: {sorted(unknown_request)}")

    scenario_id = request.get("scenario_id")
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ValueError("scenario_id is required")
    inputs = request.get("inputs")
    if not isinstance(inputs, dict):
        raise ValueError("inputs must be an object")
    forbidden = set(inputs) & DERIVED_FIELDS
    if forbidden:
        raise ValueError(f"derived inputs cannot be supplied or overridden: {sorted(forbidden)}")
    unknown_inputs = set(inputs) - EXTERNAL_FIELDS
    if unknown_inputs:
        raise ValueError(f"unknown economics input keys: {sorted(unknown_inputs)}")

    handoff = evidence_handoff.derive_handoff(packet)
    scenario_inputs = {field: _validate_external_item(field, inputs[field]) for field in sorted(inputs)}
    scenario_inputs["packaging"] = {
        "value": handoff["packaging_cost_per_order"]["value"],
        "evidence": handoff["packaging_cost_per_order"]["evidence"],
    }
    scenario_inputs["labour"] = {
        "value": handoff["direct_labour_cost_per_order"]["value"],
        "evidence": handoff["direct_labour_cost_per_order"]["evidence"],
    }

    scenario = {"scenario_id": scenario_id, "inputs": scenario_inputs}
    result = channel_economics.evaluate(scenario)
    representative_order_id = packet.get("representative_order_id", "") if isinstance(packet, dict) else ""
    packaging_configuration_id = ""
    if isinstance(packet, dict) and isinstance(packet.get("packaging"), dict):
        packaging_configuration_id = packet["packaging"].get("configuration_id", "")

    return {
        "authority": "EVIDENCE_TO_GK010_BRIDGE_ONLY",
        "commercial_pass_eligible": False,
        "correlation": {
            "scenario_id": scenario_id,
            "representative_order_id": representative_order_id,
            "packaging_configuration_id": packaging_configuration_id,
        },
        "scenario": scenario,
        "calculator_result": result,
        "note": "Bridge preserves evidence provenance and delegates economics evaluation to channel_economics; it grants no commercial approval.",
    }


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: evidence_to_scenario.py <packet.json> <request.json>", file=sys.stderr)
        return 2
    packet = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    request = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    print(json.dumps(bridge(packet, request), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
