# Planning Playbook

Use this playbook only when a trigger in `ENGINEERING_RULES.md` applies. Planning creates durable
project state and is separate from implementation.

## Sequence

1. **Problem** — What observable condition needs to change?
2. **Goal** — What outcome will resolve it?
3. **Constraints** — Which accepted intent, technical limits, security boundaries, and delivery
   constraints apply?
4. **Existing system** — What current behavior and relevant decisions are evidenced?
5. **Unknowns** — Which assumptions or missing requirements could alter the solution?
6. **Options** — What are the smallest viable approaches?
7. **Tradeoffs** — Compare complexity, reversibility, risk, maintenance, and fit with accepted
   architecture.
8. **Recommendation** — State one approach and why it is adequate.
9. **Human decision** — Obtain explicit approval where the plan or an ADR requires it.
10. **Implementation plan** — Define bounded steps, validation, acceptance criteria, and closure.

Actively challenge unnecessary complexity, speculative future requirements, irreversible changes,
architectural conflicts, and unresolved assumptions.

## Stop Conditions

Do not begin implementation when:

- material uncertainty could materially change the solution;
- required human approval is absent;
- the plan conflicts with accepted project truth;
- a required architecture decision remains Proposed;
- acceptance criteria or a feasible validation approach are missing.

Record the blocker and the decision needed rather than filling evidence gaps with assumptions.

## Plan Lifecycle

Create new formal plans from `plans/PLAN-TEMPLATE.md` in `plans/draft/` with `Status: Draft`.
Human approval is represented by moving the file to `plans/active/`, changing its status to
`Approved`, and completing the approval field. AI must not perform that transition on its own.

After implementation, conduct the template's closure review. A plan becomes Completed only after a
human authorizes closure, the closure metadata is filled, its status is changed to `Completed`, it
is moved to `plans/completed/`, and `plans/README.md` is updated. AI may prepare closure evidence but
may not authorize or perform its own Active-to-Completed transition.

Backlog ideas may live in `plans/backlog/`; they are neither approved plans nor project truth.
