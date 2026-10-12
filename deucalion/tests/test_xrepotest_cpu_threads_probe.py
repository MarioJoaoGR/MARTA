import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from deucalion import xrepotest_cpu_threads_probe as probe


class CPUThreadsProbeTests(unittest.TestCase):
    def request(self):
        return {**{k: probe.PARAMETERS[k] for k in ("model", "temperature", "top_p", "presence_penalty", "max_tokens")},
                "messages": [{"role": "system", "content": "original system"},
                             {"role": "user", "content": "original focal task"}],
                "timeout": 1800.0, "extra_body": {"reasoning_effort": "high"}}

    def test_original_messages_and_sampling_preserved_only_runtime_threads_change(self):
        original = self.request()
        before = copy.deepcopy(original)
        for count in (8, 16, 32):
            body = probe.payload(original, count)
            self.assertEqual(body["messages"], original["messages"])
            self.assertEqual(body["think"], "high")
            self.assertEqual(body["options"]["num_predict"], 16384)
            self.assertEqual(body["options"]["num_ctx"], 32768)
            self.assertEqual(body["options"]["num_gpu"], 0)
            self.assertEqual(body["options"]["num_thread"], count)
            for key in ("temperature", "top_p", "presence_penalty"):
                self.assertEqual(body["options"][key], original[key])
        self.assertEqual(original, before)
        with self.assertRaises(ValueError):
            probe.payload(original, 128)

    def test_recovery_read_only_and_rejects_other_configurations(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "api_requests.jsonl"
            original = self.request()
            path.write_text(json.dumps({"task_id": 0, "request": original}) + "\n")
            raw = path.read_bytes()
            self.assertEqual(probe.recover(path), original)
            self.assertEqual(path.read_bytes(), raw)
            for key, value in (("model", "other"), ("max_tokens", 128), ("timeout", 60),
                               ("extra_body", {"reasoning_effort": "none"})):
                changed = dict(original, **{key: value})
                path.write_text(json.dumps({"task_id": 0, "request": changed}) + "\n")
                with self.assertRaises(ValueError):
                    probe.recover(path)

    def test_diagnostic_runs_all_thread_counts_without_touching_original_checkpoints(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "api_requests.jsonl"
            source.write_text(json.dumps({"task_id": 0, "request": self.request()}) + "\n")
            checkpoint = root / "state.json"
            checkpoint.write_text('{"state":"complete","record":{"status":"error"}}')
            original = {p.name: p.read_bytes() for p in (source, checkpoint)}
            log = root / "ollama.log"
            log.write_text("")
            current, bodies = [], []
            def query(host, path, body=None):
                model = {"name": probe.PARAMETERS["model"], "digest": probe.MODEL_DIGEST,
                         "size_vram": 0, "context_length": 32768}
                if path == "/api/version":
                    return {"version": "0.30.7"}
                if path in ("/api/tags", "/api/ps"):
                    return {"models": [model]}
                current.append(body["options"]["num_thread"])
                log.write_text(log.read_text() + "system_info: n_threads = {} (n_threads_batch = {}) / 128\n".format(current[-1], current[-1]))
                return {"done_reason": "load"}
            def curl(command, input, stdout, stderr, timeout):
                self.assertIn("--max-time", command)
                self.assertIn("180", command)
                self.assertNotIn("--retry", command)
                body = json.loads(input)
                bodies.append(body)
                stdout.write(json.dumps({"message": {"thinking": "partial thinking"}}) + "\n")
                log.write_text(log.read_text() + "slot print_timing: n_decoded = 50, tg = 2.50 t/s\n")
                return probe.subprocess.CompletedProcess(command, 28)
            output = root / "diagnostic"
            with patch.object(probe, "query", side_effect=query), patch.object(probe.subprocess, "run", side_effect=curl), patch.object(probe.time, "sleep"):
                probe.run("http://127.0.0.1:25000", source, output, log)
            report = json.loads((output / "report.json").read_text())
            self.assertTrue(report["diagnostic_only"])
            self.assertFalse(report["included_in_benchmark"])
            self.assertEqual(current, [8, 16, 32])
            self.assertEqual([b["options"]["num_thread"] for b in bodies], current)
            self.assertTrue(all(b["messages"] == self.request()["messages"] for b in bodies))
            self.assertTrue(all(c["runner_reported_tokens_per_second"] == [2.5] for c in report["cases"]))
            self.assertTrue(all(not c["stream"]["done"] for c in report["cases"]))
            self.assertEqual(original, {p.name: p.read_bytes() for p in (source, checkpoint)})
            self.assertFalse((output / "processed.jsonl").exists())
            with self.assertRaises(ValueError):
                probe.run("http://127.0.0.1:25000", source, output, log)

    def test_partial_stream_never_invents_token_rate_from_chunks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "stream.jsonl"
            path.write_text(json.dumps({"message": {"thinking": "reasoning", "content": "answer"}}) + "\n{" )
            result = probe.stream_summary(path)
            self.assertFalse(result["done"])
            self.assertEqual(result["thinking_characters"], 9)
            self.assertEqual(result["answer_characters"], 6)
            self.assertNotIn("tokens_per_second", result)
            path.write_text(path.read_text().splitlines()[0] + "\n" + json.dumps({"done": True,
                            "eval_count": 40, "eval_duration": 2000000000, "done_reason": "stop"}))
            self.assertEqual(probe.stream_summary(path)["tokens_per_second"], 20)


if __name__ == "__main__":
    unittest.main()
