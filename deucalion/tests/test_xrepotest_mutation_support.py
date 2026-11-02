"""Regressions for official paths, operator methods, isolation and bad runs."""
import tempfile
import sys
from pathlib import Path
import unittest

from deucalion.xrepotest_mutation_support import execute, parse_result, resolve_subject


class SubjectTests(unittest.TestCase):
    def task(self, source, name, start, end, rel="lib/example.rb"):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source)
        self.path = path
        return {"file_path": "example/" + rel, "file_content": source,
                "function_name": name, "focal_code": "\n".join(source.splitlines()[start-1:end]).strip(),
                "function_component": {"start_line": start, "end_line": end}}

    def test_operator_and_full_rom_subproject(self):
        task = self.task("module ROM\n class Box\n def [](x)\n x\n end\n end\nend\n", "[]", 3, 5, "core/lib/rom/box.rb")
        result = resolve_subject(task, self.repo)
        self.assertEqual(result["subject"], "ROM::Box#[]")
        self.assertEqual(result["file"], "core/lib/rom/box.rb")

    def test_same_name_selects_official_range(self):
        src = "class A\n def value\n 1\n end\nend\nclass B\n def value\n 2\n end\nend\n"
        self.assertEqual(resolve_subject(self.task(src, "value", 7, 9), self.repo)["subject"], "B#value")

    def test_singleton_method(self):
        t = self.task("module A\n def self.value\n 1\n end\nend\n", "value", 2, 4)
        self.assertEqual(resolve_subject(t, self.repo)["subject"], "A.value")

    def test_singleton_class(self):
        t = self.task("class A\n class << self\n def value\n 1\n end\n end\nend\n", "value", 3, 5)
        self.assertEqual(resolve_subject(t, self.repo)["subject"], "A.value")

    def test_struct_block_candidate(self):
        t = self.task("module A\n Box = Struct.new(:a) do\n def ==(b)\n a == b\n end\n end\nend\n", "==", 3, 5)
        self.assertEqual(resolve_subject(t, self.repo)["subject"], "A::Box#==")

    def test_conditional_block_candidate(self):
        t = self.task("class A\n condition do\n def value\n 1\n end\n end\nend\n", "value", 3, 5)
        self.assertEqual(resolve_subject(t, self.repo)["subject"], "A#value")

    def test_read_text_newlines_preserved_without_changing_file(self):
        t = self.task("class A\n def value\n 1\n end\nend\n", "value", 2, 4)
        self.path.write_bytes(self.path.read_bytes().replace(b"\n", b"\r\n"))
        before = self.path.read_bytes()
        self.assertEqual(resolve_subject(t, self.repo)["subject"], "A#value")
        self.assertEqual(self.path.read_bytes(), before)

    def test_changed_source_refused(self):
        t = self.task("class A\n def value\n 1\n end\nend\n", "value", 2, 4)
        self.path.write_text(self.path.read_text().replace(" 1", " 2"))
        with self.assertRaisesRegex(ValueError, "differs"):
            resolve_subject(t, self.repo)

    def test_no_guess_for_anonymous_dsl(self):
        t = self.task("dsl do\n def value\n 1\n end\nend\n", "value", 2, 4)
        with self.assertRaisesRegex(ValueError, "named owner"):
            resolve_subject(t, self.repo)


class ResultTests(unittest.TestCase):
    good = "Mutations: 10\nResults: 10\nKills: 8\nAlive: 2\nTimeouts: 0\n"

    def test_process_timeout_preserves_log_and_is_distinct_from_exit_one(self):
        out, err, code = execute([sys.executable, "-c", "import time; print('ready', flush=True); time.sleep(30)"], Path.cwd(), 0.5)
        self.assertIn("ready", out)
        self.assertIsNone(code)

    def test_nonzero_uncovered_exit_is_valid(self):
        self.assertEqual(parse_result(self.good, "Uncovered mutations", 1, {"verified": True})["mutation_score"], 0.8)

    def test_startup_partial_and_timeout_are_not_zero_scores(self):
        for stdout, stderr, code, identity in (
            ("", "uninitialized constant RSpec", 1, {}),
            (self.good.replace("Results: 10", "Results: 9"), "", 1, {"verified": True}),
            (self.good, "", None, {"verified": True}),
            (self.good, "", 1, {"verified": False}),
            (self.good, "Neutral failure", 1, {"verified": True}),
            (self.good.replace("Timeouts: 0", "Timeouts: 1"), "", 1, {"verified": True}),
        ):
            with self.subTest(stderr=stderr, code=code):
                r = parse_result(stdout, stderr, code, identity)
                self.assertFalse(r["valid"])
                self.assertIsNone(r["mutation_score"])


if __name__ == "__main__":
    unittest.main()
