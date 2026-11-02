"""Exercise the actual pinned upstream processor with a mock API, no inference."""
import importlib.metadata
import contextlib
import io
import os
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from deucalion import xrepotest_official_generate as adapter


class OfficialGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.asset_temp = tempfile.TemporaryDirectory()
        cls.assets = Path(cls.asset_temp.name) / 'assets'
        adapter.assets(cls.assets)
        sys.path.insert(0, str(cls.assets / 'src'))
        from experiments.evaluation.generation.generate_responses import UnifiedProcessor
        from experiments.evaluation.preprocessing.preprocess_utils import preprocess_response_records
        cls.factory = UnifiedProcessor
        cls.preprocess = staticmethod(preprocess_response_records)

    @classmethod
    def tearDownClass(cls):
        cls.asset_temp.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def processor(self, replies):
        import httpx
        from openai import OpenAI
        requests = []
        def reply(request):
            requests.append(json.loads(request.content))
            answer = replies[len(requests) - 1]
            return httpx.Response(200, json={'id': 'mock', 'object': 'chat.completion',
                'created': 0, 'model': 'qwen3.6:35b', 'choices': [{'index': 0,
                'finish_reason': answer.get('finish_reason', 'stop'), 'message': {
                'role': 'assistant', 'content': answer.get('content'), 'reasoning': 'separate thoughts'}}],
                'usage': {'prompt_tokens': 10, 'completion_tokens': 80, 'total_tokens': 90}})
        processor = self.factory(api_key='mock', base_url='http://127.0.0.1:11434/v1', max_workers=1)
        processor.client.client.close()
        processor.client.client = OpenAI(api_key='mock', base_url='http://127.0.0.1:11434/v1',
             http_client=httpx.Client(transport=httpx.MockTransport(reply)))
        self.addCleanup(processor.client.client.close)
        recorded = adapter.RecordedAPI(processor.client.client.chat.completions.create, self.root)
        processor.client.client.chat.completions.create = recorded
        return processor, recorded, requests

    def test_all_pinned_prompts_and_license_are_present_and_tampering_fails(self):
        dest = self.root / 'assets'
        info = adapter.assets(dest)
        for mode in adapter.MODES:
            source = info['modes'][mode]
            rows = [json.loads(l) for l in (dest / source['path']).read_text().splitlines()]
            self.assertEqual(len(rows), 675)
            self.assertEqual({r['task_id'] for r in rows}, set(range(675)))
            self.assertEqual(adapter.sha(dest / source['path']), source['prompts_sha256'])
        self.assertIn('MIT License', (dest / 'LICENSE').read_text())
        (dest / 'src/xrepotest/config.py').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'Changed extracted'):
            adapter.assets(dest)

    def test_contexts_preserve_focal_task_and_published_retrieval_policy(self):
        import re
        descriptor = adapter.assets(self.assets)
        modes = {mode: {row['task_id']: row for row in map(json.loads,
                 (self.assets / info['path']).read_text().splitlines())}
                 for mode, info in descriptor['modes'].items()}
        for mode, rows in modes.items():
            changed = 0
            for tid, row in rows.items():
                base = modes['standard'][tid]
                self.assertEqual(row['system_prompt'], base['system_prompt'])
                self.assertTrue(row['prompt'].endswith(base['prompt']))
                changed += row['prompt'] != base['prompt']
                if mode.startswith('rag_'):
                    self.assertLessEqual(len(re.findall(r'^Example \d+:', row['prompt'], re.M)), 10)
            self.assertEqual(changed, descriptor['modes'][mode]['changed_from_standard'])
        self.assertEqual(descriptor['modes']['lsp_context']['changed_from_standard'], 170)
        for mode in ('rag_bm25', 'rag_dense'):
            self.assertEqual(descriptor['modes'][mode]['retrieval']['used_k'], 10)
            self.assertEqual(descriptor['modes'][mode]['retrieval']['window_lines'], 50)
        with self.assertRaisesRegex(ValueError, 'Official context must match'):
            adapter.prepare(self.assets, self.root / 'unused', self.root / 'unused', context_length=65536)
        with self.assertRaisesRegex(ValueError, 'Unknown official context mode'):
            adapter.prepare(self.assets, self.root / 'unused', self.root / 'unused', mode='combined')

    def test_sampler_override_preserves_official_messages_and_records_separate_reasoning(self):
        processor, recorded, requests = self.processor([{'content': '```ruby\nRSpec.describe {}\n```'}])
        prompt = {'task_id': 7, 'system_prompt': 'exact official system', 'prompt': 'exact official user'}
        rows = adapter.generate_tasks(self.root, [prompt], processor, recorded)
        self.assertEqual(rows[0]['status'], 'success')
        self.assertEqual(requests[0]['messages'], [{'role': 'system', 'content': 'exact official system'},
                                               {'role': 'user', 'content': 'exact official user'}])
        self.assertEqual(requests[0]['reasoning_effort'], 'high')
        self.assertEqual(requests[0]['max_tokens'], 16384)
        self.assertEqual(requests[0]['temperature'], 0.6)
        self.assertEqual(requests[0]['top_p'], 0.95)
        self.assertEqual(requests[0]['presence_penalty'], 0)
        self.assertEqual(self.preprocess(rows)[0]['response'], ['RSpec.describe {}\n'])
        event = json.loads((self.root / 'api_calls.jsonl').read_text())
        self.assertEqual(event['response']['choices'][0]['message']['reasoning'], 'separate thoughts')
        self.assertNotIn('separate thoughts', rows[0]['response'])

    def test_empty_length_is_terminal_and_never_retried_on_resume(self):
        processor, recorded, requests = self.processor([{'content': '', 'finish_reason': 'length'}])
        prompt = {'task_id': 8, 'system_prompt': 'system', 'prompt': 'user'}
        rows = adapter.generate_tasks(self.root, [prompt], processor, recorded)
        self.assertEqual(rows[0]['status'], 'error')
        self.assertEqual(len(requests), 1)
        resumed = adapter.generate_tasks(self.root, [prompt], processor, recorded)
        self.assertEqual(resumed, rows)
        self.assertEqual(len(requests), 1)
        self.assertEqual(self.preprocess(rows)[0]['response'], [rows[0]['response']])

    def test_interruption_is_archived_and_completed_other_tasks_are_preserved(self):
        prompts = [{'task_id': i, 'system_prompt': 'system', 'prompt': str(i)} for i in range(2)]
        processor, recorded, _ = self.processor([{'content': 'raw first'}, {'content': 'raw second'}])
        rows = adapter.generate_tasks(self.root, prompts[:1], processor, recorded)
        before = (self.root / 'tasks/0.json').read_bytes()
        adapter.atomic(self.root / 'tasks/1.json', {'state': 'running', 'task_id': 1,
                                                'prompt_sha256': adapter.prompt_hash(prompts[1])})
        both = adapter.generate_tasks(self.root, prompts, processor, recorded)
        self.assertEqual((self.root / 'tasks/0.json').read_bytes(), before)
        self.assertEqual(both[0], rows[0])
        self.assertEqual(len(list((self.root / 'interrupted_tasks/1').glob('*.json'))), 1)
        changed = dict(prompts[0], prompt='different')
        with self.assertRaisesRegex(ValueError, 'different prompt'):
            adapter.generate_tasks(self.root, [changed], processor, recorded)

    def test_transport_retries_follow_upstream_and_remain_logged(self):
        processor, recorded, _ = self.processor([])
        calls = []
        def fail(*args, **kwargs):
            calls.append(kwargs)
            raise RuntimeError('connection temporarily unavailable')
        recorded.original = fail
        processor.client.retry_delay = 0
        rows = adapter.generate_tasks(self.root, [{'task_id': 0, 'prompt': 'p', 'system_prompt': 's'}], processor, recorded)
        self.assertEqual(rows[0]['status'], 'error')
        self.assertEqual(len(calls), 3)
        events = [json.loads(l) for l in (self.root / 'api_calls.jsonl').read_text().splitlines()]
        self.assertEqual(len(events), 3)
        self.assertTrue(all('exception' in e for e in events))

    def test_reference_with_different_budget_is_rejected_before_import_or_calls(self):
        reference = self.root / 'reference'
        reference.mkdir()
        adapter.atomic(reference / 'experiment.json', {'dataset': adapter.DATA,
                       **adapter.PARAMETERS, 'max_tokens': 4096, 'runtime_env': {'OLLAMA_CTX': '32768'}})
        dataset = self.root / 'dataset'
        dataset.write_text('placeholder')
        real_sha = adapter.sha
        with patch.object(adapter, 'sha', side_effect=lambda p: adapter.DATA if p == dataset else real_sha(p)):
            with self.assertRaisesRegex(ValueError, 'Parameters differ'):
                adapter.prepare(self.assets, dataset, reference)

    def test_preprocessing_keeps_uncoded_responses_as_official_failures(self):
        rows = [{'task_id': 0, 'response': 'not ruby', 'prompt': 'unused', 'status': 'success'},
                {'task_id': 1, 'response': '```ruby\na\n```\n```ruby\nb\n```', 'status': 'success'}]
        processed = self.preprocess(rows)
        self.assertEqual(processed[0]['response'], ['not ruby'])
        self.assertEqual(processed[1]['response'], ['a\n\n\nb\n'])
        self.assertNotIn('prompt', processed[0])


    def test_full_675_export_http_logging_and_resume_with_real_sdk(self):
        dataset = Path('/Users/mario/.cache/marta-xrepotest/local-runs/qwen3_8b_standard_no_thinking_20261004/ruby_functions.jsonl')
        if not dataset.is_file():
            self.skipTest('Pinned local Ruby dataset not available')
        import httpx
        from openai import OpenAI
        import experiments.evaluation.llm.openai_client as upstream
        reference = self.root / 'reference'
        reference.mkdir()
        adapter.atomic(reference / 'experiment.json', {'dataset': adapter.DATA,
                       **adapter.PARAMETERS, 'runtime_env': {'OLLAMA_CTX': '32768'}})
        metadata = self.root / 'metadata.json'
        adapter.atomic(metadata, {'model': {'name': 'qwen3.6:35b', 'digest': adapter.MODEL_DIGEST},
                                 'ollama': {'version': '0.30.7'}})
        calls = []
        def respond(request):
            calls.append(json.loads(request.content))
            content = '' if len(calls) == 2 else '```ruby\nRSpec.describe {}\n```'
            return httpx.Response(200, json={'id': 'mock', 'object': 'chat.completion', 'created': 0,
                'model': 'qwen3.6:35b', 'choices': [{'index': 0, 'finish_reason': 'length' if not content else 'stop',
                'message': {'role': 'assistant', 'content': content, 'reasoning': 'thoughts'}}],
                'usage': {'prompt_tokens': 10, 'completion_tokens': 80, 'total_tokens': 90}})
        def factory(**kwargs):
            return OpenAI(api_key='mock', base_url=kwargs['base_url'],
                          http_client=httpx.Client(transport=httpx.MockTransport(respond)))
        generation = self.root / 'official-generation'
        environment = self.root / 'environment.json'
        adapter.atomic(environment, None)
        args = ['adapter', '--mode', 'standard', '--environment-manifest', str(environment), '--assets-dir', str(self.assets), '--dataset', str(dataset),
                '--reference', str(reference), '--output', str(generation),
                '--api-base', 'http://127.0.0.1:11434/v1', '--model-metadata', str(metadata)]
        with patch.dict(os.environ, {'OLLAMA_CTX': '32768'}), patch.object(sys, 'argv', args), \
             patch.object(upstream, 'OpenAI', factory), contextlib.redirect_stdout(io.StringIO()):
            adapter.main()
            before = (generation / 'processed.jsonl').read_bytes()
            adapter.main()
        self.assertEqual(len(calls), 675)
        self.assertEqual((generation / 'processed.jsonl').read_bytes(), before)
        rows = [json.loads(l) for l in before.splitlines()]
        self.assertEqual(len(rows), 675)
        self.assertEqual({r['task_id'] for r in rows}, set(range(675)))
        self.assertEqual(sum(r['status'] == 'error' for r in rows), 1)
        self.assertEqual(len((generation / 'http_requests.jsonl').read_text().splitlines()), 675)
        self.assertEqual(len((generation / 'http_responses.jsonl').read_text().splitlines()), 675)
        self.assertEqual(len((generation / 'api_calls.jsonl').read_text().splitlines()), 675)
        self.assertFalse((reference / 'tasks').exists())
        args[2] = 'lsp_context'
        with patch.dict(os.environ, {'OLLAMA_CTX': '32768'}), patch.object(sys, 'argv', args), \
             contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, 'Configuration changed'):
                adapter.main()
        self.assertEqual(len(calls), 675)
        args.extend(['--context-length', '32768'])
        for mode in adapter.MODES:
            args[2] = mode
            output = self.root / ('full-mode-' + mode)
            args[args.index('--output') + 1] = str(output)
            with patch.dict(os.environ, {'OLLAMA_CTX': '32768'}), patch.object(sys, 'argv', args), \
                 patch.object(upstream, 'OpenAI', factory), contextlib.redirect_stdout(io.StringIO()):
                adapter.main()
                adapter.main()
            report = json.loads((output / 'experiment.json').read_text())
            self.assertEqual(report['mode'], mode)
            self.assertEqual(report['context_length'], 32768)
            self.assertEqual(report['reference_context_length'], 32768)
            self.assertEqual(json.loads((output / 'complete.json').read_text())['tasks'], 675)
        self.assertEqual(len(calls), 675 * 6)  # original standard plus all five independent modes

        args[2] = 'standard'
        output = self.root / 'cpu-standard'
        args[args.index('--output') + 1] = str(output)
        proof_path = self.root / 'cpu-proof.json'
        proof = {'backend': 'cpu', 'model_digest': adapter.MODEL_DIGEST, 'size_vram': 0,
                 'context_length': 32768, 'ollama_version': '0.30.7',
                 'cpu_threads': 8, 'thread_control': 'LLAMA_ARG_THREADS',
                 'host': 'http://127.0.0.1:11434', 'slurm_job_id': os.getenv('SLURM_JOB_ID')}
        adapter.atomic(proof_path, proof)
        args.extend(['--backend', 'cpu', '--cpu-proof', str(proof_path)])
        with patch.dict(os.environ, {'OLLAMA_CTX': '32768'}), patch.object(sys, 'argv', args), \
             patch.object(upstream, 'OpenAI', factory), contextlib.redirect_stdout(io.StringIO()):
            adapter.main()
            adapter.main()
        self.assertEqual(len(calls), 675 * 7)
        self.assertEqual(calls[0], calls[675 * 6])  # sampler and messages identical across CPU/GPU
        cpu_manifest = json.loads((output / 'experiment.json').read_text())
        self.assertEqual(cpu_manifest['execution_backend'], 'cpu')
        self.assertEqual(cpu_manifest['cpu_runtime'], {'threads': 8, 'thread_control': 'LLAMA_ARG_THREADS'})
        for field, value in (('size_vram', 1), ('cpu_threads', 128), ('thread_control', 'unverified')):
            adapter.atomic(proof_path, {**proof, field: value})
            with patch.dict(os.environ, {'OLLAMA_CTX': '32768'}), patch.object(sys, 'argv', args):
                with self.assertRaisesRegex(ValueError, 'CPU proof differs'):
                    adapter.main()
        self.assertEqual(len(calls), 675 * 7)

if __name__ == '__main__':
    print('SDK under test:', importlib.metadata.version('openai'))
    unittest.main()
