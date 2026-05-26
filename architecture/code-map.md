# [PROJECT_NAME] Code Map

Last updated: [YYYY-MM-DD]

This is the canonical subsystem-to-code map for [PROJECT_NAME]. It is
subsystem-level, not per-file prose.

## How To Use This Map

- Start here when changing source, tests, examples, packaging, or docs that
  describe current behavior.
- Update the owning row when code ownership, public interfaces, tests, or docs
  move.
- During closeout, list changed source files and either update the related
  architecture/test anchors or explicitly state that the anchors are unchanged.
- Run `python scripts/check_doc_coverage.py` before closeout for an advisory
  drift report.

## Coverage Table

The `Source globs` column is parsed by `scripts/check_doc_coverage.py`. Keep
globs comma-separated and relative to this project root.

| Subsystem | Purpose | Source globs | Interfaces | Architecture anchors | Test anchors | Update triggers |
| --- | --- | --- | --- | --- | --- | --- |
| `[SUBSYSTEM_1]` | `[WHAT_THIS_SUBSYSTEM_OWNS]` | `[SOURCE_GLOB_1]`, `[SOURCE_GLOB_2]` | `[PUBLIC_INTERFACE_1]`, `[PUBLIC_INTERFACE_2]` | `architecture/components/[subsystem-1].md`, `SYSTEM_FLOW_INDEX.md` | `[TEST_FILE_OR_COMMAND]`, `test_index/[subsystem-1].md` | `[WHEN_TO_UPDATE_THIS_ROW]` |
| `[SUBSYSTEM_2]` | `[WHAT_THIS_SUBSYSTEM_OWNS]` | `[SOURCE_GLOB_3]` | `[PUBLIC_INTERFACE_3]` | `architecture/components/[subsystem-2].md` | `[TEST_FILE_OR_COMMAND]` | `[WHEN_TO_UPDATE_THIS_ROW]` |
| Context architecture lifecycle | Core context, handoff, architecture, placeholder folders, and closeout workflow docs. | `*.md`, `architecture/**/*.md`, `docs/**/*.md`, `test_index/**/*.md`, `knowledgebase/**/*.md`, `plans/**/*.md`, `decisions/**/*.md`, `logs/**/*.md`, `context_checkpoints/**/*.md`, `context_history/**/*.md`, `audits/**/*.md`, `errors/**/*.md` | Session start/end prompts, live context, code map, flow index, folder ownership docs. | `context_pipeline.md`, `work_prompt.md`, `architecture/code-map.md`, `architecture/components/README.md` | `python scripts/check_doc_coverage.py --help`, documentation self-review | Context lifecycle changes, folder inventory changes, closeout rule changes, or architecture coverage policy changes. |
| Repo-local skills | Stable repeatable workflows captured as project-local skills. | `skills/**/*.md`, `skills/**/*.py`, `skills/**/*.json` | Skill `SKILL.md` files and bundled helper scripts/resources. | `skills/README.md`, `architecture/code-map.md` | skill self-review, `python scripts/check_doc_coverage.py --files skills/[skill-name]/SKILL.md` | Skill trigger changes, input/output/check changes, bundled script changes, or new repeatable workflow additions. |
| Tests and validation harness | Validation code and docs that prove behavior. | `tests/**/*.py`, `test/**/*.ts`, `scripts/*.py`, `test_index/*.md` | Test runner commands and validation docs. | `architecture/code-map.md`, `test_index/README.md` | `[FULL_TEST_COMMAND]` | Test movement, validation command changes, or acceptance criteria changes. |

## Closeout Rule

If a changed source file matches one of these rows, closeout must name the row
and say which architecture anchors and test anchors were updated or why they did
not need updates.
