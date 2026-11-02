"""Real Chroma/NumPy artifact reuse with fixed vectors and no live model."""
import asyncio
import json
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
from unittest.mock import Mock

import pytest

from benchmark.xrepotest.protocol import atomic_json
from benchmark.xrepotest.reuse import ReferenceEmbeddings, prepare_analysis_reuse
from marta.ruby_backend import cache
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.tests.test_generate import _make_project


def vector(text):
    return [float(len(text)), float(text.count('a')+1)]


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}


@pytest.fixture
def reference(tmp_path, monkeypatch):
    monkeypatch.setenv('MODEL', 'reuse:test')
    monkeypatch.setenv('TRANSFORMER_PATH', 'fake-embedding')
    root = _make_project(tmp_path)
    source = tmp_path / 'normal'
    project = RubyProject(str(root), 'src', output_root=str(source)).discover()
    for t in project.analysis_targets:
        t.done_what = 'first summary ' + t.method.qualified_name
        t.what_todo = 'local intent'
        t.summary = 'normal combined ' + t.method.qualified_name
    project.class_summaries = {'Calculator': 'calculator adds numbers'}
    entries = {t.analysis_id: {'summary':t.summary, 'done_what':t.done_what,
               'what_todo':t.what_todo, 'judge':'', 'done_what_passagem1':t.done_what}
               for t in project.analysis_targets}
    atomic_json(Path(project._analysis_path('reuse:test', True)),
        {'source_hash':cache.compute_source_hash(project.files), 'model':'reuse:test',
         'fingerprint':project._analysis_fingerprint(project.analysis_targets), 'enrich':True,
         'targets':entries, 'classes':project.class_summaries})
    project.build_rag(embed_documents=lambda docs: [vector(t) for t in docs], embed_query=vector)
    # Model a completed reference whose storage is no longer being written.
    project.rag_db._client()._system.stop()
    (source / 'tasks/99').mkdir(parents=True)
    (source / 'tasks/99/state.json').write_text('{"status":"complete"}')
    (source / 'tasks/99/final_spec.rb').write_text('NEVER COPY BENCHMARK ANSWERS')
    return root, source, project


@pytest.mark.parametrize('options', [AblationOptions(), AblationOptions(no_type_hints=True),
                                     AblationOptions(no_method_retrieval=True)])
def test_unchanged_context_reuses_bundle_and_vectors_without_inference(reference, tmp_path, monkeypatch, options):
    root, source, old = reference
    before = snapshot(source)
    target = RubyProject(str(root), 'src', output_root=str(tmp_path/'new'),
                         ablation_options=options).discover()
    bank = prepare_analysis_reuse(target, source, enrich=True)
    async def fail(*args):
        raise AssertionError('Registered summaries must not be regenerated')
    asyncio.run(target.analyze_summaries(ask=fail))
    def fail_docs(docs):
        raise AssertionError('Registered document vectors must not be recomputed')
    monkeypatch.setitem(sys.modules, 'marta.embedding', SimpleNamespace(
        embedder=SimpleNamespace(embed_documents=fail_docs, embed_query=vector)))
    target.build_rag(embed_documents=bank.documents, embed_query=bank.query)
    assert [t.summary for t in target.analysis_targets] == [t.summary for t in old.analysis_targets]
    if not options.no_method_retrieval:
        assert target.rag_db.reused
        assert target.rag_db.query(target.analysis_targets[0].summary)
    if not options.no_type_hints:
        assert target.class_db.reused
    assert snapshot(source) == before
    assert not (tmp_path/'new/tasks').exists()
    audit = json.loads((tmp_path/'new/reference_artifacts.json').read_text())
    assert audit['analysis_bundle'] and audit['vectors_copied']


def test_graph_removal_never_loads_enriched_bundle_and_reuses_only_unchanged_texts(reference, tmp_path, monkeypatch):
    root, source, old = reference
    before = snapshot(source)
    target = RubyProject(str(root), 'src', output_root=str(tmp_path/'no_graph')).discover()
    bank = prepare_analysis_reuse(target, source, enrich=False)
    assert not Path(target._analysis_path('reuse:test', True)).exists()
    assert not Path(target._analysis_path('reuse:test', False)).exists()
    assert all(not t.summary for t in target.analysis_targets)
    # A summary changed by removing graph enrichment has to get a new vector.
    calls = []
    def compute(docs):
        calls.append(docs)
        return [vector(t) for t in docs]
    monkeypatch.setitem(sys.modules, 'marta.embedding', SimpleNamespace(
        embedder=SimpleNamespace(embed_documents=compute, embed_query=vector)))
    common = old.class_summaries['Calculator']
    changed = 'source-only summary after graph removal'
    assert bank.documents([common, changed]) == [vector(common), vector(changed)]
    assert calls == [[changed]]
    assert bank.documents([common, changed]) == [vector(common), vector(changed)]
    assert calls == [[changed]]
    assert snapshot(source) == before


def test_query_embeddings_are_persisted_for_later_resumes(tmp_path, monkeypatch):
    producer = Mock(return_value=[1.0,2.0])
    monkeypatch.setitem(sys.modules, 'marta.embedding', SimpleNamespace(
        embedder=SimpleNamespace(embed_query=producer)))
    path = tmp_path/'queries.json'
    bank = ReferenceEmbeddings({}, SimpleNamespace(evento=Mock()), path, 'same-embedder')
    assert bank.query('same request') == [1.0,2.0]
    assert bank.query('same request') == [1.0,2.0]
    assert producer.call_count == 1
    after = ReferenceEmbeddings({}, SimpleNamespace(evento=Mock()), path, 'same-embedder')
    assert after.query('same request') == [1.0,2.0]
    assert producer.call_count == 1
    with pytest.raises(ValueError):
        ReferenceEmbeddings({}, SimpleNamespace(evento=Mock()), path, 'another-embedder')


def test_missing_reference_is_audited_without_copying_answers(tmp_path):
    project = SimpleNamespace(files=[], analysis_targets=[],
        _analysis_fingerprint=lambda targets: 'same',
        _analysis_path=lambda model,enrich,root_dir=None: str(Path(root_dir or tmp_path/'new')/'missing.json'),
        _load_analysis_bundle=lambda *args:None, out_root=lambda:str(tmp_path/'new'),
        _recorder=lambda:SimpleNamespace(evento=Mock()))
    bank = prepare_analysis_reuse(project, tmp_path/'reference', enrich=True)
    assert bank.vectors == {}
    audit = json.loads((tmp_path/'new/reference_artifacts.json').read_text())
    assert audit['analysis_bundle'] is None and audit['registered_document_vectors'] == 0


def test_wrong_vector_identity_is_not_reused(reference, tmp_path, monkeypatch):
    import numpy as np
    root, source, old = reference
    path = Path(cache.vectors_path(str(source))) / "full_context/classes.npz"
    with np.load(path, allow_pickle=False) as data:
        ids, vectors = data["ids"].copy(), data["vectors"].copy()
    np.savez(path, ids=ids, vectors=vectors, key="unrelated-embedder-key")
    target = RubyProject(str(root), "src", output_root=str(tmp_path/"new"),
                         ablation_options=AblationOptions(no_method_retrieval=True)).discover()
    bank = prepare_analysis_reuse(target, source, enrich=False)
    calls = []
    def compute(texts):
        calls.append(texts)
        return [vector(t) for t in texts]
    monkeypatch.setitem(sys.modules, "marta.embedding", SimpleNamespace(
        embedder=SimpleNamespace(embed_documents=compute)))
    text = old.class_summaries["Calculator"]
    assert bank.documents([text]) == [vector(text)]
    assert calls == [[text]]


def test_registered_graph_is_not_built_again_for_the_same_sources(reference, tmp_path, monkeypatch):
    from benchmark.xrepotest.reuse import prepare_graph_reuse
    root, source, old = reference
    output = tmp_path / "new_graph"
    prepare_graph_reuse(old.files, source, output)
    fresh = RubyProject(str(root), "src", output_root=str(output))
    monkeypatch.setattr(fresh.backend, "build_call_graph", Mock(side_effect=AssertionError("no graph rebuild")))
    fresh.discover()
    assert fresh.call_graph.to_json() == old.call_graph.to_json()
    fresh.backend.build_call_graph.assert_not_called()


def test_registered_graph_is_not_copied_for_changed_sources(reference, tmp_path):
    from benchmark.xrepotest.reuse import prepare_graph_reuse
    root, source, old = reference
    path = root / "src/calculator.rb"
    path.write_text(path.read_text()+"\n# different source\n")
    output = tmp_path / "other_graph"
    prepare_graph_reuse(old.files, source, output)
    assert not Path(cache.call_graph_path(str(output))).exists()
