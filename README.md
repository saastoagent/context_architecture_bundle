# Context Architecture Bundle

This bundle is a starter kit for projects that need durable context,
code-referenced architecture, handoff, and validation docs.

It supports two use cases:

- create a new context architecture from a product/project idea
- populate or repair context architecture for an existing codebase

Copy the files in this folder into a project root, then replace bracketed
placeholders such as `[PROJECT_NAME]`, `[PRIMARY_RUNTIME]`, and
`[VALIDATION_COMMAND]` with project-specific content.

## File Inventory

- `critical_prompt.md` - north star, boundaries, and non-negotiables
- `context.md` - concise live restart snapshot
- `context_pipeline.md` - lifecycle and documentation ownership rules
- `instructions.md` - daily documentation workflow
- `work_prompt.md` - session start/end/feature completion prompts
- `structure.md` - maintained project tree and source ownership snapshot
- `SYSTEM_FLOW_INDEX.md` - compact runtime and UX flow index
- `architecture/` - code map and component docs
- `docs/` - user/operator/developer guides
- `test_index/` - validation ownership docs
- `knowledgebase/` - verified reusable findings
- `plans/` - active implementation and architecture plans
- `decisions/` - ADRs
- `logs/` - session logs
- `context_checkpoints/` - end-of-session checkpoints
- `context_history/` - archived prior `context.md` snapshots
- `audits/` - read-only audit reports
- `errors/` - hard debugging notes
- `skills/` - reusable repo-local skills
- `scripts/check_doc_coverage.py` - advisory code-map drift checker

## Bundle Rules

- `context.md` is concise and current; it links to anchors instead of becoming
  the architecture.
- `architecture/code-map.md` owns source-to-doc/test traceability.
- `architecture/components/` owns subsystem contracts.
- `test_index/` owns validation meaning and commands.
- `logs/` and `context_checkpoints/` own session evidence.
- Skills capture repeatable procedures only, not session history.
