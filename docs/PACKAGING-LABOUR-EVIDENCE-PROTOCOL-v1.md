# Packaging & Labour Evidence Protocol v1

**Status:** working validation protocol  
**Date:** 2026-09-14  
**Applies to:** burgers/chicken, Asian street food, healthy/protein bowls  

## Purpose
Create comparable project evidence for two high-leverage Ghost Kitchen economics inputs: packaging cost/performance and direct labour per order. This protocol does not select a concept and does not establish commercial viability by itself.

## Evidence rule
A measured value may be labelled `VERIFIED_PROJECT` only when the observation, source, date, scope and unit basis are recorded. Published supplier listings or generic benchmarks are `PUBLIC_REFERENCE`; planning values are `HYPOTHESIS`; absent or unsuitable evidence is `UNKNOWN`.

# A. Packaging protocol

## A1. Representative order definition
Before testing, record:
- concept;
- representative order ID;
- exact food components and portions;
- target service temperature where relevant;
- planned delivery/hold duration;
- packaging configuration ID.

Do not compare packaging across materially different orders without recording the difference.

## A2. Exact pack-out record
For every packaging configuration, record each component separately:
- container/tray/bowl/clamshell;
- lid;
- liner/wrap;
- sauce cup/lid;
- cutlery/napkin where used;
- tamper seal/label;
- carry bag;
- insulation/venting element if used;
- quantity consumed per order.

For each component capture supplier/source, SKU/description, pack quantity, purchase price or quote, freight treatment, GST treatment if known, source date and evidence class.

### Packaging cost formula
`packaging_cost_per_order = sum(component landed unit cost × quantity used)`

If freight, GST treatment or quantity basis is unresolved, do not promote the result to VERIFIED_PROJECT.

## A3. Pack-time observation
Measure active labour required to:
1. retrieve packaging;
2. load product;
3. add condiments/sides;
4. seal/tamper-proof;
5. label/check;
6. bag for dispatch.

Record at least three observations per configuration when practical. Record rework separately rather than averaging it invisibly into normal pack time.

## A4. Hold/delivery resilience test
Observe the same packed order at:
- T+0 minutes;
- T+20 minutes;
- T+30 minutes;
- T+40 minutes.

Where feasible, mimic realistic transport motion and orientation rather than leaving the order untouched on a bench.

At each checkpoint record:
- leakage/spillage: none/minor/material/fail;
- seal integrity: pass/fail;
- condensation: none/low/moderate/high;
- food temperature or qualitative temperature observation;
- texture degradation;
- sogginess/crispness loss where relevant;
- component migration/mixing;
- presentation on opening;
- odour containment;
- container deformation;
- customer usability;
- remake/refund risk assessment;
- overall checkpoint result: PASS / MARGINAL / FAIL.

A lower-cost pack-out cannot win the comparison if it produces unacceptable delivery quality.

## A5. Packaging acceptance gate
A packaging configuration is `PACKAGING_TESTED` only when:
- exact pack-out is recorded;
- cost provenance is recorded;
- pack time has been observed;
- 20/30/40-minute checks are complete or an explicit shorter target radius is justified;
- failure observations are retained rather than discarded;
- evidence class is explicit.

`PACKAGING_TESTED` is not a commercial PASS.

# B. Labour protocol

## B1. Labour categories
Record active human labour separately as:
- batch/prep labour;
- order-specific prep;
- active cook labour;
- assembly;
- packaging/QA;
- dispatch handoff;
- cleaning directly attributable to the order/test;
- remake/exception labour.

## B2. Concurrency rule
Elapsed appliance/cook time is not automatically labour time. For each interval record whether the worker is:
- actively handling the order;
- handling another order/task concurrently;
- waiting but unavailable for other work;
- fully available for other productive work.

This prevents a 10-minute passive oven/fryer interval from being recorded as 10 minutes of direct labour without evidence.

## B3. Timing method
For each representative order:
1. use a unique observation ID;
2. record worker count;
3. record start/end timestamp for each active task;
4. record parallel tasks explicitly;
5. flag training/test abnormalities;
6. record remake/exception activity separately;
7. repeat enough times to distinguish a one-off observation from a stable process.

Do not suppress slow or failed observations merely because they are inconvenient.

## B4. Labour-cost conversion
Direct labour cost may be calculated only when a loaded hourly labour basis is available with scope and provenance.

`direct_labour_cost_per_order = active_labour_minutes / 60 × loaded_hourly_labour_rate`

Until the applicable loaded hourly labour basis is project-validated, the labour-cost input remains UNKNOWN even if minutes have been measured.

## B5. Labour acceptance gate
A representative order is `LABOUR_TIMED` only when:
- task categories are separated;
- active vs passive/concurrent time is explicit;
- worker count is known;
- abnormal/rework observations are retained;
- source/date/observer/test conditions are recorded.

# C. Cross-concept comparison rules

Use the same measurement definitions for all candidate concepts. Compare at minimum:
- packaging cost/order;
- packaging active seconds/order;
- 20/30/40-minute resilience;
- active labour minutes/order;
- remake/exception incidence observed during tests;
- operational complexity notes.

Do not rank a concept commercially from packaging/labour evidence alone. These results feed the broader recipe, channel, AOV, waste, refunds and CAC economics gate.

# D. Fail-closed rules

Keep an economics field `UNKNOWN` when:
- evidence is missing;
- a quoted/listed price cannot be mapped to actual quantity used;
- freight or other material landed-cost treatment is unknown;
- labour minutes are inferred rather than observed;
- loaded wage basis is not applicable/validated;
- a test result cannot be tied to the representative order and packaging configuration.

Never replace UNKNOWN with zero.
