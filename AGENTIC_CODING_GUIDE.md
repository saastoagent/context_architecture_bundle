# Context Architecture Bundle For Agentic Coding

## Overview

The Context Architecture Bundle is a project memory and navigation layer for
agentic coding. It gives a repo the files an AI coding agent needs to restart
cleanly, understand the system, make changes in the right place, and close the
session without losing context.

It is useful when a project is moving fast and chat history is too fragile.
Instead of asking every agent to rediscover the architecture, the bundle puts
the important facts in the repo: `context.md` for the current restart snapshot,
`critical_prompt.md` for non-negotiables, `architecture/code-map.md` for source
ownership, `architecture/components/` for subsystem contracts, `test_index/` for
validation meaning, `decisions/` for ADRs, and `context_checkpoints/` plus
`logs/` for session evidence.

Concrete use: copy the bundle into the project root. For a new project, attach
the product spec and ask the agent to fill `critical_prompt.md`, `context.md`,
`structure.md`, `SYSTEM_FLOW_INDEX.md`, and first-pass
`architecture/code-map.md`. For an existing codebase, attach the file tree,
manifests, README, tests, and key source files, then ask the agent to populate
the bundle from live code evidence. During development, ask the agent to check
the relevant code-map row before changing files. At feature completion, ask it
to update docs, architecture, test index, and ADRs if boundaries changed. At
session end, ask it to close out using `work_prompt.md`.

The point is practical: make agentic coding less dependent on chat memory,
reduce architecture drift, save tokens, preserve context-window space, and give
every future agent a clear map before it edits code.

## Why This Helps Agentic Coding

Agentic coding sessions often waste context on rediscovery. The agent has to
ask or infer what the project does, where the important files are, what tests
matter, what decisions are already settled, and what happened in the previous
session. That burns tokens and fills the context window with repeated
orientation work instead of the actual task.

This bundle moves stable project knowledge into repo files. The agent can read
`context.md`, `architecture/code-map.md`, `work_prompt.md`, and the relevant
component docs instead of reconstructing the whole project from scratch. That
keeps prompts shorter, makes sessions more reproducible, and reduces the chance
that a long conversation pushes important constraints out of the model's
context window.

The bundle also creates a durable handoff loop. At the end of a session, the
agent updates `context.md`, writes a checkpoint, records validation evidence,
and updates architecture or ADRs when needed. The next session starts from that
compact repo-local state instead of an overloaded chat transcript.

## What Each Part Is For

- `critical_prompt.md` defines the north star, project boundaries, and
  non-negotiables.
- `context.md` is the concise live restart snapshot.
- `work_prompt.md` gives exact start, feature-completion, and session-end
  workflows.
- `instructions.md` explains the daily documentation workflow.
- `context_pipeline.md` defines what information belongs where.
- `structure.md` records the maintained project tree and source ownership
  snapshot.
- `SYSTEM_FLOW_INDEX.md` summarizes runtime and UX flows.
- `architecture/code-map.md` maps source globs to owning subsystems, docs, and
  tests.
- `architecture/components/` stores subsystem contracts, interfaces, invariants,
  tests, and update triggers.
- `test_index/` records validation commands and what each one proves.
- `decisions/` stores ADRs.
- `plans/` stores active implementation and architecture plans.
- `logs/` and `context_checkpoints/` preserve session evidence.
- `context_history/` archives older `context.md` snapshots.
- `knowledgebase/` stores verified reusable findings.
- `audits/` stores read-only audit reports.
- `errors/` stores hard debugging notes.
- `skills/` stores stable repeatable repo-local workflows.
- `scripts/check_doc_coverage.py` gives an advisory drift check between changed
  files and documented ownership.

## Exact Agentic Coding Prompts

### New Project From Idea Or Spec

Attach:

- product spec or idea brief
- README if present
- package manifests if present
- current file tree if any
- known run, test, and build commands

Prompt:

```text
I am starting a new project. Use the attached product spec, architecture notes,
and any scaffold files to create the Context Architecture Bundle.

Please:
1. Fill critical_prompt.md with the project goal, users, boundaries, and non-negotiables.
2. Fill context.md as a concise restart snapshot.
3. Fill structure.md from the actual or planned project tree.
4. Fill SYSTEM_FLOW_INDEX.md with the expected runtime and UX flows.
5. Create first-pass architecture/code-map.md rows at subsystem level.
6. Fill test_index/README.md with known or planned validation gates.
7. Keep unknowns explicit as assumptions.
8. Do not create one-off history as skills. Create repo-local skills only for stable repeatable workflows.
```

### Existing Repo Retrofit

Attach:

- README.md
- package manifests, dependency files, and lockfiles
- source tree
- tests tree
- key runtime entrypoints
- existing docs, ADRs, plans, or logs
- current git status or changed-file list

Prompt:

```text
Use the attached repo files to populate the Context Architecture Bundle for this existing codebase.

Please:
1. Inspect the live source before writing conclusions.
2. Populate context.md, structure.md, SYSTEM_FLOW_INDEX.md, and architecture/code-map.md from real code evidence.
3. Group code-map rows by subsystem ownership, not every individual file.
4. Add component docs for the highest-risk or highest-change subsystems.
5. Fill test_index/README.md with executable commands and what each command proves.
6. Add or update scripts/check_doc_coverage.py if this repo needs advisory doc coverage checks.
7. Do not invent business rules that are not supported by source, tests, or docs.
8. Preserve existing hand-written docs unless there is clear evidence they are stale.
```

### Start A Session

Attach:

- `critical_prompt.md`
- `context.md`
- latest file from `context_checkpoints/`
- `instructions.md`
- `context_pipeline.md`
- `architecture/code-map.md`
- relevant `architecture/components/` docs
- active plan from `plans/`

Prompt:

```text
I'm working on this project.

Please:
1. Read critical_prompt.md and context.md first.
2. Inspect the latest checkpoint in context_checkpoints/.
3. Review instructions.md and context_pipeline.md for the documentation workflow.
4. Review architecture/code-map.md and any relevant architecture/components/ docs if source files are in scope.
5. Review the active plan in plans/.
6. Tell me the current state, known risks, and the next concrete step.
7. Keep the response concise and cite the project files you relied on.
```

### Before Changing A Feature

Attach:

- feature request
- current `context.md`
- `architecture/code-map.md`
- relevant component docs
- relevant source files
- relevant tests

Prompt:

```text
Before implementing this feature, read critical_prompt.md, context.md,
architecture/code-map.md, and the relevant architecture/components docs.

Please:
1. Identify the owning code-map subsystem row.
2. Name the source files likely to change.
3. Name the docs, ADRs, component docs, and test_index entries that may need updates.
4. Identify the validation command that should prove the change.
5. Then implement the smallest coherent slice.
6. Do not change unrelated architecture or documentation surfaces.
```

### Feature Completion

Attach:

- `work_prompt.md`
- `architecture/code-map.md`
- changed-file list or git diff
- relevant tests and test output
- related component docs
- `test_index/README.md`
- existing ADRs in `decisions/`

Prompt:

```text
The feature is complete. Close it out using work_prompt.md.

Please:
1. Update docs/ if user or developer behavior changed.
2. Update architecture/code-map.md if source ownership, interfaces, tests, or update triggers changed.
3. Update relevant architecture/components docs.
4. Update SYSTEM_FLOW_INDEX.md only if runtime or UX flows changed.
5. Update test_index/ with validation commands and what they prove.
6. Add or update ADRs if this feature changed a boundary, direction, compatibility rule, or rejected a plausible alternative.
7. Update context.md as the concise restart snapshot.
8. List validation commands run and their results.
```

### ADR Update

Attach:

- feature summary
- changed-file list or git diff
- `architecture/code-map.md`
- relevant component docs
- existing `decisions/` folder
- test evidence

Prompt:

```text
Update ADRs for this feature.

Please:
1. Decide whether this needs a new ADR or an update to an existing ADR.
2. Create an ADR only if the change affects future implementation direction, subsystem boundaries, compatibility, migration, or rejects a plausible alternative.
3. Include status, context, decision, consequences, validation, and follow-up.
4. Link the ADR from the relevant code-map row or component doc if appropriate.
5. If no ADR is needed, state why and name any docs that were updated instead.
```

### End A Session

Attach:

- `work_prompt.md`
- current `context.md`
- `architecture/code-map.md`
- git diff or changed-file list
- test output
- notes from this session

Prompt:

```text
End this session as per work_prompt.md.

Please:
1. Create a log entry in logs/.
2. Create a checkpoint in context_checkpoints/.
3. Archive the previous context.md into context_history/ if needed.
4. Rewrite context.md as the concise live snapshot.
5. List changed source files and their owning architecture/code-map.md subsystem rows.
6. Update plans, knowledgebase, decisions, architecture, docs, and test_index if this session changed them.
7. For each changed source subsystem, update the related component doc/test_index entry or explicitly state that the documented contract is unchanged.
8. Run python scripts/check_doc_coverage.py and capture notable warnings.
9. Update SYSTEM_FLOW_INDEX.md only if runtime or UX flows changed.
10. Keep the final handoff compact enough to fit into the next agentic coding session without wasting context-window space.
```

### Debugging Or Error Capture

Attach:

- failing command and output
- relevant source files
- relevant tests
- `context.md`
- `architecture/code-map.md`
- any prior notes from `errors/`

Prompt:

```text
Investigate this failure and preserve the debugging evidence in the Context Architecture Bundle.

Please:
1. Identify the failing subsystem from architecture/code-map.md.
2. Reproduce or inspect the failure from the attached evidence.
3. Fix the smallest likely cause.
4. Run the relevant validation command.
5. Add an errors/ note only if the failure pattern is non-obvious and likely to recur.
6. Update test_index/ or component docs if the validation meaning or subsystem invariant changed.
7. Update context.md only with durable restart-relevant state.
```

## Operating Rule

The bundle should keep stable project knowledge out of the chat transcript and
inside the repo. Prompts should attach only the relevant files, and agents
should update only the surfaces whose ownership actually changed. That is what
saves tokens, protects the context window, and makes each future session start
from evidence instead of rediscovery.
