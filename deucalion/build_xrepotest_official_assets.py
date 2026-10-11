"""Build all five official Ruby prompt modes, offline in the existing venv."""
import argparse
from collections import Counter
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import tarfile
import tempfile

COMMIT = '39fb6ab3173136d3dac2d38ed7c98baf6c470270'
REVISION = 'cd694c00d20951aef189a406abac980a6b1c49d4'
DATA = '811639c4291d3bd14ff58d8b2976bfffbf4df08cbf7d7aab22080c88165747dd'
CONTEXTS = {
    'ruby_functions_enriched.jsonl': ('lsp', '9f6b9aaab20196758fbf435b3fc189c1d63f32f551306f5caf339901d8bbba04'),
    'ruby_functions_ws50_ss10_k20_enriched_bm25.jsonl': ('rag', 'a65da6a8c6a8c88f36cbf814b6319be3fdb832a4956ee7f33a5c451d380d90c0'),
    'ruby_functions_ws50_ss10_k20_enriched_unixcoder.jsonl': ('rag', '6e047a122f912e5be7e599b9ed2abc65440b2e0fb213b6ca50b284e693407c36'),
}
MODES = ('standard', 'lsp_context', 'file_context', 'rag_bm25', 'rag_dense')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--upstream', type=Path, required=True)
    p.add_argument('--upstream-archive', type=Path, required=True)
    p.add_argument('--dataset', type=Path, required=True)
    p.add_argument('--contexts-dir', type=Path, required=True)
    p.add_argument('--reference-prompts', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    base = a.dataset.read_bytes()
    if hashlib.sha256(base).hexdigest() != DATA:
        raise ValueError('Dataset differs from pinned Ruby release')
    base_rows = {r['task_id']: r for r in map(json.loads, base.splitlines())}
    files = {}
    prefix = 'XRepoTest-' + COMMIT + '/'
    with tarfile.open(a.upstream_archive, 'r:gz') as archive:
        for member in archive.getmembers():
            if member.isdir() and member.name.rstrip('/') == prefix.rstrip('/'):
                continue
            if not member.name.startswith(prefix):
                raise ValueError('Archive does not belong to the pinned commit')
            name = member.name[len(prefix):]
            if member.isfile() and ((name.startswith('src/') and name.endswith('.py')) or name in {'LICENSE', 'pyproject.toml'}):
                raw = archive.extractfile(member).read()
                if (a.upstream / name).read_bytes() != raw:
                    raise ValueError('Modified upstream source: ' + name)
                files[name] = raw
    source_data = {'data/base/ruby_functions.jsonl': DATA}
    context_bytes = {}
    for name, (group, expected) in CONTEXTS.items():
        raw = (a.contexts_dir / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError('Changed published context file: ' + name)
        rows = [json.loads(l) for l in raw.splitlines()]
        if len(rows) != 675 or {r['task_id'] for r in rows} != set(range(675)):
            raise ValueError('Published contexts must cover exactly the same 675 tasks')
        for row in rows:
            original = base_rows[row['task_id']]
            for key in ('function_name', 'file_path', 'file_content', 'focal_code', 'metadata', 'language'):
                if row.get(key) != original.get(key):
                    raise ValueError('Changed official focal task: ' + name + ':' + str(row['task_id']) + ':' + key)
            for key in ('start_line', 'end_line', 'name'):
                if row['function_component'].get(key) != original['function_component'].get(key):
                    raise ValueError('Changed focal method boundaries')
        context_bytes['data/enriched/' + group + '/' + name] = raw
        source_data['data/' + group + '/' + name] = expected
    mode_manifest = {}
    standard_rows = None
    # Run the unchanged upstream constructor against its canonical file layout.
    with tempfile.TemporaryDirectory(prefix='xrepo-official-build-') as temp:
        stage = Path(temp)
        for name, raw in {**files, **context_bytes,
                          'src/xrepotest/environments/xrepotest/ruby_functions.jsonl': base}.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        sys.path.insert(0, str(stage / 'src'))
        from experiments.evaluation.generation.generate_prompts import PromptCreator, SYSTEM_PROMPTS
        from experiments.evaluation.generation.prompts.constants import datapath, lsp_datapath, bm_25_rag_datapath, dense_rag_datapath
        paths = {'standard': datapath['ruby'], 'file_context': datapath['ruby'],
                 'lsp_context': lsp_datapath['ruby'], 'rag_bm25': bm_25_rag_datapath['ruby'],
                 'rag_dense': dense_rag_datapath['ruby']}
        for mode in MODES:
            rows = PromptCreator('ruby', paths[mode], split='ruby', system_prompt=SYSTEM_PROMPTS['ruby'],
                                 lsp_context=mode == 'lsp_context', file_context=mode == 'file_context',
                                 is_rag=mode.startswith('rag_'), top_k=10 if mode.startswith('rag_') else None).create_prompts()
            minimal = [{'task_id': r['task_id'], 'system_prompt': r.get('system_prompt', ''), 'prompt': r['prompt']} for r in rows]
            if len(minimal) != 675 or {r['task_id'] for r in minimal} != set(range(675)):
                raise ValueError('Mode lost/duplicated tasks: ' + mode)
            raw = ''.join(json.dumps(r) + '\n' for r in minimal).encode()
            if mode == 'standard':
                if raw != a.reference_prompts.read_bytes():
                    raise ValueError('Standard prompts differ from local 8B experiment')
                standard_rows = {r['task_id']: r for r in minimal}
            for r in minimal:
                reference = standard_rows[r['task_id']]
                if r['system_prompt'] != reference['system_prompt'] or not r['prompt'].endswith(reference['prompt']):
                    raise ValueError('Mode changed the standard focal task')
                if mode.startswith('rag_') and len(re.findall(r'^Example \d+:', r['prompt'], re.M)) > 10:
                    raise ValueError('More than the paper top-10 contexts')
            relative = 'prompts/' + mode + '.jsonl'
            files[relative] = raw
            mode_manifest[mode] = {'path': relative, 'tasks': 675,
                'prompts_sha256': hashlib.sha256(raw).hexdigest(),
                'changed_from_standard': sum(r['prompt'] != standard_rows[r['task_id']]['prompt'] for r in minimal),
                'max_prompt_bytes': max(len(r['prompt'].encode()) for r in minimal),
                'retrieval': {'window_lines': 50, 'stride_lines': 10, 'available_k': 20, 'used_k': 10}
                             if mode.startswith('rag_') else None}
    manifest = {'upstream_commit': COMMIT, 'dataset': DATA, 'tasks': 675, 'modes': mode_manifest,
                'source_data': {'hf_revision': REVISION, 'files': source_data},
                'files': {n: hashlib.sha256(raw).hexdigest() for n, raw in sorted(files.items())},
                'upstream_archive_sha256': hashlib.sha256(a.upstream_archive.read_bytes()).hexdigest(),
                'provenance': 'Pinned GitHub/HF files; unchanged PromptCreator; standard identical to local Qwen3-8B'}
    files['manifest.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode='w') as archive:
        for name, raw in sorted(files.items()):
            info = tarfile.TarInfo(name)
            info.size, info.mode, info.mtime = len(raw), 0o644, 0
            archive.addfile(info, io.BytesIO(raw))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open('wb') as out:
        with gzip.GzipFile(fileobj=out, mode='wb', filename='', mtime=0) as zipped:
            zipped.write(buffer.getvalue())
    descriptor = {k: manifest[k] for k in ('upstream_commit', 'dataset', 'tasks', 'modes', 'source_data')}
    descriptor['archive_sha256'] = hashlib.sha256(a.output.read_bytes()).hexdigest()
    a.output.with_suffix('.json').write_text(json.dumps(descriptor, indent=2) + '\n')
    print(json.dumps(descriptor, indent=2))


if __name__ == '__main__':
    main()
