"""Mutant parsing and opt-in integration with an already installed runtime."""
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

from marta.ruby_backend.mutation import execute, parse_result, run_mutation


class ResultTests(unittest.TestCase):
    good = "Mutations: 10\nResults: 10\nKills: 8\nAlive: 2\nTimeouts: 0\n"

    def test_survivors_exit_one_is_valid(self):
        self.assertEqual(parse_result(self.good, "", 1, {"verified": True, "mutations": 10})["mutation_score"], 0.8)

    def test_invalid_is_not_zero(self):
        for out, err, code, identity in (
            (self.good, "", None, {"verified": True, "mutations": 10}),
            (self.good, "Neutral failure", 1, {"verified": True, "mutations": 10}),
            (self.good.replace("Results: 10", "Results: 9"), "", 1, {"verified": True, "mutations": 10}),
            (self.good.replace("Timeouts: 0", "Timeouts: 1"), "", 1, {"verified": True, "mutations": 10}),
            (self.good, "", 1, {"verified": True, "mutations": 9}),
            (self.good, "", 1, {"verified": False}), ("", "missing gem", 1, {})):
            with self.subTest(code=code, err=err):
                result = parse_result(out, err, code, identity)
                self.assertFalse(result["valid"])
                self.assertIsNone(result["mutation_score"])

    def test_timeout_preserves_output(self):
        out, _, code = execute([sys.executable, "-c", "import time; print('ready',flush=True); time.sleep(30)"], Path.cwd(), 0.2)
        self.assertIn("ready", out)
        self.assertIsNone(code)


@unittest.skipUnless(os.getenv("MARTA_TEST_MUTANT") == "1", "requires preinstalled Mutant container")
class RuntimeIntegrationTests(unittest.TestCase):
    def case(self, assertion, *, wrong_identity=False, operator=False):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / "lib").mkdir()
        (root / "spec").mkdir()
        name = "[](x)" if operator else "self.double(x)"
        (root / "lib/box.rb").write_text("class Box\n  def " + name + "\n    x * 2\n  end\nend\n")
        (root / "spec/human_spec.rb").write_text("raise 'HUMAN SPEC MUST NOT LOAD'\n")
        (root / ".rspec").write_text("--require ./spec/human_spec.rb\n")
        (root / ".mutant.yml").write_text("invalid: ignored local mutation options\n")
        suite = root / "provided_spec.rb"
        suite.write_text('require "box"\nRSpec.describe Box do\n it("provided") { ' + assertion + ' }\nend\n')
        identity = {"subject": "Box#[]" if operator else "Box.double", "file": "lib/box.rb",
                    "start_line": 2, "end_line": 5 if wrong_identity else 4}
        return run_mutation(identity, suite, root, root / "audit", load_paths=[str(root / "lib")],
                            usage="opensource", timeout=90), root

    def test_positive_and_negative_controls_exclude_human_specs(self):
        positive, _ = self.case("expect(Box.double(2)).to eq(4)")
        negative, _ = self.case("expect(true).to eq(true)")
        for value in (positive, negative):
            self.assertTrue(value["valid"], value)
            self.assertTrue(value["identity"]["verified"])
            self.assertEqual(len(value["identity"]["examples"]), 1)
        self.assertEqual(positive["counts"]["mutations"], negative["counts"]["mutations"])
        self.assertGreater(positive["mutation_score"], negative["mutation_score"])

    def test_wrong_focal_range_is_unavailable(self):
        result, _ = self.case("expect(Box.double(2)).to eq(4)", wrong_identity=True)
        self.assertFalse(result["valid"])
        self.assertFalse(result["identity"]["verified"])
        self.assertIsNone(result["mutation_score"])

    def test_failing_baseline_never_runs_mutations(self):
        result, root = self.case("expect(Box.double(2)).to eq(999)")
        self.assertFalse(result["valid"])
        self.assertIn("baseline", result["reason"])
        self.assertFalse((root / "audit/stdout.txt").exists())

    def test_operator_subject_has_exact_identity(self):
        result, _ = self.case("expect(Box.new[2]).to eq(4)", operator=True)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["identity"]["subjects"][0]["subject"], "Box#[]")
