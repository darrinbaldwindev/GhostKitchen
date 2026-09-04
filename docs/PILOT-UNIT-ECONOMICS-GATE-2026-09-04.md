# Ghost Kitchen — Pilot Unit Economics Gate

**Date:** 2026-09-04  
**Status:** Decision-support gate — NOT launch approval  
**Purpose:** Convert the existing costing and delivery evidence into a deterministic input/decision gate without inventing missing commercial assumptions.

## Evidence currently available

| Input | Current evidence | Decision use |
|---|---|---|
| Burger raw-ingredient benchmark | A$5.22/serve market benchmark | Sanity check only |
| Frozen bulk chicken breast | A$9.90/kg public wholesale listing | Ingredient reference only |
| Foodservice chicken bites | A$24.90/kg MSRP; published volume discounts | Prepared-chicken reference only |
| DoorDash Marketplace | 30% published AU benchmark | Channel sensitivity input |
| DoorDash Online Ordering | 0% commission; 1.75% + A$0.30 card processing; A$5.50 delivery benchmark | Direct-order sensitivity input |
| DoorDash Drive On-Demand | A$6.99–A$10.99 published delivery benchmark | Delivery sensitivity input |
| Uber Direct | Fixed fee + distance; account quote required | Unresolved input |

These are dated public references, not contracted project costs. They must not be promoted to supplier quotes, account terms, or validated recipe costs.

## Required input register

A finalist cannot receive a commercial PASS until each required field is populated with evidence or an explicitly labelled hypothesis:

1. Candidate family and representative SKU.
2. Recipe ingredient quantities and yields.
3. Exact supplier/product identity and current price/date.
4. Packaging item and tested per-order cost.
5. Prep/cook/assembly minutes.
6. Labour rate and labour/order.
7. Selling price and AOV hypothesis.
8. Payment processing cost.
9. Delivery distance/radius and channel cost.
10. Customer-paid delivery amount, if applicable.
11. Discount/promotion allowance.
12. Refund/cancellation allowance.
13. Variable waste allowance.
14. Customer acquisition cost/order.
15. Food-safety/compliance checks for the actual menu.

## Deterministic calculation

For each SKU and bundle:

```text
net customer revenue
- ingredient cost
- packaging
- labour
- payment processing
- channel commission
- business-funded delivery
- discounts/promotions
- refunds/cancellations
- variable waste
- acquisition cost
= contribution per order
```

```text
contribution margin % = contribution per order / net customer revenue
monthly contribution = contribution per order × monthly orders
```

## Sensitivity protocol

Run three cases without silently changing evidence class:

- **Conservative:** adverse but evidence-bounded values for delivery, food cost, labour, AOV and acquisition.
- **Base:** best-supported current inputs, with hypotheses clearly marked.
- **Strong:** favourable values that remain commercially plausible and explicitly labelled as hypotheses until validated.

A concept/channel must not PASS because of a single headline commission or a favourable AOV assumption.

## Gate logic

| Gate | PASS condition | Current status |
|---|---|---|
| Recipe costing | Recipe-level quantities + supplier/product evidence | OPEN |
| Packaging | Tested cost allocated to SKU/order | OPEN |
| Labour | Time study + rate | OPEN |
| AOV/price | Evidence-backed hypothesis | OPEN |
| Delivery | Channel/radius cost evidenced | PARTIAL |
| Payment | Account/processor terms evidenced | OPEN |
| Acquisition | Testable CAC assumption/evidence | OPEN |
| Compliance | Actual menu requirements checked | OPEN |
| Contribution | Positive under conservative case | NOT TESTABLE YET |

## Current decision

**No finalist or delivery channel is approved.** Existing public benchmarks are sufficient to structure the calculation but insufficient to establish project-level unit economics.

The highest-value next evidence capture is the smallest representative menu set for at least three candidate families, using exact supplier products, recipe weights, packaging, labour time and a defined delivery radius. That dataset can then be run through this gate without changing the evidence boundary.

## Safety / governance boundary

- No production launch or supplier commitment is implied.
- No food-safety or regulatory conclusion is made without the actual menu and operating jurisdiction.
- No account-specific delivery or payment term is inferred from public pricing.
- No weighted concept score should be finalised from this gate until required inputs are evidenced.
