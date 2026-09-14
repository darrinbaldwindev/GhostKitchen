# GhostKitchen Vertical Batch — 2026-09-14-C

## Trigger
Owner instruction: `continue autonomously`.

## Fresh-scan baseline
- Canonical repo: `darrinbaldwindev/GhostKitchen`
- Default branch: `main`
- Fresh scanned tree head: `4b217247b73eefcf96f2bfb0140c9150ab4d28a1`
- Active economics implementation: `tools/channel_economics.py`
- Open draft PR #32 already covers input-item key hardening, batch metadata validation, and deterministic evidence summaries.
- PR #32 exact head `c1892e6b5f4489b62f613f827bea3bd714275009` has Economics validation run `34815445008` SUCCESS.
- Open batch issue #33 overlaps PR #32's already-implemented input-item hardening; do not duplicate that work on main.

## Vertical objective
Advance GK-001/GK-002 from calculator assurance into reusable project-evidence capture by standardising packaging and labour measurements for all three candidate concepts.

Candidate concepts remain unapproved:
1. burgers / chicken;
2. Asian street food;
3. healthy / protein bowls.

## Batch tasks

### C-01 — Packaging evidence protocol
Create a comparable hold/delivery-quality protocol covering exact pack-out, unit cost provenance, pack time, leakage, condensation, temperature/texture/presentation observations and 20/30/40-minute checks.

Acceptance:
- no price is treated as VERIFIED_PROJECT without project-specific source/date/scope;
- protocol is identical across candidate concepts where practical;
- packaging quality failure cannot be hidden by lower unit cost.

### C-02 — Labour evidence protocol
Create an observation protocol separating prep, active cook labour, assembly, pack/QA and exception/remake work, with concurrency recorded so elapsed cook time is not misclassified as direct labour.

Acceptance:
- direct labour minutes are observable and auditable;
- loaded hourly labour rate remains UNKNOWN until project-specific basis is supplied;
- same method applies across concepts.

### C-03 — Structured evidence capture template
Create a machine-readable but non-authoritative capture template that records source/date/evidence class and preserves UNKNOWN rather than silently substituting zero.

Acceptance:
- template cannot itself imply commercial PASS;
- every captured numeric field carries evidence class and source metadata;
- unresolved fields remain explicitly UNKNOWN.

### C-04 — Mission-control handoff
Record the batch outcome against active economics/concept mission control, noting that this is evidence preparation rather than concept selection.

## Guardrails
- No concept/channel approval.
- No supplier commitment or purchase.
- No invented supplier quote, labour rate, AOV, waste, refund or CAC.
- No franchise fee/royalty/earnings claim.
- No deployment or production launch.
- PR #32 remains draft/unmerged; this batch does not merge or ready it.

## Execution result
- [x] fresh repository/issue/PR/CI scan
- [x] concurrency/duplication reconciliation with PR #32 and issue #33
- [x] packaging + labour protocol created
- [x] structured evidence capture template created
- [x] mission-control handoff recorded

## Next safe vertical
Run actual evidence collection against the protocol. Highest-value closure order remains packaging pack-out/hold tests, labour timing observations, applicable payment/channel/delivery terms, recipe BOM/yields, representative AOV, then waste/refunds/CAC. Until measurements/quotes exist, calculator inputs remain UNKNOWN or decision-support evidence only.
