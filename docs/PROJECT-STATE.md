# Ghost Kitchen Project State

**Last updated:** 2026-08-28

## Repository

Canonical repository: `darrinbaldwindev/GhostKitchen`  
Default branch: `main`

The repository was initially empty. The first project foundation files have now been added.

## Current direction

Ghost Kitchen is being developed as a delivery-first franchise platform rather than a single restaurant concept.

There are two planned franchise models:

### Model A — Convenience Delivery

Packaged goods / convenience products delivered to customers. This is the lower-complexity model previously developed.

### Model B — Ghost Kitchen Delivery Template

Prepared food produced in an approved commercial kitchen and sold through digital ordering and delivery channels. This is the current primary build focus.

## Strategic architecture

The project has four major layers:

1. Franchise Models
2. Ghost Kitchen Delivery Template
3. Ghost Kitchen OS
4. Overseer / AI operations layer

The concept library sits above the template as deployable food-business modules.

## Current status

- Repository confirmed and accessible.
- Repository was empty at project start.
- Initial README created.
- Delivery Template v1 working specification created.
- Project state file created.
- No production application code exists yet.
- No final food concept has been selected.
- No final franchise fee or royalty has been fixed for Model B.
- No final kitchen/equipment specification has been approved.

## Highest-value next actions

### P0 — Business model validation

Build a conservative/base/strong unit economics model for the prepared-food franchise. Do not rely on assumptions from Model A.

### P0 — Pilot concept selection

Research candidate concepts against food cost, delivery quality, prep complexity, equipment burden, competition, order value and repeat-purchase potential.

### P0 — Pilot operating template

Design one concept from customer order through kitchen production, QA, packaging, dispatch, delivery, review and repeat purchase.

### P1 — Technology architecture

Define the vendor-neutral system boundaries for ordering, payments, kitchen workflow, inventory, delivery, CRM, reporting and franchise management.

### P1 — Franchise package

Define what the franchisee receives, what remains franchisor-controlled, training/support, setup requirements, ongoing fees and performance standards.

### P1 — Overseer integration

Define the Ghost Kitchen Overseer data, reports, task model, audit trail and escalation rules. Keep AI advisory and auditable around regulated/high-risk operational decisions.

## Decision discipline

Unknowns must remain explicitly marked as assumptions or decisions pending validation. Do not present draft pricing, legal requirements, equipment lists or financial returns as established facts.
