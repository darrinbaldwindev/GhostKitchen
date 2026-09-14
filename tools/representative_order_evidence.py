#!/usr/bin/env python3
import json
import sys
from decimal import Decimal, InvalidOperation

ALLOWED_EVIDENCE = {"VERIFIED_PROJECT", "PUBLIC_REFERENCE", "HYPOTHESIS", "UNKNOWN"}
TOP_LEVEL_KEYS = {
    "template_version", "authority", "commercial_pass_eligible", "concept",
    "representative_order_id", "observation_date", "observer", "packaging",
    "labour", "economics_handoff"
}


def _require_object(value, field):
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value


def _require_list(value, field):
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def _evidence(value, field):
    if value not in ALLOWED_EVIDENCE:
        raise ValueError(f"invalid evidence class for {field}: {value!r}")
    return value


def _non_negative_number(value, field, allow_none=True):
    if value is None and allow_none:
        return None
    try:
        parsed = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"invalid numeric value for {field}: {value!r}") from exc
    if not parsed.is_finite() or parsed < 0:
        raise ValueError(f"invalid non-negative numeric value for {field}: {value!r}")
    return parsed


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_record(record):
    record = _require_object(record, "record")
    unknown = set(record) - TOP_LEVEL_KEYS
    if unknown:
        raise ValueError(f"unknown top-level keys: {sorted(unknown)}")
    if record.get("template_version") != "1.0":
        raise ValueError("template_version must be '1.0'")
    if record.get("authority") != "EVIDENCE_CAPTURE_ONLY":
        raise ValueError("authority must remain EVIDENCE_CAPTURE_ONLY")
    if record.get("commercial_pass_eligible") is not False:
        raise ValueError("commercial_pass_eligible must remain false")

    packaging = _require_object(record.get("packaging"), "packaging")
    components = _require_list(packaging.get("components"), "packaging.components")
    pack_time = _require_object(packaging.get("pack_time_seconds"), "packaging.pack_time_seconds")
    hold_tests = _require_list(packaging.get("hold_tests"), "packaging.hold_tests")

    packaging_support_ready = bool(components)
    for index, item in enumerate(components):
        item = _require_object(item, f"packaging.components[{index}]")
        ev = _evidence(item.get("evidence", "UNKNOWN"), f"packaging.components[{index}]")
        _non_negative_number(item.get("quantity_used"), f"packaging.components[{index}].quantity_used")
        _non_negative_number(item.get("pack_quantity"), f"packaging.components[{index}].pack_quantity")
        _non_negative_number(item.get("purchase_or_quote_value"), f"packaging.components[{index}].purchase_or_quote_value")
        if ev == "VERIFIED_PROJECT":
            required = (
                _nonempty(item.get("component")),
                _nonempty(item.get("sku_or_description")),
                item.get("quantity_used") is not None,
                item.get("pack_quantity") is not None,
                item.get("purchase_or_quote_value") is not None,
                item.get("freight_treatment") != "UNKNOWN",
                item.get("gst_treatment") != "UNKNOWN",
                _nonempty(item.get("source")),
                _nonempty(item.get("source_date")),
            )
            packaging_support_ready = packaging_support_ready and all(required)
        else:
            packaging_support_ready = False

    pack_ev = _evidence(pack_time.get("evidence", "UNKNOWN"), "packaging.pack_time_seconds")
    _non_negative_number(pack_time.get("value"), "packaging.pack_time_seconds.value")
    if pack_ev == "VERIFIED_PROJECT" and not (
        pack_time.get("value") is not None and _nonempty(pack_time.get("source")) and _nonempty(pack_time.get("source_date"))
    ):
        raise ValueError("VERIFIED_PROJECT pack_time_seconds requires value, source and source_date")

    hold_minutes = []
    for index, test in enumerate(hold_tests):
        test = _require_object(test, f"packaging.hold_tests[{index}]")
        minute = test.get("minutes")
        if minute not in (20, 30, 40):
            raise ValueError("hold test minutes must be one of 20, 30, 40")
        hold_minutes.append(minute)
    if len(hold_minutes) != len(set(hold_minutes)):
        raise ValueError("duplicate hold test minutes")

    labour = _require_object(record.get("labour"), "labour")
    _non_negative_number(labour.get("worker_count"), "labour.worker_count")
    observations = _require_list(labour.get("observations"), "labour.observations")
    labour_support_ready = bool(observations)
    for index, obs in enumerate(observations):
        obs = _require_object(obs, f"labour.observations[{index}]")
        ev = _evidence(obs.get("evidence", "UNKNOWN"), f"labour.observations[{index}]")
        active = _non_negative_number(obs.get("active_seconds"), f"labour.observations[{index}].active_seconds")
        elapsed = _non_negative_number(obs.get("elapsed_seconds"), f"labour.observations[{index}].elapsed_seconds")
        if active is not None and elapsed is not None and active > elapsed:
            raise ValueError("active_seconds cannot exceed elapsed_seconds")
        if ev == "VERIFIED_PROJECT":
            labour_support_ready = labour_support_ready and all((
                _nonempty(obs.get("task")), obs.get("category") != "UNKNOWN",
                active is not None, elapsed is not None,
            ))
        else:
            labour_support_ready = False

    rate = _require_object(labour.get("loaded_hourly_labour_rate"), "labour.loaded_hourly_labour_rate")
    rate_ev = _evidence(rate.get("evidence", "UNKNOWN"), "labour.loaded_hourly_labour_rate")
    _non_negative_number(rate.get("value"), "labour.loaded_hourly_labour_rate.value")
    if rate_ev == "VERIFIED_PROJECT":
        rate_ready = all((rate.get("value") is not None, _nonempty(rate.get("source")), _nonempty(rate.get("source_date")), _nonempty(rate.get("scope"))))
        if not rate_ready:
            raise ValueError("VERIFIED_PROJECT labour rate requires value, source, source_date and scope")
    else:
        rate_ready = False
    labour_support_ready = labour_support_ready and rate_ready

    handoff = _require_object(record.get("economics_handoff"), "economics_handoff")
    pack_handoff = _require_object(handoff.get("packaging_cost_per_order"), "economics_handoff.packaging_cost_per_order")
    labour_handoff = _require_object(handoff.get("direct_labour_cost_per_order"), "economics_handoff.direct_labour_cost_per_order")
    pack_handoff_ev = _evidence(pack_handoff.get("evidence", "UNKNOWN"), "economics_handoff.packaging_cost_per_order")
    labour_handoff_ev = _evidence(labour_handoff.get("evidence", "UNKNOWN"), "economics_handoff.direct_labour_cost_per_order")
    _non_negative_number(pack_handoff.get("value"), "economics_handoff.packaging_cost_per_order.value")
    _non_negative_number(labour_handoff.get("value"), "economics_handoff.direct_labour_cost_per_order.value")

    if pack_handoff_ev == "VERIFIED_PROJECT" and not packaging_support_ready:
        raise ValueError("packaging handoff cannot be VERIFIED_PROJECT without verified packaging support")
    if labour_handoff_ev == "VERIFIED_PROJECT" and not labour_support_ready:
        raise ValueError("labour handoff cannot be VERIFIED_PROJECT without verified labour support")

    identity_ready = all((
        record.get("concept") not in (None, "", "UNKNOWN"),
        _nonempty(record.get("representative_order_id")),
        _nonempty(record.get("observation_date")),
        _nonempty(record.get("observer")),
    ))
    economics_handoff_ready = bool(
        identity_ready
        and packaging_support_ready
        and labour_support_ready
        and pack_handoff_ev == "VERIFIED_PROJECT"
        and pack_handoff.get("value") is not None
        and labour_handoff_ev == "VERIFIED_PROJECT"
        and labour_handoff.get("value") is not None
    )

    return {
        "status": "RECORD_VALID",
        "authority": "EVIDENCE_CAPTURE_ONLY",
        "commercial_pass_eligible": False,
        "identity_ready": identity_ready,
        "packaging_support_ready": packaging_support_ready,
        "labour_support_ready": labour_support_ready,
        "economics_handoff_ready": economics_handoff_ready,
    }


def main(path):
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    print(json.dumps(validate_record(payload), indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: representative_order_evidence.py <record.json>")
    main(sys.argv[1])
