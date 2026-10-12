"""Offline official XRepoTest generation, in the five published context modes; orchestration, not a baseline.

Upstream owns prompts, generation result semantics and code extraction. This
adapter sets the controlled model parameters, records API responses and keeps
terminal outcomes (including errors) when a Slurm job resumes.
"""
from __future__ import annotations

import argparse
from collections import Counter
import fcntl
import hashlib
import importlib.metadata
import inspect
import json
import os
from pathlib import Path, PurePosixPath
import sys
import tarfile
import time
from urllib.parse import urlparse

COMMIT = '39fb6ab3173136d3dac2d38ed7c98baf6c470270'
DATA = '811639c4291d3bd14ff58d8b2976bfffbf4df08cbf7d7aab22080c88165747dd'
MODEL_DIGEST = '096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47'
PARAMETERS = {'model': 'qwen3.6:35b', 'model_digest': MODEL_DIGEST,
              'thinking': 'on', 'temperature': 0.6, 'top_p': 0.95,
              'presence_penalty': 0.0, 'max_tokens': 16384,
              'request_timeout': 1800.0}
MODES = ('standard', 'lsp_context', 'file_context', 'rag_bm25', 'rag_dense')
ASSET = Path(__file__).parent / 'vendor/xrepotest-contexts-39fb6ab.tar.gz'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    with temp.open('w') as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write('\n')
        out.flush()
        os.fsync(out.fileno())
    temp.replace(path)


def append(path, value):
    with path.open('a') as out:
        out.write(json.dumps(value, ensure_ascii=False) + '\n')
        out.flush()
        os.fsync(out.fileno())


def assets(destination):
    descriptor = json.loads(ASSET.with_suffix('.json').read_text())
    if (descriptor['upstream_commit'] != COMMIT or descriptor['dataset'] != DATA
            or sha(ASSET) != descriptor['archive_sha256']):
        raise ValueError('Pinned official asset checksum failed')
    with tarfile.open(ASSET, 'r:gz') as archive:
        members = archive.getmembers()
        if len({m.name for m in members}) != len(members):
            raise ValueError('Duplicate archive members')
        if any(not m.isfile() or PurePosixPath(m.name).is_absolute()
               or '..' in PurePosixPath(m.name).parts for m in members):
            raise ValueError('Unsafe upstream archive')
        contents = {m.name: archive.extractfile(m).read() for m in members}
    manifest = json.loads(contents.pop('manifest.json'))
    actual = {n: hashlib.sha256(raw).hexdigest() for n, raw in contents.items()}
    if (actual != manifest['files'] or manifest['upstream_commit'] != COMMIT
            or manifest['modes'] != descriptor['modes']
            or set(descriptor['modes']) != set(MODES)
            or any(actual[info['path']] != info['prompts_sha256'] for info in descriptor['modes'].values())):
        raise ValueError('Official sources/prompts changed')
    expected = {**contents, 'manifest.json': (json.dumps(manifest, indent=2) + '\n').encode()}
    for name, raw in expected.items():
        path = destination / name
        if path.exists():
            if not path.is_file() or path.read_bytes() != raw:
                raise ValueError('Changed extracted asset: ' + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
    extra = {p.relative_to(destination).as_posix() for p in destination.rglob('*') if p.is_file()}
    if extra != set(expected):
        raise ValueError('Unexpected files in official source asset')
    return descriptor


def prepare(destination, dataset, reference, environment=None, mode='standard', context_length=32768):
    if context_length != 32768:
        raise ValueError('Official context must match the MARTA reference: 32768')
    if mode not in MODES:
        raise ValueError('Unknown official context mode')
    descriptor = assets(destination)
    if sha(dataset) != DATA:
        raise ValueError('Pinned Ruby dataset differs')
    info = descriptor['modes'][mode]
    rows = [json.loads(l) for l in (destination / info['path']).read_text().splitlines()]
    if (len(rows) != 675 or any(type(r['task_id']) is not int for r in rows)
            or {r['task_id'] for r in rows} != set(range(675))):
        raise ValueError('Official prompts must cover exactly 675 IDs')
    normal = json.loads((reference / 'experiment.json').read_text())
    if normal.get('dataset') != DATA or any(normal.get(k) != v for k, v in PARAMETERS.items()):
        raise ValueError('Parameters differ from the MARTA normal reference')
    if normal.get('runtime_env', {}).get('OLLAMA_CTX') != '32768':
        raise ValueError('MARTA reference context differs')
    if environment is not None and json.loads(environment.read_text()) != normal.get('environment'):
        raise ValueError('Ruby/evaluator environment differs from MARTA reference')
    sys.path.insert(0, str(destination / 'src'))
    from experiments.evaluation.generation.generate_responses import UnifiedProcessor
    from experiments.evaluation.preprocessing.preprocess_utils import preprocess_response_records
    for function, relative in ((UnifiedProcessor, 'experiments/evaluation/generation/generate_responses.py'),
                               (preprocess_response_records, 'experiments/evaluation/preprocessing/preprocess_utils.py')):
        if Path(inspect.getfile(function)).resolve() != (destination / 'src' / relative).resolve():
            raise ValueError('Generator imported outside the verified official source asset')
    versions = {name: importlib.metadata.version(name) for name in ('openai', 'httpx', 'pydantic')}
    report = {'ready': True, 'tasks': 675, 'mode': mode, 'prompt_source': info, 'asset': descriptor, 'parameters': PARAMETERS,
              'context_length': context_length, 'reference_context_length': 32768,
              'input_overflow_policy': 'unchanged-prompts-native-ollama-v0.30.7', 'reference_manifest_sha256': sha(reference / 'experiment.json'),
              'packages': versions, 'python': sys.version,
              'adapter_sha256': sha(Path(__file__)), 'environment': normal.get('environment')}
    return rows, report, UnifiedProcessor, preprocess_response_records


class RecordedAPI:
    def __init__(self, original, directory):
        self.original, self.directory = original, directory
        self.task_id = None
        self.calls = Counter()

    def __call__(self, *args, **kwargs):
        # Messages and official response handling remain untouched.
        kwargs.update(temperature=0.6, top_p=0.95, presence_penalty=0.0,
                      max_tokens=16384, timeout=1800.0,
                      extra_body={'reasoning_effort': 'high'})
        start = time.monotonic()
        self.calls[self.task_id] += 1
        event = {'task_id': self.task_id, 'sdk_call': self.calls[self.task_id],
                 'request': kwargs, 'started_unix': time.time(),
                 'slurm_job_id': os.getenv('SLURM_JOB_ID')}
        append(self.directory / 'api_requests.jsonl', event)
        try:
            response = self.original(*args, **kwargs)
            event['response'] = response.model_dump()
            return response
        except Exception as exc:
            event['exception'] = repr(exc)
            raise
        finally:
            event['seconds'] = time.monotonic() - start
            append(self.directory / 'api_calls.jsonl', event)


def generate_tasks(root, prompts, processor, recorded):
    for prompt in prompts:
        tid = prompt['task_id']
        path = root / 'tasks' / (str(tid) + '.json')
        state = json.loads(path.read_text()) if path.exists() else None
        if state and state.get('state') == 'complete':
            if state.get('task_id') != tid or state.get('prompt_sha256') != prompt_hash(prompt):
                raise ValueError('Checkpoint belongs to a different prompt')
            continue  # Terminal upstream errors count too; never try to improve them.
        if state:
            if state.get('state') != 'running' or state.get('prompt_sha256') != prompt_hash(prompt):
                raise ValueError('Unknown task checkpoint state')
            archive = root / 'interrupted_tasks' / str(tid)
            archive.mkdir(parents=True, exist_ok=True)
            path.rename(archive / (str(time.time_ns()) + '.json'))
        atomic(path, {'state': 'running', 'task_id': tid, 'prompt_sha256': prompt_hash(prompt)})
        recorded.task_id = tid
        row = processor.process_single_prompt(prompt, PARAMETERS['model'])
        if row.get('task_id') != tid:
            raise ValueError('Official processor returned a different task ID')
        atomic(path, {'state': 'complete', 'task_id': tid,
                      'prompt_sha256': prompt_hash(prompt), 'record': row})
        print('task {}: {}'.format(tid, row.get('status')), flush=True)
    return [json.loads((root / 'tasks' / (str(p['task_id']) + '.json')).read_text())['record']
            for p in prompts]


def prompt_hash(prompt):
    return hashlib.sha256(json.dumps(prompt, sort_keys=True).encode()).hexdigest()


def write_jsonl(path, rows):
    temp = path.with_name(path.name + '.tmp')
    with temp.open('w') as out:
        for row in rows:
            out.write(json.dumps(row, ensure_ascii=False) + '\n')
        out.flush()
        os.fsync(out.fileno())
    temp.replace(path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--backend', choices=('gpu', 'cpu'), default='gpu')
    p.add_argument('--cpu-proof', type=Path)
    p.add_argument('--mode', choices=MODES, required=True)
    p.add_argument('--context-length', type=int, choices=(32768,), default=32768)
    p.add_argument('--assets-dir', type=Path, required=True)
    p.add_argument('--dataset', type=Path, required=True)
    p.add_argument('--reference', type=Path, required=True)
    p.add_argument('--environment-manifest', type=Path, default=Path('/opt/xrepo/environment.json'))
    p.add_argument('--preflight-output', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--api-base')
    p.add_argument('--model-metadata', type=Path)
    a = p.parse_args()
    prompts, report, factory, preprocess = prepare(a.assets_dir, a.dataset, a.reference, a.environment_manifest, a.mode, a.context_length)
    report['execution_backend'] = a.backend
    if a.preflight_output:
        atomic(a.preflight_output, report)
    if a.output is None:
        print(json.dumps({k: report[k] for k in ('ready', 'mode', 'execution_backend', 'tasks', 'context_length', 'reference_context_length', 'prompt_source', 'packages')}, indent=2))
        return
    url = urlparse(a.api_base or '')
    if url.scheme != 'http' or url.hostname != '127.0.0.1' or url.path != '/v1':
        p.error('Only the private local Ollama /v1 endpoint is permitted')
    metadata = json.loads(a.model_metadata.read_text())
    if (metadata['model']['digest'] != MODEL_DIGEST or metadata['model']['name'] != PARAMETERS['model']
            or metadata['ollama']['version'] != '0.30.7'):
        raise ValueError('Model weights or Ollama version differ from MARTA')
    if a.backend == 'cpu':
        if not a.cpu_proof:
            raise ValueError('CPU execution requires a verified loaded CPU runner')
        proof = json.loads(a.cpu_proof.read_text())
        if (proof.get('backend') != 'cpu' or proof.get('model_digest') != MODEL_DIGEST
                or proof.get('context_length') != a.context_length or proof.get('size_vram') != 0
                or proof.get('host') != url.scheme + '://' + url.netloc
                or proof.get('ollama_version') != '0.30.7'
                or proof.get('slurm_job_id') != os.getenv('SLURM_JOB_ID')):
            raise ValueError('CPU proof differs from this job/model/context/server')
    if os.getenv('OLLAMA_CTX') != str(a.context_length):
        raise ValueError('Ollama context does not match the registered official context length')
    root = a.output.resolve()
    reference = a.reference.resolve()
    if root == reference or root in reference.parents or reference in root.parents:
        raise ValueError('Official generation and MARTA results must be separate')
    root.mkdir(parents=True, exist_ok=True)
    with (root / 'run.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        config = {'schema': 'official-xrepotest-context-mode-controlled-v2', **report,
                  'model_digest': MODEL_DIGEST, 'ollama_version': '0.30.7',
                  'execution_backend': a.backend,
                  'samples_per_task': 1, 'upstream_network_attempts': 3,
                  'checkpoint_policy': 'terminal-success-and-error-v1'}
        manifest = root / 'experiment.json'
        if manifest.exists():
            if json.loads(manifest.read_text()) != config:
                raise ValueError('Configuration changed: use a new run name')
        else:
            if set(x.name for x in root.iterdir()) != {'run.lock'}:
                raise ValueError('Refusing unregistered previous outputs')
            atomic(manifest, config)
        write_jsonl(root / 'prompts.jsonl', prompts)
        processor = factory(api_key='local-only', base_url=a.api_base, max_workers=1,
                            max_retries=3, retry_delay=1.0)
        recorded = RecordedAPI(processor.client.client.chat.completions.create, root)
        processor.client.client.chat.completions.create = recorded
        # Record actual SDK HTTP attempts too, including its automatic retries.
        http = processor.client.client._client
        def http_request(request):
            append(root / 'http_requests.jsonl', {'task_id': recorded.task_id,
                   'started_unix': time.time(), 'body': json.loads(request.content)})
        def http_response(response):
            response.read()
            append(root / 'http_responses.jsonl', {'task_id': recorded.task_id,
                   'finished_unix': time.time(), 'status_code': response.status_code,
                   'body': response.text})
        http.event_hooks['request'].append(http_request)
        http.event_hooks['response'].append(http_response)
        try:
            rows = generate_tasks(root, prompts, processor, recorded)
        finally:
            processor.client.client.close()
        write_jsonl(root / 'responses.jsonl', rows)
        processed = preprocess(rows)  # Official fences, fallback and error semantics.
        if len(processed) != 675 or {r['task_id'] for r in processed} != set(range(675)):
            raise ValueError('Official preprocessing changed the task denominator')
        write_jsonl(root / 'processed.jsonl', processed)
        atomic(root / 'complete.json', {'tasks': 675, 'processed_sha256': sha(root / 'processed.jsonl'),
                                      'upstream_status': dict(Counter(r['status'] for r in rows))})
        print('Official generation complete: ' + str(root / 'processed.jsonl'), flush=True)


if __name__ == '__main__':
    main()
