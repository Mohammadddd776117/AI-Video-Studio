from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from command_parser.parser import SimpleCommandParser
from command_schema.models import Command, CommandValidationResult, ExecutionStatus
from command_validator.validator import CommandValidator, PermissionContext


@dataclass(slots=True)
class ExecutionStep:
    name: str
    status: str


@dataclass(slots=True)
class OrchestrationResult:
    command: Command
    validation_result: CommandValidationResult
    plan: List[ExecutionStep] = field(default_factory=list)
    status: str = "planned"


class AIOrchestrator:
    """Central coordination layer for command planning and validation."""

    def __init__(self) -> None:
        self.parser = SimpleCommandParser()
        self.validator = CommandValidator()

    def handle_request(self, text: str, *, context: Dict[str, Any] | None = None) -> OrchestrationResult:
        command = self.parser.parse(text, context=context)
        permission_context = PermissionContext(
            user_id=context.get("actor_id", "user-default") if context else "user-default",
            can_approve=True,
            can_execute=True,
        )
        validation_result = self.validator.validate(command, permission_context=permission_context)

        plan = [
            ExecutionStep(name="prepare_execution", status="ready"),
            ExecutionStep(name="dispatch_to_tools", status="pending"),
        ]

        if not validation_result.valid:
            return OrchestrationResult(
                command=command,
                validation_result=validation_result,
                plan=plan,
                status="blocked",
            )

        command.execution_status = ExecutionStatus.PLANNED
        return OrchestrationResult(
            command=command,
            validation_result=validation_result,
            plan=plan,
            status="planned",
        )
