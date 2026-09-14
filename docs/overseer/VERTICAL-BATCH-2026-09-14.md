# GHOST KITCHEN VERTICAL BATCH — 2026-09-14

**Mode:** fresh repo scan → dense dependent batch → execute → verify → leave next gate

## Trigger convention

Whenever the owner says `cont` or `continue autonomously`, the Ghost Kitchen Overseer should:

1. scan the canonical repository and current issues/PRs/CI first;
2. reconcile claims against exact-head evidence;
3. choose the deepest useful batch along one dependency chain rather than scattering work horizontally;
4. execute all safe non-production work possible in that batch;
5. verify outputs with repository/CI evidence;
6. record completed work, remaining UNKNOWNs, blockers and the next smallest safe batch in-repo.

Do not merge, deploy, make purchases, contact suppliers, alter credentials, approve commercial launch, or turn hypotheses/public benchmarks into verified project evidence without owner authority and evidence.

## Fresh scan snapshot

Exact repository tree head at batch start: `ddfb2d872ca116b2cf18d3a98d53670b0c228237`.

Verified present on `main`:

- `tools/channel_economics.py`
- `tests/test_channel_economics.py`
- `fixtures/economics/channel-scenarios.sample.json`
- `.github/workflows/economics-validation.yml`
- menu/economics/packaging/channel evidence worksheets
- AgentOS Level-2 bounded workload fixture
- open draft PRs #27 and #28
- open issue #29 (`GK-010`) for deterministic delivery-channel contribution calculation

Latest Economics validation run observed for exact head `ddfb2d872ca116b2cf18d3a98d53670b0c228237`: **SUCCESS**.

## Reconciliation finding

The negative-assurance sequence previously queued in GK-010 is now materially covered on `main`:

- PUBLIC_REFERENCE/HYPOTHESIS inputs cannot produce commercial PASS;
- UNKNOWN required inputs produce `NOT_TESTABLE`;
- multiple UNKNOWNs are reported deterministically;
- invalid evidence classes fail closed;
- zero revenue cannot pass;
- negative revenue/costs are rejected;
- positive VERIFIED_PROJECT contribution can become pass-eligible;
- negative VERIFIED_PROJECT contribution cannot pass;
- duplicate/missing scenario IDs fail closed;
- non-numeric required values fail closed with field identity;
- unknown input/scenario/batch keys fail closed;
- empty batch is explicit and non-commercial;
- scenario ordering and rounding are deterministic.

This is a **narrow calculator/assurance GREEN only**. It is not a commercial GREEN and does not select a concept, supplier, kitchen, channel or franchise price.

## Vertical batch objective

Advance the critical dependency chain:

`GK-010 calculator assurance → GK-001 verified input closure → GK-002 concept comparison → GK-003 pilot operating design`

The highest-value work now is not more hypothetical scenarios. It is replacing the UNKNOWN/HYPOTHESIS fields required by the calculator with project evidence for a small comparable concept set.

## Batch missions

### VB-01 — Freeze the calculator gate

**Outcome:** treat current calculator behavior as the decision-support gate unless a new defect/evidence requirement appears.

Acceptance:

- exact-head CI success recorded;
- no public/hypothesis-only scenario can be promoted to commercial PASS;
- future changes must preserve evidence provenance and fail-closed behavior.

### VB-02 — Create one evidence-closure matrix

**Outcome:** one source tells workers exactly what must be measured/quoted before a concept can become testable with project evidence.

Candidate set for closure:

1. burgers/chicken;
2. Asian street food;
3. healthy/protein bowls.

Required project-evidence dimensions:

- net customer revenue / representative AOV;
- ingredient cost per representative order;
- packaging cost per representative order;
- direct labour minutes and loaded labour cost per order;
- payment processing;
- channel commission or first-party channel cost;
- business-funded delivery cost where applicable;
- discount/promotion allowance;
- refund/cancellation allowance;
- variable waste allowance;
- acquisition cost / CAC allocation.

Each value must carry source, date, scope, unit and evidence class. Missing values stay `UNKNOWN`.

### VB-03 — Run concept/economics gate only when comparable

Do not name a winner merely because one candidate has more evidence collected.

A concept is `COMPARISON_READY` only when the required dimensions above are either:

- `VERIFIED_PROJECT`, or
- deliberately marked `UNKNOWN` with an explicit test/quote required to close it.

A commercial PASS remains ineligible while required values are UNKNOWN, PUBLIC_REFERENCE or HYPOTHESIS.

### VB-04 — Convert unresolved fields into physical pilot tests

Highest-value field evidence to obtain next:

- recipe build and portion yield;
- packaging pack-out cost and 20/30/40-minute hold quality;
- hands-on prep/cook/pack labour timing;
- delivery quote/cost for proposed radius;
- representative menu AOV observation/test;
- waste and spoilage observation;
- refund/remake failure modes.

### VB-05 — Only then unlock operating-template design

GK-003 should consume the selected/shortlisted concept's measured workflow. It should not invent generic SOP timings that later become mistaken for validated operations.

## Execution completed in this batch

- fresh recursive repo scan completed;
- current project-state document checked and identified as stale (`Last updated: 2026-08-31`) relative to live implementation;
- live GK-010 issue/comments reconciled;
- current calculator implementation inspected;
- current test suite inspected;
- exact-head workflow history checked;
- latest `main` Economics validation at `ddfb2d872ca116b2cf18d3a98d53670b0c228237` verified SUCCESS;
- vertical dependency chain selected;
- evidence-closure matrix created alongside this batch file.

## Current gate state

- Calculator deterministic assurance: **GREEN (narrow)**
- Unit-economics project evidence: **AMBER / incomplete**
- Concept selection: **AMBER / not approved**
- Pilot operating template: **BLOCKED on comparable concept evidence**
- Franchise economics/pricing: **BLOCKED**
- Production launch: **BLOCKED**

## Next autonomous batch

Start by scanning again. If the calculator/CI remains healthy, do not repeat GK-010 assurance mechanically. Work the evidence-closure matrix top-down, prioritising the field whose closure reduces the most uncertainty across all three candidate concepts. Prefer common inputs and reusable measurement protocols before concept-specific detail.
