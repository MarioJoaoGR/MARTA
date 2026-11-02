"""Frozen-suite identity, cohort routing, terminal recovery and denominators."""
import copy
from contextlib import ExitStack, nullcontext, redirect_stdout
import io
import sys
import types
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from benchmark.xrepotest.protocol import DATA_SHA256
from deucalion.xrepotest_mutation_evaluate import (
    ARMS, LABELS, MODES, certificate, classify, fresh_row, inputs, load_core,
    recover_measurement, main)
from deucalion.xrepotest_mutation_support import POLICY, sha
from deucalion.xrepotest_paper_metrics import summarize


class MutationEvaluationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def row(self, tid=1, passed=True):
        return {"task_id": tid, "file_path": "example/lib/a.rb", "test": ["generated code"],
                "checks": [{"compilation": True, "tests": passed, "invocation": True, "mutation": True}],
                "coverage_stats": [{"covered_lines": 1, "total_lines": 2}],
                "mutation_scores": [{"killed_count": 999, "total_count": 999}]}

    def measurement(self):
        return {"policy": POLICY, "task_id": 1, "action": "run", "valid": True,
                "mutation_score": 0.5, "counts": {"kills": 2, "mutations": 4, "alive": 2, "timeouts": 0},
                "support_sha256": "support", "bootstrap_sha256": "bootstrap"}

    def test_all_eleven_cohorts_route_without_mixing_contexts(self):
        self.assertEqual(len(LABELS), 11)
        for label in LABELS:
            run, processed, core, selection = inputs(self.root, label)
            self.assertTrue(str(run).startswith(str(self.root)))
            self.assertNotIn("mutation_v1", str(core))
            self.assertEqual(selection is not None, label in ARMS)
            if label in MODES:
                self.assertIn("modes/" + label + "/", str(processed))
            if label == "no_graph":
                self.assertIn("project_parallel/merged/processed.jsonl", str(processed))

    def test_new_measurement_replaces_old_mutation_without_touching_core(self):
        old = self.row()
        original = copy.deepcopy(old)
        row = fresh_row(old, "valid", self.measurement())
        self.assertEqual(old, original)
        self.assertEqual(row["mutation_scores"][0]["killed_count"], 2)
        for key in ("test", "coverage_stats", "file_path", "task_id"):
            self.assertEqual(row[key], old[key])

    def test_unavailable_is_distinct_from_zero_and_keeps_global_denominator(self):
        a = fresh_row(self.row(), "valid", self.measurement())
        b = fresh_row(self.row(2), "unavailable", reason="no_mutant_subject")
        c = fresh_row({"task_id": 3, "test": [], "checks": []}, "no_tests")
        self.assertEqual(b["mutation_scores"], [])
        self.assertFalse(b["checks"][0]["mutation"])
        result = summarize([a, b, c])["mutation"]
        self.assertEqual(result["passing_tasks"], 2)
        self.assertEqual(result["valid_measurements"], 1)
        self.assertAlmostEqual(result["MS_pct"], 100 / 6)
        self.assertEqual(result["MS_at_Pass_pct"], 50)

    def test_failed_core_does_not_retain_old_mutation_score(self):
        result = fresh_row(self.row(passed=False), "core_failed")
        self.assertEqual(result["mutation_scores"], [])
        self.assertFalse(result["checks"][0]["tests"])

    def test_runtime_subject_failure_has_explicit_unavailable_reason(self):
        self.assertEqual(classify({"valid": False, "exit_code": 1,
                                  "identity": {"subjects": [], "verified": False}}),
                         ("unavailable", "no_mutant_subject"))
        self.assertEqual(classify({"exit_code": None})[1], "process_timeout")

    def test_finished_measurement_is_recovered_without_repeating_it(self):
        folder = self.root / "measurement"
        folder.mkdir()
        data = self.measurement()
        (folder / "result.json").write_text(json.dumps(data))
        self.assertEqual(recover_measurement(folder, "support", "bootstrap", 1), data)
        with self.assertRaisesRegex(ValueError, "provenance"):
            recover_measurement(folder, "other", "bootstrap", 1)

    def test_core_identity_and_response_hash_are_required(self):
        folder = self.root / "core"
        (folder / "tasks").mkdir(parents=True)
        processed = self.root / "processed.jsonl"
        processed.write_text("frozen export")
        manifest = {"dataset": DATA_SHA256, "responses": sha(processed),
                    "evaluator_files": {"ruby": "hash"}, "environment": {"image": "fixed"}}
        (folder / "experiment.json").write_text(json.dumps(manifest))
        (folder / "summary.json").write_text(json.dumps({"total_samples": 1}))
        row = self.row()
        (folder / "tasks/1.json").write_text(json.dumps(row))
        task = {"task_id": 1, "file_path": row["file_path"]}
        result, hashes = load_core(folder, [task], {1: row["test"]}, processed,
                                  manifest["evaluator_files"], manifest["environment"])
        self.assertEqual(result[1], row)
        self.assertIn("1", hashes)
        with self.assertRaisesRegex(ValueError, "suite changed"):
            load_core(folder, [task], {1: ["different suite"]}, processed,
                      manifest["evaluator_files"], manifest["environment"])
        processed.write_text("modified export")
        with self.assertRaisesRegex(ValueError, "does not match"):
            load_core(folder, [task], {1: row["test"]}, processed,
                      manifest["evaluator_files"], manifest["environment"])

    def test_extra_core_task_refused(self):
        folder = self.root / "core"
        (folder / "tasks").mkdir(parents=True)
        processed = self.root / "processed.jsonl"
        processed.write_text("export")
        (folder / "experiment.json").write_text(json.dumps({"dataset": DATA_SHA256,
            "responses": sha(processed), "evaluator_files": {}, "environment": {}}))
        (folder / "summary.json").write_text(json.dumps({"total_samples": 1}))
        (folder / "tasks/999.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "IDs"):
            load_core(folder, [{"task_id": 1}], {}, processed, {}, {})

    def test_pipeline_preserves_core_and_recovers_completed_task_without_new_execution(self):
        # This unit harness mocks the certificate and Mutant execution. It never
        # creates a fake validation certificate or any benchmark measurements.
        run, processed, core, unused = inputs(self.root, "standard")
        processed.parent.mkdir(parents=True)
        (core / "tasks").mkdir(parents=True)
        source = self.root / "repos/example/lib/a.rb"
        source.parent.mkdir(parents=True)
        source.write_text("immutable source")
        tasks = [{"task_id": i, "file_path": "example/lib/a.rb", "file_content": "immutable source",
                  "function_name": "value"} for i in (0, 1)]
        responses = [{"task_id": 0, "response": ["generated code"]}, {"task_id": 1, "response": []}]
        processed.write_text("".join(json.dumps(r) + "\n" for r in responses))
        a = self.row(0)
        b = {"task_id": 1, "file_path": "example/lib/a.rb", "test": [], "checks": []}
        for row in (a, b):
            (core / "tasks" / (str(row["task_id"]) + ".json")).write_text(json.dumps(row))
        environment = {"fixture": True}
        (core / "experiment.json").write_text(json.dumps({"dataset": DATA_SHA256,
            "responses": sha(processed), "environment": environment, "evaluator_files": {}}))
        (core / "summary.json").write_text(json.dumps({"total_samples": 2}))
        before = {str(p): p.read_bytes() for p in core.rglob("*") if p.is_file()}
        before[str(processed)] = processed.read_bytes()
        from deucalion import xrepotest_mutation_evaluate as module, xrepotest_mutation_support as support
        def create(focal, name, code):
            path = Path(focal).parents[1] / "spec/temp_spec.rb"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(code)
            return str(path)
        def measure(task, suite, repo, folder):
            folder.mkdir(parents=True)
            result = self.measurement()
            result.update(task_id=0, support_sha256=sha(support.__file__),
                          bootstrap_sha256=sha(Path(module.__file__).parent / "rb/xrepotest_mutation_bootstrap.rb"))
            (folder / "result.json").write_text(json.dumps(result))
            return result
        ruby_stub = types.ModuleType("ruby")
        ruby_stub.__path__ = []
        stub = types.ModuleType("ruby.test_utils")
        stub.create_ruby_file = create
        argv = ["mutation", "--root", str(self.root), "--cohort", "standard",
                "--repos", str(self.root / "repos"), "--validation", "unused-in-unit-harness"]
        with ExitStack() as stack:
            for name, value in (("load_tasks", tasks), ("evaluator_hashes", {}),
                                ("environment_manifest", environment), ("certificate", "fixture-hash"),
                                ("validate_evaluator", None)):
                stack.enter_context(patch.object(module, name, return_value=value))
            stack.enter_context(patch.object(module, "project_environment", side_effect=lambda *a: nullcontext()))
            fake = stack.enter_context(patch.object(module, "run_mutant", side_effect=measure))
            stack.enter_context(patch.dict(sys.modules, {"ruby": ruby_stub, "ruby.test_utils": stub}))
            stack.enter_context(patch.object(sys, "argv", argv))
            stack.enter_context(redirect_stdout(io.StringIO()))
            main()
            self.assertEqual(fake.call_count, 1)
            out = run / "mutation_v1"
            summary = (out / "summary.json").read_bytes()
            # Simulate interruption after the completed measurement was saved,
            # but before its task checkpoint could be published.
            (out / "tasks/0.json").unlink()
            main()
            self.assertEqual(fake.call_count, 1)
            self.assertEqual((out / "summary.json").read_bytes(), summary)
            self.assertTrue((out / "complete.json").exists())
        self.assertEqual({str(p): p.read_bytes() for p in core.rglob("*") if p.is_file()},
                         {k: v for k, v in before.items() if k != str(processed)})
        self.assertEqual(processed.read_bytes(), before[str(processed)])

    def test_matching_control_and_real_suite_certificate_is_accepted(self):
        from deucalion import xrepotest_mutation_support as support, xrepotest_mutation_evaluate as module
        names = ("capybara", "dotenv", "grape", "hanami", "hashie", "httparty", "pundit", "rom", "rspec-core", "shoryuken")
        control = {"passed": True,
                   "positive": {"valid": True, "identity": {"verified": True}, "counts": {"mutations": 12}, "mutation_score": 1.0},
                   "negative": {"valid": True, "identity": {"verified": True}, "counts": {"mutations": 12}, "mutation_score": 1 / 12}}
        d = {"policy": POLICY, "diagnostic_only": True, "included_in_benchmark": False,
             "dataset_sha256": DATA_SHA256, "environment": {"fixture": True}, "evaluator_files": {"file": "hash"},
             "support_sha256": sha(support.__file__),
             "bootstrap_sha256": sha(Path(module.__file__).parent / "rb/xrepotest_mutation_bootstrap.rb"),
             "controls": {name: copy.deepcopy(control) for name in names}, "controls_passed": True,
             "real_suites": {str(tid): {"valid": True} for tid in (4, 155, 220, 416)}}
        p = self.root / "unit-certificate.json"
        p.write_text(json.dumps(d))
        self.assertEqual(certificate(p, d["evaluator_files"], d["environment"]), sha(p))
        d["controls"]["hashie"]["negative"]["mutation_score"] = 1.0
        p.write_text(json.dumps(d))
        with self.assertRaisesRegex(ValueError, "control proof"):
            certificate(p, d["evaluator_files"], d["environment"])

    def test_old_or_partial_diagnostic_certificate_refused(self):
        p = self.root / "report.json"
        p.write_text(json.dumps({"policy": POLICY, "controls_passed": True}))
        with self.assertRaisesRegex(ValueError, "certificate"):
            certificate(p, {}, {})


if __name__ == "__main__":
    unittest.main()
