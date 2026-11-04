"""Whole-request fitting; artificial counters and scripted responses, no inference."""
import asyncio
from dataclasses import replace
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import generate, prompts, readme, summaries
from marta.ruby_backend.analysis_state import analysis_provenance
from marta.ruby_backend.prompt_budget import (
    BudgetConfigurationError, LocalChatCounter, OptionalPart, PromptBudget,
    PromptBudgetExceeded, UTF8Estimate, _local_tokenizer, budget_provenance,
)
from marta.ruby_backend.recorder import RubyRecorder
from marta.ruby_backend.tests.test_plan_source_validation import AcceptingBackend, SCENARIO


class CharacterCounter:
    # An exact artificial metric for fixtures, not a real-model tokenizer.
    identity = {"mode": "fixture-character-counter-v1", "exact_for_template": True}
    exact = True

    def __call__(self, system, user):
        return len(system) + len(user)


@pytest.fixture(autouse=True)
def isolated_config(monkeypatch):
    for name in ("MARTA_CONTEXT_TOKENS", "OLLAMA_CTX", "OLLAMA_CONTEXT_LENGTH", "LLM_MAX_TOKENS",
                 "MARTA_OUTPUT_RESERVE", "MARTA_CONTEXT_MARGIN", "MARTA_TOKENIZER_PATH",
                 "MARTA_REQUIRE_EXACT_TOKENS"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.delitem(sys.modules, "marta.gptapi", raising=False)


def configured_ask(answer="valid summary", limit=6000):
    seen = []
    async def ask(system, user):
        seen.append((system, user))
        if callable(answer):
            return answer(len(seen), system, user)
        return answer
    ask.prompt_budget = PromptBudget(limit + 20, 20, 0, CharacterCounter())
    ask.client = SimpleNamespace(max_tokens=20)
    return ask, seen


def test_full_system_user_response_and_margin_are_counted_at_boundary():
    budget = PromptBudget(20, 5, 3, CharacterCounter())
    assert budget.render("system", lambda _: "123456") == "123456"
    with pytest.raises(PromptBudgetExceeded):
        budget.render("system", lambda _: "1234567")


@pytest.mark.parametrize("context,output,margin", [(0, 1, 0), (10, 0, 0), (10, 5, -1),
                                                      (10, 5, 5), (True, 1, 0)])
def test_invalid_budget_is_configuration_failure(context, output, margin):
    with pytest.raises(BudgetConfigurationError):
        PromptBudget(context, output, margin)


def test_fitting_text_and_optional_lists_are_unmodified():
    items = ["first", "second"]
    budget = PromptBudget(500, 20, 0, CharacterCounter())
    builder = lambda v: "complete: " + ",".join(v["related"])
    assert budget.render("system", builder, [OptionalPart("related", items, [])]) == builder({"related": items})
    assert items == ["first", "second"]


def test_reduction_counts_omission_notice_and_keeps_whole_list_entries(tmp_path):
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    budget = PromptBudget(150, 20, 0, CharacterCounter(), recorder)
    original = ["first " + "a" * 400, "second " + "b" * 400]
    user = budget.render("system", lambda v: "required-tail" + "\n".join(v["items"]),
                         [OptionalPart("items", original, [])])
    assert "required-tail" in user and "first" not in user and "second" not in user
    assert "optional context reduced: items" in user
    event = json.loads((tmp_path / "events.jsonl").read_text())
    assert event["selected_input"] == len("system") + len(user) <= budget.input_limit
    assert event["original_request_sha256"] != event["selected_request_sha256"]
    assert len(original) == 2


def test_low_priority_context_is_reduced_before_high_priority_context():
    budget = PromptBudget(250, 20, 0, CharacterCounter())
    text = budget.render("S", lambda v: v["retrieval"] + "|" + v["important"],
        [OptionalPart("retrieval", "x" * 300), OptionalPart("important", "KEEP_ME")])
    assert "KEEP_ME" in text and "important." not in text
    assert len(text) + 1 <= budget.input_limit


def test_atomic_code_is_omitted_whole_not_sliced():
    budget = PromptBudget(160, 20, 0, CharacterCounter())
    code = 'def auxiliary; "' + 'x' * 500 + '"; end'
    focal = "def focal; :tail; end"
    text = budget.render("S", lambda v: v["source"],
        [OptionalPart("source", code + "\n" + focal, focal, compact=False)])
    assert focal in text and "auxiliary" not in text


def test_unicode_estimate_counts_bytes_and_identifies_itself_as_estimate():
    assert UTF8Estimate()("é", "🙂") == 2 + 4 + 64
    info = budget_provenance()
    assert not info["counter"]["exact_for_template"]
    assert info["window_source"] == "client-default-unverified-server"


def test_environment_uses_smallest_window_and_reserves_at_least_actual_cap(monkeypatch):
    ask, _ = configured_ask()
    del ask.prompt_budget
    monkeypatch.setenv("OLLAMA_CTX", "32768")
    monkeypatch.setenv("MARTA_CONTEXT_TOKENS", "8192")
    monkeypatch.setenv("MARTA_OUTPUT_RESERVE", "10")
    ask.client.max_tokens = 512
    budget = PromptBudget.from_ask(ask)
    assert budget.context_tokens == 8192 and budget.output_tokens == 512
    assert ask.client.max_tokens == 512


@pytest.mark.parametrize("value", [None, 0, -1, "4096", True])
def test_declared_invalid_or_unbounded_client_cap_is_rejected(value):
    ask, _ = configured_ask()
    ask.client.max_tokens = value
    with pytest.raises(BudgetConfigurationError):
        PromptBudget.from_ask(ask)


def test_supplied_budget_cannot_underreserve_actual_cap():
    ask, _ = configured_ask()
    ask.client.max_tokens = 512
    with pytest.raises(BudgetConfigurationError, match="reserves less"):
        PromptBudget.from_ask(ask)


@pytest.mark.parametrize("supplied", [False, True])
def test_strict_mode_rejects_estimate_even_if_budget_is_injected(monkeypatch, supplied):
    monkeypatch.setenv("MARTA_REQUIRE_EXACT_TOKENS", "1")
    ask, _ = configured_ask()
    if supplied:
        ask.prompt_budget = replace(ask.prompt_budget, counter=UTF8Estimate())
    else:
        del ask.prompt_budget
    with pytest.raises(BudgetConfigurationError, match="Exact token counting"):
        PromptBudget.from_ask(ask)


def test_local_template_is_loaded_offline_with_generation_prefix_and_thinking(tmp_path, monkeypatch):
    (tmp_path / "tokenizer_config.json").write_text('{"chat_template":"fixture"}')
    loader = Mock()
    tokenizer = loader.from_pretrained.return_value
    tokenizer.apply_chat_template.return_value = [1, 2, 3]
    monkeypatch.setitem(sys.modules, "transformers", SimpleNamespace(AutoTokenizer=loader))
    _local_tokenizer.cache_clear()
    counter = LocalChatCounter(tmp_path, thinking=True)
    assert counter("S", "U") == 3
    loader.from_pretrained.assert_called_once_with(str(tmp_path), local_files_only=True, trust_remote_code=False)
    tokenizer.apply_chat_template.assert_called_once_with(
        [{"role": "system", "content": "S"}, {"role": "user", "content": "U"}],
        tokenize=True, add_generation_prompt=True, enable_thinking=True)
    before = counter.identity
    (tmp_path / "tokenizer_config.json").write_text('{"chat_template":"changed"}')
    assert LocalChatCounter(tmp_path).identity != before
    _local_tokenizer.cache_clear()


def test_configured_tokenizer_failure_does_not_download_or_fall_back(tmp_path, monkeypatch):
    (tmp_path / "tokenizer.json").write_text("{}")
    loader = Mock()
    loader.from_pretrained.side_effect = RuntimeError("unavailable locally")
    monkeypatch.setitem(sys.modules, "transformers", SimpleNamespace(AutoTokenizer=loader))
    _local_tokenizer.cache_clear()
    with pytest.raises(BudgetConfigurationError, match="no download or fallback"):
        LocalChatCounter(tmp_path)("S", "U")
    assert loader.from_pretrained.call_args.kwargs["local_files_only"] is True
    _local_tokenizer.cache_clear()


@pytest.mark.parametrize("change", ["window", "reserve", "margin", "counter"])
def test_effective_budget_changes_analysis_provenance(change):
    ask, _ = configured_ask()
    before = analysis_provenance(ask)
    values = {"window": {"context_tokens": 7000}, "reserve": {"output_tokens": 30},
              "margin": {"margin_tokens": 2}, "counter": {"counter": UTF8Estimate()}}
    ask.prompt_budget = replace(ask.prompt_budget, **values[change])
    assert analysis_provenance(ask) != before


@pytest.mark.parametrize("phase", ["done", "enriched", "caller", "merge", "requirement", "readme", "class"])
def test_analysis_requests_fit_and_preserve_focal_tail(phase):
    focal = "def target; :complete_focal_tail; end"
    source = "# AUXILIARY " + "x" * 20000 + "\n" + focal
    ask, seen = configured_ask(limit=2500)
    if phase in ("done", "enriched"):
        call = summaries.analyze_done_what(ask, source,
            called_summaries=["callee=" + "z" * 10000] if phase == "enriched" else None, focal_source=focal)
    elif phase == "caller":
        call = summaries.analyze_what_todo_from_caller(ask, "Target#x", source, "Caller#x", "z" * 10000, focal_source=focal)
    elif phase == "merge":
        call = summaries.generate_summary(ask, source, "done" * 3000, "todo" * 3000, focal_source=focal)
    elif phase == "requirement":
        call = readme.analyze_what_todo(ask, source, "overview" * 3000, focal_source=focal)
    elif phase == "readme":
        call = readme.analyze_readme(ask, "requirements" * 3000)
    else:
        call = summaries.analyze_class(ask, "class Target\n" + "  def x; end\n" * 3000, class_core="class Target")
    assert asyncio.run(call) == "valid summary"
    assert len(seen) == 1 and len(seen[0][0]) + len(seen[0][1]) <= 2500
    if phase not in ("readme", "class"):
        assert focal in seen[0][1] and "AUXILIARY" not in seen[0][1]
    if phase == "class":
        assert "class Target" in seen[0][1]


def flow(tmp_path, ask, **kwargs):
    return asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc.x", describe_subject="Calc", method_source="def self.x; :tail; end",
        require_target="calc", load_paths=["."], spec_path="spec/x_spec.rb", cwd=str(tmp_path),
        ask=ask, backend=AcceptingBackend(), max_attempts=1, **kwargs))


def test_fitting_generation_prompts_are_byte_for_byte_unchanged(tmp_path):
    ask, seen = configured_ask(lambda n, s, u: json.dumps([SCENARIO]) if n == 1 else 'RSpec.describe("x") { it("works") {} }')
    assert flow(tmp_path, ask, summary="summary", related=["related"]).success
    expected_plan = prompts.plan_user(prompts.build_context_block(
        "Calc.x", "calc", "def self.x; :tail; end", "summary",
        "First pass: Try to achieve maximum coverage.", ["related"]))
    expected_dev = prompts.dev_user(prompts.first_dev_instruction([SCENARIO]), "def self.x; :tail; end", "calc", "Calc")
    assert seen == [(prompts.PLAN_SYS, expected_plan), (prompts.DEV_SYS, expected_dev)]


def test_oversized_mandatory_method_sends_no_request_or_success_file(tmp_path):
    ask, seen = configured_ask(limit=200)
    with pytest.raises(PromptBudgetExceeded, match="No model request was sent"):
        flow(tmp_path, ask)
    assert seen == [] and not (tmp_path / "spec/x_spec.rb").exists()


def test_repair_budget_keeps_previous_code_and_original_plan(tmp_path):
    from marta.ruby_backend import runner
    class RepairBackend(AcceptingBackend):
        def run_tests(self, *args, **kwargs):
            if not hasattr(self, "failed_once"):
                self.failed_once = True
                return runner.RSpecResult(False, [runner.ExampleResult(
                    str(i), "huge-description" * 100, "failed", 1, "observed error",
                    exception_class="NameError") for i in range(40)],
                    report_valid=True, exit_code=1, output="NameError: missing\n" + "trace\n" * 3000)
            return super().run_tests(*args, **kwargs)
    code = 'RSpec.describe("x") { it("works") {} }'
    ask, seen = configured_ask(lambda n, s, u: json.dumps([SCENARIO]) if n == 1 else code)
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    outcome = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc.x", describe_subject="Calc", method_source="def self.x; :tail; end",
        require_target="calc", load_paths=["."], spec_path="spec/x_spec.rb", cwd=str(tmp_path),
        ask=ask, backend=RepairBackend(), max_attempts=2, recorder=recorder,
        error_help_fn=lambda _: "EXAMPLE CODE " + "x" * 10000))
    assert outcome.success and len(seen) == 3
    assert all(len(s) + len(u) <= 6000 for s, u in seen)
    request = seen[-1][1]
    assert code in request and "def self.x; :tail; end" in request
    plan = json.JSONDecoder().raw_decode(request.split("ORIGINAL TEST PLAN:\n", 1)[1])[0]
    failure = json.JSONDecoder().raw_decode(request.split("CURRENT FAILURE:\n", 1)[1])[0]
    assert plan == [SCENARIO] and failure["counts"]["failed"] == 40
    assert failure["category"] == "missing_constant" and len(failure["examples"]) < 40
    assert "PREVIOUS TEST VALIDATION:" not in request
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    assert any(e["tipo"] == "prompt_budget" and e["fase"] == "dev_reparacao" and e["reduced"] for e in events)


@pytest.mark.parametrize("name,value", [("MARTA_CONTEXT_TOKENS", "100"),
                                        ("MARTA_OUTPUT_RESERVE", "200"),
                                        ("MARTA_CONTEXT_MARGIN", "128"),
                                        ("MARTA_CONTEXT_MARGIN", "-1")])
def test_injected_budget_cannot_bypass_declared_safety_bounds(monkeypatch, name, value):
    ask, _ = configured_ask()
    monkeypatch.setenv(name, value)
    with pytest.raises(BudgetConfigurationError):
        PromptBudget.from_ask(ask)


def test_overflow_before_developer_does_not_send_a_second_request(tmp_path):
    # A valid but large plan must stay complete, even if Planner's input fitted.
    large = [{"name": "scenario", "desc": "d" * 3000, "setup": "real object"}]
    ask, seen = configured_ask(json.dumps(large), limit=2800)
    with pytest.raises(PromptBudgetExceeded):
        flow(tmp_path, ask)
    assert len(seen) == 1 and seen[0][0] == prompts.PLAN_SYS
    assert not (tmp_path / "spec/x_spec.rb").exists()


def test_planner_and_developer_preserve_focal_code_when_optional_source_is_removed(tmp_path):
    focal = "def self.x; :entire_focal_tail; end"
    source = "# AUX " + "x" * 15000 + "\n" + focal
    ask, seen = configured_ask(lambda n, s, u: json.dumps([SCENARIO]) if n == 1 else 'RSpec.describe("x") { it("ok") {} }')
    result = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc.x", describe_subject="Calc", method_source=source, focal_source=focal,
        require_target="calc", load_paths=["."], spec_path="spec/x_spec.rb", cwd=str(tmp_path),
        ask=ask, backend=AcceptingBackend(), max_attempts=1,
        summary="summary " * 4000, related=["related " * 4000]))
    assert result.success and len(seen) == 2
    assert all(focal in u and "# AUX" not in u and len(s) + len(u) <= 6000 for s, u in seen)


def test_failed_analysis_budget_preserves_previous_cache_and_records_failure(tmp_path):
    from marta.ruby_backend.tests.test_analysis_provenance import make_project
    from marta.ruby_backend.tests.test_suite_validation import toolchain_ok
    if not toolchain_ok():
        pytest.skip("no Ruby/RSpec toolchain")
    ask, seen = configured_ask()
    obj = make_project(tmp_path)
    asyncio.run(obj.analyze_summaries(ask=ask))
    path = Path(obj._analysis_path("default", True))
    # MODEL may be declared by the test runner; read the recorded path's model.
    if not path.exists():
        import os
        path = Path(obj._analysis_path(os.getenv("MODEL", "default"), True))
    original = path.read_bytes()
    count = len(seen)
    ask.prompt_budget = replace(ask.prompt_budget, context_tokens=100)
    failed = make_project(tmp_path)
    with pytest.raises(PromptBudgetExceeded):
        asyncio.run(failed.analyze_summaries(ask=ask))
    assert len(seen) == count and path.read_bytes() == original
    archive = Path(failed.last_analysis_archive)
    manifest = json.loads((archive / "manifest.json").read_text())
    assert manifest["status"] == "failed" and manifest["requests"] == 0
    assert not (archive / "bundle.json").exists()


def test_changed_budget_recomputes_cached_analysis_and_keeps_old_archive(tmp_path):
    from marta.ruby_backend.tests.test_analysis_provenance import make_project
    from marta.ruby_backend.tests.test_suite_validation import toolchain_ok
    if not toolchain_ok():
        pytest.skip("no Ruby/RSpec toolchain")
    ask, seen = configured_ask()
    first = make_project(tmp_path)
    asyncio.run(first.analyze_summaries(ask=ask))
    count = len(seen)
    second = make_project(tmp_path)
    asyncio.run(second.analyze_summaries(ask=ask))
    assert len(seen) == count
    ask.prompt_budget = replace(ask.prompt_budget, context_tokens=7000)
    third = make_project(tmp_path)
    asyncio.run(third.analyze_summaries(ask=ask))
    assert len(seen) > count
    roots = [Path(obj.last_analysis_archive) for obj in (first, second, third)]
    bundles = [json.loads((root / "bundle.json").read_text()) for root in roots]
    assert bundles[0]["fingerprint"] == bundles[1]["fingerprint"] != bundles[2]["fingerprint"]
    assert json.loads((roots[1] / "manifest.json").read_text())["cache_hit"]


def test_real_local_chat_tokenizer_integration_requires_no_model_weights(tmp_path):
    from tokenizers import Tokenizer, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast
    core = Tokenizer(models.WordLevel({"[UNK]": 0, "system": 1, "user": 2, "assistant": 3, "hello": 4}, unk_token="[UNK]"))
    core.pre_tokenizer = pre_tokenizers.Whitespace()
    tokenizer = PreTrainedTokenizerFast(tokenizer_object=core, unk_token="[UNK]", clean_up_tokenization_spaces=False)
    tokenizer.chat_template = "{% for m in messages %}{{ m['role'] }} {{ m['content'] }} {% endfor %}{% if add_generation_prompt %}assistant{% endif %}"
    tokenizer.save_pretrained(tmp_path)
    _local_tokenizer.cache_clear()
    assert LocalChatCounter(tmp_path)("hello", "hello") == 5
    _local_tokenizer.cache_clear()
