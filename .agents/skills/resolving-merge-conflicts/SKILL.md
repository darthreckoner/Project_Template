---
name: resolving-merge-conflicts
description: "Use when you need to resolve an in-progress git merge/rebase conflict."
---

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve only established intent.** Preserve both intents where possible. Where incompatible,
   use the merge's stated goal only when it is supported by accepted project truth. Do not invent
   behavior. If a conflict exposes an unresolved product, architecture, security, or intent
   decision, stop and surface that decision. Aborting or deferring the merge is acceptable when a
   safe resolution cannot be established.

4. Discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish when authorized and safe.** Stage resolved files and complete the merge or rebase only
   when every conflict is resolved with sufficient evidence and repository checks pass.
