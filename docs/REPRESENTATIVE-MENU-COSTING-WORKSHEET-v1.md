# Ghost Kitchen — Representative Menu Costing Worksheet v1

**Date:** 2026-09-04  
**Status:** Working capture worksheet / NOT validated recipe costing / NOT launch approval

## Purpose

Turn the existing public benchmark evidence into a comparable, auditable capture format for three candidate families without treating benchmarks as contracted supplier costs.

The three families selected for the first comparison are **burgers, chicken, and healthy/protein bowls**. This is a costing comparison only; it does not approve a concept.

## Evidence rules

- Every ingredient cost must identify supplier/product, pack size, price, date and GST treatment.
- Public benchmarks may be used as reasonableness checks, not as contracted landed costs.
- Unknown values remain `TBD` rather than being filled with optimistic assumptions.
- Yield/waste, packaging, labour and delivery must be separated from ingredient cost.
- A SKU is not commercially validated until the underlying inputs are independently evidenced.

## Candidate comparison

| Field | Burgers | Chicken | Healthy/protein bowls |
|---|---|---|---|
| Representative SKU | TBD | TBD | TBD |
| Bundle/AOV structure | TBD | TBD | TBD |
| Recipe ID/version | TBD | TBD | TBD |
| Ingredient cost/order | TBD | TBD | TBD |
| Packaging cost/order | TBD | TBD | TBD |
| Waste/yield allowance | TBD | TBD | TBD |
| Prep/cook/assembly minutes | TBD | TBD | TBD |
| Labour cost/order | TBD | TBD | TBD |
| Delivery/channel cost/order | TBD | TBD | TBD |
| Payment/platform cost/order | TBD | TBD | TBD |
| Selling price | TBD | TBD | TBD |
| Contribution/order | TBD | TBD | TBD |
| Contribution % | TBD | TBD | TBD |
| Evidence status | INCOMPLETE | INCOMPLETE | INCOMPLETE |

## Recipe-level capture

For each representative SKU, record one row per ingredient:

| SKU | Ingredient | Quantity | Unit | Supplier/product | Pack size | Current price | Price date | Yield % | Waste % | Extended cost | Evidence URL/reference |
|---|---|---:|---|---|---|---:|---|---:|---:|---:|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

**Extended ingredient cost formula:** `quantity ÷ pack quantity × current pack price ÷ yield factor`.

Do not use a benchmark price when a supplier-specific price is available.

## Order economics

For each representative SKU/bundle:

`Food cost = sum of validated ingredient extended costs`

`Variable operating cost = food cost + packaging + labour + delivery/channel + payment/platform fees + other directly variable costs`

`Contribution = selling price − variable operating cost`

`Contribution % = contribution ÷ selling price`

Where an input is unknown, the calculation should remain incomplete rather than silently assuming zero.

## Current evidence anchors

- Existing burger benchmark: approximately **A$5.22/serve** for standard pub-style burger raw ingredients, with component benchmarks. This is a market sanity check only.
- Existing chicken reference: frozen bulk chicken breast approximately **A$9.90/kg** from a public wholesale listing; not a project quote.
- Existing packaging references: current Australian public packaging benchmarks recorded in `docs/PACKAGING-COST-BENCHMARKS-2026-09-04.md`; not contracted landed costs.
- Existing delivery economics framework: `docs/DELIVERY-CHANNEL-ECONOMICS-WORKSHEET-2026-09-04.md`.

## Validation checklist

Before any candidate can support a pilot recommendation:

- [ ] Exact recipe and gram weights captured.
- [ ] Supplier/product identity captured for every material ingredient.
- [ ] Current supplier pricing independently evidenced.
- [ ] Yield/waste tested or conservatively evidenced.
- [ ] Packaging selected and cost tested.
- [ ] Prep/cook/assembly time measured.
- [ ] Labour rate and labour allocation validated.
- [ ] Selling price/AOV hypothesis justified.
- [ ] Delivery/channel/payment assumptions validated.
- [ ] Food-safety/compliance requirements checked for the actual menu.
- [ ] Contribution remains positive under conservative sensitivity cases.

## Decision boundary

This worksheet is an evidence-capture instrument. It does not select a finalist, approve a pilot, establish a franchise fee, or establish a launch price. Final concept selection requires evidence review and explicit decision logging.