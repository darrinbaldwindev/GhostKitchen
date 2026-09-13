# GhostKitchen — AgentOS Level-2 bounded acceptance workload

Status: READY AS NON-PRODUCTION FIXTURE
Date: 2026-09-13

## Purpose
Provide a real but harmless GhostKitchen project task for supervised AgentOS Level-2 Windows-worker acceptance. This is not a production kitchen action and does not authorize supplier contact, ordering, pricing publication, deployment, credentials, or customer writes.

## Exact workload
1. Inspect `docs/PILOT-MENU-EVIDENCE-PACKET-2026-09-04.md`.
2. Create or update only `fixtures/level2/ghostkitchen-evidence-status.txt`.
3. Preserve this exact four-line schema:
   - `project=ghostkitchen`
   - `source=PILOT-MENU-EVIDENCE-PACKET-2026-09-04.md`
   - `status=EVIDENCE_REQUIRED`
   - `production_write=false`
4. Verify the file content by rereading it.
5. Produce a diff showing no other project file changed.

## Acceptance
PASS requires bounded-root enforcement, exact task/mission/result correlation, one mutation only, durable before/after evidence, successful reread, clean replay/idempotency handling, and independent Green then PRS review. Any unexpected file change, missing receipt, stale head, replay ambiguity, or verification failure is FAIL/BLOCKED.

## Commercial truth boundary
The existing pilot evidence packet remains open pending project-specific supplier/account pricing, recipe/yield inputs, measured labour, packaging selection and delivery-test evidence. This workload must not convert UNKNOWN/HYPOTHESIS inputs into VERIFIED commercial claims.