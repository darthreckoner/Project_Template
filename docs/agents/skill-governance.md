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

## Existing mappings

| Upstream skill convention | Repository convention |
| --- | --- |
| `CONTEXT.md` / `CONTEXT-MAP.md` | Relevant Vision, Requirements, Architecture, and activated domain knowledge |
| `docs/adr/` | `docs/decisions/`, reached through its index |
| Specs | Existing Requirements, issue, or approved plan as applicable |
| Plans | `plans/` and its lifecycle |
| Handoff continuity | `.agent/CONTINUITY.md` and existing durable artifacts |
| Test and validation commands | `docs/DEVELOPMENT_WORKFLOW.md` validation contract |

The installed skills may use these mappings without separate per-skill approval. A skill-specific
adapter is needed only if the skill cannot follow this policy through ordinary interpretation.
