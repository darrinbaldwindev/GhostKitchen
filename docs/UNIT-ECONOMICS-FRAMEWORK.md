# Ghost Kitchen Delivery Template — Unit Economics Framework

**Status:** Working framework — validation required
**Version:** 0.1
**Date:** 2026-08-31

## Purpose

Provide a vendor- and concept-neutral model for testing whether a prepared-food Ghost Kitchen franchise can produce an attractive operating contribution before franchise pricing or returns are represented as established.

## Model structure

### Revenue

- Average order value (AOV)
- Orders per trading day
- Trading days per week/month/year
- Gross order revenue
- Discounts/promotions
- Refunds/cancellations
- Net sales

### Variable costs

- Food/ingredient cost
- Packaging
- Payment processing
- Delivery/platform fees
- Order-channel commissions
- Variable waste

### Fixed/semi-fixed operating costs

- Kitchen rent/membership
- Utilities
- Insurance
- Software
- Cleaning/sanitation
- Waste collection
- Base labour/management
- Local marketing
- Maintenance
- Accounting/admin

### Franchise economics

- Initial franchise fee
- Equipment/setup investment
- Training/opening costs
- Working-capital requirement
- Recurring royalty
- Technology/platform fee
- Approved supplier/other system fees

All franchise economics above remain **TBD** until validated.

## Core calculations

```text
Net Sales
- Variable Costs
= Contribution Margin

Contribution Margin
- Fixed/Semi-Fixed Operating Costs
- Franchise/System Costs
= Operating Contribution
```

Also calculate:

- contribution margin %
- operating contribution %
- break-even monthly sales
- break-even orders/month
- break-even orders/day
- payback period on initial investment
- sensitivity to AOV
- sensitivity to order volume
- sensitivity to food cost
- sensitivity to labour
- sensitivity to delivery/platform cost

## Required scenarios

### Conservative

Use deliberately cautious assumptions for demand, AOV, margin and operating efficiency. No claim of expected performance should be made without evidence.

### Base

Use the current best-supported planning assumptions after research and pilot evidence.

### Strong

Demonstrate upside capacity without presenting it as a forecast or guarantee.

## Unit-economics gates

The franchise model should not progress to commercial pricing until:

1. Menu-level recipe costing is available.
2. Packaging costs are tested.
3. Delivery/platform economics are known for the intended channels.
4. Kitchen occupancy cost is validated.
5. Labour assumptions are time-tested.
6. Waste is measured.
7. Refund/cancellation allowance is measured.
8. AOV and order-frequency assumptions have evidence.
9. Conservative/base/strong scenarios are stress-tested.
10. Pilot results reconcile planned vs actual economics.

## Decision rules

- Never hide delivery, platform, payment or packaging costs inside a generic margin assumption.
- Separate franchisor revenue from franchisee operating economics.
- Do not use Model A pricing or royalty assumptions for Model B.
- Do not represent scenario outputs as guaranteed franchisee earnings.
- Flag every assumption that materially affects break-even or payback.

## Next implementation

Create a spreadsheet/data model from this framework after the first pilot concept and delivery-channel assumptions are selected. The model should be capable of changing assumptions without rewriting formulas.
