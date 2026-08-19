# Development Workflow

## Standard Flow

1. Understand the task and its authority.
2. Evaluate every planning trigger in `ENGINEERING_RULES.md`.
3. If triggered, create or use a formal plan and obtain required human approval.
4. Inspect only relevant repository context.
5. Implement the smallest adequate change without speculative architecture.
6. Run the applicable local validation commands below.
7. Review the diff for scope, security, and unintended files.
8. Confirm CI passes.
9. Complete closure and Documentation Impact Review.
10. Merge through the configured repository controls.

Never knowingly hide a validation failure or report completion while a required check fails.

## Validation Contract

During template bootstrap, governance validation is the only configured command:

- **GOVERNANCE** — Run: `python scripts/check_governance.py`
- **FORMAT** — Run: `NOT CONFIGURED (activate if applicable)`
- **LINT** — Run: `NOT CONFIGURED (activate if applicable)`
- **TYPE CHECK** — Run: `NOT CONFIGURED (activate if applicable)`
- **TEST** — Run: `NOT CONFIGURED (activate if applicable)`
- **BUILD** — Run: `NOT CONFIGURED (activate if applicable)`
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
```

A diff alone does not establish semantic consistency. Check each impact against accepted project
truth and update only with the required authorization.
