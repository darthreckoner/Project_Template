#!/usr/bin/env python3
"""Validate the small, deterministic governance contract for this template."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    ".gitignore",
    "docs/ENGINEERING_RULES.md",
    "docs/BOOTSTRAP_CHECKLIST.md",
    "docs/VISION.md",
    "docs/REQUIREMENTS.md",
    "docs/ARCHITECTURE.md",
    "docs/DEVELOPMENT_WORKFLOW.md",
    "docs/PLANNING_PLAYBOOK.md",
    "docs/REPOSITORY_POLICY.md",
    "docs/decisions/README.md",
    "docs/decisions/ADR-TEMPLATE.md",
    "plans/README.md",
    "plans/PLAN-TEMPLATE.md",
    "scripts/check_governance.py",
    ".github/CODEOWNERS",
    ".github/workflows/ci.yml",
    ".github/pull_request_template.md",
)

REQUIRED_DIRECTORIES = (
    "docs/decisions/proposed",
    "docs/decisions/accepted",
    "plans/draft",
    "plans/active",
    "plans/backlog",
    "plans/completed",
    "src",
    "tests",
)

STATUS_RULES = {
    "docs/decisions/proposed": {"Proposed", "Rejected", "Superseded"},
    "docs/decisions/accepted": {"Accepted"},
    "plans/draft": {"Draft"},
    "plans/active": {"Approved"},
    "plans/completed": {"Completed"},
}

COMPLETED_PLAN_FIELDS = (
    "Approval",
    "Completion date",
    "Related Requirements",
    "Related ADRs",
    "Implementation PR",
    "Implementation commits",
    "Validation result",
    "Documentation impact",
    "Unresolved follow-ups",
    "Requirements impact",
    "Architecture impact",
    "ADR impact",
    "Knowledge impact",
)


def markdown_files(relative_directory: str) -> list[Path]:
    directory = ROOT / relative_directory
    return sorted(
        path
        for path in directory.glob("*.md")
        if path.name.lower() not in {"readme.md", ".gitkeep"}
    )


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read as UTF-8 ({exc})")
        return ""


def field_value(text: str, field: str) -> str | None:
    match = re.search(
        rf"(?im)^(?:[-*]\s+)?{re.escape(field)}:\s*(.+?)\s*$",
        text,
    )
    return match.group(1).strip() if match else None


def check_structure(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"{relative_path}: required file is missing")
    for relative_path in REQUIRED_DIRECTORIES:
        if not (ROOT / relative_path).is_dir():
            errors.append(f"{relative_path}/: required directory is missing")


def check_lifecycle_states(errors: list[str]) -> None:
    for relative_directory, allowed_statuses in STATUS_RULES.items():
        for path in markdown_files(relative_directory):
            text = read_text(path, errors)
            status = field_value(text, "Status")
            if status not in allowed_statuses:
                allowed = ", ".join(sorted(allowed_statuses))
                errors.append(
                    f"{path.relative_to(ROOT)}: Status must be one of [{allowed}] "
                    f"for {relative_directory}/ (found {status!r})"
                )


def check_completed_plan_metadata(errors: list[str]) -> None:
    for path in markdown_files("plans/completed"):
        text = read_text(path, errors)
        for field in COMPLETED_PLAN_FIELDS:
            value = field_value(text, field)
            if value is None:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing completed-plan field '{field}:'"
                )
            elif value.lower() in {"pending", "tbd", "todo", "[pending]"}:
                errors.append(
                    f"{path.relative_to(ROOT)}: completed-plan field '{field}' is unresolved"
                )


def check_index_entries(errors: list[str]) -> None:
    decision_index = read_text(ROOT / "docs/decisions/README.md", errors)
    plan_index = read_text(ROOT / "plans/README.md", errors)

    for directory in ("docs/decisions/proposed", "docs/decisions/accepted"):
        for path in markdown_files(directory):
            text = read_text(path, errors)
            adr_id = field_value(text, "ID")
            if not adr_id or not re.fullmatch(r"ADR-\d{4}", adr_id):
                errors.append(
                    f"{path.relative_to(ROOT)}: ID must use the form ADR-0001"
                )
            elif not re.search(rf"(?m)^\|\s*{re.escape(adr_id)}\s*\|", decision_index):
                errors.append(
                    f"{path.relative_to(ROOT)}: {adr_id} is missing from "
                    "docs/decisions/README.md"
                )

    for path in markdown_files("plans/completed"):
        text = read_text(path, errors)
        plan_id = field_value(text, "Identifier")
        if not plan_id or not re.fullmatch(r"PLAN-\d{3}", plan_id):
            errors.append(f"{path.relative_to(ROOT)}: Identifier must use the form PLAN-001")
        elif not re.search(rf"(?m)^\|\s*{re.escape(plan_id)}\s*\|", plan_index):
            errors.append(
                f"{path.relative_to(ROOT)}: {plan_id} is missing from plans/README.md"
            )


def has_application_code() -> bool:
    source = ROOT / "src"
    return any(path.is_file() and path.name != ".gitkeep" for path in source.rglob("*"))


def check_application_validation(errors: list[str]) -> None:
    if not has_application_code():
        return

    workflow = read_text(ROOT / ".github/workflows/ci.yml", errors)
    contract = read_text(ROOT / "docs/DEVELOPMENT_WORKFLOW.md", errors)
    if "APPLICATION_VALIDATION: NOT_CONFIGURED" in contract:
        errors.append(
            "docs/DEVELOPMENT_WORKFLOW.md: application code exists but the validation "
            "contract is not configured"
        )
    if "APPLICATION_VALIDATION_COMMAND: NOT_CONFIGURED" in workflow:
        errors.append(
            ".github/workflows/ci.yml: application code exists but CI application "
            "validation is not configured"
        )


def main() -> int:
    errors: list[str] = []
    check_structure(errors)

    # Later checks assume the core paths exist; report structure errors cleanly first.
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Governance validation failed with {len(errors)} error(s).")
        return 1

    check_lifecycle_states(errors)
    check_completed_plan_metadata(errors)
    check_index_entries(errors)
    check_application_validation(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Governance validation failed with {len(errors)} error(s).")
        return 1

    print("Governance validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
