# GHOST KITCHEN EVIDENCE CLOSURE MATRIX — 2026-09-14

## Purpose

Convert the current Ghost Kitchen concept/economics UNKNOWNs into a finite evidence-gathering program that feeds the deterministic channel-economics gate without promoting public references or hypotheses into verified project facts.

## Candidate concepts

- Burgers / chicken
- Asian street food
- Healthy / protein bowls

These remain candidates, not approved concepts.

## Evidence classes

- `VERIFIED_PROJECT` — measured, quoted, observed or otherwise validated for this project with source/date/scope recorded.
- `PUBLIC_REFERENCE` — externally published benchmark; useful for bounds, never sufficient by itself for commercial PASS.
- `HYPOTHESIS` — scenario assumption for decision support only.
- `UNKNOWN` — no acceptable numeric input yet.

## Required comparable inputs

| Input | Burgers / chicken | Asian street food | Healthy / protein bowls | Minimum closure evidence | Reusable across concepts? |
|---|---|---|---|---|---|
| Representative net customer revenue / AOV | UNKNOWN | UNKNOWN | UNKNOWN | Observed/tested representative order mix or approved menu-price test | Partly |
| Ingredient cost / order | UNKNOWN | UNKNOWN | UNKNOWN | Recipe BOM + supplier price + yield/waste basis | No |
| Packaging / order | UNKNOWN | UNKNOWN | UNKNOWN | Exact pack-out + supplier price + quantity used | Partly |
| Direct labour / order | UNKNOWN | UNKNOWN | UNKNOWN | Timed prep/cook/assemble/pack observation + loaded hourly labour basis | Method yes |
| Payment processing | UNKNOWN | UNKNOWN | UNKNOWN | Account/provider terms or validated chosen-channel rate | Yes |
| Channel commission / first-party channel cost | UNKNOWN | UNKNOWN | UNKNOWN | Account-specific terms or validated chosen channel contract | Yes |
| Business-funded delivery | UNKNOWN | UNKNOWN | UNKNOWN | Quote/contract/test for proposed radius and service level | Yes |
| Promotions / discounts | UNKNOWN | UNKNOWN | UNKNOWN | Explicit launch/steady-state policy or observed pilot rate | Yes |
| Refunds / cancellations | UNKNOWN | UNKNOWN | UNKNOWN | Pilot observation or explicitly conservative policy bound | Method yes |
| Variable waste | UNKNOWN | UNKNOWN | UNKNOWN | Yield/spoilage/remake observation | Method yes |
| Acquisition cost allocation | UNKNOWN | UNKNOWN | UNKNOWN | Measured campaign/customer acquisition evidence | Yes |

## Physical evidence packets

### Packet A — Recipe and portion economics

For each concept, define one representative order and record:

- ingredient/SKU;
- purchase unit and price;
- usable yield;
- portion quantity;
- per-order ingredient cost;
- waste allowance source;
- source/date/evidence class.

A spreadsheet-like number without recipe/yield provenance is not `VERIFIED_PROJECT`.

### Packet B — Packaging resilience and cost

For each representative order:

- exact container/bag/seal/label set;
- quantity used;
- pack cost;
- pack time;
- 20-minute hold result;
- 30-minute hold result;
- 40-minute hold result;
- leakage, condensation, temperature, texture and presentation notes;
- pass/fail/remake observations.

The cheapest packaging is not automatically the preferred packaging if delivery quality fails.

### Packet C — Labour timing

Observe separately:

- prep minutes;
- cook minutes involving active labour;
- assembly minutes;
- pack/QA minutes;
- remake/exception time where observed.

Record concurrent work explicitly so elapsed cook time is not automatically treated as labour minutes.

### Packet D — Channel and delivery

For each proposed channel/radius:

- order-channel fee basis;
- payment fee basis;
- delivery fee charged to business;
- customer delivery charge if any;
- delivery radius;
- minimums/surcharges;
- cancellation/refund treatment;
- source/date/evidence class.

Public marketplace pages remain `PUBLIC_REFERENCE` unless they are the actual applicable commercial terms for the project and validated accordingly.

### Packet E — Demand and AOV

Use a defined representative menu rather than category popularity alone. Capture:

- item prices;
- attach-rate hypothesis/test for sides/drinks;
- representative basket;
- customer-paid delivery, if any;
- discounts;
- resulting net customer revenue available to the business.

Do not use competitor menu price as project AOV without an explicit test rationale.

## Comparison-ready gate

A candidate may enter formal concept/economics comparison when:

1. one representative order is precisely defined;
2. every required economics input has an evidence class;
3. no missing field is silently replaced by zero;
4. all UNKNOWNs are paired with a named closure test/quote;
5. packaging and labour protocols are comparable across candidates;
6. the deterministic calculator can consume the resulting scenario without schema exceptions.

`COMPARISON_READY` does not mean `COMMERCIAL_PASS`.

## Commercial-pass gate

A scenario remains ineligible for commercial PASS while any required numeric input is `UNKNOWN`, `PUBLIC_REFERENCE` or `HYPOTHESIS` under the current deterministic calculator policy. A positive contribution result built from non-project evidence is decision support only.

## Highest-leverage closure order

1. **Packaging protocol and common supplier pack costs** — reusable across concepts and directly affects delivery suitability.
2. **Labour timing protocol** — same measurement method can be applied across all concepts.
3. **Channel/payment/delivery actual terms** — common economics inputs and potentially large contribution impact.
4. **Recipe BOM/yields** — concept-specific and essential to food cost.
5. **Representative AOV/order mix** — needed to prevent popularity from substituting for unit economics.
6. **Waste/refunds/CAC** — initially measured through controlled pilot evidence and kept UNKNOWN until observed or otherwise validated.

## Stop conditions

Stop and keep the field UNKNOWN if evidence requires an unauthorised purchase, supplier commitment, production launch, credential change, or external commercial commitment. Escalate the exact missing evidence rather than guessing it.
