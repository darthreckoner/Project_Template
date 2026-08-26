# PLAN-003: Correct Skill Pruning Scope

Identifier: PLAN-003
Title: Correct Skill Pruning Scope
Status: Approved
Approval: Human correction and exact retain/remove lists recorded in Codex task conversation

## Problem

PLAN-002 incorrectly interpreted peripheral-skill pruning as retaining only two Claude-specific
skills. Commit `f0e6989` therefore removed 35 skills when the intended scope was to remove only 14
peripheral or overlapping skills while retaining the useful Codex/Claude engineering workflow.

## Goal

Correct the branch without rewriting history: restore the intended engineering and productivity
skills, retain the two Claude-specific skills, prune only the 14 explicitly identified peripheral
skills, and preserve repository governance through targeted adapters.

## Scope

- Restore the 21 mistakenly deleted retained skills from commit `47ba6e6`.
- Keep `claude-handoff` and `git-guardrails-claude-code`.
- Keep the 14 explicitly pruned skills deleted.
- Restore issue, triage, and domain routing required by retained skills.
- Restore matching lockfile provenance for retained skills.
- Adapt `domain-modeling` and `resolving-merge-conflicts` to canonical repository governance.
- Verify whether `research` mechanics work for Codex/Claude and document any required adaptation.
- Replace the two-skill exact-set validator with the corrected 23-skill set.
- Declare and install the skill validator's PyYAML dependency as isolated template tooling, and run
  the same local validator in CI.

## Prune

- `ask-matt`
- `implement-spec`
- `loop-me`
- `migrate-to-shoehorn`
- `retro`
- `scaffold-exercises`
- `setup-matt-pocock-skills`
- `setup-pre-commit`
- `setup-ts-deep-modules`
- `wizard`
- `writing-beats`
- `writing-for-agents`
- `writing-fragments`
- `writing-shape`

## Retain

- `claude-handoff`
- `code-review`
- `codebase-design`
- `diagnosing-bugs`
- `domain-modeling`
- `git-guardrails-claude-code`
- `grill-me`
- `grill-with-docs`
- `grilling`
- `handoff`
- `implement`
- `improve-codebase-architecture`
- `prototype`
- `research`
- `resolving-merge-conflicts`
- `tdd`
- `teach`
- `to-questionnaire`
- `to-spec`
- `to-tickets`
- `triage`
- `wait-what`
- `wayfinder`

## Proposed Approach

1. Restore retained skill directories and required `docs/agents/` routing from `47ba6e6`.
2. Restore `skills-lock.json` provenance, then remove only the 14 pruned entries.
3. Restore concise `AGENTS.md` routing for issue, triage, and domain configuration.
4. Adapt the two known conflicting skills and any evidenced research incompatibility.
5. Update deterministic validation to require exactly the corrected retained set.
6. Run governance, exact-set, stale-reference, and diff validation.

## Testing Plan

- Run `python scripts/check_governance.py` using the available repository runtime.
- Run `git diff --check`.
- Verify skill directories and lockfile contain the same exact 23 names.
- Confirm the 14 pruned names are absent from active routing and lockfile.
- Search for duplicate canonical paths and unsafe merge-resolution instructions.
- Inspect the complete branch diff against `main`.

## Acceptance Criteria

- [x] Exactly the 23 retained skills are installed and locked.
- [x] Exactly the 14 approved peripheral skills remain pruned.
- [x] Required issue, triage, and domain routing is restored.
- [x] `domain-modeling` uses canonical repository records rather than parallel paths.
- [x] Merge-conflict guidance stops when intent cannot be established safely.
- [x] `research` is verified or adapted for Codex/Claude mechanics.
- [x] Governance validation and `git diff --check` pass.
- [x] No force-push or history rewrite occurs.

## Related Plans

- PLAN-001: Simplify Skill Governance
- PLAN-002: Review Remediation and Claude Code Skill Pruning (scope corrected by this plan)

## Approval Record

Approved by: Justin Rutledge
Approval date: 2026-08-25

## Closure Metadata

Completion date: Pending
Related requirements: None
Related ADRs: None
Implementation PR: Pending
Implementation commits: Pending
Validation result: Governance and diff checks passed; installed and locked sets match at 23; isolated Python 3.12 tooling install succeeded with PyYAML 6.0.3; all 23 skills passed YAML validation; no stale pruned-skill references remain
Documentation impact: Restored skill routing; adapted domain, merge-conflict, architecture, and research guidance; corrected plan history
Unresolved follow-ups: Commit, push, CI, and human closure authorization remain pending

Requirements impact: None
Architecture impact: None
ADR impact: None
Knowledge impact: None
