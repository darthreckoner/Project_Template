# Installed Skill Governance

Installed skills are procedural tools. They are available for use by default, but they remain
subordinate to the repository's canonical governance.

## Rules

- `docs/ENGINEERING_RULES.md` is authoritative over every installed skill.
- Skills do not override Vision, Requirements, Architecture, accepted ADRs, security rules,
  approval gates, or protected intent.
- Skills do not create duplicate canonical artifacts because an upstream skill uses another name or
  path.
- Skills use existing project paths, terminology, workflows, validation commands, and artifact
  structures wherever possible.
- Add a local adapter only for a material conflict or extension. Do not add adapters for cleanly
  compatible skills.
- If the correct adaptation is unclear, stop and escalate.

## Installed capabilities

| Skill | Repository boundary |
| --- | --- |
| `claude-handoff` | User-invoked handoff to a Claude Code background agent; reuse existing durable artifacts and preserve protected intent. |
| `git-guardrails-claude-code` | Configure Claude Code hooks only after the user chooses project or global scope; preserve existing settings and verify the hook. |

These skills may be used without separate governance approval. Their external commands and settings
changes still require the authority and scope established by the user and repository governance.
