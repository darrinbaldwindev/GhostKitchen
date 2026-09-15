# Ghost Kitchen — Representative Order Field-Test Packet

**Status:** READY FOR PHYSICAL EVIDENCE CAPTURE — not concept or commercial approval  
**Date:** 2026-09-15  
**Authority:** EVIDENCE_CAPTURE_ONLY

## Purpose

Convert the three current finalist concept families into one comparable physical test protocol whose results can be entered into `fixtures/evidence/representative-order-evidence.template.json`, validated by `tools/representative_order_evidence.py`, and only then handed toward GK-010 economics.

No value in this packet is VERIFIED_PROJECT until it is actually observed or supported by project-applicable evidence. Blank or unresolved values remain UNKNOWN and must never be replaced with zero.

## Test principles

Run the same evidence discipline for every concept. Testing a concept does not select it. Do not change the scoring standard after seeing a result. Record abnormal/rework observations rather than deleting them. Preserve invoices, quotes, photographs, timing notes or other evidence references used to support a record.

For each representative order create a unique `representative_order_id`, record observation date and observer, and use the canonical evidence classes: `VERIFIED_PROJECT`, `PUBLIC_REFERENCE`, `HYPOTHESIS`, `UNKNOWN`.

## Common test sequence

1. Define the exact representative order before timing begins.
2. Record each packaging component and exact SKU/description.
3. Record pack quantity, purchase/quote value, freight treatment, GST treatment, source and source date.
4. Record quantities actually used for the order.
5. Time active labour separately from elapsed appliance/cook time; identify concurrent work and rework.
6. Time final pack/QA work.
7. Close the order in its delivery configuration.
8. Assess the same packed order/configuration at T+20, T+30 and T+40 minutes where the protocol permits; otherwise prepare equivalent replicates and record that fact.
9. Record leakage, seal integrity, condensation, temperature observation, texture and presentation at every interval.
10. Calculate packaging and direct-labour handoff values only from captured support. Do not promote them to VERIFIED_PROJECT unless validator provenance requirements are met.
11. Run the completed JSON record through `tools/representative_order_evidence.py` before any economics handoff.

## FT-01 — Burgers / chicken

**Concept status:** finalist under test; not selected.

### Representative-order definition

Use one realistic single-customer meal order that exercises the concept's core delivery risks. The exact recipe/SKUs and selling price remain UNKNOWN until deliberately chosen and evidenced for the test.

Minimum order structure to record:
- one core burger or chicken main;
- one hot side if part of the intended proposition;
- sauces/condiments actually supplied;
- every primary/secondary packaging component.

### Packaging configurations to test

Prioritise the smallest set that can distinguish delivery performance:
- P1 compact burger clamshell for a single main where applicable;
- P3 compartment meal clamshell when separation of main/side is intended;
- P4 paperboard/corrugated box as the venting/presentation comparator.

Do not assume the cheapest configuration wins.

### Critical observations

Capture bun/breading texture, steam/condensation, grease migration, side crispness, component separation, leakage, seal/closure integrity, temperature observation and presentation at 20/30/40 minutes.

### Labour observations

Separate prep, active cook/finish, assembly, packaging/QA and dispatch-ready work. Mark concurrent work explicitly. Appliance dwell time is not automatically labour.

## FT-02 — Asian street food

**Concept status:** finalist under test; not selected.

### Representative-order definition

Use one realistic single-customer main or main-plus-side order representative of the intended concept. Exact dish, recipe/SKUs and selling price remain UNKNOWN until deliberately chosen and evidenced.

Minimum structure:
- one core hot main;
- rice/noodle/side component if integral to the proposition;
- sauces/garnishes actually supplied;
- every packaging component.

### Packaging configurations to test

Prioritise:
- P2 larger single-compartment meal clamshell;
- P3 compartment meal clamshell where wet/dry or main/side separation is operationally meaningful;
- P4 only when a paperboard format is plausible for the exact dish.

### Critical observations

Capture sauce leakage, lid/seal integrity, condensation, rice/noodle texture, fried-component texture where applicable, mixing/migration between components, temperature observation and presentation at 20/30/40 minutes.

### Labour observations

Separate batch/prep activity from per-order active finish, assembly, packaging/QA and dispatch-ready work. Record concurrency and attributable rework rather than allocating all batch elapsed time to one order.

## FT-03 — Healthy / protein bowls

**Concept status:** finalist under test; not selected.

### Representative-order definition

Use one realistic single-customer protein-bowl order with the intended hot/cold component structure. Exact recipe/SKUs and selling price remain UNKNOWN until deliberately chosen and evidenced.

Minimum structure:
- protein component;
- base/grain/salad components actually intended;
- dressing/sauce and toppings actually supplied;
- every packaging component.

### Packaging configurations to test

Prioritise:
- P2 larger meal container when components are intentionally combined;
- P3 compartment format when hot/cold, wet/dry or texture separation is important.

P1 is not a default bowl format. P4 should only be tested if the exact meal makes it plausible.

### Critical observations

Capture hot/cold migration, condensation, wilting, dressing leakage, component mixing, protein texture, temperature observation and presentation at 20/30/40 minutes.

### Labour observations

Separate batch prep from per-order portioning, finishing, assembly, packaging/QA and dispatch-ready work. Record whether portioning or multiple components create materially higher active labour.

## Evidence capture checklist per run

A run is incomplete until the record states or explicitly leaves UNKNOWN:

- concept and representative order ID;
- observation date and observer;
- exact packaging configuration;
- each packaging component/SKU and quantity used;
- pack quantity and purchase/quote value;
- freight and GST treatment;
- evidence source and source date;
- pack time;
- T+20, T+30 and T+40 observations;
- worker count;
- task-level active and elapsed labour;
- concurrency and abnormal/rework status;
- loaded hourly labour rate provenance if one is used;
- packaging cost/order handoff;
- direct labour cost/order handoff;
- evidence class for every promotable value.

## Comparison gate

Do not rank concepts from a single catalogue price or subjective tasting result. A concept becomes comparison-ready only after its representative order has a valid evidence record and enough comparable inputs exist for the broader economics gate.

The field-test packet itself cannot produce COMMERCIAL_PASS. A validator-ready record cannot produce COMMERCIAL_PASS. Final concept selection remains governed by GK-001/GK-002 and the concept/economics gates.

## Physical work still required

ChatGPT cannot perform the kitchen observations. The outstanding project evidence is therefore intentionally UNKNOWN until a human/authorised worker performs the runs and records the evidence. The immediate execution target is one controlled representative-order run for each of FT-01, FT-02 and FT-03 using the same capture discipline.