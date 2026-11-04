"""Static Planner reuse with live repair retrieval; no model/server calls."""
import asyncio
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import project, rag
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.recorder import RubyRecorder
from marta.ruby_backend.tests.test_generate import GOOD_SPEC, BROKEN_SPEC, PLAN_RESPONSE
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


def target(identity="definition-a", query="add sum"):
    return SimpleNamespace(analysis_id=identity, summary=query, done_what="plain",
                           method=SimpleNamespace(qualified_name="Calculator#add"))


def database(revision="snapshot-1"):
    return SimpleNamespace(retrieval_revision=revision,
                           related_lines=Mock(return_value=["Calculator#sub: difference"]),
                           query=Mock(return_value=[]))


def context(tmp_path, db=None):
    obj = project.RubyProject(str(tmp_path), "src", rag_db=db or database())
    return obj, target()


def test_static_query_is_reused_without_exposing_saved_list_to_mutation(tmp_path):
    obj, t = context(tmp_path)
    first = obj._related_for(t)
    first.clear()
    assert obj._related_for(t) == ["Calculator#sub: difference"]
    obj.rag_db.related_lines.assert_called_once_with("add sum", k=3, exclude="definition-a")
    assert obj.rag_db.related_lines.return_value == ["Calculator#sub: difference"]


def test_changed_query_replaces_previous_entry_for_definition(tmp_path):
    obj, t = context(tmp_path)
    for query in ("add sum", "changed purpose", "add sum"):
        t.summary = query
        obj._related_for(t)
    assert [call.args[0] for call in obj.rag_db.related_lines.call_args_list] == [
        "add sum", "changed purpose", "add sum"]


def test_definition_identity_is_part_of_lookup_even_when_name_and_query_match(tmp_path):
    obj, t = context(tmp_path)
    other = target("definition-b")
    assert t.method.qualified_name == other.method.qualified_name
    obj._related_for(t)
    obj._related_for(other)
    obj._related_for(t)
    assert [call.kwargs["exclude"] for call in obj.rag_db.related_lines.call_args_list] == [
        "definition-a", "definition-b"]


def test_equivalent_task_selectors_share_production_definition_query(tmp_path):
    obj, t = context(tmp_path)
    t.task_id = 1
    second = target(t.analysis_id)
    second.task_id = 2
    assert obj._related_for(t) == obj._related_for(second)
    assert obj.rag_db.related_lines.call_count == 1


@pytest.mark.parametrize("change", ["revision", "replacement"])
def test_changed_index_invalidates_old_formatted_context(tmp_path, change):
    obj, t = context(tmp_path)
    obj._related_for(t)
    if change == "revision":
        obj.rag_db.retrieval_revision = "snapshot-2"
        obj.rag_db.related_lines.return_value = ["new result"]
    else:
        # Same revision string on another object is still another index.
        obj.rag_db = database()
        obj.rag_db.related_lines.return_value = ["new result"]
    assert obj._related_for(t) == ["new result"]
    assert obj._related_for(t) == ["new result"]
    assert obj.rag_db.related_lines.call_count == (2 if change == "revision" else 1)


@pytest.mark.parametrize("revision", [None, "", 1, Mock()])
def test_unversioned_custom_index_remains_supported_without_memoization(tmp_path, revision):
    obj, t = context(tmp_path, database(revision))
    obj._related_for(t)
    obj.rag_db.related_lines.return_value = ["live result"]
    assert obj._related_for(t) == ["live result"]
    assert obj.rag_db.related_lines.call_count == 2


def test_empty_or_failed_queries_are_not_cached(tmp_path):
    obj, t = context(tmp_path)
    obj.rag_db.related_lines.side_effect = [[], ConnectionError("temporary"), ["recovered"]]
    assert obj._related_for(t) is None
    with pytest.raises(ConnectionError):
        obj._related_for(t)
    assert obj._related_for(t) == ["recovered"]
    assert obj._related_for(t) == ["recovered"]
    assert obj.rag_db.related_lines.call_count == 3


def test_disabled_retrieval_or_missing_index_cannot_serve_old_context(tmp_path):
    obj, t = context(tmp_path)
    original = obj.rag_db
    obj._related_for(t)
    obj.ablation_options = AblationOptions(no_method_retrieval=True)
    assert obj._related_for(t) is None and obj._error_help_fn(t) is None
    assert original.related_lines.call_count == 1
    obj.ablation_options = AblationOptions()
    obj._related_for(t)
    assert original.related_lines.call_count == 2
    obj.rag_db = None
    assert obj._related_for(t) is None
    obj.rag_db = original
    obj._related_for(t)
    assert original.related_lines.call_count == 3


def test_empty_target_query_does_not_embed_or_query(tmp_path):
    obj, t = context(tmp_path)
    t.summary = t.done_what = ""
    assert obj._related_for(t) is None
    obj.rag_db.related_lines.assert_not_called()


def test_cache_hits_are_separate_telemetry_not_llm_usage(tmp_path):
    obj, t = context(tmp_path)
    obj.recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    obj._related_for(t)
    obj._related_for(t)
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    lookups = [e for e in events if e["tipo"] == "planner_retrieval"]
    assert [e["cache_hit"] for e in lookups] == [False, True]
    assert all(e["cacheable"] and e["results"] == 1 for e in lookups)
    assert all(len(e["query_sha256"]) == 64 for e in lookups)
    assert not any(e["tipo"] == "llm" for e in events)


def test_repair_requeries_even_same_error_and_reads_latest_available_spec(tmp_path, monkeypatch):
    obj, t = context(tmp_path)
    candidate = target("helper", "helper summary")
    obj.rag_db.query.return_value = [candidate]
    current = {"code": None}
    monkeypatch.setattr(obj, "_example_passing_spec", lambda _: current["code"])
    obj._related_for(t)
    help_for_error = obj._error_help_fn(t)
    assert "Example passing spec" not in help_for_error("NameError: same")
    current["code"] = "FIRST_AVAILABLE_SPEC"
    assert "FIRST_AVAILABLE_SPEC" in help_for_error("NameError: same")
    current["code"] = "NEW_AVAILABLE_SPEC"
    assert "NEW_AVAILABLE_SPEC" in help_for_error("ArgumentError: different")
    assert [call.args[0] for call in obj.rag_db.query.call_args_list] == [
        "NameError: same", "NameError: same", "ArgumentError: different"]
    assert obj.rag_db.related_lines.call_count == 1


def test_xrepo_repair_keeps_protection_against_generated_answer_leakage(tmp_path):
    from benchmark.xrepotest.backend import XRepoProject
    obj = XRepoProject(str(tmp_path), "src", rag_db=database())
    obj.rag_db.query.return_value = [target("helper", "helper summary")]
    t = target()
    obj._related_for(t)
    help_for_error = obj._error_help_fn(t)
    assert "Example passing spec" not in help_for_error("NameError")
    assert "Example passing spec" not in help_for_error("NameError")
    assert obj.rag_db.query.call_count == 2


def test_native_index_reinit_publishes_new_revision_even_for_reused_vectors(tmp_path):
    docs, queries = [], []
    def embed(texts):
        docs.extend(texts)
        return [[1.0, 2.0] for _ in texts]
    index = rag.RubyFunctionDatabase(embed, lambda q: queries.append(q) or [1.0, 2.0],
                                     persist_dir=str(tmp_path / "vectors"), key="fixed")
    assert index.retrieval_revision is None
    index.init([target()])
    first = index.retrieval_revision
    assert first and not index.reused
    index.init([target()])
    assert index.reused and index.retrieval_revision != first
    assert docs == ["add sum"] and not queries
    index.init([])
    assert index.retrieval_revision not in (None, first) and not index.reused
    assert index.query("add") == []


def test_failed_native_rebuild_cannot_retain_old_revision_or_collection(monkeypatch):
    index = rag.RubyFunctionDatabase(lambda docs: [[1.0] for _ in docs], lambda q: [1.0])
    index.init([target()])
    assert index.retrieval_revision
    def fail(*args):
        raise RuntimeError("cannot rebuild")
    monkeypatch.setattr(index, "_open", fail)
    with pytest.raises(RuntimeError, match="cannot rebuild"):
        index.init([target()])
    assert index.retrieval_revision is None and index._collection is None
    assert index.query("add") == []


needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def prepare_project(root):
    (root / "src").mkdir(parents=True)
    (root / "src/calculator.rb").write_text(
        "class Calculator\n  def add(a,b); a+b; end\n  def sub(a,b); a-b; end\nend\n")
    obj = project.RubyProject(str(root), "src", method_names=["Calculator#add"],
        ablation_options=AblationOptions(no_coverage_feedback=True)).discover()
    for t in obj.analysis_targets:
        t.summary = "add sum" if t.method.name == "add" else "subtract difference"
    obj._sync_generation_analysis()
    queries = []
    def vector(text):
        return [1.0 + text.count("add"), 1.0 + text.count("subtract")]
    obj.build_rag(lambda docs: [vector(d) for d in docs], lambda q: queries.append(q) or vector(q), persist=False)
    return obj, queries


@needs_ruby
def test_three_rounds_keep_identical_planner_prompts_and_live_repairs_with_fewer_queries(tmp_path):
    records = []
    for enabled in (False, True):
        obj, queries = prepare_project(tmp_path / str(enabled))
        if not enabled:
            obj.rag_db.retrieval_revision = None  # Same retriever, uncached contract.
        calls = []
        dev = 0
        async def ask(system, user):
            nonlocal dev
            calls.append((system, user))
            if "Test Plan" in system:
                return PLAN_RESPONSE
            dev += 1
            return BROKEN_SPEC if dev % 2 else GOOD_SPEC
        outcomes = asyncio.run(obj.generate_rounds(ask=ask, rounds=3, max_attempts=2))
        assert len(outcomes) == 3 and all(o.success and o.attempts == 2 for o in outcomes)
        assert len(calls) == 9
        planners = [user for system, user in calls if "Test Plan" in system]
        assert len(planners) == 3 and all("Calculator#sub" in user for user in planners)
        assert queries.count("add sum") == (1 if enabled else 3)
        assert len(queries) - queries.count("add sum") == 3  # Fresh repair retrieval each round.
        records.append((planners, [o.spec_code for o in outcomes]))
    assert records[0] == records[1]


@needs_ruby
@pytest.mark.parametrize("reset", ["discover", "analyze", "build"])
def test_project_lifecycle_discards_prior_static_context(tmp_path, reset):
    obj, queries = prepare_project(tmp_path / "repo")
    first = obj.targets[0]
    obj._related_for(first)
    assert len(queries) == 1
    if reset == "build":
        obj.build_rag(lambda docs: [[1.0, 2.0] for _ in docs], lambda q: queries.append(q) or [1.0, 2.0], persist=False)
    elif reset == "discover":
        old_db = obj.rag_db
        obj.discover()
        obj.rag_db = old_db  # Even explicit reattachment cannot restore old memoized context.
    else:
        async def ask(system, user):
            return "valid summary"
        old_db = obj.rag_db
        asyncio.run(obj.analyze_summaries(ask=ask, use_cache=False))
        obj.rag_db = old_db
    obj._related_for(first)
    assert len(queries) == 2


def test_projects_do_not_share_process_local_query_results(tmp_path):
    db = database()
    first, t = context(tmp_path / "first", db)
    second, other = context(tmp_path / "second", db)
    first._related_for(t)
    second._related_for(other)
    assert db.related_lines.call_count == 2
    first._related_for(t)
    second._related_for(other)
    assert db.related_lines.call_count == 2
