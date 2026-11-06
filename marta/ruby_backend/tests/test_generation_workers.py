"""Offline scheduler regressions: immutable scripted replies, real Ruby gates."""
import asyncio
import json
import os
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.llm_response import ChatReply
from marta.ruby_backend import execution, project, recorder, prompts, workers
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.backend import RubyBackend
from marta.ruby_backend.tests.test_generate import PLAN_RESPONSE
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def make(tmp_path, count=2, concurrency=2, **kwargs):
    (tmp_path / "src").mkdir()
    methods = "\n".join(f"  def m{i}(x)\n    x + {i}\n  end" for i in range(count))
    (tmp_path / "src/calculator.rb").write_text("class Calculator\n" + methods + "\nend\n")
    return project.RubyProject(str(tmp_path), "src", isolate_execution=True,
        generation_workers=concurrency, **kwargs).discover()


def spec(name, *, conflict=False):
    number = int(name[1:])
    prefix = f"$worker_fixture_mode = :{name}\n" if conflict else ""
    check = f"expect($worker_fixture_mode).to eq(:{name}); " if conflict else ""
    return ('```ruby\nrequire "calculator"\n' + prefix + 'RSpec.describe Calculator do\n'
            f'  it("tests {name}") {{ {check}expect(described_class.new.{name}(2)).to eq({2+number}) }}\n'
            'end\n```')


class Client:
    response_api = True

    def __init__(self, count=2, *, conflict=False):
        self.count, self.conflict = count, conflict
        self.calls, self.finished = [], []
        self.active = self.maximum = 0

    def method(self, user):
        return next(f"m{i}" for i in range(self.count) if f"def m{i}(" in user)

    async def aask_result(self, system, user):
        name = self.method(user)
        phase = "plan" if system == prompts.PLAN_SYS else "dev"
        self.calls.append((name, phase, user))
        self.active += 1
        self.maximum = max(self.maximum, self.active)
        try:
            # Force a later target to answer first, including the final Dev response.
            await asyncio.sleep(0.03 if name == "m0" else 0.001)
            text = PLAN_RESPONSE if phase == "plan" else spec(name, conflict=self.conflict)
            self.finished.append((name, phase))
            return ChatReply(text, 10, 20, "stop")
        finally:
            self.active -= 1


def run(obj, client, rounds=1, attempts=1):
    return asyncio.run(obj.generate_rounds(rounds=rounds, ask=client, max_attempts=attempts))


@pytest.mark.parametrize("value", [0, 3, True, 1.5, "2"])
def test_invalid_worker_count_rejected_before_work(value, tmp_path):
    with pytest.raises(ValueError, match="must be 1, 2 or 4"):
        project.RubyProject(str(tmp_path), "src", generation_workers=value)


def test_multiple_workers_require_explicit_isolation_and_native_backend(tmp_path):
    with pytest.raises(ValueError, match="isolate_execution"):
        project.RubyProject(str(tmp_path), "src", generation_workers=2)
    class Custom(RubyBackend):
        pass
    with pytest.raises(ValueError, match="native RubyBackend"):
        project.RubyProject(str(tmp_path), "src", generation_workers=2,
                            isolate_execution=True, backend=Custom())


def test_forked_metrics_merge_only_counters_and_preserve_control_state(tmp_path):
    parent = recorder.RubyRecorder(str(tmp_path / "events.jsonl"))
    parent.start_count_time("round")
    parent.score.coverage.append({"previous": 1})
    with parent.fase("generation"), parent.contexto(ronda=1):
        a, b = parent.fork(worker=1), parent.fork(worker=2)
        a.score.first_run, b.score.first_run = True, False
        a.score.add_syntax_pass()
        b.score.add_syntax_error()
        a.score.add_llm_call(3, 5, fase="plano")
        b.score.add_llm_call(0, 0, fase="dev", usage_reported=False)
        b.score.llm_interrupted_requests = 1
        a.score.add_subprocesso("rspec", 0.25)
        b.score.add_assertion_error_type("load")
        a.start_count_time("own")
        a.end_count_time("own")
        parent.collect_worker(2, b)
        parent.collect_worker(1, a)
        assert a._contexto == {"ronda": 1, "worker": 1}
        assert b._contexto == {"ronda": 1, "worker": 2}
    assert parent._contexto == {} and parent.fase_atual == "?"
    assert parent.score.first_run is True
    assert parent.score.coverage == [{"previous": 1}]
    assert parent.score.llm_calls == 2 and parent.score.prompt_tokens == 3
    assert parent.score.llm_usage_unknown_calls == parent.score.llm_interrupted_requests == 1
    assert parent.score.first_syntax_pass == 1 and parent.score.first_syntax_error == 0
    assert parent.score.assertion_error_types == {"load": 1}
    assert "own" not in parent.times and "round" in parent.times
    assert parent.to_json()["workers"]["2"]["llm_calls"] == 1
    b.score.assertion_error_types["load"] = 100
    assert parent.score.assertion_error_types == {"load": 1}  # No alias to a worker.
    with pytest.raises(ValueError):
        parent.score.merge_from(parent.score)
    with pytest.raises(ValueError):
        parent.score.merge_from(recorder.RubyScore(coverage=[{}]))


@needs_ruby
@pytest.mark.parametrize("concurrency", [2, 4])
def test_bounded_overlap_ordered_publication_and_exact_metrics(tmp_path, monkeypatch, concurrency):
    obj = make(tmp_path, count=4, concurrency=concurrency)
    obj.recorder = recorder.RubyRecorder(str(tmp_path / "events.jsonl"))
    client = Client(4)
    published, roots = [], []
    real_publish, real_ensure = execution.GenerationWorkspace.publish, execution.GenerationWorkspace.ensure
    def publish(self, outcome):
        published.append(outcome.method)
        return real_publish(self, outcome)
    def ensure(self):
        real_ensure(self)
        if self.root not in roots:
            roots.append(self.root)
    monkeypatch.setattr(execution.GenerationWorkspace, "publish", publish)
    monkeypatch.setattr(execution.GenerationWorkspace, "ensure", ensure)
    outcomes = run(obj, client)
    assert 1 < client.maximum <= concurrency and client.active == 0
    assert len(client.calls) == 8  # One plan and one Dev per target, no scheduler retries.
    assert client.finished.index(("m1", "dev")) < client.finished.index(("m0", "dev"))
    expected = [t.method.qualified_name for t in obj.targets]
    assert published == [o.method for o in outcomes] == expected
    assert all(o.success for o in outcomes)
    assert len(roots) == concurrency and all(not path.exists() for path in roots)
    score = obj.recorder.score
    assert score.llm_calls == 8 and score.prompt_tokens == 80 and score.completion_tokens == 160
    assert score.first_syntax_pass == score.first_assertion_pass == 4
    assert sum(s.llm_calls for s in obj.recorder.worker_scores.values()) == 8
    assert score.subprocessos["rspec"]["execucoes"] == 4
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    llm = [e for e in events if e["tipo"] == "llm"]
    assert len(llm) == 8 and all(e["ronda"] == 0 and e["worker"] in range(1, concurrency+1) for e in llm)
    assert len({e["definition_id"] for e in llm}) == 4
    state = json.loads((tmp_path / ".marta_generation/rounds.json").read_text())
    assert len(state["rounds"]) == 1 and len(state["files"]) == 4
    assert state["recipe"]["generation_schedule"]["workers"] == concurrency


@needs_ruby
def test_single_worker_and_parallel_cover_same_deterministic_fixture(tmp_path):
    runs = []
    for concurrency in (1, 2):
        folder = tmp_path / str(concurrency)
        folder.mkdir()
        obj = make(folder, concurrency=concurrency)
        client = Client()
        outcomes = run(obj, client)
        runs.append(([o.spec_code for o in outcomes], obj.measure_coverage(), len(client.calls)))
    assert runs[0] == runs[1]


@needs_ruby
def test_interacting_candidates_roll_back_in_target_order_not_finish_order(tmp_path):
    obj = make(tmp_path)
    client = Client(conflict=True)
    outcomes = run(obj, client)
    assert client.finished.index(("m1", "dev")) < client.finished.index(("m0", "dev"))
    assert [o.success for o in outcomes] == [True, False]
    assert len(obj._all_spec_paths()) == 1
    assert list((tmp_path / "rejected_specs").glob("accumulated_*/*.rb"))


@needs_ruby
def test_rounds_reuse_copies_and_dont_mix_first_round_counters(tmp_path, monkeypatch):
    obj = make(tmp_path, ablation_options=AblationOptions(no_coverage_feedback=True))
    obj.recorder = recorder.RubyRecorder()
    copy_count = 0
    real_copy = execution.shutil.copytree
    def copy(*args, **kwargs):
        nonlocal copy_count
        if Path(args[0]) == tmp_path:
            copy_count += 1
        return real_copy(*args, **kwargs)
    monkeypatch.setattr(execution.shutil, "copytree", copy)
    client = Client()
    outcomes = run(obj, client, rounds=3)
    assert len(outcomes) == 6 and len(client.calls) == 12
    assert copy_count == 2  # Not one copy per method, round or coverage gate.
    assert obj.recorder.score.syntax_pass == 6
    assert obj.recorder.score.first_syntax_pass == 2
    assert len(obj.recorder.score.coverage) == 3
    assert sum(s.first_syntax_pass for s in obj.recorder.worker_scores.values()) == 2
    # A resume revalidates retained bytes but performs no new LLM calls.
    again = run(obj, client, rounds=3)
    assert again == [] and len(client.calls) == 12
    assert obj.recorder.score.llm_calls == 12


@needs_ruby
@pytest.mark.parametrize("kind", ["legacy", "shared_attempts", "singleton"])
@pytest.mark.parametrize("wrapped", [False, True])
def test_unsafe_provider_rejected_before_any_request(tmp_path, kind, wrapped):
    obj = make(tmp_path)
    provider = SimpleNamespace(response_api=kind != "legacy",
        records_llm_attempts=kind == "shared_attempts", legacy_singleton_metrics=kind == "singleton",
        aask_result=Mock(side_effect=AssertionError("request must not run")))
    from marta.ruby_backend.requests import RubyAsk
    with pytest.raises(ValueError, match="request-local"):
        run(obj, RubyAsk(provider) if wrapped else provider)
    provider.aask_result.assert_not_called()
    assert not obj._all_spec_paths()


@needs_ruby
def test_error_cancels_sibling_and_does_not_start_queued_jobs(tmp_path):
    obj = make(tmp_path, count=4)
    obj.recorder = recorder.RubyRecorder()
    class Broken(Client):
        async def aask_result(self, system, user):
            name = self.method(user)
            self.calls.append(name)
            if len(self.calls) == 2:
                both.set()
            await both.wait()
            if name == "m0":
                raise RuntimeError("transport failed")
            try:
                await asyncio.Event().wait()
            finally:
                self.drained = True
    async def scenario():
        nonlocal both
        both = asyncio.Event()
        client = Broken(4)
        with pytest.raises(RuntimeError, match="transport failed"):
            await asyncio.wait_for(obj.generate_rounds(ask=client), timeout=5)
        assert client.drained and set(client.calls) == {"m0", "m1"}
    both = None
    asyncio.run(scenario())
    assert obj.recorder.score.llm_interrupted_requests == 2
    assert obj.recorder.score.llm_calls == 0
    assert not obj._all_spec_paths()
    assert not (tmp_path / ".marta_generation/rounds.json").exists()
    assert obj.recorder.times["round_0"] < 5


@needs_ruby
def test_completed_private_candidate_archived_if_another_worker_fails(tmp_path, monkeypatch):
    obj = make(tmp_path)
    obj.recorder = recorder.RubyRecorder()
    real_generate = execution.GenerationWorkspace.generate
    completed = None
    async def generate(self, **kwargs):
        result = await real_generate(self, **kwargs)
        if result.success and result.method.endswith("#m0"):
            completed.set()
        return result
    monkeypatch.setattr(execution.GenerationWorkspace, "generate", generate)
    class Broken(Client):
        async def aask_result(self, system, user):
            if self.method(user) == "m1":
                await completed.wait()
                raise RuntimeError("transport failed")
            return await super().aask_result(system, user)
    async def scenario():
        nonlocal completed
        completed = asyncio.Event()
        with pytest.raises(RuntimeError, match="transport failed"):
            await asyncio.wait_for(obj.generate_rounds(ask=Broken()), timeout=5)
    asyncio.run(scenario())
    assert obj.recorder.score.llm_calls == 2 and obj.recorder.score.llm_interrupted_requests == 1
    assert not obj._all_spec_paths()
    assert list((tmp_path / "rejected_specs").glob("execution_*/*.rb"))


@needs_ruby
def test_parent_cancellation_drains_requests_and_cleans_all_copies(tmp_path, monkeypatch):
    obj = make(tmp_path)
    obj.recorder = recorder.RubyRecorder()
    roots = []
    real_ensure = execution.GenerationWorkspace.ensure
    def ensure(self):
        real_ensure(self)
        roots.append(self.root)
    monkeypatch.setattr(execution.GenerationWorkspace, "ensure", ensure)
    class Waiting(Client):
        async def aask_result(self, system, user):
            self.calls.append(self.method(user))
            if len(self.calls) == 2:
                started.set()
            try:
                await asyncio.Event().wait()
            finally:
                self.finished.append(self.method(user))
    async def scenario():
        nonlocal started
        started = asyncio.Event()
        client = Waiting()
        task = asyncio.create_task(obj.generate_rounds(ask=client))
        await asyncio.wait_for(started.wait(), 5)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert len(client.finished) == 2
    started = None
    asyncio.run(scenario())
    assert roots and all(not path.exists() for path in roots)
    assert obj.recorder.score.llm_interrupted_requests == 2
    assert not obj._all_spec_paths()


@needs_ruby
def test_example_snapshot_keeps_exact_old_bytes_with_external_output(tmp_path):
    output = tmp_path.parent / (tmp_path.name + "_output")
    obj = make(tmp_path, output_root=str(output))
    target = obj.targets[0]
    path = Path(obj.root_dir, target.spec_path_for_round(0))
    path.parent.mkdir(parents=True)
    path.write_text("old certified example")
    snapshot = workers.example_snapshot(obj)
    path.write_text("new candidate must not leak")
    assert obj._example_passing_spec(target, snapshot=snapshot) == "old certified example"
    assert obj._example_passing_spec(obj.targets[1], snapshot=snapshot) is None
    assert obj._example_passing_spec(target) == "new candidate must not leak"
    with pytest.raises(TypeError):
        snapshot[str(path.parent)][path.name] = "changed"
    database = SimpleNamespace(query=Mock(return_value=[target]))
    obj.rag_db = database
    helper = obj._error_help_fn(obj.targets[1], examples=snapshot)
    assert "old certified example" in helper("error one")
    assert "new candidate" not in helper("error two")
    assert database.query.call_count == 2  # Error retrieval remains dynamic.


@needs_ruby
def test_single_pass_api_uses_the_same_coordinator_gate(tmp_path):
    obj = make(tmp_path)
    outcomes = asyncio.run(obj.generate_all(ask=Client(), max_attempts=1))
    assert all(o.success for o in outcomes) and len(obj._all_spec_paths()) == 2
    assert not (tmp_path / ".marta_generation/rounds.json").exists()


@needs_ruby
def test_empty_schedule_allocates_no_workspaces_or_requests(tmp_path, monkeypatch):
    obj = make(tmp_path, count=0, concurrency=4)
    forbidden = Mock(side_effect=AssertionError("nothing to copy"))
    monkeypatch.setattr(execution.shutil, "copytree", forbidden)
    client = Client(0)
    assert run(obj, client) == [] and not client.calls
    forbidden.assert_not_called()
    assert not obj._recorder().worker_scores


@needs_ruby
def test_limit_and_coverage_skip_do_not_allocate_idle_workers(tmp_path, monkeypatch):
    obj = make(tmp_path, count=4, concurrency=4)
    roots = set()
    real_ensure = execution.GenerationWorkspace.ensure
    def ensure(self):
        real_ensure(self)
        roots.add(self.root)
    monkeypatch.setattr(execution.GenerationWorkspace, "ensure", ensure)
    client = Client(4)
    outcomes = asyncio.run(obj.generate_rounds(rounds=3, ask=client, max_attempts=1, limit=1))
    assert len(outcomes) == 1 and outcomes[0].success
    assert len(client.calls) == 2 and len(roots) == 1
    assert set(obj._recorder().worker_scores) == {"1"}


@needs_ruby
def test_failed_publication_cannot_certify_a_partial_round(tmp_path, monkeypatch):
    obj = make(tmp_path)
    original = execution.GenerationWorkspace.publish
    def broken(self, outcome):
        if outcome.method.endswith("#m1"):
            raise OSError("publication interrupted")
        return original(self, outcome)
    with monkeypatch.context() as patch:
        patch.setattr(execution.GenerationWorkspace, "publish", broken)
        with pytest.raises(OSError, match="publication interrupted"):
            run(obj, Client())
    assert len(obj._all_spec_paths()) == 1  # Uncommitted, not a completed round.
    assert not (tmp_path / ".marta_generation/rounds.json").exists()
    assert list((tmp_path / "rejected_specs").glob("execution_*/*.rb"))
    assert all(o.success for o in run(obj, Client()))
    assert list((tmp_path / "rejected_specs").glob("resume_*/marta_specs/*.rb"))
    state = json.loads((tmp_path / ".marta_generation/rounds.json").read_text())
    assert len(state["rounds"]) == 1 and len(state["files"]) == 2


@needs_ruby
def test_one_worker_barrier_is_a_controlled_reference_for_two_workers(tmp_path):
    policies, codes = [], []
    for count in (1, 2):
        folder = tmp_path / str(count)
        folder.mkdir()
        obj = make(folder, concurrency=count, round_barrier=True)
        client = Client()
        outcomes = run(obj, client)
        assert obj._coordinated_generation and all(o.success for o in outcomes)
        assert len(client.calls) == 4
        assert obj._recorder().score.llm_calls == 4
        assert sum(s.llm_calls for s in obj._recorder().worker_scores.values()) == 4
        recipe = json.loads((folder / ".marta_generation/rounds.json").read_text())["recipe"]
        policies.append(recipe["generation_schedule"]["policy"])
        codes.append([o.spec_code for o in outcomes])
    assert policies == [workers.POLICY, workers.POLICY]
    assert codes[0] == codes[1]


def test_barrier_reference_requires_isolation_and_a_boolean_option(tmp_path):
    with pytest.raises(ValueError, match="isolate_execution"):
        project.RubyProject(str(tmp_path), "src", round_barrier=True)
    with pytest.raises(ValueError, match="boolean"):
        project.RubyProject(str(tmp_path), "src", round_barrier="yes")
