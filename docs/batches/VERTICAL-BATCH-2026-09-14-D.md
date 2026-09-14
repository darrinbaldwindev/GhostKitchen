# GhostKitchen Vertical Batch — 2026-09-14-D

## Purpose
Continue the owner-directed vertical-batch cadence after a fresh repository/CI/issue scan, advancing the deepest useful evidence dependency without duplicating open draft work or inventing project evidence.

## Fresh scan
- Canonical repository: `darrinbaldwindev/GhostKitchen`
- Exact starting `main` head: `8bcdcedc08df6c5aa5fb1c282e314b442d3800e8`
- Latest exact-head Economics validation: run `34821679841`, completed SUCCESS.
- Draft PR #32 remains open and independently covers economics batch metadata / per-input object hardening.
- Draft PR #27 (`normalize ghost-kitchen unit economics`) and draft PR #28 (`reconcile project state and missions`) are currently non-mergeable against current `main`; they are not treated as current source of truth.

## Vertical objective
Convert the highest-leverage packaging gap from a broad public-reference band into a dated, region-relevant candidate shortlist that is ready for physical delivery-resilience testing under `docs/PACKAGING-LABOUR-EVIDENCE-PROTOCOL-v1.md`.

Dependency chain:

`public packaging candidate evidence -> exact pack-out selection -> 20/30/40 minute physical test -> landed-cost validation -> VERIFIED_PROJECT packaging input -> GK-001 comparable unit economics`

## Batch tasks

### VD-01 — Reconcile existing packaging evidence
Status: COMPLETE

Observed:
- `docs/PACKAGING-COST-BENCHMARKS-2026-09-04.md` already contains Australian public price bands.
- `docs/PACKAGING-LABOUR-EVIDENCE-PROTOCOL-v1.md` defines the physical test and provenance requirements.
- Existing public bands are not landed GhostKitchen costs and remain `PUBLIC_REFERENCE`.

### VD-02 — Refresh region-relevant public references
Status: COMPLETE

Captured current public references for Queensland / Sunshine Coast applicability, including suppliers with Sunshine Coast/SEQ service or Australian delivery. New evidence remains `PUBLIC_REFERENCE` only.

### VD-03 — Create physical-test candidate packet
Status: COMPLETE

Created `docs/PACKAGING-CANDIDATE-PACKET-2026-09-14.md` with:
- candidate formats and public-reference prices;
- supplier/service notes;
- explicit freight/GST uncertainty;
- concept-fit hypotheses;
- selection rule for a small physical test set;
- exact evidence required before packaging cost can become `VERIFIED_PROJECT`.

### VD-04 — Preserve commercial gate
Status: COMPLETE

No supplier was contacted. No purchase was made. No public price was converted to `VERIFIED_PROJECT`. No packaging format, food concept or channel was commercially approved.

## Gate state after batch
- Economics calculator assurance: GREEN (narrow technical gate)
- Packaging public-reference shortlist: GREEN for decision-support research
- Packaging landed cost: UNKNOWN
- Packaging delivery resilience: UNKNOWN pending physical 20/30/40-minute tests
- Labour observations: UNKNOWN
- Concept comparison: AMBER / not approved
- Commercial PASS: BLOCKED

## Next safe vertical batch
Fresh-scan first. Then prefer one of:
1. narrow the packaging physical-test set to the fewest formats that cover all three concept candidates;
2. create a deterministic evidence-ingestion validator for representative-order evidence so malformed pilot records fail closed;
3. advance labour timing evidence only if it can be done without inventing observed measurements.

Do not contact suppliers, purchase, launch, deploy, select the final concept, or promote public references to project-verified costs without owner authorization and project evidence.
