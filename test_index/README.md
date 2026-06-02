# Test Index

This folder explains what validation protects, how to run it, and which source
subsystems it covers.

## Suite Index

| Suite | Command | Protects | Source owner |
| --- | --- | --- | --- |
| Checker help | `python scripts/check_doc_coverage.py --help` | CLI entrypoint remains usable | Tests and validation harness |
| Checker targeted mapping | `python scripts/check_doc_coverage.py --files README.md skills/create-context-architecture-bundle/SKILL.md` | Source-to-doc ownership mapping remains understandable | Context architecture lifecycle, Repo-local skills |
| Unit tests | `python -m unittest discover` | Code-map parsing, renamed-file handling, glob matching, and unmatched-file warnings | Tests and validation harness |
| Documentation self-review | Manual review of README, `docs/`, example, and GitHub templates | Public onboarding and adoption clarity | Context architecture lifecycle |

## Future Test Docs Should Include

- test approach
- fixtures used
- what each test validates
- how to run
- linked `architecture/code-map.md` subsystem rows

## Architecture Coverage Link

`architecture/code-map.md` is the source-to-test ownership map. When adding,
renaming, or deleting tests, update the matching row there and refresh any
component doc under `architecture/components/` that names the suite.
