"""Build an offline asset from byte-identical pinned upstream sources and prompts.

Run only in the existing official-generation venv. Installs nothing.
"""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile

COMMIT = '39fb6ab3173136d3dac2d38ed7c98baf6c470270'
DATA = '811639c4291d3bd14ff58d8b2976bfffbf4df08cbf7d7aab22080c88165747dd'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--upstream', type=Path, required=True)
    p.add_argument('--upstream-archive', type=Path, required=True)
    p.add_argument('--dataset', type=Path, required=True)
    p.add_argument('--reference-prompts', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if hashlib.sha256(a.dataset.read_bytes()).hexdigest() != DATA:
        raise ValueError('Dataset differs from pinned Ruby release')
    files = {}
    # Read the pinned GitHub commit archive, not unverified working files.
    prefix = 'XRepoTest-' + COMMIT + '/'
    with tarfile.open(a.upstream_archive, 'r:gz') as archive:
        for member in archive.getmembers():
            if member.isdir() and member.name.rstrip('/') == prefix.rstrip('/'):
                continue
            if not member.name.startswith(prefix):
                raise ValueError('Archive does not belong to the pinned commit')
            name = member.name[len(prefix):]
            if member.isfile() and ((name.startswith('src/') and name.endswith('.py')) or name == 'LICENSE'):
                raw = archive.extractfile(member).read()
                if (a.upstream / name).read_bytes() != raw:
                    raise ValueError('Modified upstream source: ' + name)
                files[name] = raw
    sys.path.insert(0, str(a.upstream / 'src'))
    from experiments.evaluation.generation.generate_prompts import PromptCreator, SYSTEM_PROMPTS
    rows = PromptCreator('ruby', {'file': str(a.dataset)}, split='ruby',
                         system_prompt=SYSTEM_PROMPTS['ruby']).create_prompts()
    # Exact serialization used by upstream PromptCreator.save_prompts.
    prompts = ''.join(json.dumps({'task_id': r['task_id'], 'system_prompt': r.get('system_prompt', ''),
                                 'prompt': r['prompt']}) + '\n' for r in rows).encode()
    if len(rows) != 675 or {r['task_id'] for r in rows} != set(range(675)):
        raise ValueError('Expected all 675 official tasks')
    if prompts != a.reference_prompts.read_bytes():
        raise ValueError('Official prompts differ from local 8B experiment')
    files['prompts.jsonl'] = prompts
    manifest = {'upstream_commit': COMMIT, 'dataset': DATA, 'mode': 'standard', 'tasks': 675,
                'files': {n: hashlib.sha256(raw).hexdigest() for n, raw in sorted(files.items())},
                'upstream_archive_sha256': hashlib.sha256(a.upstream_archive.read_bytes()).hexdigest(),
                'provenance': 'Pinned GitHub commit archive; PromptCreator standard; byte-identical to local Qwen3-8B prompts'}
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
    descriptor = {**{k: manifest[k] for k in ('upstream_commit', 'dataset', 'mode', 'tasks')},
                  'archive_sha256': hashlib.sha256(a.output.read_bytes()).hexdigest(),
                  'prompts_sha256': manifest['files']['prompts.jsonl']}
    a.output.with_suffix('.json').write_text(json.dumps(descriptor, indent=2) + '\n')
    print(json.dumps(descriptor, indent=2))


if __name__ == '__main__':
    main()
