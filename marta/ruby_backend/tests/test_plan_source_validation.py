"""Plan contracts and source preservation, without an LLM or a Ruby runtime."""
import asyncio
import json

import pytest

from marta.ruby_backend import generate, project, prompts, runner
from marta.ruby_backend.backend import RubyBackend
from marta.ruby_backend.recorder import RubyRecorder
from marta.ruby_backend.ruby_ast import ClassInfo, MethodInfo


SCENARIO = {"name": "positive", "desc": "positive input", "setup": "None"}
FALLBACK = [{"name": "Calc basic functionality", "desc": "Basic functionality", "setup": "None"}]


@pytest.mark.parametrize("raw", [
    "[1]", "[null]", "[true]", "[]", "not JSON", None, 4,
    json.dumps([{**SCENARIO, "setup": "\ud800"}]),
    json.dumps({"scenarios": [SCENARIO]}),
    "Here is the plan: " + json.dumps({"scenarios": [SCENARIO]}),
    json.dumps([{"name": "missing fields"}]),
    json.dumps([{**SCENARIO, "setup": None}]),
    json.dumps([{**SCENARIO, "desc": []}]),
    json.dumps([{**SCENARIO, "name": "   "}]),
    json.dumps([{**SCENARIO, "unexpected": "field"}]),
    json.dumps([SCENARIO, SCENARIO]),
    json.dumps([{**SCENARIO, "name": str(i)} for i in range(4)]),
    json.dumps([{**SCENARIO, "desc": "x" * 6001}]),
    '[{"name":"a", "name":"b", "desc":"input", "setup":"None"}]',
])
def test_invalid_plan_uses_a_complete_recorded_fallback(raw):
    plan = generate.parse_plan(raw, "Calc")
    assert plan == FALLBACK
    assert "Basic functionality" in prompts.first_dev_instruction(plan)


@pytest.mark.parametrize("wrapper", ["{}", "```json\n{}\n```", "Here is the plan:\n{}\nEnd."])
def test_valid_plan_preserves_quoted_brackets_and_code_fences(wrapper):
    scenario = {"name": "ação", "desc": "array [value]", "setup": "```ruby\nx = 1\n```"}
    raw = wrapper.format(json.dumps([scenario], ensure_ascii=False))
    assert generate.parse_plan(raw, "Calc") == [scenario]


def target(tmp_path, *, focal="def target\n  @value\nend", constructor="", statements=None,
           owner=True, name="target", kind="class"):
    prefix = f"{kind} Example\n" if owner else ""
    siblings = []
    if constructor:
        start = prefix.count("\n") + 1
        prefix += constructor + "\n"
        siblings.append(MethodInfo("initialize", "Example", False, start,
                                   start + len(constructor.splitlines()) - 1))
    start = prefix.count("\n") + 1
    path = tmp_path / "example.rb"
    path.write_text(prefix + focal + ("\nend\n" if owner else "\n"))
    method = MethodInfo(name, "Example" if owner else None, False,
                        start, start + len(focal.splitlines()) - 1)
    cls = ClassInfo("Example", "Example", kind, None, 1, start + len(focal.splitlines()),
                    body_statements=statements or []) if owner else None
    return project.MethodTarget(method, cls, str(path), "example", siblings=siblings), focal


def test_large_class_statement_cannot_remove_focal_method_or_small_constructor(tmp_path, monkeypatch):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 450)
    init = "def initialize(value)\n  @value = value\nend"
    obj, focal = target(tmp_path, constructor=init,
                        statements=['LARGE = "' + "x" * 7000 + '"', 'include Useful'])
    source = obj.context_source
    assert focal in source and init in source and "include Useful" in source
    assert "LARGE" not in source and len(source) <= 450
    assert obj.source_context.omitted_class_statements == 1


def test_large_constructor_is_omitted_whole_instead_of_cutting_the_focal_method(tmp_path, monkeypatch):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 350)
    init = "def initialize(value)\n  # " + "x" * 7000 + "\n  @value = value\nend"
    obj, focal = target(tmp_path, constructor=init)
    assert focal in obj.context_source and "def initialize" not in obj.context_source
    assert len(obj.context_source) <= 350 and obj.source_context.omitted_constructor


@pytest.mark.parametrize("owner", [False, True])
def test_oversized_focal_method_is_never_silently_truncated(tmp_path, monkeypatch, owner):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 250)
    focal = "def target\n  # " + "x" * 1200 + "\n  :complete_focal_tail\nend"
    obj, _ = target(tmp_path, owner=owner, focal=focal)
    assert focal in obj.context_source
    assert obj.source_context.over_limit
    assert obj.source_context.method_chars == len(focal)


def test_constructor_target_is_included_only_once(tmp_path):
    obj, focal = target(tmp_path, focal="def initialize(v)\n  @value = v\nend", name="initialize")
    assert focal in obj.context_source and obj.context_source.count("def initialize") == 1
    assert not obj.source_context.reduced


def test_module_declaration_retains_its_actual_kind(tmp_path):
    obj, focal = target(tmp_path, kind="module")
    assert "module Example" in obj.context_source and focal in obj.context_source


def test_context_reduction_and_soft_limit_excess_are_recorded(tmp_path, monkeypatch):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 200)
    obj, focal = target(tmp_path, focal="def target\n # " + "x" * 500 + "\n :tail\nend")
    proj = project.RubyProject(str(tmp_path), ".")
    proj.recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    assert focal in proj._source_for(obj, "plano")
    event = json.loads((tmp_path / "events.jsonl").read_text().splitlines()[-1])
    assert event["tipo"] == "source_context" and event["over_limit"]
    assert event["limit"] == 200 and event["method_chars"] == len(focal)


class AcceptingBackend(RubyBackend):
    def syntax_check(self, source):
        return None

    def run_tests(self, *args, **kwargs):
        return runner.RSpecResult(True, [runner.ExampleResult("id", "example", "passed", 1, None)],
                                  report_valid=True, exit_code=0)


def test_invalid_plan_does_not_crash_add_requests_or_hide_its_fallback(tmp_path):
    seen = []
    async def ask(system, user):
        seen.append(user)
        return "[1]" if len(seen) == 1 else 'RSpec.describe("example") { it("works") {} }'
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    outcome = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc.x", describe_subject="Calc", method_source="def self.x; 1; end",
        require_target="calc", load_paths=["."], spec_path="spec/x_spec.rb", cwd=str(tmp_path),
        ask=ask, backend=AcceptingBackend(), recorder=recorder, max_attempts=1))
    assert outcome.success and outcome.attempts == 1 and len(seen) == 2
    assert outcome.plan_fallback and outcome.plan_validation_error
    event = next(json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()
                 if json.loads(line)["tipo"] == "plan_validation")
    assert event["fallback_used"] and event["raw_plan"] == "[1]"
    assert event["effective_plan"] == FALLBACK


@pytest.mark.parametrize("count,chars", [(0, 6000), (3, 0), (True, 6000)])
def test_invalid_configuration_is_not_misreported_as_a_model_failure(count, chars):
    from marta.ruby_backend.planning import validate_plan
    with pytest.raises(ValueError, match="positive"):
        validate_plan(json.dumps([SCENARIO]), "Calc", max_scenarios=count, max_chars=chars)


def test_valid_plan_metadata_and_normalization():
    from marta.ruby_backend.planning import validate_plan
    parsed = validate_plan(json.dumps([{**SCENARIO, "name": "  positive  "}]), "Calc")
    assert not parsed.fallback_used and parsed.error is None
    assert parsed.scenarios == [SCENARIO]


def test_short_nonmethod_statements_after_a_large_one_are_not_lost(tmp_path, monkeypatch):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 350)
    obj, focal = target(tmp_path, statements=['A = "' + 'x' * 6000 + '"', 'attr_reader :value'])
    assert focal in obj.context_source and 'attr_reader :value' in obj.context_source
    assert obj.source_context.omitted_class_statements == 1


@pytest.mark.parametrize("limit", [0, -1])
def test_invalid_source_limit_is_explicit(tmp_path, monkeypatch, limit):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", limit)
    obj, _ = target(tmp_path)
    with pytest.raises(ValueError, match="positive"):
        _ = obj.context_source



def test_omission_notice_cannot_displace_a_constructor_that_fits(tmp_path, monkeypatch):
    monkeypatch.setattr(project, "MAX_CONTEXT_CHARS", 220)
    init = "def initialize(v)\n  @value = v\nend"
    obj, focal = target(tmp_path, constructor=init, statements=['LONG = "' + 'x' * 1000 + '"'])
    assert focal in obj.context_source and init in obj.context_source
    assert not obj.source_context.omitted_constructor and len(obj.context_source) <= 220
