import copy
import unittest
from deucalion import verify_ollama_cpu as gate


class CPUProofTests(unittest.TestCase):
    def payloads(self):
        model = {"name": gate.PARAMETERS["model"], "digest": gate.MODEL_DIGEST,
                 "context_length": 32768, "size_vram": 0}
        return {"/api/version": {"version": "0.30.7"}, "/api/tags": {"models": [model]},
                "/api/generate": {"done_reason": "load", "done": True}, "/api/ps": {"models": [model]}}

    def test_load_only_verifies_real_runner_fields_without_generating_tokens(self):
        data, calls = self.payloads(), []
        def query(path, payload=None):
            calls.append((path, payload))
            return data[path]
        proof = gate.verify("http://127.0.0.1:25000", gate.PARAMETERS["model"], 32768, query)
        self.assertEqual(proof["backend"], "cpu")
        self.assertEqual(proof["size_vram"], 0)
        self.assertEqual(calls[2][1]["prompt"], "")
        self.assertEqual(calls[2][1]["options"], {"num_ctx": 32768})

    def test_rejects_gpu_wrong_weights_context_version_or_generated_load(self):
        for field, value in (("size_vram", 1), ("digest", "other"), ("context_length", 4096)):
            data = self.payloads()
            data["/api/ps"] = copy.deepcopy(data["/api/ps"])
            data["/api/ps"]["models"][0][field] = value
            with self.assertRaises(ValueError):
                gate.verify("http://127.0.0.1:25000", gate.PARAMETERS["model"], 32768,
                            lambda path, payload=None: data[path])
        for path, replacement in (("/api/version", {"version": "0.30.8"}),
                                  ("/api/generate", {"done_reason": "stop", "response": "answer"})):
            data = self.payloads()
            data[path] = replacement
            with self.assertRaises(ValueError):
                gate.verify("http://127.0.0.1:25000", gate.PARAMETERS["model"], 32768,
                            lambda path, payload=None: data[path])


if __name__ == "__main__":
    unittest.main()
