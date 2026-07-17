"""Smoke tests for the Prism-based Ruby parser wrapper.

Requires a Ruby >= 3.3 reachable via $MARTA_RUBY_BIN or `ruby` on PATH.
Skips (rather than fails) when no suitable Ruby is available, so the Python
suite stays green on machines without the Ruby toolchain.
"""
import os

import pytest

from marta.ruby_backend import ruby_ast

FIXTURE = os.path.join(os.path.dirname(ruby_ast.__file__), "rb", "fixtures", "sample.rb")


def _ruby_ok() -> bool:
    try:
        ruby_ast.parse_source("def x; end", "probe")
        return True
    except ruby_ast.RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _ruby_ok(), reason="no Ruby >= 3.3 with Prism available")


def test_fixture_parses_clean():
    fp = ruby_ast.parse_file(FIXTURE)
    assert fp.ok, fp.errors


def test_classes_and_mixins():
    fp = ruby_ast.parse_file(FIXTURE)
    by_name = {c.name: c for c in fp.classes}
    assert by_name["Greetable"].kind == "module"
    calc = by_name["Calculator"]
    assert calc.kind == "class"
    assert calc.superclass == "Numeric"
    assert calc.includes == ["Greetable"]
    assert calc.extends == ["Comparable"]


def test_method_param_kinds():
    fp = ruby_ast.parse_file(FIXTURE)
    compute = next(m for m in fp.methods if m.name == "compute")
    assert [(p.name, p.kind) for p in compute.params] == [
        ("a", "req"), ("b", "opt"), ("rest", "rest"),
        ("k", "keyreq"), ("k2", "key"), ("opts", "keyrest"), ("blk", "block"),
    ]
    assert compute.owner == "Calculator"
    assert compute.qualified_name == "Calculator#compute"


def test_singleton_and_toplevel():
    fp = ruby_ast.parse_file(FIXTURE)
    version = next(m for m in fp.methods if m.name == "version")
    assert version.singleton is True
    assert version.qualified_name == "Calculator.version"

    top = next(m for m in fp.methods if m.name == "top_level_helper")
    assert top.owner is None
    assert top.qualified_name == "top_level_helper"


def test_syntax_error_reported_not_raised():
    fp = ruby_ast.parse_source("def broken(", "bad.rb")
    assert not fp.ok
    assert fp.errors  # helper returns errors instead of crashing
