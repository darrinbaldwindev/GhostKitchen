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


def money(value, field="value"):
    try:
        return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError) as error:
        raise ValueError(f"invalid numeric value for {field}: {value!r}") from error


def evaluate(scenario):
    scenario_id = scenario.get("scenario_id")
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ValueError("scenario_id is required")

    missing = []
    values = {}
    evidence = {}

    for field in REQUIRED:
        item = scenario.get("inputs", {}).get(field)
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
    scenarios = payload.get("scenarios", [])
    if not isinstance(scenarios, list):
        raise ValueError("scenarios must be a list")
    ids = []
    for scenario in scenarios:
        sid = scenario.get("scenario_id") if isinstance(scenario, dict) else None
        if not isinstance(sid, str) or not sid.strip():
            raise ValueError("scenario_id is required")
        ids.append(sid)
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate scenario_id")
    return [evaluate(scenario) for scenario in sorted(scenarios, key=lambda item: item["scenario_id"])]


def main(path):
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    print(json.dumps({"results": evaluate_batch(payload)}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: channel_economics.py <scenario.json>")
    main(sys.argv[1])
