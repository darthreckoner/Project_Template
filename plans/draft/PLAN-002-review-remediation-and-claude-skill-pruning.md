# PLAN-002: Review Remediation and Claude Code Skill Pruning

Identifier: PLAN-002
Title: Review Remediation and Claude Code Skill Pruning
Status: Draft
Approval: Withdrawn after the human clarified that the pruning scope was misunderstood

## Problem

Review of `codex/skills-eval` found one surviving universal human-closure requirement, two installed
skills that contradict repository governance, an unfulfilled GitHub CLI bootstrap assumption, a
duplicated planning sentence, and no defined owner for Level 1 decision notes. The branch also
contains 37 installed skills, while the desired template scope is now limited to skills specifically
related to Claude Code.

## Goal

Make the branch merge-ready by correcting the review findings, retaining only the two explicitly
Claude Code-specific skills, and removing skill-derived configuration that no longer has a consumer.

## Scope

- Correct ordinary closure so human approval is required only for protected authority transitions.
- Define where Level 1 decisions are recorded without creating a new artifact lifecycle.
- Remove the duplicate formal-planning sentence.
- Retain only `claude-handoff` and `git-guardrails-claude-code`.
- Remove all other installed skill directories and their entries from `skills-lock.json`.
- Remove or simplify routing and configuration that exists only for removed skills.
- Keep the repository-wide skill governance policy, narrowed to the remaining Claude Code skills.
- Update deterministic governance checks and bootstrap guidance to match the resulting repository.
- Re-run local governance validation and review the final branch diff before PR/merge.

## Out of Scope

- Installing, invoking, or configuring either retained Claude Code skill.
- Modifying global Claude Code settings or hooks.
- Contacting upstream skill authors.
- Changing remote GitHub settings, opening a PR, or merging the branch.
- Adding replacement skills for any removed capability.

## Current System and Review Disposition

| Review finding | Planned disposition |
| --- | --- |
| Universal human confirmation before every closure | Replace with verification and closure records for ordinary work; retain human approval only for formal-plan activation/completion, ADR acceptance, protected intent changes, and other explicit human gates. |
| `domain-modeling` creates `CONTEXT.md` and `docs/adr/` | Remove `domain-modeling` and its callers because they are outside the Claude Code-only skill scope. Remove orphaned domain-routing configuration rather than adapting the deleted skill. |
| `resolving-merge-conflicts` says always resolve | Remove the skill because it is outside the Claude Code-only scope. Repository-wide stop/escalate rules remain authoritative for any future conflict work. |
| GitHub Issues skills assume an available authenticated `gh` CLI | Remove the issue-backed skills and their skill-specific issue/triage/domain routing. Do not add a `gh` bootstrap dependency solely for deleted skills. |
| Duplicate formal-planning sentence | Remove the duplicate. |
| Level 1 decision-note location undefined | State that Level 1 decisions belong in the most relevant existing durable artifact, issue, or active work record; prohibit a standalone Level 1 note system. |

## Skill Inventory

### Retain

- `claude-handoff`
- `git-guardrails-claude-code`

### Remove

- `ask-matt`
- `code-review`
- `codebase-design`
- `diagnosing-bugs`
- `domain-modeling`
- `grill-me`
- `grill-with-docs`
- `grilling`
- `handoff`
- `implement`
- `implement-spec`
- `improve-codebase-architecture`
- `loop-me`
- `migrate-to-shoehorn`
- `prototype`
- `research`
- `resolving-merge-conflicts`
- `retro`
- `scaffold-exercises`
- `setup-matt-pocock-skills`
- `setup-pre-commit`
- `setup-ts-deep-modules`
- `tdd`
- `teach`
- `to-questionnaire`
- `to-spec`
- `to-tickets`
- `triage`
- `wait-what`
- `wayfinder`
- `wizard`
- `writing-beats`
- `writing-for-agents`
- `writing-fragments`
- `writing-shape`

## Proposed Approach

1. Correct `docs/DEVELOPMENT_WORKFLOW.md` closure language and define the Level 1 record location.
2. Remove the duplicate sentence in `docs/ENGINEERING_RULES.md` and keep the three-level planning
   model unchanged.
3. Delete the 35 out-of-scope skill directories and prune `skills-lock.json` to the two retained
   entries without altering their recorded upstream hashes.
4. Remove the `AGENTS.md` issue-tracker, triage, and domain-skill routing added for deleted skills.
5. Remove `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and
   `docs/agents/domain.md` if no non-skill repository requirement still consumes them.
6. Simplify `docs/agents/skill-governance.md` to govern the remaining Claude Code skills and remove
   mappings that exist only for deleted skills.
7. Update `scripts/check_governance.py` so it requires the repository-wide skill policy but not
   deleted skill configuration. Add a bounded check that the lockfile and installed skill folders
   contain only the approved Claude Code skill set.
8. Add conditional bootstrap guidance for the retained skills: verify the Claude Code CLI and
   required background-agent capability only when `claude-handoff` will be used; do not make Claude
   Code a universal application runtime dependency.
9. Run validation and inspect the branch against `main` for scope, stale references, and unintended
   files.

## Affected Components / Files

- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/ENGINEERING_RULES.md`
- `docs/BOOTSTRAP_CHECKLIST.md`
- `AGENTS.md`
- `docs/agents/skill-governance.md`
- `docs/agents/domain.md` (remove if orphaned)
- `docs/agents/issue-tracker.md` (remove if orphaned)
- `docs/agents/triage-labels.md` (remove if orphaned)
- `.agents/skills/` (retain two named directories; remove 35 named directories)
- `skills-lock.json`
- `scripts/check_governance.py`
- `README.md` if skill/bootstrap wording becomes inaccurate
- `plans/README.md`

## Risks

- Broad deletion could remove a skill the user intended to retain; mitigate with the explicit
  retain/remove inventory above and human approval before implementation.
- Orphaned references could remain after pruning; mitigate with repository-wide searches for every
  removed skill name, `CONTEXT.md`, `docs/adr/`, setup-skill references, issue-tracker routing, and
  triage routing.
- Lockfile and directory inventory could drift; mitigate with deterministic validation of the exact
  retained set.
- `claude-handoff` may rely on Claude Code functionality unavailable in a new project; mitigate with
  conditional bootstrap verification and clear failure behavior.

## Testing Plan

- Run `python scripts/check_governance.py` using the repository's available Python runtime.
- Run `git diff --check`.
- Verify `.agents/skills/` contains exactly `claude-handoff` and
  `git-guardrails-claude-code`.
- Verify `skills-lock.json` contains exactly the same two skills and valid JSON.
- Search for stale references to removed skills and removed paths.
- Confirm CI still runs the same governance validator.
- Review `git diff main...HEAD` plus the corrective working-tree diff before committing.
- Verify the branch remains based on current `main` before PR/merge.

## Acceptance Criteria

- [x] Ordinary changes no longer require universal human confirmation before closure.
- [x] Protected authority transitions retain their existing human gates.
- [x] Level 1 decisions have a simple existing-record owner and no standalone lifecycle.
- [x] The duplicate planning sentence is removed.
- [x] Only `claude-handoff` and `git-guardrails-claude-code` remain installed and locked.
- [x] No removed skill's configuration or canonical-artifact assumptions remain active.
- [x] The GitHub CLI is not introduced as a bootstrap dependency solely for deleted skills.
- [x] Governance validation and `git diff --check` pass.
- [x] No stale references or unintended files remain in the branch diff.
- [x] A fresh template checkout can complete the applicable bootstrap checks.

## Related Requirements

- None; this remediates review findings within the repository governance refactor.

## Related ADRs

- None.

## Related Plans

- `PLAN-001: Simplify Skill Governance` (Approved, active)

## Open Questions

- None. The retained and removed skill sets are explicitly defined above.

## Approval Record

Approved by: Withdrawn
Approval date: Withdrawn on 2026-08-25

## Closure Metadata

Completion date: Pending
Related requirements: None
Related ADRs: None
Implementation PR: Pending
Implementation commits: Pending
Validation result: Passed current-tree and isolated fresh-template governance checks; controlled extra-skill fixture failed as expected; git diff --check passed
Documentation impact: Updated engineering rules, workflow, bootstrap checklist, agent routing, skill policy, and plan index
Unresolved follow-ups: Human closure authorization; commit, PR, and CI status remain pending

Requirements impact: None
Architecture impact: None
ADR impact: None
Knowledge impact: None
