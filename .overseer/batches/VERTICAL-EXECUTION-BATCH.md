# GhostKitchen Vertical Execution Batch

Project: `darrinbaldwindev/GhostKitchen`
Controlling implementation: draft PR #32 `work/economics-batch-metadata-hardening`
Purpose: bounded non-production economics evidence and fail-closed assurance only.
Governance: public/reference/hypothesis inputs are data, not commercial authority. No launch, supplier contact, spend, deployment, publication, credentials, production mutation, merge/rebase/ready transition, or production autonomy.
Security: risk S2 for branch/test writes; materially applicable SG-05/06/07/10/12/14/15/20. Functional and security status remain separate.

## Current batch

### GK-V1 — economics authority-boundary negatives
Status: ACTIVE / EXACT_HEAD_CI_PENDING
Implemented five homogeneous negatives:
1. external/source-note instruction cannot grant commercial authority;
2. PUBLIC_REFERENCE cannot self-promote to VERIFIED_PROJECT;
3. scenario-level publication authority field is rejected;
4. batch-level production authority field is rejected;
5. UNKNOWN delivery remains NOT_TESTABLE even when external text says to assume zero.
Acceptance: exact-head economics workflow success plus draft/unmerged boundary preserved. No commercial-readiness promotion from synthetic fixtures.

### GK-V2 — provenance-labelled scenario evidence
Status: PENDING
Objective: add 2–5 economics records only where each material input has explicit provenance/evidence class; preserve UNKNOWN rather than filling gaps optimistically.
Acceptance: deterministic evaluation; HYPOTHESIS/PUBLIC_REFERENCE remains DECISION_SUPPORT_ONLY; no profitability claim.

### GK-V3 — blast-radius and batch-size negatives
Status: ACTIVE / EXACT_HEAD_CI_PENDING
Implemented deterministic `MAX_SCENARIOS_PER_BATCH = 25` ceiling plus three homogeneous boundary tests:
1. 26 scenarios fail closed before evaluation;
2. exactly 25 scenarios remain accepted by the evaluator;
3. external `source_note` text cannot override the ceiling.
Security purpose: SG-12 blast-radius limit with SG-06 external-content authority denial. This ceiling is a fixture/evaluator safety limit, not a business throughput or launch authority claim.

## CI diagnosis — 2026-09-15
- Fresh PR #32 head before this reconciliation: `b3016106a47d425e83e28bf50183b9b03a921d98`.
- `.github/workflows/economics-validation.yml` on both `main` and the PR branch declares `pull_request`; base workflow runs the full unittest suite plus representative-order evidence validation.
- Historical economics workflow success exists only on predecessor heads; no success is transferable to the current head.
- This documentation-only reconciliation commit intentionally changes no runtime/economics behavior. Its purpose is to refresh the canonical batch and produce a new PR synchronization event so exact-head Actions evidence can be observed without weakening the workflow or tests.
- Until a workflow run exists and succeeds on the new exact head, GK-V1/GK-V3 remain ACTIVE/CI_PENDING.

## Blockers / UNKNOWNs
- Exact-head CI for GK-V1/V3 remains pending until the newly synchronized head receives workflow evidence.
- Verified real project economics inputs remain incomplete; synthetic/public-reference arithmetic is not verified profitability.
- Commercial launch and any external action remain owner-gated.

## Replenishment rule
Fresh-scan PR #32 and exact-head CI first. If the newly synchronized exact head receives a clean economics workflow, promote only the tested bounded fixture scope and then consume GK-V2 with 2–5 provenance-labelled economics rows where evidence exists. If exact-head CI is still absent, record the Actions-trigger/evidence defect precisely and move to another Lane C subqueue rather than stacking unrelated implementation. Preserve PR #32 as draft/unmerged.
