# Documentation Instructions - [PROJECT_NAME]

Use this workflow whenever source, runtime behavior, architecture, tests, or
project state changes.

## Default Documentation Flow

1. Read `context.md` and `architecture/code-map.md`.
2. Identify the subsystem row for changed source files.
3. Update source code or docs in the smallest coherent slice.
4. Run the relevant validation command from `test_index/` or the code-map row.
5. Update component docs when interfaces, ownership, or invariants changed.
6. Update `SYSTEM_FLOW_INDEX.md` only when runtime or UX flow changed.
7. Update `context.md` as the concise restart state.

## Where Information Belongs

| Information | Location |
| --- | --- |
| Current restart state | `context.md` |
| Session evidence | `logs/`, `context_checkpoints/` |
| Source ownership | `architecture/code-map.md` |
| Subsystem contracts | `architecture/components/` |
| User/developer guides | `docs/` |
| Test meaning and commands | `test_index/` |
| Architectural decisions | `decisions/` |
| Reusable findings | `knowledgebase/` |
| Repeatable procedures | `skills/` |
| Debugging failures | `errors/` |

## Source Change Closeout Checklist

- Changed source files are listed.
- Each changed source file maps to a code-map subsystem row.
- Related architecture/component docs are updated or explicitly unchanged.
- Related test docs are updated or explicitly unchanged.
- Validation commands and results are recorded.
- `context.md` links to current anchors instead of duplicating them.

## Skill Rule

Create a repo-local skill only when the workflow is stable, repeatable, and has
clear invocation criteria, inputs, outputs, checks, and stop conditions. Do not
create skills for one-off fixes or session-specific history.
