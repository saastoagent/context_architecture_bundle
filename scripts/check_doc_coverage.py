"""Generic advisory code-map coverage checker.

Copy this script into a project that uses architecture/code-map.md. It maps
changed source files to subsystem rows and prints architecture/test anchors to
review during closeout. It always exits 0.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CODE_MAP = PROJECT_ROOT / "architecture" / "code-map.md"
SOURCE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".json", ".toml", ".yaml", ".yml", ".md"}


@dataclass(frozen=True)
class CoverageRow:
    subsystem: str
    source_globs: tuple[str, ...]
    architecture_anchors: tuple[str, ...]
    test_anchors: tuple[str, ...]


def _extract_code_items(cell: str) -> tuple[str, ...]:
    return tuple(match.strip() for match in re.findall(r"`([^`]+)`", cell))


def load_rows() -> list[CoverageRow]:
    rows: list[CoverageRow] = []
    for line in CODE_MAP.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("| Subsystem ") or line.startswith("| --- "):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 7:
            rows.append(CoverageRow(cells[0], _extract_code_items(cells[2]), _extract_code_items(cells[4]), _extract_code_items(cells[5])))
    if not rows:
        raise ValueError(f"No coverage rows parsed from {CODE_MAP}")
    return rows


def run_git(args: list[str]) -> str:
    completed = subprocess.run(["git", *args], cwd=PROJECT_ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    return completed.stdout


def parse_status_paths(status_output: str, git_root: Path, project_root: Path) -> list[str]:
    """Return project-relative changed file paths from git status porcelain."""
    paths: list[str] = []
    for line in status_output.splitlines():
        if not line.strip():
            continue
        path_text = line[3:]
        if " -> " in path_text:
            path_text = path_text.split(" -> ", 1)[1]
        absolute = (git_root / path_text.replace("\\", "/").strip('"')).resolve()
        try:
            project_path = absolute.relative_to(project_root).as_posix()
        except ValueError:
            continue
        if (project_root / project_path).is_dir():
            paths.extend(child.relative_to(project_root).as_posix() for child in (project_root / project_path).rglob("*") if child.is_file())
        else:
            paths.append(project_path)
    return sorted(set(paths))


def changed_files() -> list[str]:
    git_root = Path(run_git(["rev-parse", "--show-toplevel"]).strip()).resolve()
    return parse_status_paths(run_git(["status", "--porcelain"]), git_root, PROJECT_ROOT)


def match(path: str, pattern: str) -> bool:
    pattern = pattern.replace("\\", "/")
    variants = [pattern]
    if "/**/" in pattern:
        variants.append(pattern.replace("/**/", "/"))
    return any(fnmatch.fnmatch(path, variant) for variant in variants)


def main() -> int:
    parser = argparse.ArgumentParser(description="Map changed source files to architecture/test anchors.")
    parser.add_argument("--files", nargs="+", help="Specific project-relative files to check.")
    args = parser.parse_args()

    changed = changed_files()
    files = [path.replace("\\", "/") for path in args.files] if args.files else changed
    source_files = [path for path in files if Path(path).suffix in SOURCE_SUFFIXES]
    rows = load_rows()

    print("Context architecture doc coverage advisory")
    print("Code map: architecture/code-map.md")
    if not source_files:
        print("No changed source files to map.")
        print("Result: advisory only; exit code remains 0.")
        return 0

    for path in source_files:
        owners = [row for row in rows if any(match(path, pattern) for pattern in row.source_globs)]
        if not owners:
            print(f"\nWARN: {path}")
            print("  No subsystem owner found in architecture/code-map.md.")
            continue
        print(f"\nOK: {path}")
        for row in owners:
            print(f"  Subsystem: {row.subsystem}")
            print("  Architecture anchors: " + (", ".join(row.architecture_anchors) or "(none)"))
            print("  Test anchors: " + (", ".join(row.test_anchors) or "(none)"))
    print("\nResult: advisory only; exit code remains 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
