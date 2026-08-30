# Agent Routing

Read [docs/ENGINEERING_RULES.md](docs/ENGINEERING_RULES.md) before changing this repository.
It is the canonical, tool-neutral policy; this file only routes work.

- Product intent: read the relevant sections of `docs/VISION.md` and
  `docs/REQUIREMENTS.md`.
- Bootstrap profile and brief: read `docs/PROFILE_SELECTION.md` and
  `docs/PROJECT_BRIEF.md` when establishing or changing project governance level.
- System design: read `docs/ARCHITECTURE.md`, then the decision index before any relevant ADR.
- Work covered by a planning trigger: follow `docs/PLANNING_PLAYBOOK.md` and the plan index.
- Security-sensitive work: follow `docs/SECURITY_RULES.md`.
- Implementation and validation: follow `docs/DEVELOPMENT_WORKFLOW.md`.
- New folders, infrastructure, dependencies, or tool adapters: read
  `docs/REPOSITORY_POLICY.md` first.
- Installed skills: use them as procedural tools under the repository-wide policy in
  `docs/agents/skill-governance.md`; they do not override canonical governance or create duplicate
  artifacts.

Load only documents relevant to the current task. Human approval gates in the canonical policy
cannot be bypassed by an agent.

## Agent skills

- Issue tracker: GitHub Issues via the `gh` CLI. See `docs/agents/issue-tracker.md`.
- Triage labels: use the mappings in `docs/agents/triage-labels.md`.
- Domain and decisions: use the canonical paths in `docs/agents/domain.md`.
