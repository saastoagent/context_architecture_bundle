# Usage

The bundle works by making agents read and update a small set of repo files at
the right moments.

## Start A Session

Use `work_prompt.md` or paste:

```text
I'm working on this project.

Please read critical_prompt.md and context.md first. If resuming, inspect the
latest checkpoint in context_checkpoints/. Review architecture/code-map.md and
the relevant component docs if source files are in scope. Tell me the current
state, known risks, and the next concrete step.
```

## Before A Feature Change

Ask the agent to identify ownership before editing:

```text
Before implementing this feature, read critical_prompt.md, context.md,
architecture/code-map.md, and the relevant component docs.

Name the owning subsystem row, likely source files, docs that may need updates,
and the validation command that should prove the change.
```

## During Closeout

Run the advisory checker:

```powershell
python scripts/check_doc_coverage.py
```

Then ask:

```text
Close out using work_prompt.md. Update context.md, create a checkpoint, record
validation evidence, and name changed source files with their owning code-map
rows.
```

## Good Maintenance Habits

- Keep `context.md` short and current.
- Put durable architecture in `architecture/`, not in session logs.
- Update `test_index/` when validation commands or their meaning changes.
- Add ADRs only when a decision affects future implementation.
- Create repo-local skills only for stable repeatable workflows.

## What Not To Do

- Do not turn `context.md` into a full architecture document.
- Do not create logs for every passing thought.
- Do not invent source ownership that is not supported by code, tests, or docs.
- Do not use skills for one-off session history.
