import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from deucalion import xrepotest_cpu_request_probe as probe


class CPURequestProbeTests(unittest.TestCase):
    def sources(self, root):
        sdk = {"model": probe.PARAMETERS["model"], "temperature": 0.6, "top_p": 0.95,
               "presence_penalty": 0.0, "max_tokens": 16384, "timeout": 1800.0,
               "messages": [{"role": "system", "content": "original system"}, {"role": "user", "content": "original task"}],
               "extra_body": {"reasoning_effort": "high"}}
        body = {k: v for k, v in sdk.items() if k not in ("timeout", "extra_body")}
        body.update(sdk["extra_body"])
        paths = root / "http_requests.jsonl", root / "api_requests.jsonl"
        paths[0].write_text(json.dumps({"task_id": 0, "body": body}) + "\n")
        paths[1].write_text(json.dumps({"task_id": 0, "request": sdk}) + "\n")
        return paths, body

    def test_exact_original_http_request_one_attempt_and_no_benchmark_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths, body = self.sources(root)
            checkpoint = root / "state.json"
            checkpoint.write_text('{"state":"complete","record":{"status":"error"}}')
            before = {p.name: p.read_bytes() for p in (*paths, checkpoint)}
            log = root / "runner.log"
            log.write_text("system_info: n_threads = 8 (n_threads_batch = 8) / 128\n")
            calls = []
            def curl(command, input, stdout, stderr, timeout):
                calls.append(copy.deepcopy(json.loads(input)))
                self.assertEqual(json.loads(input), body)
                self.assertNotIn("--retry", command)
                self.assertEqual(command[command.index("--max-time") + 1], "1800")
                self.assertTrue(command[-1].endswith("/v1/chat/completions"))
                response = {"choices": [{"finish_reason": "stop", "message": {"content": "test code", "reasoning": "thinking"}}],
                            "usage": {"prompt_tokens": 100, "completion_tokens": 1000}}
                Path(command[command.index("--output") + 1]).write_text(json.dumps(response))
                return subprocess.CompletedProcess(command, 0, stdout=b"200")
            output = root / "diagnostic"
            with patch.object(probe, "verify", return_value={"cpu_threads": 8, "size_vram": 0}), patch.object(probe.subprocess, "run", side_effect=curl):
                probe.run("http://127.0.0.1:25000", *paths, output, log)
            report = json.loads((output / "report.json").read_text())
            self.assertEqual(len(calls), 1)
            self.assertTrue(report["usable_response"])
            self.assertFalse(report["included_in_benchmark"])
            self.assertEqual(report["confirmed_cpu_threads_after_request"], 8)
            self.assertEqual(before, {p.name: p.read_bytes() for p in (*paths, checkpoint)})
            self.assertFalse((output / "processed.jsonl").exists())
            with self.assertRaises(ValueError):
                probe.run("http://127.0.0.1:25000", *paths, output, log)

    def test_modified_http_body_is_rejected_before_inference(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths, body = self.sources(Path(tmp))
            body["max_tokens"] = 128
            paths[0].write_text(json.dumps({"task_id": 0, "body": body}) + "\n")
            with self.assertRaisesRegex(ValueError, "differ"):
                probe.original_body(*paths)


if __name__ == "__main__":
    unittest.main()
