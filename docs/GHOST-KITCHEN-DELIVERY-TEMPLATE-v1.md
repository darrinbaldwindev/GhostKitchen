# Ghost Kitchen Delivery Template v1

**Status:** Working specification  
**Version:** 1.0-draft  
**Date:** 2026-08-28

## 1. Objective

Create a repeatable franchise template for a prepared-food, delivery-first business operated from an approved commercial kitchen. The template should allow an approved food concept to be deployed without redesigning the underlying business, technology, training, reporting or governance systems.

## 2. What the franchisee receives

The franchise package is intended to include, subject to final legal and commercial definition:

- approved brand/concept package
- kitchen operating specification
- equipment specification
- recipes and production standards
- menu and pricing framework
- supplier and purchasing framework
- packaging specification
- online ordering and order-management workflow
- delivery workflow and integrations
- launch marketing system
- operating manuals and training
- KPI and financial reporting
- franchise support and compliance framework
- access to Ghost Kitchen OS capabilities as released
- AI-assisted operational guidance and reporting where available

## 3. Kitchen model

The first release should target an approved commercial kitchen rather than a home kitchen. Exact kitchen requirements must be determined from the selected food concept and applicable Australian state/local requirements.

The template should define:

- minimum usable production area
- storage requirements
- refrigeration/freezer requirements
- preparation areas
- cooking equipment by concept
- extraction/ventilation requirements
- handwashing and sanitation requirements
- waste handling
- receiving and dispatch flow
- customer/delivery-driver handoff area
- opening and closing standards

No equipment specification should be treated as final until validated against the selected menu and applicable regulatory requirements.

## 4. Concept engine

A concept is a deployable module consisting of:

**Brand + Menu + Recipes + Suppliers + Packaging + Pricing + Marketing**

Concept modules should plug into the same Ghost Kitchen Delivery Template and Ghost Kitchen OS.

Initial concept families to investigate:

- burgers
- chicken
- Asian street food
- healthy/protein bowls
- loaded fries/sides
- dessert-focused concepts

These are research candidates, not approved franchise concepts.

## 5. Operating workflow

```text
Customer
  ↓
Digital storefront / ordering channel
  ↓
Order management
  ↓
Kitchen production queue
  ↓
Preparation + quality control
  ↓
Packaging + order verification
  ↓
Delivery dispatch
  ↓
Customer
  ↓
Review / retention / repeat order
```

Every stage should have an owner, measurable KPI, standard operating procedure and exception path.

## 6. Unit economics

Do not hard-code franchise pricing before the unit model is validated.

The model must calculate at minimum:

- average order value
- orders per day
- trading days
- gross sales
- food cost
- packaging cost
- delivery/platform costs
- kitchen occupancy/rent
- labour
- marketing/customer acquisition
- software/technology
- insurance and other operating expenses
- franchise fees/royalties
- operating contribution/profit
- break-even sales and orders
- sensitivity to lower/higher order volume

The model should support conservative, base and strong-performance scenarios.

## 7. Multi-brand expansion

The template should support controlled multi-brand operation from one kitchen only after the first concept is operationally proven.

The franchisor/platform should control:

- which concepts may operate together
- kitchen capacity limits
- menu overlap and ingredient reuse
- equipment compatibility
- trading hours
- quality standards
- customer-facing brand separation
- delivery-zone configuration

A franchisee should not independently create additional brands under the system without approval.

## 8. Technology

The target technology architecture should separate the business logic from individual vendors wherever practical.

Core capabilities:

- ordering
- payments
- order routing
- kitchen display/work queue
- inventory
- recipe/food-cost management
- customer data
- promotions
- delivery integration
- reporting
- franchise dashboard
- support/ticketing
- audit trail

## 9. Ghost Kitchen OS

Ghost Kitchen OS is the central operating layer intended to connect franchise-level data and workflows.

The first useful dashboard should surface:

- revenue
- order count
- average order value
- gross margin
- food cost percentage
- labour percentage
- delivery time
- cancellation/refund rate
- repeat-customer rate
- marketing spend
- customer acquisition cost where measurable
- operating contribution

## 10. AI / Overseer layer

The AI layer should assist with:

- daily operational summaries
- anomaly detection
- KPI interpretation
- task creation/recommendation
- menu and pricing analysis
- supplier/cost-change alerts
- marketing recommendations
- customer/review trend analysis
- franchise compliance prompts

AI recommendations must remain auditable and should not override food-safety, legal, financial or franchise governance controls.

## 11. Franchise support

The template should eventually provide:

- pre-opening checklist
- training pathway
- launch checklist
- first-30-day plan
- first-90-day plan
- weekly operating review
- monthly business review
- approved supplier management
- approved marketing assets
- escalation process
- quality audit process

## 12. Release gates

Before a concept is offered commercially, it should pass:

1. Menu feasibility review
2. Food-cost validation
3. Kitchen/equipment validation
4. Food-safety/regulatory review
5. Packaging and transport test
6. Delivery-time test
7. Customer acceptance test
8. Unit-economics test
9. Operating manual completion
10. Franchise/legal review

## 13. Immediate build sequence

1. Define the template's canonical operating model.
2. Build the unit economics model.
3. Research and shortlist viable food concepts.
4. Select one pilot concept.
5. Define the pilot kitchen specification.
6. Define technology and delivery architecture.
7. Build SOP/training framework.
8. Define KPI/dashboard requirements.
9. Define franchise package and support model.
10. Validate the pilot before commercial franchise launch.
