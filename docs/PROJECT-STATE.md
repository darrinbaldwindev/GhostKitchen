# Ghost Kitchen Project State

**Last updated:** 2026-08-31

## Repository

Canonical repository: `darrinbaldwindev/GhostKitchen`  
Default branch: `main`

The repository foundation is established and the project has moved from documentation bootstrap into validation/design work.

## Current direction

Ghost Kitchen is being developed as a delivery-first franchise platform rather than a single restaurant concept.

There are two planned franchise models:

### Model A — Convenience Delivery

Packaged goods / convenience products delivered to customers. This is the lower-complexity model previously developed.

### Model B — Ghost Kitchen Delivery Template

Prepared food produced in an approved commercial kitchen and sold through digital ordering and delivery channels. This remains the primary build focus.

## Strategic architecture

The project has four major layers:

1. Franchise Models
2. Ghost Kitchen Delivery Template
3. Ghost Kitchen OS
4. Overseer / AI operations layer

The concept library sits above the template as deployable food-business modules.

## Current status

- Repository confirmed and accessible.
- Initial project architecture and decisions established.
- Delivery Template v1 working specification established.
- Overseer operating charter established.
- Mission register established.
- Unit economics specification v1 established.
- Pilot concept evaluation framework established.
- No production application code exists yet.
- No final food concept has been selected.
- No final franchise fee or royalty has been fixed for Model B.
- No final kitchen/equipment specification has been approved.

## Active priorities

### P0 — Unit economics

Build Conservative/Base/Strong scenarios using recipe-level food cost, packaging, labour, kitchen occupancy, delivery/platform fees, payment costs, marketing and overhead. Explicitly model the economics of any free-delivery customer proposition.

### P0 — Pilot concept selection

Evaluate candidate concepts against delivery resilience, food economics, prep complexity, labour efficiency, equipment burden, ingredient overlap, order value, repeat purchase, market demand, competition, packaging, consistency, scalability and compliance complexity.

### P0 — Pilot operating template

After concept selection, design the complete customer-order-to-repeat workflow with owners, SOPs, KPIs, QA controls and exception paths.

### P1 — Technology architecture

Define vendor-neutral boundaries for ordering, payments, kitchen workflow, inventory, delivery, CRM, reporting and franchise management.

### P1 — Franchise package

Define franchisee deliverables, franchisor-controlled standards, training/support, setup requirements, ongoing fees and performance standards after economics are validated.

### P1 — Ghost Kitchen OS

Define dashboard, KPI, reporting, task, audit and escalation requirements.

## Regulatory/evidence guardrail

Queensland requirements are being treated as evidence inputs, not assumptions. Prepared-food businesses generally require local-government licensing, food premises must meet applicable food-safety requirements, and current Queensland guidance identifies additional food-safety-management obligations for specified category-one/category-two businesses. Exact requirements must be confirmed for the target premises, menu and jurisdiction before launch.

## Decision discipline

Unknowns must remain explicitly marked as assumptions or decisions pending validation. Do not present draft pricing, legal requirements, equipment lists or financial returns as established facts.

See `docs/OVERSEER.md` for the operating loop and `docs/MISSIONS.md` for active mission control.
