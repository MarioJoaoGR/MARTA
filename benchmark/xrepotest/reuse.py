"""Read compatible registered analysis without copying benchmark answers."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

from .protocol import atomic_json, digest


def _hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _copy(source, target):
    before = _hash(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_name(target.name + '.reuse-partial')
    shutil.copy2(source, partial)
    if _hash(partial) != before or _hash(source) != before:
        partial.unlink()
        raise ValueError('Reference changed while copying analysis')
    partial.replace(target)
    return before


class ReferenceEmbeddings:
    """Reuse exact document texts; compute only embeddings absent from storage."""
    def __init__(self, vectors, recorder, query_cache, embed_model):
        self.vectors, self.recorder = vectors, recorder
        self.query_cache = query_cache
        self.key = digest(['bge-masked-mean-v1', embed_model])
        self.queries = {}
        if query_cache.is_file():
            data = json.loads(query_cache.read_text())
            if data.get('key') != self.key:
                raise ValueError('Query embedding cache changed')
            self.queries = data['queries']

    def documents(self, texts):
        missing = list(dict.fromkeys(t for t in texts if t not in self.vectors))
        if missing:
            from marta.embedding import embedder
            results = embedder.embed_documents(missing)
            if len(results) != len(missing):
                raise ValueError('Embedder returned an incorrect document count')
            self.vectors.update(zip(missing, results))
        self.recorder.evento(tipo='embedding_reference', documents=len(texts),
                             computed=len(missing), reused=len(texts)-len(missing))
        return [self.vectors[t] for t in texts]

    def query(self, text):
        if text not in self.queries:
            from marta.embedding import embedder
            self.queries[text] = list(map(float, embedder.embed_query(text)))
            atomic_json(self.query_cache, {'key': self.key, 'queries': self.queries})
            reused = False
        else:
            reused = True
        self.recorder.evento(tipo='embedding_query_cache', reused=reused)
        return self.queries[text]


def prepare_analysis_reuse(project, reference, *, enrich):
    """Caller must first verify the experiment reference with its manifest.

    Whole enriched bundles are copied only to graph-enabled arms. For graph
    removal, only identical document embeddings are read from the reference;
    its enriched analysis is never applied. Original files are never opened
    through ChromaDB (which can write): extraction uses a disposable copy.
    """
    import numpy as np
    from marta.ruby_backend import cache

    model = os.getenv('MODEL', 'default')
    embed_model = os.getenv('TRANSFORMER_PATH', 'default')
    src_hash = cache.compute_source_hash(project.files)
    fingerprint = project._analysis_fingerprint(project.analysis_targets)
    path = Path(project._analysis_path(model, True, root_dir=str(reference)))
    bundle = project._load_analysis_bundle(str(path), src_hash, model, fingerprint, True)
    audit = {'source': str(reference), 'analysis_bundle': None, 'vectors_copied': {}, 'vector_reference_hashes': {},
             'registered_document_vectors': 0,
             'note': 'Only production analysis is reused; no tests or task states are copied.'}
    vectors = {}
    if bundle is not None:
        audit['source_bundle_sha256'] = _hash(path)
        destination = Path(project._analysis_path(model, True))
        if enrich and not destination.exists():
            audit['analysis_bundle'] = _copy(path, destination)
        # These are exactly the inputs used by the frozen normal build_rag key.
        docs = [(t.analysis_id, (bundle['targets'].get(t.analysis_id, {}).get('summary')
                 or bundle['targets'].get(t.analysis_id, {}).get('done_what') or ''))
                for t in project.analysis_targets]
        text_hash = hashlib.sha256(json.dumps(
            [docs, sorted(bundle['classes'].items())], ensure_ascii=True).encode()).hexdigest()
        key = cache.vectors_key(src_hash + ':' + fingerprint + ':' + text_hash, model, embed_model)
        source_vectors = Path(cache.vectors_path(str(reference))) / 'full_context'
        target_vectors = Path(cache.vectors_path(project.out_root())) / 'full_context'
        if source_vectors.is_dir():
            files = sorted(p for p in source_vectors.rglob('*') if p.is_file())
            if any(p.is_symlink() for p in source_vectors.rglob('*')):
                raise ValueError('Symlinks in reference vector store are not allowed')
            audit['vector_reference_hashes'] = {str(p.relative_to(source_vectors)): _hash(p) for p in files}
            # Copy intact stores to unchanged-context arms, preserving HNSW too.
            # Existing destination stores are validated by the ordinary RAG code.
            if enrich and not target_vectors.exists():
                for p in files:
                    rel = p.relative_to(source_vectors)
                    audit['vectors_copied'][str(rel)] = _copy(p, target_vectors / rel)
            class_file = source_vectors / 'classes.npz'
            if class_file.is_file() and not project.ablation_options.no_type_hints:
                with np.load(class_file, allow_pickle=False) as data:
                    classes = list(bundle['classes'].items())
                    ids = [f'{i}|{name}' for i, (name, _) in enumerate(classes)]
                    matrix = data['vectors']
                    if (str(data['key']) == key and list(data['ids']) == ids
                            and matrix.ndim == 2 and len(matrix) == len(classes)
                            and np.isfinite(matrix).all()):
                        vectors.update((text, vector.tolist())
                                       for (_, text), vector in zip(classes, matrix))
            if not project.ablation_options.no_method_retrieval and (source_vectors/'chroma.sqlite3').is_file():
                # Never instantiate PersistentClient against the original store.
                with tempfile.TemporaryDirectory(prefix='marta-reference-vectors-') as tmp:
                    for p in files:
                        _copy(p, Path(tmp) / p.relative_to(source_vectors))
                    import chromadb
                    client = chromadb.PersistentClient(path=tmp)
                    try:
                        collection = client.get_collection('functions', embedding_function=None)
                        expected = {f'{i}|{identity}': text
                                    for i, (identity, text) in enumerate((d for d in docs if d[1]))}
                        if (collection.metadata or {}).get('key') == key:
                            data = collection.get(include=['embeddings'])
                            matrix = np.asarray(data['embeddings'])
                            if (set(data['ids']) == set(expected) and matrix.ndim == 2
                                    and len(matrix) == len(expected) and np.isfinite(matrix).all()):
                                vectors.update((expected[identity], vector.tolist())
                                               for identity, vector in zip(data['ids'], matrix))
                    finally:
                        # Pinned Chroma 0.5.23 has no public close API. Stop the
                        # disposable client's workers before deleting its files.
                        client._system.stop()
        audit['registered_document_vectors'] = len(vectors)
    # The audit is per project because some normal projects may have no bundle yet.
    atomic_json(Path(project.out_root()) / 'reference_artifacts.json', audit)
    return ReferenceEmbeddings(vectors, project._recorder(),
                               Path(project.out_root()) / 'embedding_queries.json', embed_model)


def prepare_graph_reuse(files, reference, destination):
    """Reuse the recorded static graph; its use in summaries remains optional."""
    from marta.ruby_backend import cache
    from marta.ruby_backend.call_graph import RESOLVER_VERSION
    source = Path(cache.call_graph_path(str(reference)))
    target = Path(cache.call_graph_path(str(destination)))
    key = cache.compute_source_hash(files) + f':r{RESOLVER_VERSION}'
    if cache.load_call_graph(str(source), key) is None:
        return
    if not target.exists():
        identity = _copy(source, target)
        atomic_json(Path(destination)/'graph_reuse.json',
                    {'source':str(source), 'sha256':identity, 'key':key})
