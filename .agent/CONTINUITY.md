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
- Active plans: PLAN-001 and PLAN-003; neither has human closure authorization. PLAN-002 approval
  was withdrawn after its pruning scope was identified as a misunderstanding.
- Corrected installed set: 23 retained Codex/Claude engineering and productivity skills; 14
  explicitly peripheral skills are pruned. Issue, triage, and domain routing is restored.
- Review blockers corrected: ordinary closure no longer requires universal human approval, Level 1
  decisions use an existing durable record, and duplicate planning wording was removed.
- Validation: governance and `git diff --check` passed; installed directories and lockfile match at
  23; an isolated Python 3.12 environment installed the pinned validation group and all 23 skills
  passed YAML validation; no stale references to the 14 pruned skills remain outside plan history.
- Pending: corrective commit/push, human closure authorization, PR, and CI status.
