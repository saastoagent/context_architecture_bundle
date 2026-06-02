# Context Architecture Bundle

Repo-local memory for AI coding agents.

Context Architecture Bundle is a copyable project template that helps Codex,
Claude, Gemini, and other coding agents restart cleanly, understand the system,
change the right files, and close a session with evidence instead of scattered
chat history.

Use it when a project is moving faster than its docs. The bundle gives your repo
a durable context layer: current state, architecture ownership, validation
meaning, decisions, handoff checkpoints, and repeatable agent workflows.

## Why This Exists

Agentic coding often burns time on rediscovery. Every new session has to ask:

- What does this project do?
- Which files own this behavior?
- What tests prove the change?
- What decisions are already settled?
- What happened in the previous session?

This bundle moves those answers into repo files so the next agent starts from
evidence, not memory.

## Who It Is For

- Developers using AI coding agents on real repos.
- Open-source maintainers who want contributors to understand project context
  before editing.
- Teams that need a lightweight handoff loop without adopting a heavy process
  tool.

This is template-first. There is no package to install for v1: copy the files,
fill the project-specific templates, and run the advisory checker.

## Try It In 5 Minutes

```powershell
git clone https://github.com/YOUR_ORG/context_architecture_bundle.git
cd context_architecture_bundle
python scripts/check_doc_coverage.py --help
python scripts/check_doc_coverage.py --files README.md skills/create-context-architecture-bundle/SKILL.md
```

Then inspect the filled example:

```text
examples/tiny-task-tracker/
```

The example shows the difference between the blank template files and a
populated context architecture for a small app.

## Use It In Your Project

1. Copy the bundle files into your project root.
2. Replace placeholders such as `[PROJECT_NAME]`, `[PRIMARY_RUNTIME]`, and
   `[VALIDATION_COMMAND]`.
3. Fill the core files first:
   - `critical_prompt.md`
   - `context.md`
   - `structure.md`
   - `SYSTEM_FLOW_INDEX.md`
   - `architecture/code-map.md`
   - `test_index/README.md`
4. Ask your coding agent to use `work_prompt.md` at session start and closeout.
5. Run the advisory checker before closeout:

```powershell
python scripts/check_doc_coverage.py
```

Detailed setup steps live in `docs/setup.md`. Daily usage lives in
`docs/usage.md`.

## What The Bundle Adds

| Path | Purpose |
| --- | --- |
| `critical_prompt.md` | Stable north star, boundaries, and non-negotiables. |
| `context.md` | Concise live restart snapshot. |
| `work_prompt.md` | Start, feature-completion, and session-end prompts. |
| `context_pipeline.md` | Rules for where project knowledge belongs. |
| `architecture/code-map.md` | Subsystem-to-source/test/doc ownership map. |
| `architecture/components/` | Focused contracts for high-change subsystems. |
| `SYSTEM_FLOW_INDEX.md` | Compact runtime and UX flow index. |
| `test_index/` | Validation commands and what each one proves. |
| `decisions/` | Architecture decision records. |
| `logs/` and `context_checkpoints/` | Session evidence and handoff notes. |
| `skills/` | Optional repo-local agent workflows. |
| `scripts/check_doc_coverage.py` | Advisory drift checker for changed files. |

## Example Agent Workflow

Start a session:

```text
I'm working on this project.

Please read critical_prompt.md and context.md first, then inspect
architecture/code-map.md and the relevant component docs. Tell me the current
state, known risks, and the next concrete step.
```

Before changing a feature:

```text
Before implementing this feature, identify the owning code-map row, likely
source files, docs that may need updates, and the validation command that should
prove the change.
```

End a session:

```text
Close out using work_prompt.md. Update context.md, add a checkpoint, record
validation evidence, and run python scripts/check_doc_coverage.py.
```

More ready-to-use prompts are in `AGENTIC_CODING_GUIDE.md`.

## Optional Repo-Local Skills

The bundle includes two optional skills for agents that support repo-local
skills:

- `skills/create-context-architecture-bundle` creates the bundle from a new
  project idea or early scaffold.
- `skills/populate-context-architecture` retrofits the bundle onto an existing
  codebase using live source evidence.

The files still work without skills. The public interface is the file structure
plus the checker script.

## Contributing

Useful first contributions:

- improve the filled example
- add docs for another agent workflow
- strengthen `scripts/check_doc_coverage.py`
- add tests around edge cases
- propose clearer templates or prompts

Read `CONTRIBUTING.md` and `ROADMAP.md` before opening a pull request.

## Sponsorship

If this project saves you repeated context rebuilding, consider sponsoring the
maintainer through the links in `.github/FUNDING.yml`. Sponsorship helps fund
examples, docs, tests, and compatibility work for real agentic coding workflows.

## License

MIT. See `LICENSE`.
