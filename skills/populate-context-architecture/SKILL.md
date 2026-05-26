---
name: populate-context-architecture
description: Use when adding or repairing context, architecture, code-map, handoff, and validation docs for an existing codebase with real source files and tests.
---

# Populate Context Architecture

Use this skill to retrofit an existing project with code-referenced context and
architecture docs.

## Inputs

Start from live repo evidence:

- current `README.md`, package manifests, run/test commands
- source directories and test directories
- existing docs, ADRs, plans, and logs
- current git status and latest baseline commit
- known product/runtime boundaries

## Workflow

1. Inspect the repo before writing.
   Prefer source, tests, manifests, and existing docs over memory.
2. Create or update the core context files:
   - `critical_prompt.md`
   - `context.md`
   - `context_pipeline.md`
   - `instructions.md`
   - `work_prompt.md`
   - `structure.md`
   - `SYSTEM_FLOW_INDEX.md`
3. Build `architecture/code-map.md` from real directories and tests.
   Group by subsystem ownership, not by every file.
4. Add component docs for the highest-risk/high-change subsystems first.
   Each component doc must name owner files, public interfaces, dependent flows,
   tests, and update triggers.
5. Populate `test_index/README.md` with executable validation commands and what
   each protects.
6. Add missing placeholder folders with README files only when they represent a
   real lifecycle surface.
7. Add or update `scripts/check_doc_coverage.py`.
8. Run the checker in default mode and with at least one known source file via
   `--files`.
9. Run the fastest meaningful existing validation command.

## Output Checklist

- `context.md` is a concise restart snapshot.
- `architecture/code-map.md` maps real source globs to docs/tests.
- Component docs cover major active subsystems.
- `work_prompt.md` enforces changed-source closeout.
- `test_index/README.md` explains validation ownership.
- Checker output is captured in closeout.
- Existing user changes are preserved.

## Stop Conditions

Stop and ask before writing if:

- the repo has multiple plausible project roots
- existing docs conflict and source evidence cannot resolve the conflict
- the requested retrofit would overwrite substantial hand-written docs
- tests or run commands are dangerous or require credentials not available locally
