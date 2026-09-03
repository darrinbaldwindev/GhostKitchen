# Ghost Kitchen Delivery Template — Delivery Channel Economics Worksheet

**Date:** 2026-09-04  
**Status:** Decision-support worksheet — NOT a launch approval  
**Purpose:** Turn current published delivery-channel pricing into a comparable calculation structure for GK-009/GK-001 without inventing AOV, food cost, labour, acquisition or delivery assumptions.

## Channel scenarios

| Scenario | Revenue / order | Channel cost | Delivery cost | Payment cost | Acquisition allowance | Customer delivery charge | Direct-customer value | Status |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Marketplace + platform delivery | INPUT | 30% benchmark* | Included/verify | INPUT | INPUT | INPUT | Lower | TEST |
| Direct order + DoorDash Online Ordering | INPUT | 0% commission | AU$5.50/order* | 1.75% + AU$0.30* | INPUT | INPUT | Higher | TEST |
| Direct order + DoorDash Drive On-Demand | INPUT | 0% commission | $6.99–$10.99 published benchmark* | INPUT | INPUT | INPUT | Higher | TEST |
| Direct order + Uber Direct | INPUT | 0% marketplace commission | Fixed fee + distance; account quote required | INPUT | INPUT | INPUT | Higher | TEST |
| Customer-paid delivery | INPUT | INPUT | INPUT | INPUT | INPUT | CUSTOMER PAYS | Highest | TEST |

\* Public Australian pricing checked 2026-09-04. These are reference inputs, not account-specific contractual terms; revalidate before launch.

## Calculation

For each scenario:

```text
Net customer revenue
- food / ingredient cost
- packaging
- payment processing
- channel commission
- delivery cost absorbed by business
- discounts / promotions
- refund / cancellation allowance
- variable waste
- acquisition allowance
= contribution per order
```

Then calculate:

```text
contribution margin % = contribution per order / net customer revenue
monthly contribution = contribution per order × monthly orders
```

## Required sensitivity cases

Run Conservative / Base / Strong cases for at least:

- AOV
- food cost %
- packaging cost
- labour/order
- order volume
- delivery cost
- customer-paid delivery amount
- acquisition cost/order
- refund/cancellation rate

Do not select a channel using headline commission alone.

## Evidence boundary

Current published DoorDash evidence states Marketplace delivery is 30%, Pickup 15%; Online Ordering is commission-free with 1.75% + AU$0.30 card processing and AU$5.50 delivery; Drive On-Demand is a flat delivery fee and a separate DoorDash page currently publishes $6.99–$10.99 per delivery. Uber Eats publicly describes Marketplace pricing as plan-dependent and offers Uber Direct/online-ordering alternatives; exact account pricing must be verified during onboarding.

Sources checked 2026-09-04:
- DoorDash AU merchant pricing: https://merchants.doordash.com/en-au/pricing
- DoorDash AU Drive On-Demand: https://merchants.doordash.com/en-au/products/drive-on-demand
- Uber Eats AU merchant signup/pricing: https://merchants.ubereats.com/au/en/s/signup/

## Gate

This worksheet does not approve a channel. A channel recommendation requires actual pilot assumptions/evidence for AOV, recipe cost, packaging, labour, delivery distance, payment costs, acquisition and customer-paid delivery behaviour.
