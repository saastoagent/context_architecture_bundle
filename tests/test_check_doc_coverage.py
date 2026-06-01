from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import check_doc_coverage


class CheckDocCoverageTests(unittest.TestCase):
    def test_load_rows_parses_code_map_table(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            code_map = root / "architecture" / "code-map.md"
            code_map.parent.mkdir()
            code_map.write_text(
                "\n".join(
                    [
                        "| Subsystem | Purpose | Source globs | Interfaces | Architecture anchors | Test anchors | Update triggers |",
                        "| --- | --- | --- | --- | --- | --- | --- |",
                        "| API | Routes | `app/**/*.py`, `app/*.py` | `GET /tasks` | `architecture/components/api.md` | `pytest tests/test_api.py` | Route changes |",
                    ]
                ),
                encoding="utf-8",
            )

            with mock.patch.object(check_doc_coverage, "CODE_MAP", code_map):
                rows = check_doc_coverage.load_rows()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].subsystem, "API")
        self.assertEqual(rows[0].source_globs, ("app/**/*.py", "app/*.py"))
        self.assertEqual(rows[0].architecture_anchors, ("architecture/components/api.md",))
        self.assertEqual(rows[0].test_anchors, ("pytest tests/test_api.py",))

    def test_parse_status_paths_handles_renamed_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            (root / "docs").mkdir()
            (root / "docs" / "new.md").write_text("new", encoding="utf-8")

            paths = check_doc_coverage.parse_status_paths(
                'R  docs/old.md -> docs/new.md\n?? "README.md"\n',
                root,
                root,
            )

        self.assertEqual(paths, ["README.md", "docs/new.md"])

    def test_match_supports_double_star_middle_variant(self) -> None:
        self.assertTrue(check_doc_coverage.match("app/main.py", "app/**/*.py"))
        self.assertTrue(check_doc_coverage.match("app/api/main.py", "app/**/*.py"))
        self.assertFalse(check_doc_coverage.match("web/main.ts", "app/**/*.py"))

    def test_main_reports_unmatched_source_warning(self) -> None:
        row = check_doc_coverage.CoverageRow(
            subsystem="API",
            source_globs=("app/**/*.py",),
            architecture_anchors=("architecture/components/api.md",),
            test_anchors=("pytest tests/test_api.py",),
        )

        output = io.StringIO()
        with mock.patch.object(check_doc_coverage, "load_rows", return_value=[row]):
            with mock.patch.object(check_doc_coverage, "changed_files", return_value=[]):
                with mock.patch("sys.argv", ["check_doc_coverage.py", "--files", "web/main.ts"]):
                    with contextlib.redirect_stdout(output):
                        exit_code = check_doc_coverage.main()

        self.assertEqual(exit_code, 0)
        self.assertIn("WARN: web/main.ts", output.getvalue())
        self.assertIn("No subsystem owner found", output.getvalue())


if __name__ == "__main__":
    unittest.main()
