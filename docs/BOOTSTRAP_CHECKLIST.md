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

## Security and GitHub Protection Verification

For settings dependent on repository visibility or GitHub plan, record one of `Enabled`, `Not
supported`, or `Not applicable` with a brief reason. Do not represent an unsupported setting as
enforced.

- [ ] Secret scanning: Enabled / Not supported / Not applicable with reason.
- [ ] Push protection: Enabled / Not supported / Not applicable with reason.
- [ ] Dependency graph: Enabled / Not supported / Not applicable with reason.
- [ ] Dependabot alerts: Enabled / Not supported / Not applicable with reason.
- [ ] Dependabot security updates: Enabled / Not supported / Not applicable with reason.
- [ ] GitHub Actions use explicit least-privilege permissions.
- [ ] Third-party Actions use immutable full commit SHAs.
- [ ] Security-sensitive files are covered by CODEOWNERS.
- [ ] Applicable code scanning has been evaluated; activate it when an executable application
  language warrants it.
- [ ] Passing secret scan verified.
- [ ] Controlled failing secret scan verified through an unmerged PR or CI test branch: add a
  temporary file containing `ghp_` followed by 36 zero digits, verify the `secret-scan` job fails,
  then delete the branch. This is a nonfunctional pattern-only fixture, never a real credential.
- [ ] Pull-request and required-status-check enforcement verified where supported.
- [ ] CODEOWNERS approval enforcement verified where supported and meaningful with a distinct
  reviewer/automation identity.

Record completion in the first project-specific PR or another durable project record.
