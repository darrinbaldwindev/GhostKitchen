#!/usr/bin/env python3
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

REQUIRED = [
    "net_customer_revenue",
    "ingredient_cost",
    "packaging",
    "labour",
    "payment_processing",
    "channel_commission",
    "business_funded_delivery",
    "discounts_promotions",
    "refunds_cancellations",
    "variable_waste",
    "acquisition_cost",
]

ALLOWED_EVIDENCE = {"VERIFIED_PROJECT", "PUBLIC_REFERENCE", "HYPOTHESIS", "UNKNOWN"}
ALLOWED_SCENARIO_KEYS = {"scenario_id", "inputs"}
ALLOWED_BATCH_KEYS = {"status", "source_note", "scenarios"}


def money(value, field="value"):
    try:
        return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError) as error:
        raise ValueError(f"invalid numeric value for {field}: {value!r}") from error


def evaluate(scenario):
    if not isinstance(scenario, dict):
        raise ValueError("scenario must be an object")
    unknown_scenario_keys = set(scenario) - ALLOWED_SCENARIO_KEYS
    if unknown_scenario_keys:
        raise ValueError(f"unknown scenario keys: {sorted(unknown_scenario_keys)}")

    scenario_id = scenario.get("scenario_id")
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ValueError("scenario_id is required")

    inputs = scenario.get("inputs", {})
    if not isinstance(inputs, dict):
        raise ValueError("inputs must be an object")
    unknown_input_keys = set(inputs) - set(REQUIRED)
    if unknown_input_keys:
        raise ValueError(f"unknown economics input keys: {sorted(unknown_input_keys)}")

    missing = []
    values = {}
    evidence = {}

    for field in REQUIRED:
        item = inputs.get(field)
        if not isinstance(item, dict):
            missing.append(field)
            continue
        ev = item.get("evidence", "UNKNOWN")
        if ev not in ALLOWED_EVIDENCE:
            raise ValueError(f"invalid evidence class for {field}: {ev}")
        evidence[field] = ev
        if item.get("value") is None or ev == "UNKNOWN":
            missing.append(field)
            continue
        value = money(item["value"], field)
        if field == "net_customer_revenue" and value < 0:
            raise ValueError("negative net_customer_revenue is not allowed")
        if field != "net_customer_revenue" and value < 0:
            raise ValueError(f"negative cost input is not allowed for {field}")
        values[field] = value

    if missing:
        return {
            "scenario_id": scenario_id,
            "status": "NOT_TESTABLE",
            "missing_or_unknown": sorted(set(missing)),
            "commercial_pass_eligible": False,
        }

    revenue = values["net_customer_revenue"]
    costs = sum((values[f] for f in REQUIRED if f != "net_customer_revenue"), Decimal("0.00"))
    contribution = money(revenue - costs, "contribution")
    margin = None if revenue == 0 else (contribution / revenue * Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    evidence_classes = sorted(set(evidence.values()))
    fully_verified = evidence_classes == ["VERIFIED_PROJECT"]

    return {
        "scenario_id": scenario_id,
        "status": "CALCULATED",
        "contribution_per_order": str(contribution),
        "contribution_margin_percent": None if margin is None else str(margin),
        "evidence_classes": evidence_classes,
        "decision_state": "PROJECT_EVIDENCE_READY" if fully_verified else "DECISION_SUPPORT_ONLY",
        "commercial_pass_eligible": bool(fully_verified and contribution > 0),
    }


def evaluate_batch(payload):
    if not isinstance(payload, dict):
        raise ValueError("batch payload must be an object")
    unknown_batch_keys = set(payload) - ALLOWED_BATCH_KEYS
    if unknown_batch_keys:
        raise ValueError(f"unknown batch keys: {sorted(unknown_batch_keys)}")
    scenarios = payload.get("scenarios", [])
    if not isinstance(scenarios, list):
        raise ValueError("scenarios must be a list")
    if not scenarios:
        return {"status": "EMPTY", "commercial_pass_eligible": False, "results": []}

    ids = []
    for scenario in scenarios:
        sid = scenario.get("scenario_id") if isinstance(scenario, dict) else None
        if not isinstance(sid, str) or not sid.strip():
            raise ValueError("scenario_id is required")
        ids.append(sid)
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate scenario_id")
    results = [evaluate(scenario) for scenario in sorted(scenarios, key=lambda item: item["scenario_id"])]
    return {"status": "EVALUATED", "commercial_pass_eligible": any(item.get("commercial_pass_eligible") for item in results), "results": results}


def main(path):
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    print(json.dumps(evaluate_batch(payload), indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: channel_economics.py <scenario.json>")
    main(sys.argv[1])
