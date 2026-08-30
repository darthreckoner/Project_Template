# Optional Skill Extensions

This directory contains the optional, lockfile-pinned skill bundle for projects that need
capabilities beyond the reviewed core skills in `.agents/skills/`.

Install or enable extensions deliberately for the project. Every extension remains subordinate to
`docs/ENGINEERING_RULES.md` and `docs/agents/skill-governance.md`; installation grants no semantic
authority. The bundle and its hashes are declared in `skills-lock.json` and checked by
`python scripts/check_skills.py`.

To enable an extension for a derived project, review its lockfile entry and copy only the selected
skill directory into that project's `.agents/skills/` directory, or configure the agent host to
load this extension directory if it supports additional skill roots. Run
`python scripts/check_skills.py` after the change and keep the lockfile entry unchanged unless the
upstream skill is deliberately reviewed and re-pinned.
