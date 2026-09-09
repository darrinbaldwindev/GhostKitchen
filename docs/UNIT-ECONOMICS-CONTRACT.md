# Ghost Kitchen Unit Economics Contract

Status date: 2026-09-09

Purpose: normalize concept/channel research into one comparable contribution model without making an earnings claim or selecting a final concept/channel.

## Required scenario inputs

Each scenario must provide conservative / base / strong values for:
- average order value (AOV)
- food cost %
- packaging cost per order
- labour minutes per order
- loaded labour rate
- marketplace commission OR direct payment cost
- delivery subsidy / customer-paid delivery treatment
- customer acquisition cost where applicable
- occupancy / kitchen fixed costs
- software, insurance and other fixed costs
- refunds / waste / remakes allowance

Unknown inputs stay UNKNOWN; they are never silently set to zero.

## Canonical calculations

Variable cost per order = food + packaging + labour + channel/payment cost + delivery subsidy + variable CAC + refund/waste allowance.

Contribution per order = AOV - variable cost per order.

Contribution margin % = contribution per order / AOV.

Monthly fixed-cost breakeven orders = total monthly fixed costs / contribution per order.

Daily breakeven orders = monthly breakeven orders / operating days per month.

If contribution per order <= 0, breakeven is not representable as a finite order count and the scenario must be flagged NOT VIABLE UNDER INPUTS.

## Channel comparison rule

Marketplace, direct-order and direct-delivery scenarios must share the same underlying product/order assumptions unless a documented channel-specific reason changes them. Do not make one channel look better by changing AOV, food cost, labour or waste assumptions without evidence.

## Required sensitivity checks

At minimum vary:
1. AOV ±10%
2. food cost +5 percentage points
3. labour minutes +20%
4. delivery/channel cost +5 percentage points or equivalent per-order increase
5. refunds/waste doubled
6. order volume -25%

## Evidence labels

Every input must be tagged one of:
- VERIFIED CURRENT
- DATED PUBLISHED REFERENCE
- INTERNAL ASSUMPTION
- UNKNOWN

Published marketplace rates are dated references, not permanent contractual terms.

## Decision boundary

This model may compare scenarios and identify what evidence would change the ranking. It must not by itself select a final concept, kitchen, supplier, menu, pricing promise, royalty structure, earnings claim or production launch.
