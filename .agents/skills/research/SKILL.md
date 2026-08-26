---
name: research
description: Investigate a question against high-trust primary sources and capture source-backed findings as Markdown in the repository.
---

Delegate to a background or subagent when the active Codex or Claude environment supports that
capability and the user's scope permits it. Otherwise perform the research in the current session;
background execution is an optimization, not a prerequisite.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repository already keeps such notes. If no durable research location exists,
   follow `docs/REPOSITORY_POLICY.md` before proposing a new module or path.
