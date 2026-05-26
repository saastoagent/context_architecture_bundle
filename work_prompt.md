# Work Prompt - [PROJECT_NAME]

Use this prompt to start, resume, or close work on [PROJECT_NAME].

## Session Start Prompt

```text
I'm working on the [PROJECT_NAME] project.

Please:
1. Read critical_prompt.md and context.md first
2. If resuming, inspect the latest checkpoint in context_checkpoints/
3. Review instructions.md and context_pipeline.md for the documentation workflow
4. Review architecture/code-map.md and any relevant architecture/components/ doc if source files are in scope
5. Review the active plan in plans/
6. Tell me the current state and the next concrete step
```

## Session End Prompt

```text
We're wrapping up this session. Please:

1. Create a log entry in logs/
2. Create a checkpoint in context_checkpoints/
3. Archive the previous context.md into context_history/ if needed
4. Rewrite context.md as the concise live snapshot
5. List changed source files and their owning architecture/code-map.md subsystem rows
6. Update plans, knowledgebase, decisions, architecture, docs, and test_index if this session changed them
7. For each changed source subsystem, update the related component doc/test_index entry or explicitly state that the documented contract is unchanged
8. Run python scripts/check_doc_coverage.py and capture notable warnings
9. Update SYSTEM_FLOW_INDEX.md only if runtime or UX flows changed
```

## Feature Completion Prompt

```text
The feature is complete. Please:

1. Update docs/
2. Update architecture/code-map.md and relevant architecture/components/ docs if source ownership, interfaces, tests, or update triggers changed
3. Update SYSTEM_FLOW_INDEX.md if flows changed
4. Update test_index/ with validation meaning and commands
5. Update context.md
6. Add ADRs or knowledgebase notes if needed
```
