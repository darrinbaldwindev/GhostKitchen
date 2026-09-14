# Ghost Kitchen Missions

**Last updated:** 2026-09-13

## Mission status legend

- `QUEUED` — prioritised and awaiting execution
- `IN PROGRESS` — actively being worked
- `BLOCKED` — dependency prevents progress
- `PENDING VALIDATION` — draft/evidence exists but acceptance is not yet satisfied
- `READY FOR TEST` — bounded artifact/workload exists and is awaiting governed execution/verification
- `COMPLETE` — acceptance criteria independently verified

## Canonical P0 execution chain

`GK-P0-008 evidence research -> GK-P0-002 concept evaluation -> GK-P0-004 menu/recipe evidence -> GK-P0-005 delivery economics -> GK-P0-001 unit economics -> GK-P0-003 pilot operating model`

No mission in this chain authorizes commercial launch, franchise earnings claims, supplier commitment, production writes or final concept approval by itself.

## GK-P0-001 — Unit economics

**Status:** IN PROGRESS  
**GitHub:** issue #16 (`GK-001`)  
**Objective:** Build and validate Conservative/Base/Strong unit economics for Model B.  
**Current evidence:** Unit economics framework/specification, deterministic pilot gate, representative costing inputs and delivery-channel worksheet exist. Draft PR #27 proposes a normalized contribution-model contract and remains unmerged.  
**Remaining acceptance:** Primary recipe, packaging, labour, kitchen, delivery/payment, marketing and waste/refund inputs; break-even and downside sensitivity using evidence-labelled inputs.  
**Dependency:** Representative pilot concept/menu evidence.

## GK-P0-002 — Pilot concept selection

**Status:** IN PROGRESS  
**GitHub:** issue #17 (`GK-002`)  
**Objective:** Select one prepared-food concept for pilot development using evidence, not preference.  
**Current evidence:** Market/regulatory evidence, concept framework, scorecard and pilot scoring worksheet exist. Burgers/chicken remain serious research candidates; alternatives remain open. No concept is approved.  
**Remaining acceptance:** Comparable recipe-level economics, delivery resilience, labour/equipment burden, supplier evidence and disqualifier checks for finalists.  
**Dependency:** GK-P0-008 plus GK-P0-004/GK-P0-005 evidence.

## GK-P0-003 — Pilot operating model

**Status:** QUEUED  
**GitHub:** issue #18 (`GK-003`)  
**Objective:** Map order-to-repeat workflow for the selected concept.  
**Acceptance:** Owners, SOPs, KPIs, data events, exception paths and QA/food-safety controls defined for ordering, production, packaging, dispatch, delivery, service/recovery and retention.  
**Dependency:** Pilot concept selection and initial unit-economics validation.

## GK-P0-004 — Candidate menu and recipe evidence

**Status:** IN PROGRESS / PENDING VALIDATION  
**GitHub:** issue #10 and supporting evidence artifacts  
**Objective:** Build comparable representative SKUs and bundles for at least three leading candidate families.  
**Current evidence:** Representative costing inputs, packaging benchmarks, comparable three-family worksheet and `docs/PILOT-MENU-EVIDENCE-PACKET-2026-09-04.md` exist.  
**Remaining acceptance:** Project-specific supplier/account pricing, recipes/quantities/yields, measured labour, selected packaging and delivery-test evidence.  
**Dependency:** Candidate shortlist/evidence research.

## GK-P0-005 — Delivery-channel economics

**Status:** IN PROGRESS  
**GitHub:** issue #24 (`GK-009`), supported by issue #8 history  
**Objective:** Compare marketplace-heavy, hybrid and direct-order-led channel mixes, including customer-paid/threshold/subsidised delivery structures.  
**Current evidence:** Published Australian marketplace/direct-order references and a delivery-channel economics worksheet exist.  
**Remaining acceptance:** Comparable per-order contribution using common product assumptions, account-specific terms where available, CAC/retention treatment, and sensitivity analysis.  
**Dependency:** Representative menu/AOV assumptions.

## GK-P0-006 — Queensland pilot compliance pathway

**Status:** PENDING VALIDATION  
**GitHub:** issue #9  
**Objective:** Confirm licence, food-safety-management, supervisor, premises and delivery/transport requirements for the selected concept/location.  
**Current evidence:** Queensland regulatory research log and current public guidance are recorded.  
**Remaining acceptance:** Target council/premises/menu-specific confirmation and professional/local-authority review where appropriate.  
**Dependency:** Concept and pilot location.

## GK-P0-007 — Pilot test protocol

**Status:** QUEUED  
**GitHub:** issue #11  
**Objective:** Define controlled tests for food quality, delivery resilience, throughput, order accuracy, safety controls and economics.  
**Acceptance:** Dated test protocol, measurable pass/fail thresholds, evidence capture, corrective-action loop and release-gate mapping exist before pilot launch.

## GK-P0-008 — Pilot concept evidence research

**Status:** IN PROGRESS  
**GitHub:** issue #23 (`GK-008`)  
**Objective:** Gather current Australian-market evidence required to score candidate concepts.  
**Current evidence:** `docs/PILOT-EVIDENCE-BASE-2026-08-31.md` and `docs/RESEARCH/CONCEPT-EVIDENCE-2026-09-01.md` / `2026-09-02.md` provide dated directional market, channel and regulatory evidence.  
**Remaining acceptance:** Convert broad evidence gaps into supplier, menu, packaging, kitchen and delivery-test evidence for an actionable shortlist.

## GK-P0-009 — Queensland pilot kitchen shortlist

**Status:** QUEUED  
**GitHub:** issue #14  
**Objective:** Identify suitable commercial/shared-kitchen options without committing to a lease.  
**Acceptance:** Occupancy model, equipment, storage, extraction, dispatch access, hours, delivery radius and council pathway compared.  
**Dependency:** Concept shortlist and compliance pathway.

## GK-P0-010 — Free-delivery/customer delivery offer economics

**Status:** QUEUED / PARTLY COVERED BY GK-P0-005  
**GitHub:** issue #15  
**Objective:** Compare customer-funded, threshold-based, partially subsidised and fully subsidised delivery structures.  
**Acceptance:** Impact on AOV, conversion, margin, repeat rate and contribution per order is visible; final offer remains open until pilot validation.

## GK-P1-001 — Technology architecture

**Status:** QUEUED  
**GitHub:** issue #19 (`GK-004`)  
**Objective:** Define vendor-neutral system boundaries for ordering, payments, KDS/work queue, inventory, delivery, CRM, reporting and franchise management.  
**Dependency:** Pilot operating model and channel decisions.

## GK-P1-002 — Franchise package

**Status:** QUEUED  
**GitHub:** issue #20 (`GK-005`)  
**Objective:** Define franchisee deliverables, franchisor controls, support, training, setup requirements and performance standards.  
**Dependency:** Validated unit economics and operating model. Final fee/royalty/earnings representations remain explicitly out of scope until evidence and professional/legal review support them.

## GK-P1-003 — Ghost Kitchen OS

**Status:** QUEUED  
**GitHub:** issue #21 (`GK-006`) and issue #12 for KPI/event-model detail  
**Objective:** Define dashboard, KPI, reporting, task, audit, exception and escalation requirements.  
**Dependency:** Technology architecture and operating model.

## GK-P1-004 — QA/compliance evidence structure

**Status:** QUEUED  
**GitHub:** issue #22 (`GK-007`)  
**Objective:** Define traceable QA, compliance and professional-review evidence needed before commercial launch.  
**Dependency:** Operating workflow, compliance pathway and validation gates.

## GK-P1-005 — Franchise replication/onboarding gates

**Status:** QUEUED  
**GitHub:** issue #13  
**Objective:** Define the location onboarding and first-30/90-day replication process.  
**Dependency:** Validated operating system.

## PORTFOLIO-L2-001 — AgentOS Level-2 GhostKitchen acceptance workload

**Status:** READY FOR TEST  
**Artifact:** `docs/level2/AGENTOS-WORKLOAD-2026-09-13.md`  
**Fixture:** `fixtures/level2/ghostkitchen-evidence-status.txt`  
**Objective:** Supply AgentOS with a real, bounded, non-production GhostKitchen task that tests controlled inspection, one permitted file mutation, reread verification, diff containment, durable evidence, replay/idempotency handling and independent Green/PRS review.  
**Guardrail:** This workload does not authorize supplier contact, orders, customer writes, deployment, credentials, pricing publication or conversion of unknown commercial evidence into verified claims.

## Issue hygiene note

Older issue numbers #2-#15 contain earlier mission generations and supporting sub-missions. The current GK-numbered mission issues #16-#24 are the preferred canonical trackers where an equivalent exists. Duplicate GK-010 pricing-evidence issues #25/#26 are closed. Avoid creating another parallel mission family; update the canonical tracker or this register instead.
