# Ghost Kitchen

A delivery-first food business and franchise platform.

## Purpose

Ghost Kitchen is being developed as a repeatable operating system for delivery-first food businesses. The platform is designed to support multiple franchise models and multiple approved food concepts from a common operational, technology, training, analytics and AI foundation.

## Current franchise models

1. **Convenience Delivery** — packaged goods / convenience delivery model.
2. **Ghost Kitchen Delivery Template** — prepared-food, delivery-first commercial kitchen model.

The second model is the primary build focus in the current phase.

## Architecture

```text
Ghost Kitchen
├── Franchise Models
│   ├── Convenience Delivery
│   └── Ghost Kitchen Delivery
├── Ghost Kitchen Delivery Template
│   ├── Business Model
│   ├── Kitchen Operations
│   ├── Menu System
│   ├── Supplier System
│   ├── Delivery System
│   ├── Technology
│   ├── Marketing
│   ├── Training
│   └── Franchise Operations
├── Ghost Kitchen OS
│   ├── Franchise Dashboard
│   ├── KPI System
│   ├── Reporting
│   ├── AI Operations
│   └── Integrations
└── Overseer
    ├── Governance
    ├── Tasks
    ├── Audits
    ├── Decisions
    └── Reports
```

## Design principles

- Delivery-first rather than storefront-first.
- Modular concepts rather than one fixed restaurant concept.
- Standardise the operating system; customise the approved concept layer.
- Validate unit economics before fixing franchise pricing.
- Keep franchisor-controlled standards separate from franchisee operating decisions.
- Build for one kitchen / one concept first, then controlled multi-brand expansion.
- Treat AI as an operational assistance and oversight layer, not a substitute for legal, food-safety or professional advice.
- Keep technology provider-agnostic where practical.

## Status

Repository initialized on 28 August 2026. The repository started empty; this README establishes the initial project architecture and scope.

See `docs/` for the working specification and decisions.
