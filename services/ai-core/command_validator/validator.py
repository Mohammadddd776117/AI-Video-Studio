from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from command_schema.models import ApprovalState, Command, CommandValidationResult, ExecutionStatus, ValidationIssue


@dataclass(slots=True)
class PermissionContext:
    user_id: str
    can_approve: bool = False
    can_execute: bool = True


class CommandValidator:
    """Validates command structure, required fields, permissions, and execution constraints."""

    def validate(self, command: Command, *, permission_context: Optional[PermissionContext] = None) -> CommandValidationResult:
        issues: list[ValidationIssue] = []

        if not command.command_id:
            issues.append(ValidationIssue(code="missing_required_field", message="command_id is required"))
        if not command.session_id:
            issues.append(ValidationIssue(code="missing_required_field", message="session_id is required"))
        if not command.actor_id:
            issues.append(ValidationIssue(code="missing_required_field", message="actor_id is required"))
        if not command.intent:
            issues.append(ValidationIssue(code="missing_required_field", message="intent is required"))
        if not command.assets:
            issues.append(ValidationIssue(code="missing_required_field", message="assets must include at least one item"))
        if not command.operations:
            issues.append(ValidationIssue(code="missing_required_field", message="operations must include at least one item"))
        if not 0 <= command.confidence <= 1:
            issues.append(ValidationIssue(code="invalid_confidence", message="confidence must be between 0 and 1"))

        if command.approval_state == ApprovalState.EXPLICIT and not permission_context:
            issues.append(ValidationIssue(code="approval_required", message="explicit approval requires a permission context"))

        requires_approval = command.approval_state in {ApprovalState.REVIEW, ApprovalState.EXPLICIT} or any(
            operation.type.lower() in {"export", "publish", "render", "delete"} or command.intent.lower() in {"export", "publish", "delete"}
            for operation in command.operations
        )

        if requires_approval and permission_context is not None and not permission_context.can_approve:
            issues.append(ValidationIssue(code="approval_required", message="approval is required for this command"))

        if command.execution_status in {ExecutionStatus.EXECUTING, ExecutionStatus.COMPLETED, ExecutionStatus.FAILED}:
            if not command.operations:
                issues.append(ValidationIssue(code="invalid_execution_state", message="execution state requires operations"))

        if not permission_context:
            permission_context = PermissionContext(user_id=command.actor_id, can_approve=True, can_execute=True)

        if not permission_context.can_execute:
            issues.append(ValidationIssue(code="permission_denied", message="actor cannot execute commands"))

        return CommandValidationResult(valid=not issues, issues=issues)
