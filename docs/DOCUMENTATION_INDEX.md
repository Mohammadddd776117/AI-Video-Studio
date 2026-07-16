# Documentation Index

## Purpose

This document is the official documentation map for AI Video Studio. It provides the project’s navigation structure, a clear hierarchy of documentation responsibilities, and the source-of-truth rules that should govern how future documentation is added and maintained.

This index is not a replacement for the existing architecture and product documents. It is the governance layer that explains how those documents relate to one another.

---

## Documentation Hierarchy

The documentation set for AI Video Studio should be read as a layered system:

1. Product and strategy layer
   - Defines the why of the platform.
   - Establishes market, user, and capability intent.

2. System and architecture layer
   - Defines the how of the platform at a cross-cutting system level.
   - Establishes major components, boundaries, contracts, and responsibilities.

3. Domain and implementation layer
   - Defines area-specific application, backend, AI, API, security, data, and testing expectations.
   - Provides detailed engineering guidance for implementation teams.

4. Operations and maintenance layer
   - Defines release, review, quality, and governance practices.
   - Keeps documentation current as the system evolves.

---

## Product Documentation

These documents define the product intent, value proposition, and user-facing capability direction.

### Canonical product documents

- VISION.md — strategic intent and platform vision
- PRODUCT_REQUIREMENTS.md — user and business requirements baseline
- PRODUCT_SPECIFICATION.md — master functional specification and product capability framing
- EDITOR_OPERATIONS.md — product capability and editing operations model
- UI_UX_ARCHITECTURE.md — user experience architecture and interaction structure

### Product documentation purpose

- Describe what the platform is for.
- Describe who it serves and what outcomes it enables.
- Establish the product language used across architecture and engineering documents.

---

## Architecture Documentation

These documents define the structural operating model of the platform and should be treated as the main architectural reference set.

### Canonical architecture documents

- ARCHITECTURE.md — overall platform decomposition and architectural baseline
- SYSTEM_DESIGN.md — master system blueprint that consolidates the architectural intent of the broader set
- API_CONTRACTS.md — API contract model and cross-service interface expectations
- DATA_MODELS.md — shared data and domain model framing
- DATABASE_SCHEMA.md — persistence and schema architecture
- SECURITY_ARCHITECTURE.md — security and trust controls
- VIDEO_ENGINE_SPECIFICATION.md — deterministic media rendering and processing design

### Architecture documentation purpose

- Define ownership boundaries.
- Define major subsystems and how they interact.
- Clarify layers, contracts, and non-functional expectations.

---

## AI System Documentation

These documents define the AI layer, its orchestration model, and the command/agent execution framework.

### Canonical AI documents

- AI_SYSTEM.md — overarching AI system model
- AI_RUNTIME_ARCHITECTURE.md — runtime behavior and execution flow
- AI_COMMAND_SPEC.md — command structure and semantics
- AGENT_PROTOCOL.md — agent interaction model
- TOOL_SCHEMA.md — tool and capability contract model

### AI documentation purpose

- Describe how user intent becomes structured execution.
- Define orchestration boundaries between AI planning, tool execution, and deterministic engine work.
- Maintain the command language and agent/tool contracts as the shared AI execution vocabulary.

---

## Engineering Documentation

These documents define the engineering standards and implementation expectations that should guide delivery across all major system layers.

### Canonical engineering documents

- DEVELOPMENT_GUIDELINES.md — engineering standards and collaboration rules
- CODEBASE_STRUCTURE.md — repository and module organization expectations
- CI_CD_STRATEGY.md — engineering quality and delivery workflow expectations
- TESTING_STRATEGY.md — validation strategy and quality baseline
- REPOSITORY_STRUCTURE.md — proposed monorepo layout and ownership expectations

### Engineering documentation purpose

- Establish consistency across implementation work.
- Define how code, testing, delivery, and repository ownership should be coordinated.

---

## Development Documentation

Development documentation should support onboarding, execution, and operational continuity rather than duplicate the product and architecture narrative.

### Development documentation areas

- implementation readiness and milestone context in CURRENT_STATE.md
- implementation decisions and rationale in DECISIONS.md
- release and change history in CHANGELOG.md
- roadmap and sequencing in ROADMAP.md

### Development documentation purpose

- Provide historical continuity.
- Record what has already been decided and what remains in progress.
- Support future implementation planning without rewriting the architecture baseline.

---

## Relationship Between Documents

The existing documentation set should be interpreted using the following relationships:

- VISION.md and PRODUCT_SPECIFICATION.md define the product purpose and scope.
- ARCHITECTURE.md and SYSTEM_DESIGN.md define the system blueprint.
- AI_SYSTEM.md and AI_RUNTIME_ARCHITECTURE.md define the AI execution model.
- FLUTTER_APPLICATION_ARCHITECTURE.md and UI_UX_ARCHITECTURE.md define the user experience and application-facing structure.
- BACKEND_SERVICES.md and BACKEND_SERVICES_DESIGN.md define backend service layering and ownership.
- API_CONTRACTS.md and DATA_MODELS.md define the shared contract and domain vocabulary.
- DEVELOPMENT_GUIDELINES.md and TESTING_STRATEGY.md define how implementation should be governed.

The relationship rule is simple:

- Product documents explain intent.
- Architecture documents explain system structure.
- AI and domain documents explain execution boundaries.
- Engineering documents explain how teams should work within that structure.

---

## Source-of-Truth Rules

The following rules define how documentation authority should be interpreted:

1. Product intent is authoritative in VISION.md, PRODUCT_REQUIREMENTS.md, and PRODUCT_SPECIFICATION.md.
2. System structure is authoritative in ARCHITECTURE.md and SYSTEM_DESIGN.md.
3. AI orchestration and command semantics are authoritative in AI_SYSTEM.md, AI_COMMAND_SPEC.md, AGENT_PROTOCOL.md, and TOOL_SCHEMA.md.
4. Shared contracts are authoritative in API_CONTRACTS.md and DATA_MODELS.md.
5. Platform implementation standards are authoritative in DEVELOPMENT_GUIDELINES.md and CI_CD_STRATEGY.md.
6. When two documents appear to conflict, the more specific governing document should be treated as the source of truth for its domain, and the broader document should be read as context rather than contradiction.
7. Architecture and product documents should not be rewritten for implementation detail; implementation detail should be added in code and in implementation-specific documentation, not by duplicating the same facts in multiple narrative docs.

---

## Rules for Adding Future Documentation

Future documentation should follow these rules:

1. Add documentation only when it clarifies ownership, behavior, contract, process, or historical context.
2. Use the existing category model: product, architecture, AI system, engineering, and development.
3. Do not create a new document that restates an existing canonical document without adding a distinct layer of value.
4. Every new document should identify its relationship to the existing source-of-truth set.
5. New documents should use consistent naming patterns:
   - VISION, REQUIREMENTS, SPECIFICATION, ARCHITECTURE, SYSTEM, GUIDELINES, STRATEGY, REVIEW, SCHEMA, CONTRACTS
6. New documents should use a short purpose statement at the top so readers can understand whether the document is authoritative, explanatory, or historical.
7. New documents should link back to the governing document set instead of creating separate parallel taxonomies.
8. Maintenance responsibility should be explicit. A document should not exist without a clear owner or stewardship expectation.

---

## Governance Summary

The documentation system for AI Video Studio should remain:

- layered rather than flat
- explicit about hierarchy and ownership
- stable in its canonical references
- conservative about duplication
- disciplined about future additions

The goal is not to add more documents, but to make the current documentation set easier to navigate, govern, and maintain over time.
