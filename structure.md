# Structure - [PROJECT_NAME]

Last updated: [YYYY-MM-DD HH:MM TZ]

This file summarizes the project tree and source ownership. It is a maintained
snapshot, not a full recursive listing.

## Root

```text
[PROJECT_ROOT]/
  README.md
  critical_prompt.md
  context.md
  context_pipeline.md
  instructions.md
  work_prompt.md
  SYSTEM_FLOW_INDEX.md
  architecture/
  docs/
  test_index/
  plans/
  decisions/
  knowledgebase/
  logs/
  context_checkpoints/
  context_history/
  audits/
  errors/
  skills/
  scripts/
  [SOURCE_DIR_1]/
  [SOURCE_DIR_2]/
  [TEST_DIR]/
```

## Source Ownership

| Path | Owner subsystem | Notes |
| --- | --- | --- |
| `[SOURCE_DIR_1]/` | `[SUBSYSTEM_1]` | `[WHAT_IT_OWNS]` |
| `[SOURCE_DIR_2]/` | `[SUBSYSTEM_2]` | `[WHAT_IT_OWNS]` |
| `[TEST_DIR]/` | Tests and validation | `[TEST_SCOPE]` |

## Generated / Ignored Paths

- `[GENERATED_PATH]` - `[WHY_IGNORED]`
- `[CACHE_PATH]` - `[WHY_IGNORED]`

## Update Rule

Update this file when a major directory, subsystem boundary, or generated path
changes. Update `architecture/code-map.md` for source-to-test/doc ownership.
