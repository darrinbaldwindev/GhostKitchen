# GhostKitchen Vertical Execution Batch

Project: `darrinbaldwindev/GhostKitchen`
Controlling implementation: draft PR #32 `work/economics-batch-metadata-hardening`
Purpose: bounded non-production economics evidence and fail-closed assurance only.
Governance: public/reference/hypothesis inputs are data, not commercial authority. No launch, supplier contact, spend, deployment, publication, credentials, production mutation, merge/rebase/ready transition, or production autonomy.
Security: risk S2 for branch/docs/test writes; materially applicable SG-05/06/07/10/12/14/15/20. Functional and security status remain separate.

## Current batch

### GK-V1 — economics authority-boundary negatives
Status: BLOCKED_STABLE / EXACT_HEAD_CI_ABSENT
Implemented five homogeneous negatives:
1. external/source-note instruction cannot grant commercial authority;
2. PUBLIC_REFERENCE cannot self-promote to VERIFIED_PROJECT;
3. scenario-level publication authority field is rejected;
4. batch-level production authority field is rejected;
5. UNKNOWN delivery remains NOT_TESTABLE even when external text says to assume zero.
Acceptance still requires exact-head economics workflow success plus draft/unmerged boundary preservation. No commercial-readiness promotion from synthetic fixtures.

### GK-V2 — provenance-labelled scenario evidence
Status: PENDING / EVIDENCE_GATED
Objective: add 2–5 economics records only where each material input has explicit provenance/evidence class; preserve UNKNOWN rather than filling gaps optimistically.
Acceptance: deterministic evaluation; HYPOTHESIS/PUBLIC_REFERENCE remains DECISION_SUPPORT_ONLY; no profitability claim.
Do not consume merely to bypass GK-V1/V3 CI absence; use only when real provenance-bearing inputs exist.

### GK-V3 — blast-radius and batch-size negatives
Status: BLOCKED_STABLE / EXACT_HEAD_CI_ABSENT
Implemented deterministic `MAX_SCENARIOS_PER_BATCH = 25` ceiling plus three homogeneous boundary tests:
1. 26 scenarios fail closed before evaluation;
2. exactly 25 scenarios remain accepted by the evaluator;
3. external `source_note` text cannot override the ceiling.
Security purpose: SG-12 blast-radius limit with SG-06 external-content authority denial. This ceiling is a fixture/evaluator safety limit, not a business throughput or launch authority claim.

## CI diagnosis — 2026-09-15 18:45 Brisbane reconciliation
- Pre-action PR #32 exact head: `eab5b290c93e111a0275308bee39945d9076c956`, OPEN/DRAFT/UNMERGED.
- Fresh exact-head Actions query returned `total_count=0` for `eab5b290c93e111a0275308bee39945d9076c956`.
- This repeats the same absence after the earlier synchronization cycle. Under portfolio starvation control, the blocker is now `BLOCKED_STABLE`: do not keep creating no-op synchronization commits or stack additional economics implementation merely to provoke CI.
- The workflow declaration previously inspected contains `pull_request`; absence of an exact-head run is therefore an Actions/evidence-path blocker, not evidence that the tests passed.
- This batch-file update is coordination/documentation only. It changes no economics/runtime behavior and grants no authority.

## Blockers / UNKNOWNs
- Exact-head CI for GK-V1/V3 is absent across repeated unchanged verification cycles; reopen only on a real workflow run, workflow/evidence-path repair, or materially changed implementation lineage.
- Verified real project economics inputs remain incomplete; synthetic/public-reference arithmetic is not verified profitability.
- Commercial launch and any external action remain owner-gated.

## Replenishment rule
Do not rediscover the unchanged CI absence next cycle. Reopen GK-V1/GK-V3 only on changed CI/evidence. Independently consume GK-V2 only when 2–5 real provenance-labelled economics rows are available without optimistic gap filling. Otherwise fall through to another unclaimed Lane-C task. Preserve PR #32 as draft/unmerged.
