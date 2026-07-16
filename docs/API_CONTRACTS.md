# API Contracts

## Overview

This document defines the architectural contract for APIs across the AI Video Studio platform. It establishes how clients, services, and external integrations exchange data in a consistent, versioned, and secure manner.

The API layer is the primary interface between the mobile application, backend services, AI orchestration runtime, media processing pipeline, collaboration features, and future external integrations.

---

## API Design Principles

The platform should follow these principles:

- Contract-first design: interfaces should be explicitly defined before implementation.
- Stable identifiers: resources should be addressed through durable IDs and ownership boundaries.
- Provider-neutral communication: services should not depend on a single provider implementation detail.
- Explicit error semantics: failures should be structured, actionable, and traceable.
- Security by default: authentication, authorization, and tenant context should be enforced at the contract boundary.
- Auditability: every major request should be traceable through correlation identifiers.
- Backward compatibility: additive changes should be preferred over breaking changes.

---

## API Architecture Layers

### Client APIs

Client APIs are used by the Flutter application and other front-end experiences. They support:

- authentication and session lifecycle
- workspace and project management
- media import, retrieval, and processing state
- AI command submission and status tracking
- rendering, exporting, and delivery workflows
- collaboration and notification flows

### Internal Service APIs

Internal service APIs support communication between backend services, including:

- project service to timeline and media service communication
- AI orchestration to command execution or rendering services
- collaboration service to notification and project services
- billing service to entitlement evaluation services

### External Developer APIs

External developer APIs should expose a governed subset of core capabilities for partners and integrations, including:

- project creation and status retrieval
- media import and export status
- AI command submission and monitoring
- collaboration and publishing workflows

---

## Authentication and Authorization

### Authentication Flow

The platform should support:

- session-based authentication for end users
- OAuth or identity-provider-based login for enterprise environments
- service-to-service tokens for backend-to-backend communication
- refresh token handling and revocation workflows

### Authorization Model

Access should be evaluated using:

- user identity
- workspace or tenant context
- project permissions
- feature entitlements
- policy rules for sensitive or high-impact operations

### Sensitive Operations

Operations such as export, destructive edits, AI generation against external providers, billing changes, admin actions, and cross-tenant operations should require elevated privileges or explicit approval.

---

## Common Request and Response Standards

### Common Request Envelope

Requests should include the following metadata where applicable:

- request_id
- correlation_id
- actor_id
- timestamp
- tenant_id or workspace_id
- api_version
- request_context

### Common Response Envelope

Responses should include:

- status
- resource_state
- data or result payload
- metadata
- trace information
- structured errors when applicable

### Resource Representation

Resources should be represented in a normalized form that exposes:

- stable IDs
- ownership and permission metadata
- version or revision state
- related resource links
- timestamps and audit data

---

## Error Response Standards

Errors should be represented by a structured schema that includes:

- error_code
- message
- severity
- retryable flag
- correlation_id
- suggested action or remediation

### Error Categories

- validation_error
- authentication_failure
- authorization_failure
- resource_not_found
- conflict_or_concurrency_error
- downstream_dependency_failure
- rate_limit_error
- quota_violation

---

## User APIs

User-facing APIs should manage account and identity concerns.

### Core Capabilities

- retrieve current user profile
- update user preferences
- list workspaces or organizations
- manage notification preferences
- retrieve entitlement or plan state

### Design Expectations

These endpoints should be lightweight, permission-aware, and safe for repeated use by the mobile client.

---

## Project APIs

Project APIs manage the core lifecycle of editing work.

### Core Capabilities

- create or open a project
- retrieve project metadata
- update project state
- list associated timelines and assets
- manage collaboration membership
- retrieve revision history

### Design Expectations

Project APIs should preserve project integrity and support optimistic concurrency for collaborative editing.

---

## Asset Upload and Media APIs

Media APIs should support asset ingestion, retrieval, and processing state.

### Upload APIs

- initiate upload session
- submit file chunk or multipart payloads
- report upload progress
- confirm completion and storage references
- trigger processing or analysis jobs

### Retrieval APIs

- retrieve asset metadata
- retrieve thumbnail or proxy references
- query processing status
- list assets associated with a project or workspace

### Design Expectations

These APIs should support both interactive and background workflows for large media files.

---

## AI Command APIs

AI command APIs are a critical contract layer for the platform.

### Command Submission

Clients should submit AI requests as structured command payloads that include:

- command_id
- command_type
- actor context
- target assets or project context
- requested operation and parameters
- approval expectations
- execution preferences

### Command Execution Response

Responses should describe:

- accepted state
- queued or executing state
- preview availability
- completion status
- error details and rollback state where relevant

These APIs should align with AI_COMMAND_SPEC.md and AGENT_PROTOCOL.md.

---

## Agent Execution APIs

Agent execution APIs should expose the runtime lifecycle of AI agents and delegated tasks.

### Core Capabilities

- submit an agent-driven task
- retrieve execution status
- retrieve intermediate results or progress events
- confirm completion or failure
- request approval or revision of an execution plan

### Design Expectations

Agent APIs should support both single-step and multi-agent workflows while preserving traceability and audit visibility.

---

## Timeline Operation APIs

Timeline APIs should support the editorial workflow state required by the application.

### Core Capabilities

- retrieve timeline structure
- apply edit operations
- update track and clip metadata
- request preview state
- manage undo, redo, and revision state

These APIs should align with the editing model defined in EDITOR_OPERATIONS.md and VIDEO_ENGINE_SPECIFICATION.md.

---

## Rendering and Export APIs

Rendering APIs should manage long-running output generation workflows.

### Core Capabilities

- submit render job
- retrieve render status
- retrieve artifacts or output references
- cancel or retry a render job
- list export history

These APIs should support asynchronous completion and background processing.

---

## WebSocket Events

Real-time communication should be supported through WebSocket or similar streaming channels for collaboration and status updates.

### Event Categories

- collaboration_presence
- project_update
- timeline_change
- ai_execution_progress
- render_progress
- notification_delivery
- review_comment_update

### Event Contract Expectations

Events should include:

- event_id
- event_type
- timestamp
- tenant_id or workspace_id
- resource references
- payload
- correlation_id

---

## API Versioning Strategy

The API layer should support explicit versioning to preserve compatibility as the platform evolves.

### Versioning Principles

- use versioned resource paths or media types for major changes
- preserve backward compatibility where possible
- introduce additive changes before breaking changes
- deprecate old versions with clear timelines
- maintain migration guidance for clients and partners

### Compatibility Expectations

- mobile clients should be able to operate against supported API versions without unexpected breakage
- enterprise integrations should receive migration guidance for major changes
- AI command schemas and tool contracts should evolve separately from transport versioning where appropriate

---

## Relationship to the Existing Architecture

This document should be read together with:

- ARCHITECTURE.md for the overall platform decomposition
- AI_SYSTEM.md for AI runtime expectations
- AI_COMMAND_SPEC.md for command semantics
- AGENT_PROTOCOL.md for agent execution workflow expectations
- TOOL_SCHEMA.md for approved tool contracts
- DATA_MODELS.md for canonical domain entities
- FLUTTER_APPLICATION_ARCHITECTURE.md for client-facing integration expectations

- signed retrieval or scoped access
- support for proxies, exports, and preview assets
- efficient access for mobile and web clients

---

## WebSocket and Real-Time Events

Real-time communication should support collaboration and workflow progress updates.

### Event Types

- project state change
- collaborator presence or activity
- AI command status updates
- render progress updates
- notification delivery
- sync conflict or resolution events

### Event Contract Principles

- event payloads should be versioned and stable
- events should carry correlation identifiers
- events should support replay or recovery where appropriate

---

## Relationship to Existing Architecture

This document should be read alongside:

- AI_COMMAND_SPEC.md for structured command contracts
- AGENT_PROTOCOL.md for AI activity coordination
- TOOL_SCHEMA.md for tool capability contracts
- ARCHITECTURE.md for service-system boundaries
- VIDEO_ENGINE_SPECIFICATION.md for execution-oriented operations and outputs
