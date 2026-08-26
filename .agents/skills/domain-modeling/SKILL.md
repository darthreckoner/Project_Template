---
name: domain-modeling
description: Build and sharpen a project's domain model using its canonical intent, terminology, and decision records.
---

# Domain Modeling

Actively sharpen the project's domain model while designing. Challenge ambiguous terms, test them
against concrete scenarios, and capture durable conclusions in the repository's existing canonical
records. Follow `docs/agents/domain.md` and `docs/agents/skill-governance.md`.

## During the session

### Challenge against accepted language

When a term conflicts with Vision, Requirements, Architecture, or an accepted decision, surface the
conflict and ask which meaning is intended. Do not silently rewrite accepted intent.

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Capture resolved language

Record resolved terminology in the most relevant existing durable artifact. Semantic changes to
accepted Vision, Requirements, Architecture, or decisions require the repository's existing human
authorization. If no existing artifact is appropriate, propose a location and obtain direction
before creating a new canonical record.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Draft new decisions from
`docs/decisions/ADR-TEMPLATE.md` in `docs/decisions/proposed/`; only a human may accept them.
