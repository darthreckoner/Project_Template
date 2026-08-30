# AI-Assisted Engineering Repository Template

A reusable GitHub repository template for solo developers who use AI-assisted code while retaining
durable intent, explicit human decisions, deterministic validation, and professional engineering
discipline. The repository is institutional memory; chats and agent threads are temporary working
memory.

## Start a Project

1. Mark this repository as a GitHub Template Repository, then choose **Use this template**.
2. Read [Profile Selection](docs/PROFILE_SELECTION.md) and complete the
   [Project Brief](docs/PROJECT_BRIEF.md). Personal Baseline is the concise default; select
   Governed Engineering for shared, sensitive, production, or materially consequential work.
3. Select a runtime/toolchain and set the exact validation contract in
   [the development workflow](docs/DEVELOPMENT_WORKFLOW.md) and CI.
4. Install template tooling with `python -m pip install --upgrade "pip>=25.1"` followed by
   `python -m pip install --group validation`; run `python scripts/check_governance.py` and
   `python scripts/check_skills.py`, then intentionally test CI.
5. Choose applicable collaboration and GitHub controls. Use the
   [bootstrap checklist](docs/BOOTSTRAP_CHECKLIST.md) for the full Governed Engineering path.

The template deliberately contains no project plan instances in a derived project. Create formal
plans and ADRs when the objective planning triggers apply; direct localized work can proceed as
Level 0 and bounded durable choices can be recorded as Level 1 decisions.

## How Governance Works

Authority descends from human decisions to accepted project truth, approved plans, proposals and
Draft plans, backlog ideas, then conversation. Lower-authority content cannot silently override
higher-authority content. The concise canonical rules are in
[Engineering Rules](docs/ENGINEERING_RULES.md).

Formal planning is required by objective triggers covering persistent state, architecture, external
contracts, security/trust, accepted intent, material uncertainty, and cross-system impact. See the
[Planning Playbook](docs/PLANNING_PLAYBOOK.md). AI may draft plans and ADRs, but only a human may
approve/activate a formal plan or accept an ADR.

Work is classified as Level 0 direct implementation, Level 1 lightweight decision note, or Level 2
formal plan. When classification is uncertain, escalate rather than downgrade. Installed skills are
available by default as procedural tools, but remain subordinate to the repository-wide policy in
[Installed Skill Governance](docs/agents/skill-governance.md).

Context stays economical through progressive disclosure: load the small routing policy and current
task first, then only relevant requirements, decisions, plans, code, and tests. Historical plans,
unrelated rationale, and raw sources remain cold and are retrieved index-first.

Optional modules such as `knowledge/`, `data/`, `config/`, `migrations/`, or `.devcontainer/` are
created only after their documented trigger is met. See [Repository Policy](docs/REPOSITORY_POLICY.md).

## Validation and GitHub Enforcement

Bootstrap validation:

```shell
python scripts/check_governance.py
```

The validation scripts check core structure, the selected profile, lifecycle/directory consistency,
closure metadata, index entries, both skill bundles, and whether application code has appeared
before application validation is configured. CI installs the same template-tooling dependency group
and runs both checks. Before executable code is merged, configure exact stack-specific commands in
the validation contract and replace the deliberate CI failure placeholder.

`CODEOWNERS` establishes review ownership but does not itself enforce approval. Personalize it and
configure a GitHub ruleset or branch protection to require code-owner review and the CI check. A
template cannot ship those repository settings. If AI shares the human's GitHub identity, GitHub
cannot reliably distinguish their actions; a technically enforced human gate needs a distinct
automation/contributor identity and a human reviewer.

## Lifecycle

```text
Explore -> evaluate planning triggers -> plan and approve when required -> implement
        -> local validation -> CI -> review -> documentation/knowledge synchronization
        -> closure -> merge
```

Use [the development workflow](docs/DEVELOPMENT_WORKFLOW.md) for implementation and closure.
