# Critical Prompt - [PROJECT_NAME]

Use this file as the stable north star for [PROJECT_NAME]. It should be short
enough to read at every session start and strict enough to prevent drift.

## Product / System Goal

[PROJECT_NAME] exists to [ONE_SENTENCE_GOAL].

The primary users are:

- [USER_OR_ACTOR_1]
- [USER_OR_ACTOR_2]
- [DEVELOPER_OR_OPERATOR_IF_RELEVANT]

The core workflow is:

```text
[STARTING_STATE]
  -> [MAJOR_STEP_1]
  -> [MAJOR_STEP_2]
  -> [SUCCESSFUL_OUTCOME]
```

## Non-Negotiable Boundaries

- [BOUNDARY_1: e.g. product code owns domain behavior]
- [BOUNDARY_2: e.g. framework code stays product-neutral]
- [BOUNDARY_3: e.g. no credentials in repo docs]
- [BOUNDARY_4: e.g. runtime truth lives in backend/database/graph, not UI-local state]

## Current Architecture Posture

- Runtime owner: `[PRIMARY_RUNTIME]`
- UI owner: `[PRIMARY_UI_STACK]`
- Persistence owner: `[PRIMARY_DATA_STORE]`
- Integration owner: `[PRIMARY_INTEGRATION_LAYER]`
- Validation owner: `test_index/` plus executable tests

## Design Defaults

- Prefer code-referenced architecture over broad narrative docs.
- Prefer small subsystem contracts over per-file prose.
- Keep `context.md` concise; put durable architecture in `architecture/`.
- Update docs and tests when runtime contracts move.
- Record decisions in `decisions/` when a choice changes future implementation.

## Stop Conditions

Stop and re-plan if:

- the requested work crosses a boundary in this file
- source ownership is unclear in `architecture/code-map.md`
- a behavior claim cannot be verified with a command, test, or live evidence
- the implementation would require deleting or rewriting unrelated user work
