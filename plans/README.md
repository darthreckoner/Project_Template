# Plan Index

Use this lightweight index to determine relevance before opening a plan. `completed/` is cold
context and should not be scanned or loaded wholesale.

| Plan ID | Status | Title | Related ADR | Implementation reference |
| --- | --- | --- | --- | --- |
| — | — | No plans recorded | — | — |

Example entry format:

```text
PLAN-001 | Completed | SQLite persistence | ADR-0003 | PR #12
PLAN-002 | Approved  | Save-game ingestion | None     | —
PLAN-003 | Backlog   | Web interface       | None     | —
```

## Lifecycle

- Draft: create from `PLAN-TEMPLATE.md` in `draft/` with `Status: Draft`.
- Approved: after explicit human approval, move to `active/`, set `Status: Approved`, and record
  approval. AI must not make this transition independently.
- Completed: after closure review and explicit human closure authorization, move to `completed/`,
  set `Status: Completed`, fill closure metadata, and update this index. AI must not authorize or
  perform its own Active-to-Completed transition.
- Backlog: unapproved ideas in `backlog/`; these are not executable plans or project truth.

Implementation references may use a PR or earlier implementation commits. A completed plan does
not need to contain the SHA of the same commit that records its completion.
