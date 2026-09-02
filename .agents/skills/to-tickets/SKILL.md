---
name: to-tickets
description: Split a ready, traceable specification into vertical tickets that preserve requirement and verification coverage.
disable-model-invocation: true
metadata:
  local_adaptation: Requirement and verification coverage gate for Project_Template.
---

# To Tickets

Break one ready formal specification into tracer-bullet tickets. Each ticket
delivers a narrow, complete behavior and declares what blocks it.

Read `docs/agents/issue-tracker.md` and `docs/agents/triage-labels.md`. If
either is missing, stop and report the missing repository configuration.

## Preconditions

Read the full source specification and its comments when it is referenced by
path, number, or URL. It must state **Ready for Implementation**, contain
`REQ-###` requirements and `VERIFY-###` properties, and have no unresolved
behavioral questions.

If the source is missing, contradictory, unready, or has incomplete requirement
coverage, stop and return it to `/to-spec`. Do not create tickets by inventing
interpretations. Except for the legacy exception below, do not ticket a source
without complete requirement coverage. A legacy prose specification may use the
existing ticket workflow only when the user explicitly accepts that it has no
formal coverage guarantee.

## Process

1. Inspect relevant code only as needed to size vertical slices, respect domain
   terminology and ADRs, and identify genuine blockers.

2. Draft tracer-bullet tickets. Each ticket must deliver a complete, demoable or
   verifiable behavior, fit a fresh context window, and remain vertical across
   the layers it needs. A mechanical wide refactor may instead use an
   expand-migrate-contract sequence that keeps each migration batch green where
   practical.

3. Add `Implements` and `Verifies` fields to every ticket. The fields list the
   `REQ-###` and `VERIFY-###` identifiers covered by that ticket. Keep the
   acceptance criteria in user-observable language; identifiers supplement them
   rather than replacing them.

4. Before asking for approval or publishing, prove coverage: every `REQ-###`
   and `VERIFY-###` in the source appears in at least one ticket, every listed
   identifier exists, blocker edges are genuine and acyclic, and no ticket
   changes the specification. Return any gap or contradiction to `/to-spec`.

5. Present the numbered breakdown to the user with title, blockers, delivered
   behavior, `Implements`, and `Verifies`. Iterate until the user approves the
   granularity and dependency graph.

6. Publish approved tickets in dependency order through the configured tracker.
   Apply `ready-for-agent` to tickets, not to a new competing specification.
   Do not close or rewrite the parent specification.

## Ticket template

```markdown
## Parent
<Canonical specification issue, if applicable>

## What to build
<End-to-end behavior from the user's perspective.>

## Implements
- `REQ-001`

## Verifies
- `VERIFY-001`

## Acceptance criteria
- [ ] Observable criterion

## Blocked by
- None (can start immediately)
```

For a local tracker, preserve the same fields in each numbered issue file.
