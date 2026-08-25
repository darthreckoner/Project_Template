# Development Workflow

## Standard Flow

1. Understand the task and read the relevant accepted intent documents when the task might affect
   them.
2. Classify the work as Level 0, Level 1, or Level 2 using `ENGINEERING_RULES.md`.
3. If classification is uncertain, escalate rather than downgrade.
4. For Level 1, record the bounded decision in the most relevant existing durable artifact, issue,
   or active work record. Do not create a standalone Level 1 note system. For Level 2, create or use
   a formal plan and obtain required human approval.
5. Inspect only relevant repository context.
6. Implement the smallest adequate change without speculative architecture.
7. Run the applicable local validation commands below.
8. Review the diff for scope, security, and unintended files.
9. Confirm CI passes.
10. Complete closure and Documentation Impact Review.
11. Merge through the configured repository controls.

Never knowingly hide a validation failure or report completion while a required check fails.

## Validation Contract

During template bootstrap, governance validation is the only configured command:

- **GOVERNANCE** — Run: `python scripts/check_governance.py`
- **FORMAT** — Run: `NOT CONFIGURED (activate if applicable)`
- **LINT** — Run: `NOT CONFIGURED (activate if applicable)`
- **TYPE CHECK** — Run: `NOT CONFIGURED (activate if applicable)`
- **TEST** — Run: `NOT CONFIGURED (activate if applicable)`
- **BUILD** — Run: `NOT CONFIGURED (activate if applicable)`
- **SECURITY** — Run: configured security checks when applicable; current template CI includes a
  routine secret scan.
- **FULL APPLICATION VALIDATION** — Run: `NOT CONFIGURED`

`APPLICATION_VALIDATION: NOT_CONFIGURED`

Once a stack is selected, replace applicable placeholders with exact commands and set the marker to
`APPLICATION_VALIDATION: CONFIGURED`. Update `.github/workflows/ci.yml` to execute the same full
validation command. Remove inapplicable categories or mark them `Not applicable` with a brief
reason. Executable application code must not be merged while the application-validation contract
or CI command remains unconfigured.

## Closure and Documentation Impact Review

For formal plans, confirm acceptance criteria, automated tests, CI, temporary/debug artifacts,
unresolved issues, and implementation references. Record:

```text
Requirements impact: None / Updated: ...
Architecture impact: None / Updated: ...
ADR impact: None / Added: ...
Knowledge impact: None / Updated: ...
Security impact: None / Updated: ...
```

Every completed change requires verification and a closure record identifying changed files or
system areas, confirming that applicable requirements remain satisfied, and synchronizing
architecture or ADR records when applicable. Human approval is required only for authority
transitions protected by repository governance, including formal-plan activation or completion,
ADR acceptance, protected intent changes, and other explicitly human-gated actions. Level 0 and
Level 1 work do not require a formal plan unless a planning trigger applies.

A diff alone does not establish semantic consistency. Check each impact against accepted project
truth and update only with the required authorization.
