import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from command_schema.models import ApprovalState, Command, CommandAsset, CommandOperation, ExecutionStatus
from command_parser.parser import CommandParsingError, SimpleCommandParser
from command_validator.validator import PermissionContext, ValidationIssue, CommandValidator
from ai_orchestrator.orchestrator import AIOrchestrator


def test_command_creation_supports_core_fields():
    command = Command(
        command_id="cmd-001",
        session_id="session-001",
        actor_id="user-001",
        intent="edit",
        assets=[CommandAsset(id="asset-001", type="clip", name="intro")],
        operations=[CommandOperation(id="op-001", type="transform", parameters={"preset": "social-short"})],
        parameters={"target_length": 12},
        confidence=0.82,
        approval_state=ApprovalState.REVIEW,
        execution_status=ExecutionStatus.PLANNED,
    )

    assert command.intent == "edit"
    assert command.assets[0].name == "intro"
    assert command.operations[0].parameters["preset"] == "social-short"
    assert command.confidence == 0.82


def test_validator_accepts_valid_commands_and_rejects_missing_required_fields():
    validator = CommandValidator()
    valid_command = Command(
        command_id="cmd-002",
        session_id="session-002",
        actor_id="user-002",
        intent="export",
        assets=[CommandAsset(id="asset-002", type="timeline")],
        operations=[CommandOperation(id="op-002", type="export")],
        confidence=0.9,
    )

    result = validator.validate(valid_command)
    assert result.valid is True
    assert result.issues == []

    invalid_command = Command(
        command_id="",
        session_id="session-003",
        actor_id="user-003",
        intent="",
        assets=[],
        operations=[],
        confidence=1.2,
    )

    result = validator.validate(invalid_command)
    assert result.valid is False
    assert any(issue.code == "missing_required_field" for issue in result.issues)
    assert any(issue.code == "invalid_confidence" for issue in result.issues)


def test_parser_converts_natural_language_to_structured_command():
    parser = SimpleCommandParser()
    command = parser.parse("Create a short social clip with captions from the intro scene")

    assert command.intent == "edit"
    assert command.operations[0].type == "generate_captions"
    assert command.parameters["source_text"].startswith("Create a short social clip")
    assert command.confidence >= 0.6


def test_parser_and_validator_handle_errors_gracefully():
    parser = SimpleCommandParser()
    validator = CommandValidator()

    try:
        parser.parse("   ")
    except CommandParsingError as exc:
        assert "required" in str(exc).lower()
    else:
        raise AssertionError("Expected parser to reject blank input")

    permission_context = PermissionContext(user_id="user-004", can_approve=False)
    command = Command(
        command_id="cmd-004",
        session_id="session-004",
        actor_id="user-004",
        intent="export",
        assets=[CommandAsset(id="asset-004", type="timeline")],
        operations=[CommandOperation(id="op-004", type="export")],
        confidence=0.75,
    )

    result = validator.validate(command, permission_context=permission_context)
    assert result.valid is False
    assert any(issue.code == "approval_required" for issue in result.issues)


def test_orchestrator_builds_plan_for_valid_command():
    orchestrator = AIOrchestrator()
    result = orchestrator.handle_request(
        "Create a short social clip with captions",
        context={"asset_ids": ["asset-100"]},
    )

    assert result.command.intent == "edit"
    assert result.validation_result.valid is True
    assert result.plan[0].name == "prepare_execution"
    assert result.status == "planned"
