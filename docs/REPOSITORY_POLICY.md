# Repository Policy

## Core and Top-Level Policy

The starter's mandatory core is the root policy files, `docs/`, `plans/`, `src/`, `tests/`,
`scripts/`, and `.github/`. Optional modules are absent until their activation conditions are met.

Do not create optional project infrastructure merely because it appears in a generic best-practices
list.

Before adding a new top-level directory, determine whether an existing location is appropriate and
whether the documented activation trigger has been met. Prefer the least structure that satisfies
current evidenced needs.

Do not add speculative service layers, unused configuration systems, agent-role directories,
orchestration systems, or multi-agent frameworks. The initial model is one capable agent, good
instructions, durable project state, deterministic validation, and human approval gates.

## Optional Modules

### `knowledge/`

Activate when durable domain information is repeatedly required, external sources need distilling,
or reusable project knowledge must survive conversations. Create `knowledge/README.md`,
`knowledge/domain/`, and `knowledge/sources/`.

Synthesized knowledge contains reusable conclusions. Raw material belongs in sources and is not
loaded wholesale. Read the index, then a relevant synthesized module, and open raw evidence only
when required. `knowledge/sources/` is cold context.

### `data/`

Activate for persistent non-code datasets, raw-to-processed pipelines, or reusable sample/reference
datasets. Put test-only fixtures in `tests/fixtures/`.

### `config/`

Activate when behavior legitimately varies by environment, shared runtime settings must be editable
without source changes, or shared configuration exists. Do not use it for random constants,
single-use values, or hypothetical settings.

### `migrations/`

Activate only when persistent data exists and schema evolution must preserve it.

### Logging infrastructure

Activate when unattended/background failures need diagnosis, integrations require observability, or
operations can fail without a user watching. Generated runtime logs normally remain uncommitted; do
not create `logs/` merely by convention.

### `.devcontainer/`

Activate when OS parity matters, native dependencies are difficult, setup repeatedly diverges, or
isolated reproducibility has demonstrated value.

## Tool Adapters

`docs/ENGINEERING_RULES.md` is canonical:

```text
ENGINEERING_RULES.md
      |-- AGENTS.md
      |-- CLAUDE.md
      `-- future adapter
```

Create an adapter only when that tool enters the workflow. It must point to the canonical policy,
contain only tool-specific behavior, and avoid duplicating canonical rules.

## Context and Accumulation

Accumulation-prone areas use index-first retrieval: `docs/decisions/`, `plans/completed/`, and
`knowledge/` when activated. Index entries should communicate status and relevance without forcing
readers to open every historical file. Update the relevant index in the same change that adds or
changes an indexed document.

## Reproducibility

When external packages or a version-sensitive runtime are introduced, add a runtime version
declaration where applicable, a dependency manifest, a lockfile where supported, deterministic
installation instructions, and exact validation commands. README prose alone is insufficient once
dependency drift matters.

Use deterministic scripts only for repeated, objective checks. Do not add scripts simply to make
the repository appear sophisticated.
