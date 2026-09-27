import hashlib
import json
import os

import pytest

from benchmark.xrepotest import runtime
from benchmark.xrepotest.environment.prepare_mutation import locked_versions
from benchmark.xrepotest.environment.repair_evaluator import corrected_source


@pytest.fixture
def repaired(tmp_path, monkeypatch):
    root = tmp_path / "task" / "repo"
    root.mkdir(parents=True)
    lock = root / "Gemfile.xrepotest.lock"
    lock.write_text("fixed dependencies\n")
    manifest = tmp_path / "environment.json"
    manifest.write_text(json.dumps({"projects": {"hanami": {
        "ruby_prefix": "/opt/xrepo/ruby33", "bundle_config": "/opt/xrepo/hanami-config",
        "gemfile": "Gemfile.xrepotest",
        "env": {"COVERAGE": "false"},
        "lock_sha256": hashlib.sha256(lock.read_bytes()).hexdigest(),
    }}}))
    monkeypatch.setattr(runtime, "MANIFEST", manifest)
    return root


def test_runtime_uses_disposable_task_gemfile_and_restores_after_exception(repaired, monkeypatch):
    monkeypatch.setenv("GEM_HOME", "/original/gems")
    monkeypatch.setenv("MARTA_RUBY_BIN", "/old/ruby")
    before = dict(os.environ)
    with pytest.raises(RuntimeError, match="diagnostic"):
        with runtime.project_environment(repaired, "hanami"):
            assert os.environ["BUNDLE_GEMFILE"] == str(repaired / "Gemfile.xrepotest")
            assert os.environ["PATH"].startswith("/opt/xrepo/ruby33/bin:")
            assert "GEM_HOME" not in os.environ
            assert "MARTA_RUBY_BIN" not in os.environ
            assert os.environ["BUNDLE_FROZEN"] == "true"
            assert os.environ["COVERAGE"] == "false"
            raise RuntimeError("diagnostic")
    assert dict(os.environ) == before


def test_runtime_rejects_modified_lock(repaired):
    (repaired / "Gemfile.xrepotest.lock").write_text("different dependencies")
    with pytest.raises(ValueError, match="lock differs"):
        runtime.project_env(repaired, "hanami")


def test_original_image_environment_is_preserved(tmp_path, monkeypatch):
    monkeypatch.setattr(runtime, "MANIFEST", tmp_path / "absent.json")
    base = {"PATH": "/old/bin", "GEM_HOME": "/old/gems"}
    assert runtime.project_env(tmp_path, "hashie", base) == base


def test_evaluator_repair_rejects_unknown_upstream():
    with pytest.raises(ValueError, match="Unexpected upstream"):
        corrected_source(b"# different evaluator version\n")


def test_evaluation_rejects_modified_or_missing_evaluator_file(tmp_path, monkeypatch):
    manifest = tmp_path / "environment.json"
    expected = {"ruby/command_utils.py": "fixed-hash", "base/metrics.py": "original-hash"}
    manifest.write_text(json.dumps({"evaluator": {"files_after": expected}}))
    monkeypatch.setattr(runtime, "MANIFEST", manifest)
    runtime.validate_evaluator(dict(expected))
    for changed in ({**expected, "base/metrics.py": "different"},
                    {"ruby/command_utils.py": "fixed-hash"}):
        with pytest.raises(ValueError, match="Evaluator files differ"):
            runtime.validate_evaluator(changed)


def test_lock_comparison_includes_git_and_path_versions(tmp_path):
    lock = tmp_path / "Gemfile.lock"
    lock.write_text("GIT\n  specs:\n    example (2.3.2)\n      helper (~> 1)\n"
                    "GEM\n  specs:\n    helper (1.1.0-x86_64-linux)\nDEPENDENCIES\n  example!\n")
    assert locked_versions(lock) == {"example": "2.3.2", "helper": "1.1.0-x86_64-linux"}


def test_feedback_uses_nearest_gemfile_for_monorepo(tmp_path):
    from benchmark.xrepotest.backend import XRepoBackend
    (tmp_path / "Gemfile").write_text("gemspec")
    (tmp_path / "core/lib").mkdir(parents=True)
    (tmp_path / "core/Gemfile").write_text('eval_gemfile "../Gemfile"')
    backend = XRepoBackend()
    backend.focal_source_rel = "core/lib/example.rb"
    package = backend._package_root(str(tmp_path))
    assert package == str(tmp_path / "core")
    source = tmp_path / "generated.rb"
    source.write_text('RSpec.describe("example") {}')
    staged = backend._stage([source], package)
    assert staged == str(tmp_path / "core/spec/temp_spec.rb")
