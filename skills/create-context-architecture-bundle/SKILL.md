---
name: create-context-architecture-bundle
description: Use when creating a complete context, architecture, handoff, and validation documentation bundle from a new project idea, product spec, or early repository scaffold.
---

# Create Context Architecture Bundle

Use this skill to create a repo-local context architecture system for a new or
early project from a project idea/spec.

## Inputs

Gather or infer:

- project name and root path
- project goal and primary users
- expected runtime, UI, data store, and integration layers
- known commands for run/test/build, if any
- initial subsystem guesses
- non-negotiable boundaries and safety rules

## Workflow

1. Copy the bundle template files into the target project root.
2. Replace placeholders in the core files:
   - `critical_prompt.md`
   - `context.md`
   - `context_pipeline.md`
   - `instructions.md`
   - `work_prompt.md`
   - `structure.md`
   - `SYSTEM_FLOW_INDEX.md`
3. Create first-pass architecture rows in `architecture/code-map.md`.
   Use subsystem-level rows, not one row per file.
4. Create component docs only for major planned subsystems.
   Use `architecture/components/component-template.md` as the pattern.
5. Fill `test_index/README.md` with known validation commands.
   If no tests exist yet, name the planned validation gates explicitly.
6. Keep placeholder folder READMEs in place so future agents know where
   information belongs.
7. Copy or retain `scripts/check_doc_coverage.py`.
8. Leave `context.md` concise. Put durable architecture in `architecture/`.

## Output Checklist

- Core context files exist at project root.
- Placeholder folders exist with README guidance.
- `architecture/code-map.md` has at least one subsystem row plus tests row.
- `work_prompt.md` requires code-map closeout for changed source files.
- `scripts/check_doc_coverage.py --help` runs.
- Remaining unknowns are recorded as assumptions, not hidden.

## Stop Conditions

Stop and ask before writing if:

- the target root is ambiguous
- the user wants global Codex skills rather than repo-local skills
- copying files would overwrite non-template project docs without approval
- the project idea does not define enough scope to name a goal and primary user
