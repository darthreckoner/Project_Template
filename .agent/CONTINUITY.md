# Continuity

## Security v1

- Branch: `codex/security-v1`.
- Scope: repository-file implementation of the Security v1 baseline; no remote GitHub settings.
- Planning gate: bypassed once by explicit human authorization on 2026-08-21 because no active
  approved formal plan existed.
- Validation completed: bundled Python governance validation passed; the deterministic negative
  test correctly failed when `docs/SECURITY_RULES.md` was removed; all workflow actions were
  checked for full-SHA pins.
- Local Gitleaks executable was unavailable. The controlled failing scan is documented for the
  unmerged PR/CI path; no scanner or dependency was installed for this template-only change.

## Skill governance review remediation

- Branch: `codex/skills-eval`.
- Active plans: PLAN-001 and approved PLAN-002; neither has human closure authorization.
- Retained installed skills: `claude-handoff` and `git-guardrails-claude-code`; 35 other skills and
  their orphaned issue, triage, and domain routing were removed under PLAN-002.
- Review blockers corrected: ordinary closure no longer requires universal human approval, Level 1
  decisions use an existing durable record, and duplicate planning wording was removed.
- Validation: current-tree and isolated fresh-template governance checks passed; a controlled
  unapproved-skill fixture failed as expected; `git diff --check` passed.
- Pending: human closure authorization, commit, PR, and CI status.
