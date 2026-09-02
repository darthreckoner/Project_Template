---
name: to-spec
description: Turn an aligned conversation into a traceable, human-confirmed behavioral specification and publish it when it is ready for agents.
disable-model-invocation: true
metadata:
  local_adaptation: Formal contract, coverage, and readiness gate for Project_Template.
---

# To Spec

Turn accepted intent into one canonical specification that an implementation
agent can follow without inventing product decisions.

Do not restart the broad interview. Synthesize the conversation and repository
context already available. Ask only targeted questions when a material behavior
remains ambiguous.

Read `docs/agents/issue-tracker.md` and `docs/agents/triage-labels.md`. If
either is missing, stop and report the missing repository configuration.

## Process

1. Inspect the relevant repository context. Follow the repository's authority
   hierarchy, use its domain vocabulary, and identify the accepted sources of
   intent. Do not elevate a derived issue, draft, or conversation above an
   authoritative source.

2. Draft the specification using
   [the formal specification reference](references/formal-specification.md).
   Give each normative requirement a `REQ-###` identifier and each verification
   property a `VERIFY-###` identifier. Record each extracted source requirement
   and source location, then show that it is covered, deliberately excluded, or
   unresolved.

3. Use the lightest formalism that removes ambiguity. Let the behavior and
   established project conventions choose the form: schemas or type shapes for
   typed interfaces, state transitions for stateful behavior, and ordering or
   idempotency rules for asynchronous behavior. Omit sections with no meaningful
   content. Do not pad a simple change with pseudo-formal language.

4. If two reasonable implementations could produce materially different
   observable behavior, resolve the question from authoritative context. If it
   remains unresolved, show the user the decision, the valid outcomes, and the
   implementation impact. Do not publish or label the specification
   `ready-for-agent` until the user resolves every blocking question.

5. Identify the smallest sufficient set of existing test seams. Preserve a
   previously accepted seam unless the formal contract proves it cannot verify a
   required property. Link every significant `REQ-###` to one or more
   `VERIFY-###` properties.

6. Run the readiness check in the reference. Present the completed behavioral
   contract, resolved decisions, coverage, and test seams for human confirmation.
   Do not treat the agent's own judgment as confirmation.

7. After confirmation and a `Ready for Implementation` result, publish one
   canonical specification issue through `docs/agents/issue-tracker.md` and
   apply the mapped `ready-for-agent` label. Preserve the issue as the source
   for `/to-tickets`; do not publish a competing specification artifact.

## Boundaries

Formalization clarifies accepted intent. It does not make product, architecture,
or policy decisions that the sources and user have not settled. A specification
with blocking questions is useful, but it is **Not Ready for Implementation**.
