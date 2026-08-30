# PLAN-001: Reduce Bootstrap Friction Through Progressive Profiles

Identifier: PLAN-001
Title: Reduce Bootstrap Friction Through Progressive Profiles
Status: Draft
Approval: Pending human approval

## Problem

Project_Template provides strong durable governance and GitHub security defaults, but a small solo project must confront a large documentation and configuration surface before it can begin. The template requires separate Vision, Requirements, Architecture, planning, decision, validation, GitHub-control, and skill-governance artifacts even when a project is still a bounded prototype.

That friction encourages one of two undesirable outcomes: a user avoids the template entirely, or fills durable records with boilerplate that does not represent real decisions.

## Goal

Preserve the template's security posture, validation discipline, human authority boundaries, and upgrade path while allowing a new project to start from a concise personal baseline and deliberately opt into the full governed profile when its risk, collaboration, or complexity warrants it.

## Scope

- Define two explicitly named repository profiles: **Personal Baseline** and **Governed Engineering**.
- Make the README present the Personal Baseline as the default first-use path and the Governed Engineering profile as an intentional activation path.
- Replace the three initial product-intent templates with one short, project-owned Project Brief at first use; split it into Vision, Requirements, and Architecture only when a documented trigger applies.
- Consolidate first-use guidance so a new project can find essential steps without reading every policy document.
- Retain formal plan/ADR capability but make it created or activated by planning triggers, rather than foregrounding lifecycle mechanics during initial bootstrap.
- Offer the current non-core skills as an optional extension bundle while retaining a smaller reviewed core skill set in the distributable default.
- Keep the existing security and validation controls in every profile unless their inapplicability is explicitly documented.

## Out of Scope

- Do not remove Gitleaks, SHA-pinned Actions, workflow least privilege, Dependabot, secret-safe ignore rules, or the requirement to declare application validation before executable application code is merged.
- Do not relax the authority order, human approval for protected state transitions, or the prohibition on an AI accepting its own ADR/plan.
- Do not configure GitHub branch rules, repository visibility, push protection, code scanning, or secret-scanning settings automatically.
- Do not change an existing derived project's chosen governance level without a project-specific decision.
- Do not implement these changes under this draft plan.

## Current System

- `README.md` prescribes five initial steps, including completing Vision, Requirements, Architecture, and Python-based governance/skill validation.
- `docs/ENGINEERING_RULES.md` provides the canonical authority order, planning triggers, approval gates, and template-distribution hygiene.
- `docs/BOOTSTRAP_CHECKLIST.md` contains detailed runtime, validation, GitHub, security, and review setup requirements.
- `.github/workflows/ci.yml` performs governance validation and a bounded Gitleaks secret scan. It deliberately blocks application code from being merged while the application validation contract remains unconfigured.
- The default distribution includes 23 locked skills and formal plan/ADR lifecycle directories.

## Proposed Approach

### 1. Define profiles without duplicate policy

Keep `docs/ENGINEERING_RULES.md` canonical. Add a compact profile-selection document and README decision point:

| Profile | Intended use | Required first-use records | Escalation trigger |
| --- | --- | --- | --- |
| Personal Baseline | solo, exploratory, bounded, or low-risk projects | Project Brief; validation declaration; applicable security choices | any existing Level 2 planning trigger or a collaboration/production requirement |
| Governed Engineering | shared, long-lived, externally integrated, sensitive, or materially consequential work | Vision, Requirements, Architecture; full validation and GitHub-control checklist; normal plan/ADR lifecycle | selected explicitly or activated by trigger |

Profiles must not redefine authority or security rules. They only select which records must exist now and which documents remain available on demand.

### 2. Use a Project Brief for first use

Add a concise `docs/PROJECT_BRIEF.md` template with:

- purpose and intended users;
- current scope and non-goals;
- primary runtime/toolchain choice;
- validation declaration link or summary;
- known external dependencies/integrations;
- selected profile and date;
- escalation decision or reason that the Personal Baseline remains appropriate.

The Personal Baseline does not require separate Vision, Requirements, or Architecture files. The Governed Engineering activation guide must explain how to derive those records from the brief without losing approved content.

### 3. Make planning progressive

Retain plan and ADR templates, indexes, statuses, validation, and human approval rules. Initial navigation should say:

- direct localized work proceeds as Level 0;
- a bounded durable choice is recorded in the most relevant existing artifact as Level 1;
- a Level 2 trigger creates a formal draft plan or proposed ADR using the existing lifecycle.

Avoid asking a new project to manage empty lifecycle folders as a first-use task. The folders may remain in the repository if required by deterministic validation; their existence must be presented as infrastructure, not mandatory initial documentation work.

### 4. Split essential from optional bootstrap work

The README's default path must contain only:

1. choose a profile and complete Project Brief;
2. choose a stack and set the exact validation contract;
3. run template validations and verify the secret scan;
4. choose collaboration/GitHub controls appropriate to the project.

Move detailed GitHub capability verification, strict code-owner configuration, advanced scanning evaluation, and optional tool integrations to the Governed Engineering checklist. A Personal Baseline may record `Not applicable` with a reason; it must never falsely claim those controls are active.

### 5. Curate default skills

Retain these default core skills:

- `code-review`
- `codebase-design`
- `diagnosing-bugs`
- `domain-modeling`
- `git-guardrails-claude-code`
- `implement`
- `research`
- `resolving-merge-conflicts`
- `tdd`

Move the remaining currently installed skills into an optional, lockfile-pinned extension bundle with clear installation/review instructions. The extension bundle must remain governed by `docs/ENGINEERING_RULES.md`; installation grants no semantic authority.

Before adoption, evaluate whether `prototype` belongs in the core set for the template's target users. The default decision is to leave it optional unless the user confirms frequent exploratory work.

### 6. Preserve hard validation gates

Refactor `scripts/check_governance.py` into profile-aware validation rather than weakening it:

- validate the core policy, security workflow, skill lock, and selected profile in all cases;
- require a Project Brief and explicit validation declaration in Personal Baseline;
- require Vision, Requirements, Architecture, full governed checklist evidence, and existing lifecycle/index controls in Governed Engineering;
- retain the failure when executable application code appears before exact application validation and the CI command are configured.

The CI workflow must run the same deterministic validator. The validator must report a specific remediation path, rather than a generic missing-file error.

## Affected Components / Files

- `README.md`
- `AGENTS.md`
- `docs/ENGINEERING_RULES.md`
- `docs/BOOTSTRAP_CHECKLIST.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/PLANNING_PLAYBOOK.md`
- `docs/REPOSITORY_POLICY.md`
- `docs/PROJECT_BRIEF.md` (new)
- `docs/PROFILE_SELECTION.md` (new)
- `docs/profiles/personal-baseline.md` (new)
- `docs/profiles/governed-engineering.md` (new)
- `scripts/check_governance.py`
- `scripts/check_skills.py`
- `skills-lock.json`
- `.agents/skills/`
- `.github/workflows/ci.yml`

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A lighter path accidentally weakens security | High | Keep secret scanning, immutable Action pins, least privilege, dependency updates, and validation declaration mandatory in both profiles. |
| Two profiles create ambiguous or duplicate policy | Medium | Keep one canonical engineering policy; profiles only control timing and required records. |
| Removing default skills breaks existing agent workflows | Medium | Publish an explicit core-to-extension mapping, preserve lock hashes, and validate both bundles before release. |
| Derived projects cannot upgrade cleanly | Medium | Provide an idempotent, documented activation checklist that detects existing project documents and does not overwrite them. |
| Profile selection becomes paperwork without value | Low | Keep the selection in the Project Brief and require only a short rationale. |

## Testing Plan

- Install the validation dependency group with Python 3.12, then run `python scripts/check_governance.py` and `python scripts/check_skills.py`.
- Create fixture copies representing a Personal Baseline and a Governed Engineering project; verify each passes only with its required records.
- Add a temporary application source file to each fixture before validation configuration; verify both local validation and CI fail with a targeted remediation message.
- Configure exact application validation in each fixture; verify the gate clears only when CI executes the same command.
- Verify all default and extension skills against their lockfile hashes and frontmatter rules.
- Run `git diff --check` and review the generated template tree for absence of project-specific plans, accepted ADRs, credentials, and stale maintenance records.
- In a non-merged test branch, verify the Gitleaks job still fails on the documented pattern-only credential fixture.

## Acceptance Criteria

- [ ] A new user can follow the Personal Baseline path from README to a valid first commit without creating empty product-intent documents.
- [ ] The Personal Baseline requires an explicit profile, Project Brief, and verification method before application code is merged.
- [ ] Selecting or triggering Governed Engineering requires the full durable-intent and governance record set.
- [ ] No profile permits an AI to approve or complete its own formal plan/ADR transition.
- [ ] Existing security workflow, Action SHA pins, Gitleaks behavior, Dependabot policy, and least-privilege permissions are retained or strengthened.
- [ ] The validator rejects an incomplete selected profile and reports exact remediation.
- [ ] The default skill bundle is smaller, verified, and sufficient for common implementation, review, diagnosis, design, research, and test-first work.
- [ ] Optional skills remain available through an explicit, reviewed, hash-pinned extension mechanism.
- [ ] The distributed template contains no project plan instances after this maintenance work is closed.

## Related Requirements

None — template-maintenance proposal.

## Related ADRs

None.

## Open Questions

- Is the template's target user primarily a solo developer, a small collaborating team, or both? This determines whether the Personal Baseline or Governed Engineering profile should be the README default.
- Should `prototype` remain a core skill? The recommended default is optional.
- Should `CODEOWNERS` remain distributed as a commented example, or be created only when a project explicitly adopts collaboration review? The recommended default is deferred creation.
- How should the optional skill extension bundle be installed in supported agent environments without duplicating repository policy?

## Approval Record

Approved by: Pending
Approval date: Pending

## Closure Metadata

Completion date: Pending
Related requirements: Pending
Related ADRs: Pending
Implementation PR: Pending
Implementation commits: Pending
Validation result: Pending
Documentation impact: Pending
Unresolved follow-ups: Pending

Requirements impact: Pending
Architecture impact: Pending
ADR impact: Pending
Knowledge impact: Pending
