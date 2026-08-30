# Profile Selection

Profiles select the amount of durable project documentation required at the current stage. They do
not change the authority order, security baseline, validation gates, or human approval rules in
`docs/ENGINEERING_RULES.md`.

## Personal Baseline

Use for solo, exploratory, bounded, or low-risk work. Complete `PROJECT_BRIEF.md`, declare the
exact application validation contract, and record applicable security and collaboration choices.
Create Vision, Requirements, Architecture, a formal plan, or an ADR when a planning trigger or
material decision requires it.

Escalate to Governed Engineering for any Level 2 trigger, production or sensitive use, external
contract, persistent state, collaboration requirement, or other consequential change.

## Governed Engineering

Use for shared, long-lived, externally integrated, sensitive, or materially consequential work.
Complete the Project Brief, Vision, Requirements, Architecture, and the full governed checklist;
use the normal plan and ADR lifecycles.

To activate it in a derived project, preserve the approved content in the Project Brief while
deriving the three durable intent records. Do not overwrite existing project records; link the
derived records to their source brief and record the activation decision.

## Decision rule

When uncertain, choose Governed Engineering or create a formal draft plan before implementation.
The source template itself uses `Selected profile: Template` until a derived project makes this
decision.
