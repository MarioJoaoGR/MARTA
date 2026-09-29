"""Production loading guidance and failure evidence, without a live model."""
import asyncio
import json

import pytest

from marta.ruby_backend import generate, loading, prompts, runner
from marta.ruby_backend.recorder import RubyRecorder


def write(root, rel, text=""):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def test_nearest_subgem_entry_namespace_order_and_no_test_helpers(tmp_path):
    write(tmp_path, "outer.gemspec")
    write(tmp_path, "core/rom-core.gemspec")
    write(tmp_path, "core/lib/rom/core.rb")
    write(tmp_path, "core/lib/rom/nested.rb")
    write(tmp_path, "core/lib/rom/nested/leaf.rb")
    write(tmp_path, "core/spec/spec_helper.rb", "raise 'must never be loaded'")
    plan = loading.loading_plan(tmp_path, "core/lib/rom/nested/leaf.rb", "rom/nested/leaf")
    assert plan["package"] == "core"
    assert plan["entry_file"] == "core/lib/rom/core.rb"
    assert plan["requires"] == ["rom/core", "rom/nested", "rom/nested/leaf"]
    text = loading.loading_context(plan)
    assert 'require "rom/core"' in text
    assert "spec_helper" not in text and "preload" in text


def test_ambiguous_entries_are_not_guessed(tmp_path):
    for name in ("alpha", "beta"):
        write(tmp_path, name + ".gemspec")
        write(tmp_path, "lib/" + name + ".rb")
    write(tmp_path, "lib/unrelated.rb")
    plan = loading.loading_plan(tmp_path, "lib/unrelated.rb", "unrelated")
    assert plan["entry"] is None
    assert loading.loading_context(plan) == ""
    write(tmp_path, "lib/beta/child.rb")
    assert loading.loading_plan(tmp_path, "lib/beta/child.rb", "beta/child")["entry"] == "beta"


@pytest.mark.parametrize("declared,references,expected", [
    (False, True, []), (True, False, []), (True, True, ["dry/system"]),
])
def test_optional_integration_requires_both_declared_dependency_and_production_reference(
        tmp_path, declared, references, expected):
    write(tmp_path, "sample.gemspec", "s.add_dependency 'dry-system'" if declared else "")
    write(tmp_path, "lib/sample.rb")
    write(tmp_path, "lib/sample/provider.rb", "class Sample::Provider < Dry::System::Provider; end" if references else "")
    write(tmp_path, "lib/sample/child.rb", "class Sample::Child < Sample::Provider; end")
    # A test reference alone must not supply a production integration.
    write(tmp_path, "spec/spec_helper.rb", "require 'dry/system'; Dry::System")
    plan = loading.loading_plan(tmp_path, "lib/sample/child.rb", "sample/child")
    assert plan["integrations"] == expected
    assert plan["requires"] == expected + ["sample", "sample/child"]


def test_target_outside_project_rejected(tmp_path):
    with pytest.raises(ValueError, match="inside the project"):
        loading.loading_plan(tmp_path, "../outside.rb", "outside")


def test_loading_guidance_reaches_planner_and_each_dev_attempt_and_preserves_failure(tmp_path):
    from marta.ruby_backend.backend import RubyBackend

    class Backend(RubyBackend):
        def syntax_check(self, code):
            return None

        def run_tests(self, test_path, load_paths, cwd):
            return runner.RSpecResult(all_passed=False, output="uninitialized constant Config", load_error=True)

    calls = []
    async def ask(system, user):
        calls.append((system, user))
        if len(calls) == 1:
            return '[{"name":"behavior"}]'
        return '```ruby\nrequire "sample"\nRSpec.describe Config do; end\n```'

    rec = RubyRecorder(str(tmp_path / "events.jsonl"))
    hint = "PRODUCTION LOADING CONTEXT: require sample before sample/internal"
    out = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Sample#x", describe_subject="Sample", method_source="def x; end",
        require_target="sample/internal", load_paths=["lib"], spec_path="spec/x_spec.rb",
        cwd=str(tmp_path), ask=ask, backend=Backend(), loading_context=hint,
        recorder=rec, max_attempts=2))
    assert not out.success and out.attempts == 2
    assert len(calls) == 3 and all(hint in user for _, user in calls)
    assert "uninitialized constant Config" in calls[-1][1]
    assert not (tmp_path / "spec/x_spec.rb").exists()
    checks = [json.loads(l) for l in (tmp_path / "events.jsonl").read_text().splitlines()
              if json.loads(l)["tipo"] == "generation_validation"]
    assert len(checks) == 2 and [e["tentativa"] for e in checks] == [1, 2]
    assert all(e["code"].startswith('require "sample"') and e["load_error"] for e in checks)
    assert all(e["output"] == "uninitialized constant Config" for e in checks)


def test_default_dev_prompt_retains_focal_require():
    assert 'require "sample/internal"' in prompts.dev_user("instruction", "source", "sample/internal", "Sample")
