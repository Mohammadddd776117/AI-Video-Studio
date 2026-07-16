# Documentation Cleanup Plan

## Purpose

This document defines a documentation governance and consolidation plan for AI Video Studio. It is intended to reduce ambiguity, identify overlapping responsibilities, and make the repository’s documentation set more coherent without deleting or rewriting existing files.

The plan assumes the current documentation corpus is already substantial and directionally mature. The main goal is to create a maintenance and consolidation model that preserves the architecture baseline while improving navigability and consistency.

---

## Current Documentation Issues Identified

The current documentation structure shows several governance concerns that should be addressed through planned consolidation rather than ad hoc new documents.

### 1. Duplicate or near-duplicate document intent

The following pairs show clear overlap in intent and should be treated as consolidation candidates:

- PRODUCT_REQUIREMENTS.md and PRODUCT_SPECIFICATION.md
  - Both describe product scope and capability intent.
  - One should remain the requirements baseline; the other should remain the master functional framing.

- ARCHITECTURE.md and SYSTEM_DESIGN.md
  - Both describe the platform blueprint.
  - One should remain the high-level architectural reference; the other should remain the end-to-end synthesis artifact.

- AI_SYSTEM.md and AI_RUNTIME_ARCHITECTURE.md
  - Both define AI system behavior and orchestration expectations.
  - One should remain the broader AI system definition; the other should remain the runtime execution detail layer.

- BACKEND_SERVICES.md and BACKEND_SERVICES_DESIGN.md
  - Both define backend service structure and design concerns.
  - One should serve as the primary backend overview; the other should remain the deeper service design reference.

- FLUTTER_ARCHITECTURE.md and FLUTTER_APPLICATION_ARCHITECTURE.md
  - Both describe the Flutter application structure and experience model.
  - One should be designated as the canonical client architecture reference and the other treated as a supplemental or historical companion.

- ARCHITECTURE_REVIEW.md and ARCHITECTURE_REVIEW_REPORT.md
  - Both are architecture review artifacts.
  - One should remain the review narrative, and the other should be treated as a supporting historical or evidence artifact.

### 2. Overlapping responsibilities

Some documents appear to serve both reference and synthesis roles, which can create ambiguity when teams need a single authoritative answer.

Examples include:

- SYSTEM_DESIGN.md currently acts as a synthesis layer for several architecture domains.
- ARCHITECTURE.md currently serves as the top-level decomposition reference.
- PRODUCT_SPECIFICATION.md and PRODUCT_REQUIREMENTS.md both carry product framing language.
- AI_SYSTEM.md and AI_RUNTIME_ARCHITECTURE.md can both be read as operational definitions for the AI layer.

This is not inherently incorrect, but it means that governance is needed to define which document is canonical for which concern.

---

## Documents That Should Become Canonical References

The following documents are the best candidates to become the stable canonical references for the documentation set:

### Product

- VISION.md — canonical strategic product direction
- PRODUCT_SPECIFICATION.md — canonical functional product framing
- UI_UX_ARCHITECTURE.md — canonical experience structure reference

### Architecture

- ARCHITECTURE.md — canonical high-level platform decomposition
- SYSTEM_DESIGN.md — canonical master system synthesis document
- API_CONTRACTS.md — canonical API contract reference
- DATABASE_SCHEMA.md — canonical persistence architecture reference

### AI system

- AI_SYSTEM.md — canonical AI orchestration and system model
- AI_COMMAND_SPEC.md — canonical command structure reference
- AGENT_PROTOCOL.md — canonical agent interaction contract reference
- TOOL_SCHEMA.md — canonical tool capability model

### Engineering

- DEVELOPMENT_GUIDELINES.md — canonical engineering governance reference
- TESTING_STRATEGY.md — canonical quality and validation strategy reference
- CODEBASE_STRUCTURE.md — canonical repository organization reference

These documents should be treated as the primary navigational anchors for the repository’s documentation system.

---

## Documents That May Require Future Merging

The following documents should be considered candidates for future merge or one-primary-reference designation:

### Candidate merge set 1: product framing

- PRODUCT_REQUIREMENTS.md
- PRODUCT_SPECIFICATION.md

Recommended direction:
- Keep one as the requirements baseline.
- Keep one as the functional spec/feature framing reference.
- Use cross-links instead of duplicate wording.

### Candidate merge set 2: platform architecture synthesis

- ARCHITECTURE.md
- SYSTEM_DESIGN.md

Recommended direction:
- Keep ARCHITECTURE.md as the concise system decomposition summary.
- Keep SYSTEM_DESIGN.md as the cross-domain synthesis blueprint.
- Avoid duplicating the same architectural facts in both documents.

### Candidate merge set 3: AI layer definitions

- AI_SYSTEM.md
- AI_RUNTIME_ARCHITECTURE.md

Recommended direction:
- Keep AI_SYSTEM.md as the primary AI layer narrative.
- Keep AI_RUNTIME_ARCHITECTURE.md as the execution-oriented supplement.

### Candidate merge set 4: backend layer definitions

- BACKEND_SERVICES.md
- BACKEND_SERVICES_DESIGN.md

Recommended direction:
- Keep one as the service overview reference and one as the design detail reference.
- Ensure service ownership and cross-service roles remain consistent.

### Candidate merge set 5: Flutter scope

- FLUTTER_ARCHITECTURE.md
- FLUTTER_APPLICATION_ARCHITECTURE.md

Recommended direction:
- Designate one as the canonical client architecture document.
- Treat the other as a supplementary or implementation-facing companion.

### Candidate merge set 6: architecture review artifacts

- ARCHITECTURE_REVIEW.md
- ARCHITECTURE_REVIEW_REPORT.md

Recommended direction:
- Preserve review history with clear status labels.
- Avoid treating both as equally current sources of truth.

---

## Naming Consistency Rules

Future documentation should follow naming rules that reduce ambiguity.

### Recommended naming patterns

- VISION.md — strategic direction
- PRODUCT_REQUIREMENTS.md — requirement baseline
- PRODUCT_SPECIFICATION.md — feature and capability specification
- ARCHITECTURE.md — top-level decomposition
- SYSTEM_DESIGN.md — cross-layer synthesis
- AI_SYSTEM.md — AI domain definition
- AI_RUNTIME_ARCHITECTURE.md — runtime execution model
- BACKEND_SERVICES.md — service overview
- BACKEND_SERVICES_DESIGN.md — service design details
- FLUTTER_APPLICATION_ARCHITECTURE.md — client architecture
- DEVELOPMENT_GUIDELINES.md — standards and operating rules
- TESTING_STRATEGY.md — quality and validation strategy
- SECURITY_ARCHITECTURE.md — security model
- DATABASE_SCHEMA.md — persistence architecture

### Naming principles

- Use consistent suffixes: VISION, REQUIREMENTS, SPECIFICATION, ARCHITECTURE, SYSTEM, GUIDELINES, STRATEGY, REVIEW, SCHEMA, CONTRACTS.
- Avoid creating multiple names for the same responsibility area unless one is clearly a supplement.
- Prefer a single canonical name for a domain and use derivative names only when the document adds a distinct audience or detail level.

---

## Documentation Maintenance Rules

The following maintenance rules should govern how the documentation set evolves:

1. No document should be added without a clear governance role.
2. No new document should duplicate an established canonical source-of-truth unless it adds a new perspective that is not already covered.
3. If a document becomes outdated, it should be marked clearly for review rather than silently left as a competing reference.
4. Cross-references should be maintained whenever a document changes ownership boundaries, contracts, or responsibilities.
5. Review datedness should be treated as part of governance. Architecture, product, AI, and engineering documents should be reviewed periodically for drift.
6. Historical documents should remain readable and clearly labeled as historical references where appropriate.
7. Canonical documents should remain the entry points for implementation decisions.

---

## Recommended Cleanup Steps Before Implementation

The implementation sequence for documentation governance should remain lightweight and non-destructive.

1. Establish DOCUMENTATION_INDEX.md as the canonical navigation document.
2. Use DOCUMENTATION_CLEANUP_PLAN.md to classify all current documents by role.
3. Identify the single canonical reference per domain.
4. Add cross-links where overlapping documents currently compete for authority.
5. Treat the current documentation set as a layer-based system rather than introducing new parallel structures.
6. Avoid any file deletion or content rewrite during this governance phase.
7. Schedule a follow-up consolidation exercise after the first implementation milestone, when ownership boundaries are more stable.

---

## Governance Outcome

The documentation cleanup objective is not to reduce the number of files immediately. It is to stabilize the documentation model so that the repository supports implementation without drifting into competing architectural narratives.

The most important governance outcome is this:

- one canonical reference per major domain
- explicit relationship rules between documents
- no undocumented duplication
- no destructive cleanup during the governance foundation phase
