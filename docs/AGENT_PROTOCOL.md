# Agent Protocol

## Overview
This document defines the communication rules for AI agents operating within AI Video Studio.

## Agent Roles
- Supervisor Agent: coordinates overall workflow and task decomposition.
- Planning Agent: converts intent into command graphs and dependencies.
- Editing Agent: performs content transforms on the project timeline.
- Analysis Agent: extracts meaning from media, audio, transcripts, and scene structure.
- QA Agent: validates output quality and safety.
- Memory Agent: stores and retrieves contextual history.
- Execution Agent: invokes tools and service endpoints.

## Message Format
- Messages should use a structured envelope that includes sender, recipient, task identifier, action type, payload, timestamp, and correlation identifiers.
- Payloads should be versioned and tied to the active command schema.
- Message content should remain auditable and machine-readable.

## Task Delegation
- Agents should delegate work only when they have the necessary permissions, context, and tool availability.
- Delegation should preserve the parent task context and execution history.
- The system should support nested task chains for complex workflows.

## Permissions
- Each agent should operate within a defined scope based on tenant, workspace, project, and role.
- Sensitive operations should require explicit approval or escalation.
- Agents should not access data outside their assigned scope.

## Conflict Resolution
- Conflicting instructions should be resolved through priority rules, approval gates, and explicit human review where necessary.
- When multiple agents propose incompatible actions, the supervisor should determine the final execution path.

## Failure Recovery
- Agent failures should trigger retry, fallback, or escalation logic.
- Partial progress should be preserved for resume and rollback.
- Recovery actions should be logged for auditability and troubleshooting.
