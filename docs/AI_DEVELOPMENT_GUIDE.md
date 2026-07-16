# AI Development Guide

## Purpose

This document is the official development guide for AI Video Studio. It is intended to serve as the primary context reference for AI coding assistants, Google AI Labs, Gemini, and future development agents that work on this repository.

This guide explains the product identity, the architectural operating model, the engineering expectations, and the implementation sequence that future AI-assisted development should follow.

---

## 1. Project Identity

### What AI Video Studio is

AI Video Studio is a global AI-powered video editing platform designed to help creators, teams, and enterprises create and refine video workflows with a combination of mobile-first editing experience, structured AI orchestration, and scalable media execution.

### Main product vision

The product vision is to provide a professional-grade editing platform where user intent can be translated into structured, validated, and deterministic execution across editing, AI assistance, rendering, review, and delivery workflows.

### Target users and market

The platform is designed for:

- individual creators seeking faster editing workflows
- collaborative creative teams
- enterprise customers requiring governance, security, and scale
- developer and partner ecosystems that need clear integration capabilities

The market focus is a professional AI-assisted content creation platform with enterprise-readiness and long-term extensibility.

---

## 2. Architecture Rules

### Monorepo structure

AI Video Studio should remain organized as a monorepo with clear ownership boundaries across the following layers:

- Flutter application
- backend services
- AI Core
- Video Engine
- shared packages
- infrastructure and test layers

### Relationship between major layers

The architecture relationship should be understood as a layered system:

- Flutter application
  - owns the user experience and surface-level workflow presentation
- Backend services
  - own domain operations, API delivery, service orchestration, and workflow coordination
- AI Core
  - owns natural-language interpretation, command planning, agent coordination, and tool orchestration
- Video Engine
  - owns deterministic media execution, rendering, preview, and export-oriented workflows
- Shared packages
  - own common contracts, models, schema definitions, and reusable cross-layer assets

This layer relationship must remain stable. Future AI-assisted work should preserve the separation between experience, domain ownership, AI semantics, media execution, and shared contracts.

---

## 3. AI Development Rules

Future AI coding work must follow strict governance behavior.

### Never create random files

Do not create files without a clear architectural or implementation reason.

### Always follow existing architecture documents

Any work must remain aligned with the published architecture and governance documents, especially:

- ARCHITECTURE.md
- AI_SYSTEM.md
- AI_COMMAND_SPEC.md
- AGENT_PROTOCOL.md
- TOOL_SCHEMA.md
- DATA_MODELS.md
- API_CONTRACTS.md
- DATABASE_SCHEMA.md
- FLUTTER_APPLICATION_ARCHITECTURE.md
- BACKEND_SERVICES_DESIGN.md
- IMPLEMENTATION_ROADMAP.md

### Always review related documentation before coding

Before making changes, the AI assistant must identify the relevant documents for the target area and understand the expected ownership, dependencies, and contract boundaries.

### Keep services separated

The following separation must remain explicit:

- client experience stays in the Flutter application layer
- business and workflow ownership stays in backend services
- semantic AI planning stays in the AI Core
- deterministic media execution stays in the Video Engine
- shared models and contracts stay in shared packages

### Maintain scalability and enterprise standards

Implementation should prioritize:

- modularity
- traceability
- contract stability
- security discipline
- testability
- operational readiness

---

## 4. Coding Principles

The repository should be developed according to the following principles.

### Clean architecture

The codebase should stay organized around clear boundaries between layers, responsibilities, and interfaces.

### Modular design

Every major area should remain modular so that implementation can scale without creating hidden coupling.

### Versioned contracts

Shared interfaces, schemas, and contracts must remain well-defined and versionable.

### Testability

Code should be structured so that it can be validated by unit, integration, and end-to-end test suites.

### Security

Security and permission boundaries must be treated as first-class architectural requirements.

### Performance

The platform should preserve performance expectations for user experience, AI workflows, media processing, and cloud-scale execution.

---

## 5. Implementation Order

The official development sequence for AI Video Studio is as follows.

### Phase 1: AI Command Layer

Implement the command representation and validation flow that converts user intent into structured AI execution requests.

### Phase 2: AI Agent Orchestration

Build the orchestration layer that coordinates agent behavior, task routing, and execution workflow control.

### Phase 3: Tool Execution Framework

Create the bounded tool execution capability layer that supports safe, structured AI actions.

### Phase 4: Backend Foundation

Establish the backend runtime and service ownership model that governs project, workflow, and coordination responsibilities.

### Phase 5: Database Layer

Implement the persistence and storage design that supports transactional data, metadata, media references, and operational state.

### Phase 6: Flutter Application Foundation

Create the application shell and client architecture that handles user-facing workflow presentation.

### Phase 7: Timeline Editor

Build the editor experience and timeline interaction model on top of the project and backend foundation.

### Phase 8: Video Engine

Implement deterministic media execution, preview, rendering, and export flow integration.

### Phase 9: AI Provider Integration

Integrate provider abstraction support for selected model providers while preserving the architecture contract boundaries.

### Phase 10: Testing and Production Deployment

Expand the implementation into a validated, reviewable, deployable production-ready baseline.

---

## 6. AI Agent Instructions

AI assistants working on this repository should behave as follows.

### Analyze before modifying

Before making any change, the assistant should inspect the repository structure, relevant documentation, and current dependencies to understand the existing system model.

### Do not overwrite existing architecture

AI-generated changes must preserve the architecture set and should not overwrite or bypass documented ownership boundaries.

### Explain changes after implementation

After making changes, the assistant should clearly describe:

- what was created or edited
- why it was necessary
- which architecture documents governed the work
- what validation or review steps were performed

### Keep commits organized

Future work should remain scoped, reviewable, and easy to understand in commit history.

### Preserve compatibility

Any implementation must preserve compatibility with existing contracts, interfaces, service responsibility boundaries, and system expectations.

---

## 7. Documentation References

The primary source documents for AI-assisted implementation are:

- docs/ARCHITECTURE.md
- docs/AI_SYSTEM.md
- docs/AI_COMMAND_SPEC.md
- docs/AGENT_PROTOCOL.md
- docs/TOOL_SCHEMA.md
- docs/DATA_MODELS.md
- docs/API_CONTRACTS.md
- docs/DATABASE_SCHEMA.md
- docs/FLUTTER_APPLICATION_ARCHITECTURE.md
- docs/BACKEND_SERVICES_DESIGN.md
- docs/IMPLEMENTATION_ROADMAP.md

These are the authoritative references that must guide future design decisions and coding work.

---

## Summary

This guide is the repository’s operational context for AI-assisted development. It preserves the intended architecture, keeps implementation boundaries clear, and helps future agents work in a disciplined, enterprise-focused manner.
