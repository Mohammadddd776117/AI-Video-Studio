from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ApprovalState(str, Enum):
    AUTO = "auto"
    REVIEW = "review"
    EXPLICIT = "explicit"


class ExecutionStatus(str, Enum):
    PENDING = "pending"
    PLANNED = "planned"
    APPROVED = "approved"
    EXECUTING = "executing"
    VALIDATING = "validating"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


@dataclass(slots=True)
class CommandAsset:
    id: str
    type: str
    name: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class CommandOperation:
    id: str
    type: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    depends_on: Optional[List[str]] = None


@dataclass(slots=True)
class Command:
    command_id: str
    session_id: str
    actor_id: str
    intent: str
    assets: List[CommandAsset] = field(default_factory=list)
    operations: List[CommandOperation] = field(default_factory=list)
    parameters: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    approval_state: ApprovalState = ApprovalState.AUTO
    execution_status: ExecutionStatus = ExecutionStatus.PENDING
    schema_version: str = "1.0"
    source: str = "user"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ValidationIssue:
    code: str
    message: str


@dataclass(slots=True)
class CommandValidationResult:
    valid: bool
    issues: List[ValidationIssue] = field(default_factory=list)
