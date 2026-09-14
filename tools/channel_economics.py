#!/usr/bin/env python3
import json
import sys
from decimal import Decimal, ROUND_HALF_UP

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


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def evaluate(scenario):
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
        values[field] = money(item["value"])

    if missing:
        return {
            "scenario_id": scenario.get("scenario_id"),
            "status": "NOT_TESTABLE",
            "missing_or_unknown": sorted(set(missing)),
            "commercial_pass_eligible": False,
        }

    revenue = values["net_customer_revenue"]
    costs = sum((values[f] for f in REQUIRED if f != "net_customer_revenue"), Decimal("0.00"))
    contribution = money(revenue - costs)
    margin = None if revenue == 0 else (contribution / revenue * Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    evidence_classes = sorted(set(evidence.values()))
    fully_verified = evidence_classes == ["VERIFIED_PROJECT"]

    return {
        "scenario_id": scenario.get("scenario_id"),
        "status": "CALCULATED",
        "contribution_per_order": str(contribution),
        "contribution_margin_percent": None if margin is None else str(margin),
        "evidence_classes": evidence_classes,
        "decision_state": "PROJECT_EVIDENCE_READY" if fully_verified else "DECISION_SUPPORT_ONLY",
        "commercial_pass_eligible": bool(fully_verified and contribution > 0),
    }


def main(path):
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    results = [evaluate(s) for s in payload.get("scenarios", [])]
    print(json.dumps({"results": results}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: channel_economics.py <scenario.json>")
    main(sys.argv[1])
