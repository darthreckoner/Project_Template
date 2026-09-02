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

## Repository mappings

| Skill convention | Repository convention |
| --- | --- |
| Domain terminology | Relevant Vision, Requirements, Architecture, accepted decisions, and explicitly activated supporting knowledge |
| ADRs | `docs/decisions/`, reached through its index and lifecycle |
| Specs | Existing Requirements, GitHub issue, or approved plan as applicable |
| Formal plans | `plans/` and its lifecycle |
| Handoff continuity | `.agent/CONTINUITY.md` and existing durable artifacts |
| Test and validation commands | `docs/DEVELOPMENT_WORKFLOW.md` validation contract |
| Research execution | Background/subagent when supported; current session otherwise |

Installed skills may use these mappings without separate governance approval. External commands,
repository writes, and settings changes still require the authority and scope established by the
user and repository governance.

## Local adaptations

The following upstream-derived core skills have repository-specific adaptations.
Their `skills-lock.json` entries retain upstream origin so maintainers can inspect
upstream changes before updating. Reapply or reconsider the adaptation when an
upstream update touches the same behavior.

| Skill | Local adaptation |
| --- | --- |
| `to-spec` | Creates a traceable `REQ-###` and `VERIFY-###` behavioral contract, resolves blocking ambiguity with the user, and publishes only after readiness confirmation. |
| `to-tickets` | Requires a ready formal specification and proves requirement and verification coverage before ticket publication. |
| `ask-matt` | Describes formalization as part of the existing `to-spec` stage. |
| `code-review` | Reviews formal requirements and verification evidence by identifier, while retaining prose fallback for legacy specifications. |
