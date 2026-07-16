# Code Architecture Guidelines

## Purpose

This document defines the engineering architecture rules that should govern code organization, dependency management, and implementation discipline for AI Video Studio. It is intended to keep the codebase aligned with the existing product, system, AI, and backend architecture foundation without adding new architectural ambiguity.

This document is not a coding standard for every detail of implementation. It is the governance document for how code should be organized so that architecture remains coherent as the project moves from documentation into implementation.

---

## Code Organization Principles

The codebase should be organized around the architectural layers already defined in the repository documentation.

### Primary organization principles

- Keep product-facing experience separate from platform orchestration.
- Keep AI planning separate from deterministic execution.
- Keep backend domain ownership explicit and independent of client rendering concerns.
- Keep shared contracts and models centralized rather than duplicated across layers.
- Keep cross-cutting concerns such as security, observability, and release policy enforced through consistent infrastructure and platform patterns.

### Refactoring principle

If a change blurs a layer boundary, the implementation should first be reviewed against the documented architecture and adjusted to restore separation rather than expanding the ambiguity.

---

## Naming Conventions

Names should communicate responsibility, capability, and ownership clearly.

### Naming standards

- Use domain-oriented names rather than generic implementation names when the domain is already documented.
- Prefer names that express business or platform responsibility.
- Keep module names stable and predictable across client, backend, AI, and shared packages.
- Use terminology that aligns with the project’s published contracts and architecture vocabulary.

### Naming expectations

- Client modules should reflect user workflows and experience surfaces.
- Backend modules should reflect domain ownership and service responsibility.
- AI modules should reflect command, agent, tool, provider, and orchestration responsibilities.
- Shared packages should reflect stable contracts, domain types, and reusable abstractions.

---

## Module Boundaries

Module boundaries should be treated as architectural guarantees, not suggestions.

### Boundary rules

- User interface code should not own backend domain execution logic.
- Backend service code should not absorb AI semantic planning unless the architecture explicitly designates that ownership.
- Media execution code should not directly implement AI planning behavior.
- Shared packages should remain contract- and model-oriented, not service-specific in behavior.

### Boundary intent

A module should own one set of responsibilities and should expose stable interfaces to other modules. If a module needs deep knowledge of another module’s internal implementation, that relationship should be reviewed because it may indicate a boundary violation.

---

## Dependency Rules

Dependencies should be directional, stable, and traceable.

### Dependency principles

- Higher-level experience layers should depend on stable contracts rather than concrete implementations.
- Shared abstractions should be consumed by multiple layers, not recreated in each layer.
- Cross-layer coupling should be minimized and justified.
- Runtime dependencies should remain explicit, documented, and testable.

### Dependency safety rules

- Do not let client code depend on backend implementation details.
- Do not let AI orchestration code depend on domain-specific media execution internals.
- Do not allow service-specific logic to be duplicated across clients and servers without a documented shared contract.

---

## Package Responsibilities

The repository’s package structure should reflect the existing architecture model.

### apps/

The apps layer is responsible for user-facing experiences and workflow orchestration at the interaction surface.

### services/

The services layer is responsible for backend and platform execution domains, including AI orchestration, workflow coordination, and operational services.

### packages/

The packages layer is responsible for shared contracts, models, validation logic, and reusable domain components that multiple layers need to consume consistently.

### docs/

The docs layer is the governance and architectural reference layer for the platform.

### tests/

The tests layer is the validation layer that ensures user, contract, service, and AI behavior remain aligned with the documented expectations.

---

## Backend Service Rules

Backend service ownership must stay clean and predictable.

### Service ownership expectations

- Each service should own one clear domain or workflow responsibility.
- Service boundaries should align with the existing architecture documents.
- Service-to-service communication should use documented contracts rather than implicit or ad hoc conventions.
- Work that is asynchronous or long-running should remain observable and recoverable.

### Backend design rules

- Do not collapse domain services into a single monolithic execution unit.
- Do not overload one service with both direct AI orchestration and transactional domain authority unless the documentation explicitly supports that pattern.
- Preserve traceability of user requests, job status, and state transitions.

---

## Flutter Architecture Rules

Flutter implementation should remain aligned with the documented client architecture and user-experience structure.

### Flutter implementation expectations

- Keep the UI responsible for presentation and state reflection.
- Keep domain workflows and editing intent separate from infrastructure detail.
- Keep API and service integration behind stable, reviewable interfaces.
- Preserve a clear separation between local interaction state and platform state.

### Client architectural rule

The Flutter client should not become the authority for platform-wide execution decisions. It should collect intent, surface state, and submit work through documented interfaces.

---

## AI Core Isolation Rules

The AI Core must remain isolated from non-AI runtime concerns and must preserve a strong contract boundary.

### Isolation rules

- AI Core should own command interpretation, agent orchestration, tool selection, and execution planning.
- AI Core should not become a replacement for deterministic media execution services.
- AI Core should remain provider-agnostic at the orchestration contract layer.
- AI Core should expose stable outputs that can be validated and observed without leaking provider-specific behavior into unrelated services.

### Architectural protection rule

If an AI implementation starts to own business operations that belong to backend services or the media engine, that work should be re-scoped to preserve the intended architecture.

---

## Maintainability Standards

Maintainability should be an explicit engineering requirement, not an afterthought.

### Required standards

- Write code that can be understood by another team without hidden assumptions.
- Preserve explicit module ownership and clear public interfaces.
- Use shared contracts as the default integration mechanism.
- Keep the number of undocumented cross-layer shortcuts at zero by default.
- Ensure all major behavior changes remain aligned with the existing architecture set.

### Review criteria

A change should be considered maintainable only if it:

- respects documented boundaries,
- uses stable contracts,
- avoids hidden coupling,
- remains testable,
- and is visible in the relevant architecture or governance artifacts when required.

---

## Governance Summary

The code architecture for AI Video Studio must remain:

- layered
- explicit in ownership
- contract-driven
- provider-agnostic where appropriate
- maintainable over time

Implementation should improve the product without weakening the architectural separation that has already been documented.
