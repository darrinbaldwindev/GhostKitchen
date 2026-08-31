# Ghost Kitchen Unit Economics Specification v1

**Status:** Working specification  
**Version:** 1.0-draft  
**Date:** 2026-08-31

## Purpose

Define the canonical unit-economics model for the prepared-food, delivery-first franchise before any franchise fee, royalty, launch-cost or return claim is treated as established.

## Model structure

The model must operate at order, day, month and annual levels and support Conservative, Base and Strong scenarios.

### Revenue

- Average food/order value
- Add-on and upsell revenue
- Orders/day
- Trading days/month
- Gross sales
- Discounts/promotions
- Refunds/cancellations
- Net sales

### Variable costs

- Ingredients / food cost
- Packaging
- Delivery/platform fees
- Payment processing
- Order-specific labour where separately measurable
- Promotional/customer acquisition cost

### Fixed/semi-fixed operating costs

- Kitchen rent/occupancy
- Utilities
- Core labour
- Insurance
- Software
- Cleaning/pest/waste
- Repairs/maintenance
- Accounting/admin
- Franchise support/technology fees where applicable
- Other operating overhead

## Required outputs

1. Net sales
2. Contribution per order
3. Contribution margin
4. Monthly operating contribution
5. Break-even orders/day
6. Break-even net sales/month
7. Cash requirement to launch
8. Sensitivity to order volume
9. Sensitivity to average order value
10. Sensitivity to food cost
11. Sensitivity to labour cost
12. Sensitivity to delivery/platform cost
13. Scenario comparison

## Delivery economics rule

Third-party delivery must be modelled explicitly rather than buried inside a generic expense line. Current Australian marketplace pricing can materially affect contribution; for example, Uber Eats currently publishes a 30% marketplace fee for Uber Delivery and 16% for self-delivery, with separate options for own-channel delivery. These are reference inputs only and must be replaced with the actual commercial terms selected for the pilot.

## Food-cost rule

Food-cost assumptions must be based on the selected menu's recipe-level costing and supplier quotes. Industry benchmarks may be used as reasonableness checks, never as substitutes for recipe costing.

## Labour rule

Labour must be modelled from the actual production workflow, staffing requirements, operating hours and applicable employment conditions. A single percentage-of-sales assumption is insufficient for final validation.

## Free-delivery/customer-price rule

If the customer proposition includes free delivery, the model must show who economically absorbs delivery cost: platform margin, menu pricing, minimum-order threshold, promotional budget, delivery subsidy or another mechanism. Free delivery must not be treated as zero cost.

## Validation gates

The model is not commercially validated until:

- one pilot concept has been selected;
- recipes have been costed;
- supplier pricing has been checked;
- packaging has been costed;
- kitchen occupancy has been quoted or benchmarked for the target location;
- labour requirements have been mapped;
- delivery/payment terms have been identified;
- realistic order-volume assumptions have evidence;
- Conservative/Base/Strong scenarios have been reviewed;
- break-even has been tested under downside conditions.

## Regulatory note

Regulatory requirements must be validated separately for the target jurisdiction and premises. This document is an economic modelling specification, not legal or food-safety advice.

## Decision discipline

All unvalidated inputs must be labelled `ASSUMPTION`. Evidence-backed inputs should include a source/date. Final commercial pricing requires explicit approval after pilot validation.
