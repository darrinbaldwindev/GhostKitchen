# Ghost Kitchen Project State

**Last updated:** 2026-09-13

## Repository

Canonical repository: `darrinbaldwindev/GhostKitchen`  
Default branch: `main`

The repository foundation is established and the project is in controlled validation/design. It is not yet a production Ghost Kitchen application or commercially approved franchise system.

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

## Verified current state

- Repository confirmed and accessible on `main`.
- Delivery Template v1 working specification established.
- Overseer operating charter and mission register established.
- Unit economics framework/specification and deterministic pilot unit-economics gate exist.
- Concept evaluation framework, scorecard and pilot scoring worksheet exist.
- Delivery-channel economics worksheet exists.
- Representative menu-costing inputs, packaging benchmarks and comparable menu-costing worksheet exist.
- Pilot menu evidence-capture packet exists and remains OPEN pending project-specific primary evidence.
- Current market/regulatory research is recorded under `docs/RESEARCH/` and supporting evidence files.
- AgentOS Level-2 bounded GhostKitchen acceptance workload and deterministic fixture exist for non-production worker validation.
- No production application code exists yet.
- No final food concept has been selected.
- No final franchise fee or royalty has been fixed for Model B.
- No final kitchen/equipment specification has been approved.
- No commercial launch or earnings claim is approved.

## Active P0 execution chain

The canonical execution sequence is:

`GK-008 evidence research -> GK-002 concept evaluation -> representative menu/recipe evidence -> GK-009 delivery economics -> GK-001 unit economics -> GK-003 pilot operating model`

Supporting P0 work includes Queensland compliance validation, pilot kitchen/location research, delivery-offer economics and pilot test protocol design.

## Current evidence boundary

The project has enough framework and directional evidence to run disciplined comparisons, but not enough primary evidence to approve a pilot concept.

The principal missing inputs are:

- supplier/account-specific ingredient pricing;
- representative recipes, quantities and validated yields;
- measured prep/cook/pack labour;
- selected packaging and tested unit cost;
- real delivery-quality tests over target delivery windows;
- pilot kitchen occupancy/equipment evidence;
- account-specific delivery/payment/channel terms where relevant;
- observed waste, remake and refund data.

Unknown values remain `UNKNOWN`, `HYPOTHESIS` or equivalent evidence classes. They must not be silently replaced with zeroes or presented as verified commercial facts.

## Active pull request

Draft PR #27, `docs: normalize ghost-kitchen unit economics`, proposes a normalized contribution model and evidence labels. It remains unmerged and must be reconciled against the existing unit-economics framework, worksheet and pilot gate before any merge decision.

## AgentOS Level-2 contribution

`docs/level2/AGENTOS-WORKLOAD-2026-09-13.md` defines a bounded, non-production acceptance workload for the governed AgentOS Windows worker. It may mutate only the dedicated fixture, requires reread/diff verification, and does not authorize supplier contact, ordering, pricing publication, deployment, credentials or customer writes.

## Regulatory/evidence guardrail

Queensland requirements are treated as evidence inputs, not assumptions. Exact licensing, food-safety-management, premises, supervisor and delivery/transport requirements must be confirmed for the chosen menu, premises and jurisdiction before launch, with local-authority/professional confirmation where appropriate.

## Decision discipline

Do not present draft pricing, legal requirements, equipment lists, financial returns or concept preferences as established facts. Passing a documentation gate does not equal commercial readiness; primary evidence and pilot validation control progression.

See `docs/OVERSEER.md` for the operating loop, `docs/MISSIONS.md` for mission control, `docs/VALIDATION-GATES.md` for release gates and `docs/PILOT-MENU-EVIDENCE-PACKET-2026-09-04.md` for the current primary evidence-capture contract.
