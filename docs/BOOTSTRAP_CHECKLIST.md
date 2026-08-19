# Bootstrap Checklist

A project created from this template is fully bootstrapped when the applicable items are complete.
Keep `Not applicable` decisions brief and explicit.

## Project Intent

- [ ] Replace repository and document placeholders.
- [ ] Define the project name, purpose, and intended audience.
- [ ] Complete and human-approve the initial `VISION.md`, including Non-Goals.
- [ ] Complete and human-approve the initial accepted `REQUIREMENTS.md`.
- [ ] Complete and human-approve the initial `ARCHITECTURE.md`.

## Runtime and Validation

- [ ] Select and declare the runtime/toolchain and versions where applicable.
- [ ] Add dependency/version manifests and a lockfile where supported.
- [ ] Add deterministic setup/install instructions.
- [ ] Replace applicable validation-contract placeholders with exact commands.
- [ ] Replace the application-validation placeholder in `.github/workflows/ci.yml`.
- [ ] Run `python scripts/check_governance.py` successfully.
- [ ] Intentionally exercise both passing and failing CI behavior.

## GitHub Controls

- [ ] Personalize `.github/CODEOWNERS`.
- [ ] Establish the default branch.
- [ ] Enable the PR workflow where appropriate.
- [ ] Configure a branch-protection rule or GitHub ruleset.
- [ ] Require the governance/full-validation CI check.
- [ ] Require code-owner review where technically meaningful.
- [ ] If a strict human gate is needed, use a distinct AI/automation identity and human reviewer.

## GitHub Protection Verification

- [x] Pull requests required for `main`
- [x] CI status check configured
- [x] Governance CI verified to pass on valid changes
- [x] Governance CI verified to fail on invalid governance state
- [x] Required status check enforcement verified
  - Current state: repository is private and ruleset enforcement is unavailable on the current GitHub plan.
  - Resolution options:
    - Make this repository public, or
    - Use a GitHub plan that supports ruleset enforcement for private repositories.
- [ ] CODEOWNERS approval enforcement verified
  - Enable only when platform support and a distinct reviewer/automation identity make this practical.

Record completion in the first project-specific PR or another durable project record.
