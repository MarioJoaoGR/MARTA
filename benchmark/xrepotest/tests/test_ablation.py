"""Immutable subsets, exact-prompt reuse and isolation between experiment arms."""
import asyncio
import copy
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from benchmark.xrepotest import ablation, protocol, run
from benchmark.xrepotest.tests.test_adapter import task
from marta.ruby_backend.ablation import AblationOptions


def test_selection_keeps_official_order_and_does_not_rewrite_the_release(tmp_path):
    tasks = [task(0), task(1), task(2)]
    path = tmp_path / "ids.json"
    path.write_text("[2, 0]")
    before = copy.deepcopy(tasks)
    chosen, selection = ablation.select_tasks(tasks, path)
    assert chosen == [tasks[0], tasks[2]] and tasks == before
    assert selection["task_ids"] == [0, 2]
    path.write_text("[0,2]")
    assert ablation.select_tasks(tasks, path)[1] == selection
    assert ablation.select_tasks(tasks) == (tasks, None)


@pytest.mark.parametrize("ids", [[], [0,0], [True], [1.0], ["0"], [999], {}, None])
def test_invalid_subset_is_refused(tmp_path, ids):
    path = tmp_path / "ids.json"
    path.write_text(json.dumps(ids))
    with pytest.raises(ValueError):
        ablation.select_tasks([task(0)], path)


def _reference(tmp_path, code=ablation.FROZEN_NORMAL_CODE):
    base = {"schema": protocol.SCHEMA, "marta_code": code,
            "no_graph": False, "model": "local:model", "model_digest": "fixed-weights",
            "rounds": 3, "attempts": 3, "thinking": "on", "max_tokens": 16384,
            "input_hashes": {"a": "source-a", "b": "source-b"},
            "runtime_hashes": {"a": "runtime-a", "b": "runtime-b"}}
    path = tmp_path / "reference"
    path.mkdir()
    (path / "experiment.json").write_text(json.dumps(base))
    config = {k:v for k,v in base.items() if k != "schema"}
    config.update(marta_code="new-code", ablations={"no_repair": True}, effective_attempts=1,
                  task_selection={"task_ids": [0]}, input_hashes={"a":"source-a"},
                  runtime_hashes={"a":"runtime-a"})
    return path, base, config


@pytest.mark.parametrize("code", [ablation.FROZEN_NORMAL_CODE, ablation.COVERAGE_OUTPUT_NORMAL_CODE])
def test_subset_can_reuse_verified_normal_context_with_separate_generation_options(tmp_path, code):
    path, before, config = _reference(tmp_path, code)
    provenance = ablation.verify_analysis_reference(path, config)
    assert provenance["scope"] == "compatible-production-analysis"
    assert json.loads((path / "experiment.json").read_text()) == before
    config["no_graph"] = True
    assert ablation.verify_analysis_reference(path, config)["scope"] == "exact-local-prompts-and-vectors"


@pytest.mark.parametrize("change", [
    {"marta_code": "unknown-code"}, {"model_digest": "other-weights"},
    {"thinking": "off"}, {"max_tokens": 32768}, {"no_graph": True},
    {"input_hashes": {"a":"changed-source"}}, {"runtime_hashes": {"a":"changed-runtime"}},
    {"ablations": {"no_type_hints": True}},
])
@pytest.mark.parametrize("code", [ablation.FROZEN_NORMAL_CODE, ablation.COVERAGE_OUTPUT_NORMAL_CODE])
def test_incompatible_analysis_reference_is_rejected(tmp_path, change, code):
    path, base, config = _reference(tmp_path, code)
    (path / "experiment.json").write_text(json.dumps({**base, **change}))
    with pytest.raises(ValueError):
        ablation.verify_analysis_reference(path, config)


def test_exact_normal_summary_reuse_never_calls_model_or_copies_tests(tmp_path):
    source, target = tmp_path / "reference/calls", tmp_path / "new/calls"
    recorder = SimpleNamespace(fase_atual="what_todo_raiz", evento=Mock())
    producer = SimpleNamespace(aask=AsyncMock(return_value="local intent"), last_call={})
    asyncio.run(run.SummaryCheckpoints(source, producer, recorder)("sys", "source"))
    consumer = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError("no inference")), last_call={})
    result = asyncio.run(run.SummaryCheckpoints(target, consumer, recorder, source,
                                               share_all_phases=True)("sys", "source"))
    assert result == "local intent"
    consumer.aask.assert_not_awaited()
    assert not target.exists()
    assert recorder.evento.call_args.kwargs["source"] == "analysis_reference"
    assert recorder.evento.call_args.kwargs["checkpoint"] == protocol.digest(
        ["what_todo_raiz", "sys", "source"])


def test_each_ablation_is_part_of_resume_identity(tmp_path):
    base = {"model":"fixed"}
    protocol.guard_run(tmp_path, base)
    for name in AblationOptions.__dataclass_fields__:
        with pytest.raises(ValueError, match="configuration changed"):
            protocol.guard_run(tmp_path, {**base, "ablations": {name:True}})
    assert json.loads((tmp_path / "experiment.json").read_text()) == {"schema":protocol.SCHEMA, **base}


def test_selected_response_contract_keeps_no_tests_and_rejects_other_denominators(tmp_path):
    from benchmark.xrepotest.evaluate import load_responses
    path = tmp_path / "ids.json"
    path.write_text("[0,2]")
    selected, _ = ablation.select_tasks([task(0), task(1), task(2)], path)
    responses = tmp_path / "processed.jsonl"
    rows = [{"task_id":0,"response":["RSpec.describe('sample') {}"]},
            {"task_id":2,"response":[]}]
    responses.write_text("\n".join(json.dumps(r) for r in rows))
    assert load_responses(responses, selected) == {0: rows[0]["response"], 2: []}
    responses.write_text(json.dumps(rows[0]))
    with pytest.raises(ValueError, match="every official task"):
        load_responses(responses, selected)
    responses.write_text("\n".join(json.dumps(r) for r in rows + [{"task_id":1,"response":[]}]))
    with pytest.raises(ValueError, match="every official task"):
        load_responses(responses, selected)


def test_identical_local_readme_request_can_reuse_fallback_as_root(tmp_path):
    source = tmp_path / "reference"
    recorder = SimpleNamespace(fase_atual="what_todo_fallback", evento=Mock())
    producer = SimpleNamespace(aask=AsyncMock(return_value="same local intent"), last_call={})
    asyncio.run(run.SummaryCheckpoints(source, producer, recorder)("local", "exact request"))
    recorder.fase_atual = "what_todo_raiz"
    consumer = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError("no new call")), last_call={})
    result = asyncio.run(run.SummaryCheckpoints(tmp_path/"new", consumer, recorder, source,
                                               share_all_phases=True)("local", "exact request"))
    assert result == "same local intent"
    assert recorder.evento.call_args.kwargs["reference_phase"] == "what_todo_fallback"
    consumer.aask.assert_not_awaited()


def test_repaired_normal_reference_allows_paired_first_round(tmp_path):
    path, before, config = _reference(tmp_path, ablation.COVERAGE_OUTPUT_NORMAL_CODE)
    config.update(ablations={"no_coverage_feedback": True}, effective_attempts=3)
    assert ablation.verify_first_round_reference(path, config)["scope"] == "paired-first-round-v1"
    assert json.loads((path / "experiment.json").read_text()) == before
    config["attempts"] = 1
    with pytest.raises(ValueError, match="same repair attempt budget"):
        ablation.verify_first_round_reference(path, config)
