---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work.
For this repository, update or reference `.agent/CONTINUITY.md` when the information is durable
workflow state; use the operating-system temporary directory only for disposable session notes.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

Do not create a second durable handoff system. Reference existing plans, issues, decisions, and
continuity records instead of copying them.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
