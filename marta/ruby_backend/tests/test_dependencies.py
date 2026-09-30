"""Dependency facts come from installed production source, never library recipes."""
from pathlib import Path

import pytest

from marta.ruby_backend import dependencies as dep, loading


def write(root, relative, source=""):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(source)
    return path


def entry(root, name="acme", definitions=None):
    return {"gem": name, "version": "1.2.3", "require": name,
            "path": str(root / (name + ".rb")), "roots": [str(root)],
            "definitions": definitions or {}}


def facts(*references):
    return {"references": list(references), "production_files": ["lib/focal.rb"]}


def test_resolution_requires_unique_provider_and_prefers_exact_namespace(tmp_path):
    broad = entry(tmp_path, "broad", {"Acme": ["acme.rb"]})
    precise = entry(tmp_path, "precise", {"Acme::Client": ["acme/client.rb"]})
    index = {"entries": [broad, precise]}
    result = dep.resolve(index, facts("Acme::Client::Error"))
    assert [d["gem"] for d in result["resolved"]] == ["precise"]
    assert result["resolved"][0]["evidence"][0]["namespace"] == "Acme::Client"
    duplicate = entry(tmp_path, "other", {"Acme::Client": ["other.rb"]})
    result = dep.resolve({"entries": [precise, duplicate]}, facts("Acme::Client"))
    assert not result["resolved"]
    assert result["ambiguous"] == {"Acme::Client": [("other", "other"), ("precise", "precise")]}


def test_bundle_is_scoped_to_project_and_excludes_own_source(tmp_path, monkeypatch):
    monkeypatch.delenv("BUNDLE_GEMFILE", raising=False)
    def forbidden(*args):
        raise AssertionError("No project Gemfile: do not inspect host gems")
    monkeypatch.setattr(dep, "_query", forbidden)
    assert not dep.bundle_index(tmp_path)["entries"]
    outside = write(tmp_path.parent, tmp_path.name + "-Gemfile")
    monkeypatch.setenv("BUNDLE_GEMFILE", str(outside))
    assert not dep.bundle_index(tmp_path)["entries"]
    monkeypatch.delenv("BUNDLE_GEMFILE")
    write(tmp_path, "Gemfile")
    installed = tmp_path / "vendor/bundle/gems/acme-1.2.3"
    rows = [{"gem": "own", "version": "1", "gem_path": str(tmp_path),
             "roots": [], "entries": [{"require": "own", "path": "own.rb"}]},
            {"gem": "acme", "version": "1.2.3", "gem_path": str(installed),
             "roots": [str(installed / "lib")], "entries": [{"require": "acme", "path": "acme.rb"}]}]
    monkeypatch.setattr(dep, "_query", lambda mode, root: rows)
    assert [e["gem"] for e in dep.bundle_index(tmp_path)["entries"]] == ["acme"]


def test_prism_facts_ignore_comments_strings_and_keep_namespace_declarations(tmp_path):
    source = write(tmp_path, "lib/a.rb", '''
      # Wrong::Comment
      message = "Wrong::String"
      module Acme
        class Client < External::Base
          def call; External::Driver.run; end
        end
      end
    ''')
    actual = dep._query("--files", tmp_path, {"files": [str(source)]})[str(source)]
    assert actual["definitions"] == ["Acme", "Acme::Client"]
    assert "External::Base" in actual["references"]
    assert "External::Driver" in actual["references"]
    assert not any(r.startswith("Wrong") for r in actual["references"])


@pytest.mark.parametrize("filename", ["acme/data_driver.rb", "acme/datadriver.rb"])
def test_provider_requires_real_namespace_file_and_matching_declaration(tmp_path, filename):
    lib = tmp_path / "bundle/lib"
    source = write(lib, filename, "module Acme; class DataDriver; end; end")
    write(lib, "acme.rb", "require 'acme/data_driver'")
    patch_lib = tmp_path / "patch/lib"
    write(patch_lib, "patch.rb", "module Acme; class DataDriver; end; end")
    result = dep.resolve({"entries": [entry(lib), entry(patch_lib, "patch")]},
                         facts("Acme::DataDriver::Error"), tmp_path)
    assert [d["gem"] for d in result["resolved"]] == ["acme"]
    assert result["resolved"][0]["evidence"][0]["definition_files"] == [str(source)]
    source.write_text("module Different; class DataDriver; end; end")
    assert not dep.resolve({"entries": [entry(lib)]}, facts("Acme::DataDriver"), tmp_path)["resolved"]


def test_source_traversal_follows_local_base_classes_once_and_never_tests(tmp_path):
    child = write(tmp_path, "lib/sample/child.rb", "class Sample::Child < Sample::Base; end")
    base = write(tmp_path, "lib/sample/base.rb", "class Sample::Base < External::Base; Sample::Child; end")
    write(tmp_path, "spec/spec_helper.rb", "Hidden::Provider")
    actual = dep.source_references(tmp_path, child, tmp_path, [])
    assert actual["production_files"] == sorted([str(base), str(child)])
    assert "External::Base" in actual["references"]
    assert "Hidden::Provider" not in actual["references"]


def test_symlink_outside_require_root_is_not_dependency_evidence(tmp_path):
    lib = tmp_path / "lib"
    lib.mkdir()
    outside = write(tmp_path, "outside.rb", "class Acme; end")
    (lib / "acme.rb").symlink_to(outside)
    assert not dep.resolve({"entries": [entry(lib)]}, facts("Acme"), tmp_path)["resolved"]


def test_loading_plan_includes_verified_dependency_before_own_entry(tmp_path):
    write(tmp_path, "sample.gemspec")
    write(tmp_path, "lib/sample.rb")
    write(tmp_path, "lib/sample/child.rb", "class Sample::Child < External::Base; end")
    lib = tmp_path / "vendor/acme/lib"
    write(lib, "external/base.rb", "module External; class Base; end; end")
    write(lib, "acme.rb", "require 'external/base'")
    plan = loading.loading_plan(tmp_path, "lib/sample/child.rb", "sample/child",
                                {"entries": [entry(lib)]})
    assert plan["requires"] == ["acme", "sample", "sample/child"]
    context = loading.loading_context(plan)
    assert "External::Base" in context and "acme 1.2.3" in context
    assert "external/base.rb" in context
    assert not plan["dependencies"]["ambiguous"]
