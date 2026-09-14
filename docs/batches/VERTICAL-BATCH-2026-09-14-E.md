# GhostKitchen Vertical Batch — 2026-09-14-E

## Purpose
Continue the owner-directed vertical-batch cadence after a fresh exact-head / issue / PR scan, advancing the representative-order evidence boundary without inventing project observations or commercial facts.

## Fresh scan
- Canonical repository: `darrinbaldwindev/GhostKitchen`
- Exact starting `main` head: `9de30860d8cdee66881fe7d48185054388b333d5`
- `fixtures/evidence/representative-order-evidence.template.json` exists as capture structure but, before this batch, had no deterministic ingestion validator.
- Draft PR #32 remains open and overlaps economics metadata hardening; this batch does not duplicate or merge that work.
- No supplier contact, purchase, physical observation, concept selection, launch or deployment is authorised by this batch.

## Vertical objective
Make representative-order evidence fail closed before it can be handed into unit economics.

Dependency chain:

`captured pilot record -> deterministic structure/evidence validation -> support-proven economics handoff -> channel economics -> project decision`

The validator may declare an evidence handoff structurally ready. It can never declare commercial PASS.

## Tasks

### VE-01 — Add deterministic evidence validator
Status: COMPLETE

Created `tools/representative_order_evidence.py`.

Controls include:
- exact capture authority must remain `EVIDENCE_CAPTURE_ONLY`;
- `commercial_pass_eligible` must remain false;
- unknown top-level keys fail closed;
- evidence classes restricted to `VERIFIED_PROJECT`, `PUBLIC_REFERENCE`, `HYPOTHESIS`, `UNKNOWN`;
- non-negative finite numeric fields;
- active labour seconds cannot exceed elapsed seconds;
- hold-test minutes constrained to 20/30/40 and cannot duplicate;
- a `VERIFIED_PROJECT` packaging handoff requires verified packaging support/provenance;
- a `VERIFIED_PROJECT` labour handoff requires verified labour observations and loaded-rate provenance;
- handoff readiness requires representative-order identity fields and both supported economics inputs.

### VE-02 — Add adversarial tests
Status: COMPLETE

Created `tests/test_representative_order_evidence.py` covering:
- untouched template remains valid capture-only and not handoff-ready;
- authority escalation rejected;
- commercial-pass flag escalation rejected;
- unknown top-level field rejected;
- invalid evidence class rejected;
- unsupported verified packaging handoff rejected;
- unsupported verified labour handoff rejected;
- impossible labour timing rejected;
- duplicate hold interval rejected;
- fully supported synthetic fixture can become economics-handoff-ready while still remaining commercially ineligible.

Synthetic test data is test-only and is not project evidence.

### VE-03 — Integrate validator into CI
Status: IN PROGRESS

The existing Economics validation workflow already runs all `test_*.py`; this batch also adds explicit rendering/validation of the representative-order template so CLI integrity is exercised on every workflow run.

### VE-04 — Preserve evidence/commercial boundary
Status: COMPLETE

This batch does not calculate a project packaging cost, labour cost, AOV, contribution margin or concept PASS. It adds an integrity gate only.

## Gate state
- Evidence record structural validator: implemented
- Evidence adversarial tests: implemented
- Economics handoff: BLOCKED until real project evidence satisfies support rules
- Packaging physical tests: UNKNOWN / not performed
- Labour observations: UNKNOWN / not performed
- Concept selection: AMBER / not approved
- Commercial PASS: BLOCKED

## Next safe vertical
After exact-head CI verification, advance actual evidence collection readiness rather than inventing observations. Preferred next dependency is a concept-specific representative-order test packet that can be printed/executed physically and later fed through this validator.
