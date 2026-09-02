# Formal specification reference

Use this reference when `/to-spec` creates the canonical specification. Keep
the document proportional to the feature. Omit a section that has no meaningful
content and say nothing merely to fill a template.

## Normative language

- `MUST` states required behavior.
- `MUST NOT` states prohibited behavior.
- `MAY` states an allowed but optional behavior.

The problem statement, solution, and behavioral summary orient the reader. The
`REQ-###` clauses are the normative contract.

## Specification shape

```markdown
## Problem statement

## Solution

## Source of intent
| Source reference | Authority and relevance |
| --- | --- |
| ... | ... |

## User stories
1. As a ..., I want ..., so that ...

## Accepted decisions
- Decision and its source.

## Behavioral requirements

### <Relevant behavior group>
`REQ-001` - The system MUST ...

Source: <source reference>

### State, transitions, rules, interfaces, failures, or quality constraints
Include only groups that describe meaningful behavior for this feature.

## Testing seams and verification properties
<Identify the smallest sufficient existing test seam or seams.>

`VERIFY-001` - Given ..., when ..., then ...

Verifies: `REQ-001`, `REQ-002`

## Coverage
| Source requirement and location | Requirements | Verification | Disposition |
| --- | --- | --- | --- |
| ... | `REQ-001` | `VERIFY-001` | Covered |

## Out of scope

## Unresolved behavioral questions
<For each blocking question: decision, source gap, valid outcomes, and impact.>

## Readiness
Ready for Implementation
```

## Contract rules

- A `REQ-###` clause states one observable behavior or constraint and cites its
  source of intent.
- Add one coverage row for each extracted source requirement. A broad document
  citation is not enough when that document contains multiple requirements.
- A `VERIFY-###` property names observable evidence, not a private helper or
  incidental implementation step.
- State definitions identify ownership, valid values, initial values, and
  persistence only when those properties matter.
- Rejected, failed, repeated, stale, or concurrent operations state whether
  they mutate state, preserve state, retry, recover, or terminate when relevant.
- Deterministic behavior specifies its inputs, outputs, ordering, tie-breaking,
  and boundary values whenever different implementations could disagree.
- Interface and data contracts state accepted inputs, outputs, validation,
  compatibility, ordering, and idempotency where the feature crosses a boundary.
- Sourced accessibility, performance, security, compatibility, timing, or visual
  constraints belong in the relevant behavior group. Do not invent them.

## Readiness check

Mark the specification **Ready for Implementation** only when all of these are
true:

- authoritative sources and inherited scope are identified;
- every extracted source requirement has one coverage row and is covered,
  excluded with a source-backed reason, or shown as unresolved;
- every normative requirement has a stable `REQ-###` identifier;
- each material requirement has a verification path;
- material ambiguity, contradictory sources, and unsupported decisions are
  absent;
- the user has confirmed the contract and testing seams.

Otherwise mark it **Not Ready for Implementation**, list the blockers, and do
not publish it as `ready-for-agent`.
