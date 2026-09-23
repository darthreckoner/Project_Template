# PLAN-004: Workflow prompt approval and template hygiene

Identifier: PLAN-004
Title: Workflow prompt approval and template hygiene
Status: Approved
Approval: Justin Rutledge, 2026-09-23; one-time authorization in the current task for this maintenance scope and clean-template closure.

## Problem

Commit `e606638` adds the reviewed optional workflow-improvement planning prompt.
The user requests a formal plan/approval record on `Workflow-Improvement-Loop`
before merge, followed by cleanup to a reusable template state. Current continuity
still reports removed skills, an already merged PR #17, and source-specific history.

## Goal

Record the user's bounded approval and validate the existing prompt, then remove
temporary maintenance records from the distributable tree while retaining the
plan, approval, closure evidence, and exact original context in local Git history.

## Scope

- Draft and activate this maintenance plan using the user's current authorization.
- Verify the committed prompt supports templates and existing repositories without
  installing or executing its proposed workflow.
- Replace stale source-specific continuity with concise reusable startup guidance.
- Validate, record closure, then remove this plan, its index entry, and temporary
  context archive under the source-template maintenance exception.
- Make scoped local commits to preserve evidence and finish with a clean worktree.

## Out of Scope

- Changing canonical governance, CI, security settings, or approval rules.
- Installing a workflow/skill, running a pilot, or changing another repository.
- Pushing, opening/merging a PR, or claiming remote CI/merge approval.

## Current System

- Clean branch `Workflow-Improvement-Loop` starts at `e606638`.
- The prompt is optional and planning-only; the project profile remains Template.
- Only `context-maintenance` is bundled under `.agents/skills`.
- PR #17 merge `0954f1f` is in the current branch's ancestry.
- No plan instances are currently distributed. Historical identifiers reach PLAN-003.
- Exact original continuity and plan-index bytes are preserved in
  `.agent/context-history/2026-09-23-workflow-prompt-hygiene/snapshot.json`.
  Base64 source bytes and SHA-256 values preserve checkout line endings too.

## Proposed Approach

Use a temporary maintenance plan and the existing source-template exception.
Permanent policy relaxation would exceed the user's one-time request; retaining
the plan in the final tree would conflict with distribution hygiene. Preserve
approved and completed states in local commits, then remove only these temporary
artifacts and restore the reusable plan index.

The current user explicitly authorizes drafting, marking approved, and hygiene
maintenance back to a clean template. Apply that authorization only to this
bounded plan and its necessary closure/cleanup; it is not self-approval or a
standing exception. This records authorization now, not retroactive approval
before the existing prompt commit was written.

## Affected Components / Files

- This plan and `plans/README.md`: temporary lifecycle records.
- `.agent/CONTINUITY.md`: replace historical maintenance notes with starter context.
- `.agent/context-history/2026-09-23-workflow-prompt-hygiene/snapshot.json`:
  temporary exact-byte preservation, retained in Git history after cleanup.
- `docs/codex_workflow_improvement_prompt.md`: review only, preserve its SHA-256
  `b3f447678bef817ff9a6116d6cca0215322823805ddf89abbc48676ad09c592b`.

## Risks

- Losing provenance: commit approval/closure and verify archived bytes before removal.
- Importing maintenance history into a new project: remove temporary plan/archive
  and keep final continuity generic.
- Overstating readiness: local validation does not establish remote CI or mergeability.
- Concurrent edits: recheck original hashes before replacing files; stage exact paths.

## Testing Plan

- `python scripts/check_governance.py`
- `python -m unittest discover -s tests -p 'test_*.py'`
- `git diff --check` and staged whitespace checks before each commit.
- Verify archive hashes, prompt hash, unchanged policy/CI, placeholder-only lifecycle
  directories, restored plan index, valid local Markdown links, and final Git status.
- Manual scope/authority review of the prompt; no pilot or application execution.

## Acceptance Criteria

- [x] User authorization is recorded on an Approved plan before hygiene edits.
- [ ] Existing prompt remains unchanged, portable, optional, and planning-only.
- [ ] Stale context is replaced with reusable startup guidance; exact originals survive.
- [ ] Local governance, test suite, and whitespace checks pass.
- [ ] Closure is preserved in history; final template has no plan/archive instances.
- [ ] Final working tree is clean and no push/merge or permanent policy change occurred.

## Related Requirements

- None; canonical template distribution and context rules remain unchanged.

## Related ADRs

- None.

## Open Questions

- None within this maintenance scope. Remote CI and merge remain subsequent actions.

## Approval Record

Approved by: Justin Rutledge
Approval date: 2026-09-23

User instruction: "I give you one time approval to draft the plan, mark it approved,
then run a hygiene maintenance to bring us back to a clean template state."
The plan was drafted and then activated under that explicit instruction. Closure
and removal of temporary maintenance artifacts implement the requested final state.

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
Security impact: Pending
