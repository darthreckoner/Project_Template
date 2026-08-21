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
