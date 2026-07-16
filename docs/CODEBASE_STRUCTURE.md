# Codebase Structure

## Overview

This document defines the future repository structure for AI Video Studio before production implementation begins. Its purpose is to provide a clear engineering blueprint that prevents overlapping responsibilities, duplicated systems, and architectural conflicts.

The structure below is intentionally aligned with the existing architecture, API, backend, AI, Flutter, and data model documents. It does not replace those documents; it organizes them into a practical repository blueprint for implementation.

---

## 1. Repository Root Structure

The repository should be organized into a small set of high-level areas with clear ownership.

```text
AI-Video-Studio/
├── apps/
├── services/
├── packages/
├── infrastructure/
├── database/
├── docs/
├── tests/
├── scripts/
├── .github/
├── README.md
├── docker-compose.yml
├── Makefile
├── package.json / pyproject.toml / pubspec.yaml
```

### Root Directory Responsibilities

#### apps/

Contains user-facing applications.

Responsibilities:
- host the Flutter application
- keep client-facing experience isolated from core backend implementation
- contain product-specific features and UI flows

#### services/

Contains backend services and runtime components.

Responsibilities:
- host domain-specific backend services
- keep business logic separated by service ownership
- contain AI orchestration, media processing, and workflow runtimes

#### packages/

Contains reusable shared libraries that are consumed by multiple applications or services.

Responsibilities:
- centralize shared contracts, domain models, validation rules, and event schemas
- prevent duplication across the mobile app, backend services, and AI runtime
- ensure cross-cutting code remains versioned and reusable

#### infrastructure/

Contains deployment, observability, automation, and environment configuration.

Responsibilities:
- define deployment topology and infrastructure-as-code assets
- host CI/CD pipelines and environment templates
- centralize logging, monitoring, and operational configuration

#### database/

Contains database-related assets.

Responsibilities:
- host migration files
- store schema definitions and documentation
- preserve versioned database changes and seed data

#### docs/

Contains architecture, product, process, and planning documents.

Responsibilities:
- preserve the decision history and architecture rationale
- keep implementation guidance consistent with the system design
- serve as the source of truth for cross-team coordination

#### tests/

Contains system-level and cross-service validation assets.

Responsibilities:
- host end-to-end and integration test suites
- cover backend services, AI workflows, and client flows
- keep quality standards aligned with the architecture

#### scripts/

Contains repository automation, setup, and utility scripts.

Responsibilities:
- provide local development helpers
- support environment bootstrapping and maintenance
- keep operational tasks reproducible

---

## 2. Application Layer Structure

### Flutter Application Structure

The Flutter application should remain organized by product capability rather than by technical concern alone.

```text
apps/mobile/
├── lib/
│   ├── app/
│   ├── core/
│   ├── features/
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── projects/
│   │   ├── editor/
│   │   ├── media/
│   │   ├── ai/
│   │   ├── export/
│   │   ├── collaboration/
│   │   └── settings/
│   ├── shared/
│   └── main.dart
```

#### Expected Responsibilities

##### screens/

The application should expose screens for:
- authentication and onboarding
- workspace and project selection
- editor workspace
- asset browser
- AI assistant experience
- export workflow
- collaboration review flow
- settings and account management

##### features/

Feature modules should remain cohesive and domain-oriented:
- auth
- dashboard
- projects
- editor
- media
- ai
- export
- collaboration
- settings

##### state management/

The application should adopt explicit state ownership for:
- authentication state
- workspace and project state
- editor state
- AI session state
- export state
- collaboration state
- offline and sync state

##### networking/

The client should isolate network access through dedicated clients and repositories for:
- API communication
- authentication flows
- project and asset retrieval
- AI request submission
- export and status polling

##### local storage/

The client should manage:
- cached project metadata
- local drafts and preferences
- thumbnails and lightweight assets
- queued offline operations
- secure token storage

##### project workspace/

The project workspace module should own the user experience for:
- project discovery
- project open/close flows
- timeline context
- editor session state

##### timeline editor/

The timeline editor should own the editing experience and provide the UI for:
- selection
- clips and track manipulation
- timeline state display
- preview interaction
- edit action orchestration

##### AI assistant interface/

The AI assistant interface should manage:
- prompt input
- command submission
- approval and revision UI
- result display
- error and warning presentation

##### shared UI components/

Shared UI components should host reusable UI primitives, panels, forms, overlays, and editor controls.

### Backend Structure

The backend should be organized into service-oriented modules with explicit ownership.

```text
services/
├── api-gateway/
├── auth-service/
├── project-service/
├── asset-service/
├── ai-orchestration/
├── agent-runtime/
├── video-processing/
├── rendering-service/
├── notification-service/
└── shared-runtime/
```

#### Expected Responsibilities

##### API Gateway

Owns request entry, routing, policy enforcement, and authentication propagation.

##### authentication service

Owns identity, session, enterprise access, and permission context resolution.

##### project service

Owns project lifecycle, version state, metadata, and collaboration-related project actions.

##### asset service

Owns media metadata, asset registration, and asset ownership state.

##### AI orchestration service

Owns the orchestration of AI requests, plan construction, and execution coordination.

##### agent runtime

Owns agent lifecycle, communication, execution context, and delegation rules.

##### video processing service

Owns media analysis and processing workflows that are not purely UI-facing.

##### rendering service

Owns final media output workflows and render job lifecycle.

##### notification service

Owns event-driven user notifications and workflow status delivery.

---

## 3. AI System Code Organization

The AI system should remain modular and provider-agnostic.

```text
services/ai-core/
├── command-schema/
├── command-parser/
├── command-validator/
├── ai-orchestrator/
├── agents/
│   ├── supervisor/
│   ├── planning/
│   ├── editing/
│   ├── analysis/
│   ├── qa/
│   ├── memory/
│   └── execution/
├── prompts/
├── providers/
├── tools/
├── memory/
└── tests/
```

#### Expected Responsibilities

##### AI Orchestrator

Owns overall request planning, workflow state, and orchestration control.

##### Supervisor Agent

Owns orchestration and delegation decisions across the agent graph.

##### Planning Agent

Converts user intent into a command graph and dependency plan.

##### Editing Agent

Handles edit-related planning and transformation coordination.

##### Analysis Agent

Handles media or content understanding and semantic analysis.

##### QA Agent

Validates quality, risks, consistency, and confidence.

##### Memory Agent

Manages contextual memory and retrieval logic.

##### Execution Agent

Invokes tools and other runtime capabilities safely.

##### Prompt management

Stores prompt templates, policies, and prompt versioning separately from runtime logic.

##### Model providers

Defines provider abstractions for future connector implementations such as Gemini, DeepSeek, and Ollama.

##### Tool registry

Owns tool discovery, metadata, validation, and execution routing.

##### Command schema

Owns the canonical internal command contract used across the AI system.

---

## 4. Shared Packages

Shared packages should remain the single authoritative place for reusable contracts and models.

```text
packages/shared/
├── models/
├── api-contracts/
├── command-schema/
├── auth-models/
├── events/
├── tools/
├── validation/
├── errors/
└── utilities/
```

#### Expected Responsibilities

##### command schemas

Defines the reusable command contract used by the AI layer and backend services.

##### API contracts

Defines request and response envelopes, resource models, and versioned interfaces.

##### shared models

Defines common domain entities used by multiple layers.

##### authentication models

Defines shared identity, token, session, and permission-related structures.

##### event definitions

Defines the event schema used by queues, notification systems, and workflow coordination.

##### tool definitions

Defines tool interfaces, capability metadata, and compatibility expectations.

##### validation rules

Defines reusable validation logic that should be shared across services rather than duplicated.

---

## 5. Infrastructure Organization

Infrastructure should be organized to support both local development and future cloud deployment.

```text
infrastructure/
├── docker/
├── kubernetes/
├── terraform/
├── environments/
├── ci/
├── monitoring/
├── logging/
└── secrets/
```

#### Expected Responsibilities

##### Docker

Contains container definitions for local development and service packaging.

##### Cloud deployment

Contains deployment templates and environment-specific configuration for future cloud environments.

##### CI/CD

Contains pipeline definitions, build steps, and release automation.

##### Environment configuration

Stores development, staging, and production configuration templates.

##### Monitoring

Contains dashboards, alerting definitions, and service health expectations.

##### Logging

Defines structured logging conventions and correlation identifiers across services.

##### Cloud resources

Defines future cloud resource references, environment variables, and infrastructure modules.

---

## 6. Database Organization

The database structure should be versioned and documented to preserve consistency over time.

```text
database/
├── migrations/
├── schemas/
├── seeds/
├── docs/
└── backups/
```

#### Expected Responsibilities

##### migrations/

Contains incremental database changes for schema evolution.

##### schemas/

Contains database schema definitions and structural documentation.

##### seed data/

Contains standard or test data used during development and validation.

##### database documentation/

Explains ownership, relationships, lifecycle, and backup expectations.

---

## 7. Testing Structure

Testing should be split by concern to preserve clarity and reduce risk.

```text
tests/
├── unit/
├── integration/
├── api/
├── ai-evaluation/
├── performance/
└── e2e/
```

#### Expected Responsibilities

##### unit tests

Validate individual modules, entities, validators, and pure logic.

##### integration tests

Validate interactions between services, modules, or subsystems.

##### API tests

Validate contracts, request handling, error behavior, and response shapes.

##### AI evaluation tests

Validate prompt handling, command formation, tool routing, and output quality expectations.

##### performance tests

Validate throughput, latency, memory behavior, and media processing scaling expectations.

---

## 8. Dependency Rules

The repository structure should enforce clear dependency boundaries.

### Allowed Communication

The following layers may communicate as defined below:

- Flutter application may call backend APIs and local services.
- Backend services may communicate with other backend services through approved contracts.
- AI orchestration may call tool and command execution services through the defined interfaces.
- Services may consume shared packages for contracts, models, and validation rules.

### Restricted Communication

The following should not occur directly:

- UI layer should not directly access the video engine or database layer.
- AI layer should not bypass the command contract and tool validation layer.
- Backend services should not directly depend on Flutter-specific modules.
- Shared packages should not depend on application-specific or service-specific implementations.

### Service Communication Rules

- Services should communicate through versioned APIs or event contracts.
- Direct database access across services should be avoided unless explicitly defined.
- Each service should own its own state and publish changes through stable interfaces.

### Shared Package Usage Rules

- Shared packages should contain reusable abstractions only.
- Shared packages should not contain implementation-specific logic tied to one service or application.
- Shared packages should remain stable and backward-compatible as the platform evolves.

### Circular Dependency Prevention

To avoid circular dependencies:

- keep the dependency direction simple: app → services → shared packages
- avoid letting shared packages import from feature modules or service implementations
- keep orchestration logic in the orchestrator layer rather than spreading it across multiple layers
- separate interface definitions from concrete implementations

---

## 9. Development Order

The implementation sequence should follow the architecture in a controlled and incremental manner.

### Phase 1: Foundation and Shared Contracts

#### Objective

Create the foundation needed for all future work.

#### Required Components

- repository structure
- shared package skeleton
- core models and contracts
- API envelope definitions
- validation conventions
- environment and repository tooling

#### Expected Output

A stable platform foundation that can be extended safely.

### Phase 2: Backend Core

#### Objective

Build the first backend services and their contracts.

#### Required Components

- API Gateway
- authentication service
- project service
- asset service
- core persistence

#### Expected Output

A working backend core that can handle project and asset lifecycle operations.

### Phase 3: AI Command System

#### Objective

Implement the structured AI command lifecycle.

#### Required Components

- command schema
- parser and validator
- orchestrator skeleton
- tool registry interfaces
- initial tests

#### Expected Output

A provider-neutral AI command layer that can be extended with agents and tools.

### Phase 4: Agent Runtime

#### Objective

Introduce the agent hierarchy and execution runtime.

#### Required Components

- supervisor and planning agents
- execution and validation agents
- memory interfaces
- agent coordination rules

#### Expected Output

A reusable runtime for intelligent task delegation and tool execution.

### Phase 5: Flutter Application

#### Objective

Deliver the first user-facing experience.

#### Required Components

- authentication and workspace flows
- project dashboard
- editor experience
- AI assistant interface
- export workflow UI

#### Expected Output

A usable client application that interacts with the backend and AI system.

### Phase 6: Video Engine Integration

#### Objective

Connect the deterministic editing engine to the broader platform workflow.

#### Required Components

- execution hooks
- rendering integration
- preview pipeline
- export workflow support
- rollback and revision handling

#### Expected Output

A complete editing-and-export path from request to rendered output.

### Phase 7: Cloud Scaling

#### Objective

Prepare the platform for production scale and enterprise readiness.

#### Required Components

- deployment automation
- observability and monitoring
- scaling and queue-based orchestration
- security hardening
- tenant and billing support

#### Expected Output

A platform ready for broader release and growth.

---

## Final Architectural Guidance

This repository structure is intended to support the architecture decisions already documented in the project without introducing unnecessary complexity. The structure keeps the application, services, shared libraries, AI runtime, infrastructure, and tests clearly separated so that responsibilities remain understandable and maintainable.

The most important principle is that implementation should follow the layers already defined in the architecture documents rather than creating new ad hoc systems inside the same repository boundaries.
