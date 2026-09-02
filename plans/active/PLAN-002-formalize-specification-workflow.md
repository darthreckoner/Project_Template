# PLAN-002: Formalize specification workflow

Identifier: PLAN-002
Title: Formalize specification workflow
Status: Approved
Approval: Approved by Justin Rutledge on 2026-09-02

## Problem

`to-spec` can publish an implementation-ready issue without proving that it
preserves accepted intent or resolves materially ambiguous behavior. That lets
requirements disappear or change during ticketing and implementation.

## Goal

Produce one human-confirmed, traceable behavioral contract before tickets are
published, then retain its requirements through tickets and code review.

## Scope

- Formalize the governed `to-spec`, `to-tickets`, `ask-matt`, and `code-review`
  workflow skills.
- Add a progressive-disclosure reference for the formal specification template
  and readiness checklist.
- Update local-adaptation provenance, hashes, continuity, and skill governance.
- Reduce the personal `to-formal-spec` skill to an optional audit tool.
- Validate the workflow with isolated independent scenarios and repository
  validators.

## Out of Scope

- Changing product requirements, architecture, or application runtime choices.
- Adding a new tracker label or a separate mandatory workflow stage.
- Publishing implementation tickets for a product feature.

## Current System

`to-spec` synthesizes a conversation, checks testing seams, publishes an issue,
and immediately applies `ready-for-agent`. `to-tickets` can work from a plan,
specification, or conversation, but has no requirement-level traceability.
`code-review` checks a specification through prose quotations. The core skills
are upstream-derived copies governed by `docs/ENGINEERING_RULES.md`.

## Proposed Approach

Make formalization a conditional phase inside `to-spec`. The skill will use
source references, `REQ-###` requirements, `VERIFY-###` properties, a coverage
table, targeted ambiguity questions, a human confirmation gate, and one
canonical published issue. Require `to-tickets` and the Spec review axis to
preserve those identifiers. Keep the personal audit skill separate for existing
or externally produced specifications.

## Affected Components / Files

- `.agents/skills/to-spec/`, `.agents/skills/to-tickets/`,
  `.agents/skills/ask-matt/`, and `.agents/skills/code-review/`
- `docs/agents/skill-governance.md`, `skills-lock.json`, and
  `.agent/CONTINUITY.md`
- `C:\Users\Justin Rutledge\.codex\skills\to-formal-spec\`

## Risks

- The new contract could turn small changes into ceremony. Mitigation: omit
  inapplicable sections and restrict formalization to meaningful ambiguity.
- Local adaptations could be overwritten by upstream updates. Mitigation:
  document the adaptations and retain upstream provenance with current hashes.
- Instruction changes can look correct without changing agent behavior.
  Mitigation: run independent isolated scenario trials before delivery.

## Testing Plan

- `python scripts/check_governance.py`
- `python scripts/check_skills.py`
- `git diff --check`
- The skill-creator quick validator for the personal audit skill.
- Independent scenarios for trivial, stateful, ambiguous, omitted-source,
  ticket-coverage, code-review, and legacy-specification behavior.

## Acceptance Criteria

- [x] `to-spec` publishes only a human-confirmed, ready formal specification
  with traceable requirements and verification properties.
- [x] `to-tickets` preserves complete `REQ-###` and `VERIFY-###` coverage.
- [x] `code-review` evaluates identified requirements and retains legacy prose
  fallback.
- [x] `ask-matt` routes the main flow through the strengthened `to-spec`.
- [x] The personal skill audits existing specifications without publishing.
- [x] Repository and personal skill validators pass with no unrelated changes.

## Related Requirements

None

## Related ADRs

None

## Open Questions

None

## Approval Record

Approved by: Justin Rutledge
Approval date: 2026-09-02

## Closure Metadata

Completion date: Pending
Related requirements: None
Related ADRs: None
Implementation PR: Pending
Implementation commits: Pending
Validation result: `check_governance.py`, `check_skills.py`, personal skill validation, lock-hash verification, and `git diff --check` passed on 2026-09-02; independent workflow scenarios passed.
Documentation impact: Pending
Unresolved follow-ups: Pending

Requirements impact: None
Architecture impact: None
ADR impact: None
Knowledge impact: None
