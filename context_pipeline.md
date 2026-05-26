# Context Pipeline - [PROJECT_NAME]

This project uses a structured context pipeline for continuity, planning, code
traceability, and clean handoffs.

## Goals

1. Session continuity
2. Clean handoffs between sessions
3. Verified planning before implementation
4. Auditable progress history
5. Code-referenced architecture coverage
6. Reusable workflows captured as skills only when truly repeatable

## Layers

### Vision

- `critical_prompt.md` - product/system scope and north star

### State

- `context.md` - live current state
- `context_history/` - archived prior `context.md` snapshots
- `context_checkpoints/` - end-of-session handoff snapshots
- `structure.md` - project tree and source ownership snapshot

### Process

- `instructions.md` - documentation workflow
- `work_prompt.md` - session start/end templates
- `context_pipeline.md` - this file

### Architecture And Validation

- `architecture/code-map.md` - subsystem-to-code/test/doc ownership map
- `architecture/components/` - focused component contracts
- `SYSTEM_FLOW_INDEX.md` - compact runtime and UX flow index
- `test_index/` - validation docs and commands

### History And Decisions

- `logs/` - session activity history
- `decisions/` - ADRs
- `errors/` - hard debugging notes
- `audits/` - read-only audit reports

### Knowledge And Planning

- `plans/` - active plans
- `knowledgebase/` - verified reusable findings
- `skills/` - reusable workflows only

## Session Lifecycle

### Session Start

Read, in order:

1. `critical_prompt.md`
2. `context.md`
3. Latest file in `context_checkpoints/` if resuming
4. `architecture/code-map.md` when source files, tests, or architecture are in scope
5. Relevant component doc in `architecture/components/`
6. Relevant active plan in `plans/`
7. Relevant repo-local skill in `skills/`

### Planning Phase

1. Verify uncertain technical details from code.
2. Record reusable findings in `knowledgebase/`.
3. Create or refine a plan in `plans/`.
4. Create an ADR in `decisions/` when the choice changes future work.

### Implementation Phase

1. Implement according to the accepted plan.
2. Track changed source files against `architecture/code-map.md`.
3. Keep `context.md` current.
4. Add or update component docs, test docs, ADRs, or KB notes when contracts move.

### Session End

1. Create a log entry in `logs/`.
2. Create a checkpoint in `context_checkpoints/`.
3. Archive previous `context.md` into `context_history/` if meaningfully changed.
4. Rewrite `context.md` as the concise live snapshot.
5. Name changed source files and owning `architecture/code-map.md` rows.
6. Update related component/test docs or explicitly state why they are unchanged.
7. Run `python scripts/check_doc_coverage.py` and include notable warnings.

## Working Rule

Do not turn `context.md` into a full architecture document. It should point to
the current anchors and summarize restart state. Durable architecture belongs in
`architecture/`; validation meaning belongs in `test_index/`.
