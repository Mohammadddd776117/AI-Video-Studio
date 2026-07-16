from __future__ import annotations

from typing import Any, Dict, Optional
from uuid import uuid4

from command_schema.models import ApprovalState, Command, CommandAsset, CommandOperation, ExecutionStatus


class CommandParsingError(ValueError):
    """Raised when a natural language request cannot be parsed into a command."""


class CommandParser:
    """Provider-independent interface for converting natural language into a structured command."""

    def parse(self, text: str, *, context: Optional[Dict[str, Any]] = None) -> Command:
        raise NotImplementedError


class SimpleCommandParser(CommandParser):
    """A lightweight parser that uses heuristic rules for an initial prototype."""

    def parse(self, text: str, *, context: Optional[Dict[str, Any]] = None) -> Command:
        if not text or not text.strip():
            raise CommandParsingError("Input text is required")

        normalized = text.strip()
        lower_text = normalized.lower()

        intent = "edit" if any(keyword in lower_text for keyword in ["clip", "edit", "caption", "scene"]) else "analyze"
        operations: list[CommandOperation] = []

        if "caption" in lower_text:
            operations.append(CommandOperation(id=str(uuid4()), type="generate_captions"))
        if "clip" in lower_text or "edit" in lower_text:
            operations.append(CommandOperation(id=str(uuid4()), type="transform"))

        if not operations:
            operations.append(CommandOperation(id=str(uuid4()), type="review"))

        assets = []
        asset_ids = context.get("asset_ids", []) if context else []
        for index, asset_id in enumerate(asset_ids[:3], start=1):
            assets.append(CommandAsset(id=str(asset_id), type="clip", name=f"asset-{index}"))

        if not assets:
            assets.append(CommandAsset(id=str(uuid4()), type="timeline", name="current-project"))

        return Command(
            command_id=str(uuid4()),
            session_id=context.get("session_id", "session-default") if context else "session-default",
            actor_id=context.get("actor_id", "user-default") if context else "user-default",
            intent=intent,
            assets=assets,
            operations=operations,
            parameters={"source_text": normalized},
            confidence=0.72 if "clip" in lower_text or "caption" in lower_text else 0.6,
            approval_state=ApprovalState.REVIEW if "export" in lower_text else ApprovalState.AUTO,
            execution_status=ExecutionStatus.PLANNED,
            metadata={"parser": "simple-heuristic", "provider": "none"},
        )
