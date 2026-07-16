# Database Schema Architecture

## Overview

This document defines the database architecture for AI Video Studio. It specifies the persistence strategy, core entities, relationships, ownership boundaries, versioning approaches, audit requirements, and multi-tenant considerations that support the product’s editing, AI execution, collaboration, media, and billing workflows.

The persistence model must balance transactional integrity for core business objects with flexible storage for large media assets, AI execution history, and operational metadata.

---

## Database Architecture Principles

The platform should follow these design principles:

- Use transactional databases for structured, consistency-sensitive domain objects.
- Use object storage for large binary assets and derived media artifacts.
- Use metadata or search stores for fast content discovery and enrichment results.
- Preserve auditability for edits, AI operations, permissions, and exports.
- Support versioned state for projects, timelines, and AI workflows.
- Design for horizontal growth and enterprise-scale usage.

---

## Storage Architecture

### Operational Database

The operational database should store transactional data such as:

- users and accounts
- workspaces and memberships
- projects and timelines
- permissions and roles
- collaboration data
- billing and entitlements
- audit records and operational events

### Object Storage

Object storage should host large media files and generated artifacts such as:

- original source assets
- raw uploads and temporary staging files
- proxy media and thumbnails
- renders and exports
- AI-generated intermediate assets
- analysis outputs and packaged delivery assets

### Metadata and Search Layer

A metadata or search layer should support fast access to:

- asset metadata
- transcripts and captions
- scene and content analysis results
- project history and searchable operations
- collaboration comments and review context

---

## Core Entity Domains

### User and Account Entities

The persistence layer should represent:

- users
- accounts
- sessions
- preferences
- subscription and entitlement state

These entities capture identity, access context, and product usage state.

### Workspace and Organization Entities

The database should represent:

- workspaces
- organizations
- workspace memberships
- roles and permissions
- collaboration policies
- integration connections

### Project Entities

Project entities should describe:

- project identifier and ownership
- workspace association
- project metadata and status
- lifecycle state
- associated timeline and assets
- current and historical versions

### Timeline Entities

Timeline entities should represent the editing structure of a project and should include:

- timeline identifier
- associated project and version
- track structure
- clip placement and timing
- effect and transition assignments
- synchronization metadata
- revision markers and state snapshots

### Media Asset Entities

Media assets should be modeled as first-class entities with:

- asset identifier and ownership
- source location and storage reference
- media type and file characteristics
- metadata and analysis results
- derivative references such as proxies and thumbnails
- lifecycle state and permissions

---

## Relationship Model

The core relationships should be modeled as follows:

- A workspace contains many projects and memberships.
- A project belongs to one workspace and may have many timelines and assets.
- A timeline belongs to one project and contains many tracks and clips.
- A media asset may be associated with many projects and timelines.
- A user may belong to many workspaces and hold many roles.
- AI execution records reference the relevant project, asset, agent, tool, and user context.

These relationships should be represented using relational references and, where appropriate, durable link tables for many-to-many associations.

---

## Data Ownership

Each domain should have a clearly authoritative persistence owner.

- User and identity data is owned by the identity and user services.
- Workspace and membership data is owned by the workspace and organization domain.
- Project and timeline state is owned by the project and timeline services.
- Asset and media metadata is owned by the media service.
- AI execution lineage is owned by the AI orchestration and execution services.
- Billing and entitlement data is owned by the billing service.

This ownership model avoids ambiguous writes and cross-service data duplication.

---

## Project Versioning and History

The architecture should support history-aware persistence for project and timeline state.

### Versioning Requirements

- versioned project snapshots
- timeline revision records
- branch or alternative state references where relevant
- immutable change records for auditable editing workflows
- rollback and compare support for collaborative operations

### Recommended Pattern

The system should persist:

- current project state
- a version history log
- snapshot data for major checkpoints
- metadata describing the cause and context of each revision

---

## AI History and Execution Storage

The database should preserve a durable history of AI activity.

### AI Execution Records

AI execution data should include:

- execution identifier
- request identifier and session context
- source command reference
- provider and model version information
- agent and tool execution references
- execution state and result summary
- approval, rollback, and error state

### Agent Execution Records

The system should record:

- agent identity and role
- task identifier and parent context
- assigned operation
- status changes
- output references
- error and retry information

### Tool Invocation Records

Tool execution should be persisted for reproducibility, debugging, and auditing.

---

## Asset Metadata and Media Representation

Media assets should be represented in a way that separates physical storage from logical metadata.

### Asset Metadata

Asset metadata should include:

- asset identifier
- owner and visibility
- media type and format
- technical characteristics
- processing status
- storage references
- derived asset references
- tags and labels

### Asset Relationships

Assets should be linked to:

- projects
- timelines
- clips or edits
- AI analysis outputs
- rendering results

---

## Timeline Representation

Timeline data should be structured so the editor can efficiently read and update project state.

### Timeline Structure

The timeline representation should include:

- track definitions
- clip placement and timing
- sequencing information
- effect and transition assignments
- reference to source assets
- revision markers and snapshots

### Edit History

The database should preserve a structured history of edits, including:

- operation type
- actor identity
- timestamp
- before and after state references
- associated revision IDs

---

## Collaboration and Audit Records

The persistence model should support collaboration and auditability.

### Collaboration Records

The system should store:

- comments and review threads
- approval or rejection state
- shared access history
- presence or activity events where relevant

### Audit Records

The platform should maintain records for:

- authentication events
- project modification events
- AI execution events
- rendering and export events
- permission changes
- collaboration actions

These records should be retained in a way that supports compliance review and operational troubleshooting.

---

## Multi-Tenant Considerations

The database design should enforce tenant boundaries at the data model level.

### Requirements

- every tenant-scoped record should carry tenant or workspace context
- access policies must be enforceable at query time
- cross-tenant joins should be avoided unless explicitly required
- audit and billing records should remain easily segregated

### Data Partitioning Strategy

The architecture should support:

- shared schema with tenant discriminator fields where appropriate
- logical partitioning per tenant or workspace for sensitive domains
- separate storage policies for high-volume or high-sensitivity data where needed

---

## Scalability and Performance Considerations

The persistence design should support growth without introducing data bottlenecks.

### Scalability Requirements

- efficient reads for active project state
- scalable write paths for collaboration and AI operations
- caching for hot metadata paths
- asynchronous write support for non-critical events
- separation of operational data from large binary payloads

### Storage Strategy Recommendations

- transactional database for relational state
- object storage for media files and artifacts
- search/indexing layer for metadata and content discovery
- event log or stream for workflow state propagation where appropriate

---

## Relationship to Existing Architecture

This document should be read alongside:

- DATA_MODELS.md for conceptual domain modeling
- AI_COMMAND_SPEC.md for execution lineage needs
- AGENT_PROTOCOL.md for agent execution and state records
- VIDEO_ENGINE_SPECIFICATION.md for timeline and rendering-state persistence requirements
- ARCHITECTURE.md for the overall system decomposition
