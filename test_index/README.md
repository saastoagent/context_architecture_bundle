# Test Index

This folder explains what validation protects, how to run it, and which source
subsystems it covers.

## Suite Index

| Suite | Command | Protects | Source owner |
| --- | --- | --- | --- |
| `[FAST_SUITE]` | `[FAST_CHECK_COMMAND]` | `[BEHAVIOR]` | `[CODE_MAP_ROW]` |
| `[FULL_SUITE]` | `[FULL_CHECK_COMMAND]` | `[BEHAVIOR]` | `[CODE_MAP_ROW]` |

## Each Test Doc Should Include

- test approach
- fixtures used
- what each test validates
- how to run
- linked `architecture/code-map.md` subsystem rows

## Architecture Coverage Link

`architecture/code-map.md` is the source-to-test ownership map. When adding,
renaming, or deleting tests, update the matching row there and refresh any
component doc under `architecture/components/` that names the suite.
