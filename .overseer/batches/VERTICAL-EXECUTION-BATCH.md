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
Implementation lineage: `256dfa7193da8a5e9c7713cb6bdbce23c83f218b` -> `1b8182b53ffbbf78d7aadcc1241b5a19d1777a03`.
Implemented deterministic `MAX_SCENARIOS_PER_BATCH = 25` ceiling plus three homogeneous boundary tests:
1. 26 scenarios fail closed before evaluation;
2. exactly 25 scenarios remain accepted by the evaluator;
3. external `source_note` text cannot override the ceiling.
Security purpose: SG-12 blast-radius limit with SG-06 external-content authority denial. This ceiling is a fixture/evaluator safety limit, not a business throughput or launch authority claim.
Verification: exact-head Actions query for `1b8182b5...` returned zero runs; no predecessor CI borrowed.

## Blockers / UNKNOWNs
- Exact-head CI for GK-V1/V3 remains pending/absent.
- Verified real project economics inputs remain incomplete; synthetic/public-reference arithmetic is not verified profitability.
- Commercial launch and any external action remain owner-gated.

## Replenishment rule
On the next cycle: fresh-scan PR #32 and exact-head CI first. If the exact changed head receives a clean economics workflow, promote only the tested bounded fixture scope. Then consume GK-V2 with 2–5 provenance-labelled economics rows only where evidence exists. If CI remains absent, diagnose workflow trigger/Actions state rather than stacking unrelated implementation. Preserve PR #32 as draft/unmerged.
