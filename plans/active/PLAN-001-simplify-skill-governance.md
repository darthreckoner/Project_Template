# PLAN-001: Simplify Skill Governance

Identifier: PLAN-001
Title: Simplify Skill Governance
Status: Approved
Approval: Human approval recorded in Codex task conversation

## Problem

The repository contains a growing set of installed engineering skills. Requiring a separate
governance contract or approval gate for every skill would add administrative overhead and create
another layer of durable policy. The repository needs one simple rule: skills are procedural tools
that remain subordinate to the existing canonical governance.

## Goal

Refactor the template so selected installed skills are usable by default when compatible with the
repository, while preserving durable intent, human approval gates, deterministic validation, and
explicit escalation for conflicts or uncertainty.

## Scope

- Clarify canonical governance and terminology around intent-first work, planning levels, skill use,
  and closure.
- Define one repository-wide skill governance policy.
- Preserve Level 0, Level 1, and Level 2 planning classification.
- Audit selected installed skills and add only material-conflict adapters or mappings.
- Update bootstrap and CI governance validation for the revised policy.
- Validate a fresh template bootstrap, an ordinary change path, a trigger-based change path, and
  skill routing without duplicate canonical artifacts.

## Out of Scope

- Individual approval or formal governance contracts for every installed skill.
- Requiring every skill to be used.
- Replacing the repository's canonical Vision, Requirements, Architecture, decision, plan, security,
  or workflow records with upstream skill conventions.
- External GitHub settings or contacting upstream skill authors.
- Application runtime/toolchain configuration beyond the existing template bootstrap contract.

## Current System

`docs/ENGINEERING_RULES.md` is the canonical policy. It currently defines authority, context
economy, broad planning triggers, human approval transitions, and working rules. Installed skills
are present under `.agents/skills/`, with provenance in `skills-lock.json`; existing repository
guidance is under `docs/agents/` and `AGENTS.md`.

## Proposed Approach

1. Add a repository-wide skill policy stating that installed skills are available by default but
   cannot override repository governance, create duplicate canonical artifacts, or silently
   downgrade uncertainty.
2. Define the three planning levels:
   - Level 0: clearly specified, localized, low-risk work changing no durable intent.
   - Level 1: bounded implementation choices that do not alter requirements, architecture,
     security boundaries, major system behavior, or similarly durable intent.
   - Level 2: consequential changes affecting requirements, architecture, trust/security boundaries,
     persistent schemas, public interfaces, migrations, multiple system areas, accepted decisions,
     or similarly durable intent.
3. Require escalation rather than downgrade when classification is uncertain.
4. Update the workflow, README, and relevant routing guidance to use the simplified model without
   duplicating canonical rules.
5. Review the selected skills for actual conflicts and write only necessary local adapters or
   mappings.
6. Extend deterministic governance checks and CI evidence for the revised structure.

## Affected Components / Files

- `docs/ENGINEERING_RULES.md`
- `docs/PLANNING_PLAYBOOK.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `README.md`
- `AGENTS.md`
- `.agents/skills/` selected skill files or adapters only where required
- `docs/agents/` routing records only where required
- `scripts/check_governance.py`
- `.github/workflows/ci.yml`
- `plans/README.md`

## Risks

- Simplification could accidentally weaken approval or intent protections; mitigate with explicit
  protected artifacts, escalation rules, and negative validation cases.
- “Available by default” could be mistaken for “compatible without inspection”; mitigate with the
  repository-wide policy and targeted conflict audit.
- Skill assumptions may introduce duplicate paths or terminology; mitigate by preserving canonical
  ownership and adding adapters only for material conflicts.
- Existing user changes in `.agents/`, `docs/agents/`, and `skills-lock.json` may overlap this work;
  preserve and inspect them before editing.

## Testing Plan

- Run `python scripts/check_governance.py`.
- Run the repository's controlled negative governance checks where applicable.
- Verify CI invokes the same governance command.
- Perform a fresh-template bootstrap check.
- Exercise representative Level 0/1/2 routing examples and verify no duplicate canonical artifact
  is required by selected skills.

## Acceptance Criteria

- [ ] One repository-wide skill governance policy is canonical and no per-skill approval gate is
  required.
- [ ] Existing governance remains authoritative over installed skills.
- [ ] Level 0, Level 1, and Level 2 planning are documented consistently across routing and workflow
  documents.
- [ ] Uncertain planning classification escalates rather than downgrades.
- [ ] Only material skill conflicts receive local adapters or mappings.
- [ ] Bootstrap validation passes and CI runs the same governance validation.
- [ ] Fresh-template, ordinary-change, trigger-based-change, and skill-routing checks are evidenced.

## Related Requirements

- None recorded; this plan refines accepted repository governance and template behavior.

## Related ADRs

- None.

## Open Questions

- Whether the revised canonical terminology requires a proposed ADR after implementation review.
- Which selected skills require material adapters after the audit.

## Approval Record

Approved by: Justin Rutledge
Approval date: 2026-08-25

## Closure Metadata

Completion date: Pending
Related requirements: Pending
Related ADRs: Pending
Implementation PR: Pending
Implementation commits: Pending
Validation result: Pending
Documentation impact: Pending
Unresolved follow-ups: Pending

Requirements impact: Pending
Architecture impact: Pending
ADR impact: Pending
Knowledge impact: Pending
