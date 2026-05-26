# [PROJECT_NAME] Architecture

This folder maps architecture to source code, package boundaries, and
validation.

## Structure

- `code-map.md` - canonical subsystem-to-code/test/doc ownership map
- `components/` - focused subsystem contracts
- `dev_validated_docs/` - implementation notes backed by validation evidence
- `diagrams/` - architecture diagrams or textual diagrams

## Current Architecture

```text
[STATE_OWNER]
  -> [DOMAIN_OR_RUNTIME_LAYER]
    -> [INTERFACE_OR_PROJECTION_LAYER]
      -> [CLIENT_OR_AGENT_LAYER]
```

## Code-Referenced Coverage

Use `code-map.md` before editing runtime, UI, API, package, or validation code.
It maps subsystems to source globs, architecture anchors, test anchors, and
update triggers.

Run `python scripts/check_doc_coverage.py` for an advisory report before
session closeout.
