#!/usr/bin/env python3
"""Validate installed skill structure and YAML metadata for this template."""

from __future__ import annotations

import re
import sys
import json
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    print(
        'ERROR: PyYAML is required. Run: python -m pip install --upgrade "pip>=25.1" '
        "then python -m pip install --group validation"
    )
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIRECTORIES = {
    "core": ROOT / ".agents" / "skills",
    "extensions": ROOT / ".agents" / "skills-extensions",
}
MAX_SKILL_NAME_LENGTH = 64
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "argument-hint",
    "disable-model-invocation",
}


def parse_yaml(path: Path, text: str, errors: list[str]) -> object | None:
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML ({exc})")
        return None


def validate_skill(skill_directory: Path, errors: list[str]) -> None:
    skill_path = skill_directory / "SKILL.md"
    if not skill_path.is_file():
        errors.append(f"{skill_path.relative_to(ROOT)}: required file is missing")
        return

    try:
        content = skill_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{skill_path.relative_to(ROOT)}: cannot read as UTF-8 ({exc})")
        return

    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        errors.append(f"{skill_path.relative_to(ROOT)}: invalid YAML frontmatter boundary")
        return

    frontmatter = parse_yaml(skill_path, match.group(1), errors)
    if frontmatter is None:
        return
    if not isinstance(frontmatter, dict):
        errors.append(f"{skill_path.relative_to(ROOT)}: frontmatter must be a mapping")
        return

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        errors.append(
            f"{skill_path.relative_to(ROOT)}: unexpected frontmatter keys "
            f"{sorted(unexpected)!r}"
        )

    name = frontmatter.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{skill_path.relative_to(ROOT)}: name must be hyphen-case")
    elif len(name) > MAX_SKILL_NAME_LENGTH:
        errors.append(
            f"{skill_path.relative_to(ROOT)}: name exceeds {MAX_SKILL_NAME_LENGTH} characters"
        )
    elif name != skill_directory.name:
        errors.append(
            f"{skill_path.relative_to(ROOT)}: name {name!r} does not match directory "
            f"{skill_directory.name!r}"
        )

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_path.relative_to(ROOT)}: description must be a non-empty string")
    elif len(description) > 1024:
        errors.append(f"{skill_path.relative_to(ROOT)}: description exceeds 1024 characters")

    disabled = frontmatter.get("disable-model-invocation")
    if disabled is not None and not isinstance(disabled, bool):
        errors.append(
            f"{skill_path.relative_to(ROOT)}: disable-model-invocation must be boolean"
        )

    if re.search(r"(?m)^[ ]{0,3}\[TODO:[^\n]*\][ \t]*$", content[match.end() :]):
        errors.append(f"{skill_path.relative_to(ROOT)}: unfinished TODO placeholder")

    metadata_path = skill_directory / "agents" / "openai.yaml"
    if metadata_path.is_file():
        try:
            metadata_text = metadata_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(
                f"{metadata_path.relative_to(ROOT)}: cannot read as UTF-8 ({exc})"
            )
        else:
            metadata = parse_yaml(metadata_path, metadata_text, errors)
            if metadata is not None and not isinstance(metadata, dict):
                errors.append(f"{metadata_path.relative_to(ROOT)}: metadata must be a mapping")


def main() -> int:
    errors: list[str] = []
    skill_directories = []
    for bundle_directory in SKILLS_DIRECTORIES.values():
        skill_directories.extend(
            path for path in bundle_directory.iterdir() if path.is_dir()
        )
    for skill_directory in sorted(skill_directories):
        validate_skill(skill_directory, errors)

    try:
        lock = json.loads((ROOT / "skills-lock.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"skills-lock.json: cannot read valid JSON ({exc})")
    else:
        for bundle, directory in SKILLS_DIRECTORIES.items():
            for skill_directory in directory.iterdir():
                if skill_directory.is_dir():
                    entry = lock.get("skills", {}).get(skill_directory.name, {})
                    if not entry.get("computedHash"):
                        errors.append(
                            f"skills-lock.json: {skill_directory.name} in {bundle} "
                            "bundle has no computedHash"
                        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Skill validation failed with {len(errors)} error(s).")
        return 1

    print(f"Skill validation passed for {len(skill_directories)} skills across core and extensions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
