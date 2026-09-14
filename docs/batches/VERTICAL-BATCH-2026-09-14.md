# GhostKitchen Vertical Batch — 2026-09-14

## Purpose
Maximise useful progress per communication cycle by scanning current repository evidence first, selecting one vertical objective, executing bounded tasks, verifying exact evidence, and recording what remains blocked.

## Trigger
Run this workflow whenever the owner says `cont` or `continue autonomously`:
1. fresh-scan repository main, open issues/PRs, current CI and relevant evidence;
2. select the highest-value unblocked vertical objective;
3. avoid creating parallel mission/authority/governance systems;
4. execute a homogeneous batch of bounded work;
5. verify exact resulting repository state and CI where available;
6. record verified completion, failures, UNKNOWNs and next safe batch.

## Fresh scan — 2026-09-14

Canonical repository: `darrinbaldwindev/GhostKitchen`
Default branch: `main`
Fresh head observed before this batch: `ddfb2d872ca116b2cf18d3a98d53670b0c228237`

Verified current vertical:
- P0 issue #29 — deterministic delivery-channel contribution calculator.
- `tools/channel_economics.py` exists on main.
- `tests/test_channel_economics.py` exists on main.
- `fixtures/economics/channel-scenarios.sample.json` exists on main.
- `.github/workflows/economics-validation.yml` runs deterministic tests and renders sample scenarios.
- latest scanned Economics validation run on head `ddfb2d872ca116b2cf18d3a98d53670b0c228237` completed SUCCESS.

## Batch objective
Harden the P0 economics calculator's fail-closed numeric-input boundary without changing commercial assumptions, selecting a concept/channel, or promoting public/hypothesis evidence to verified project evidence.

## Tasks

### VB-01 — Non-finite numeric hardening
Status: IN PROGRESS

Acceptance:
- NaN and +/-Infinity cannot enter contribution calculations;
- rejection is deterministic and field-specific;
- no non-finite input can become commercial-pass eligible.

### VB-02 — Deterministic regression tests
Status: IN PROGRESS

Acceptance:
- tests cover NaN, positive infinity and negative infinity;
- existing public-reference/hypothesis/UNKNOWN safeguards remain intact;
- test output remains deterministic.

### VB-03 — Exact-head CI verification
Status: PENDING

Acceptance:
- GitHub Actions run for the resulting exact head is inspected;
- SUCCESS is claimed only when observed;
- failure is recorded rather than inferred away.

### VB-04 — Issue/evidence checkpoint
Status: PENDING

Acceptance:
- resulting evidence is linked back to active P0 issue #29 where tooling permits;
- no overall commercial GREEN is claimed;
- next safe batch is named from fresh evidence.

## Guardrails
- No franchise pricing, royalty or earnings claim.
- No concept or delivery-channel launch approval.
- No supplier contact, purchase, credential change, deployment or production write.
- No invented supplier quote, labour study, CAC, AOV or account-specific platform term.
- `VERIFIED_PROJECT` remains a deliberately high evidence class; public references and hypotheses remain decision-support only.
- Repo/CI evidence controls completion.

## Execution log
- Batch file created after fresh repository, issue, test/tool and CI scan.
- Baseline CI observed SUCCESS at head `ddfb2d872ca116b2cf18d3a98d53670b0c228237`.
