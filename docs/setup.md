# Setup

Context Architecture Bundle is a file-based template. You copy it into a repo,
fill the project-specific placeholders, and use the files as the shared memory
layer for AI coding sessions.

## Copy Into A Project

From this repo:

```powershell
Copy-Item -Recurse critical_prompt.md,context.md,context_pipeline.md,instructions.md,work_prompt.md,structure.md,SYSTEM_FLOW_INDEX.md,architecture,docs,test_index,knowledgebase,plans,decisions,logs,context_checkpoints,context_history,audits,errors,skills,scripts C:\path\to\your-project
```

On Unix-like shells:

```bash
cp -R critical_prompt.md context.md context_pipeline.md instructions.md work_prompt.md structure.md SYSTEM_FLOW_INDEX.md architecture docs test_index knowledgebase plans decisions logs context_checkpoints context_history audits errors skills scripts /path/to/your-project/
```

## Fill The Core Files

Replace placeholders in this order:

1. `critical_prompt.md` - project goal, users, boundaries, owners, and stop
   conditions.
2. `context.md` - current state, commands, contracts, recent work, and next
   step.
3. `structure.md` - maintained tree snapshot and source ownership.
4. `SYSTEM_FLOW_INDEX.md` - active runtime, UX, command, or API flows.
5. `architecture/code-map.md` - subsystem rows that map source globs to docs
   and tests.
6. `test_index/README.md` - validation commands and what they prove.

Keep unknowns explicit as assumptions. Do not hide uncertainty behind polished
language.

## Validate The Checker

Run:

```powershell
python scripts/check_doc_coverage.py --help
python scripts/check_doc_coverage.py --files README.md
```

The checker is advisory. It maps changed files to `architecture/code-map.md`
rows and always exits 0 so it can be used during handoff without blocking work.

## First Agent Prompt

```text
I am adding the Context Architecture Bundle to this project.

Please inspect the live repo before writing conclusions. Populate
critical_prompt.md, context.md, structure.md, SYSTEM_FLOW_INDEX.md,
architecture/code-map.md, and test_index/README.md from source, tests, manifests,
and existing docs. Keep unknowns explicit as assumptions.
```
