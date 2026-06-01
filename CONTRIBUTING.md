# Contributing

Thanks for helping improve Context Architecture Bundle.

This repo is template-first. Contributions should make it easier for developers
to understand, copy, test, adapt, and maintain the bundle in real projects.

## Good First Contributions

- Improve docs or prompts.
- Add a filled example for another project type.
- Add tests for `scripts/check_doc_coverage.py`.
- Clarify a template placeholder or folder rule.
- Propose a workflow that helps AI coding agents preserve context.

## Before Opening A Pull Request

1. Read `README.md`, `docs/setup.md`, and `docs/usage.md`.
2. If changing workflow rules, check `context_pipeline.md` and
   `work_prompt.md`.
3. If changing checker behavior, add or update tests.
4. Run:

```powershell
python -m unittest discover
python scripts/check_doc_coverage.py --files README.md skills/create-context-architecture-bundle/SKILL.md
```

## Pull Request Expectations

- Explain the user problem.
- Keep changes focused.
- Include validation commands and results.
- Update docs when behavior, prompts, or file ownership changes.
- Avoid adding process for its own sake.

## Template Compatibility

Avoid renaming core files unless the benefit is worth a migration note. Many
forks and copied projects may rely on these file names.
