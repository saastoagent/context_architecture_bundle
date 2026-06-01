# Adoption Guide

This guide is for maintainers who want the bundle to help a repo attract better
conversations, contributions, and sponsorship.

## Make The Value Visible

Add a short note to your project README:

```md
This repo uses a Context Architecture Bundle for AI-assisted development.
Start with `context.md`, then read `architecture/code-map.md` before changing
source files.
```

Link to:

- `critical_prompt.md`
- `context.md`
- `architecture/code-map.md`
- `test_index/README.md`
- `work_prompt.md`

## Help Contributors Succeed

In `CONTRIBUTING.md`, ask contributors to:

- read `context.md` before opening a PR
- name the owning `architecture/code-map.md` row for source changes
- update component docs when contracts move
- record validation commands and results

This creates better PRs because reviewers can see intent, ownership, and proof.

## Keep Forks Healthy

Recommended release practice for this template:

- tag template releases such as `v0.1.0`
- keep `CHANGELOG.md` or release notes focused on template changes
- avoid breaking file names without a migration note
- document new folders or closeout rules in `context_pipeline.md`

## Sponsorship Readiness

Sponsors usually support projects that show durable maintenance. Prioritize:

- a clear README promise
- a working example
- a visible roadmap
- tests for project scripts
- issue templates for bug reports and workflow proposals
- documented ways to contribute without needing permission first
