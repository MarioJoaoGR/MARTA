"""Tests for refinements 2 (what_todo propagation via graph) and 3 (class
summaries + semantic type hints)."""
import asyncio

import pytest

from marta.ruby_backend import project, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


SRC = """\
class Wallet
  def deposit(amount)
    apply(amount)
  end

  def apply(amount)
    @balance = amount
  end
end
"""


def _project(tmp_path, src=SRC):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "wallet.rb").write_text(src)
    return project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()


# --- item 2: what_todo propagation ----------------------------------------- #
def test_called_method_inherits_requirement_from_caller(tmp_path):
    proj = _project(tmp_path)
    # sanity: deposit -> apply edge exists
    assert "Wallet#apply" in proj.call_graph.callees("Wallet#deposit")

    prompts_by_kind = {"root": [], "propagated": []}

    async def ask(system, user):
        if "called method" in user and "Intent of the caller" in user:
            prompts_by_kind["propagated"].append(user)
            return "WT-PROPAGATED"
        if "intended to do" in user or "two summaries" in user.lower():
            return "MERGED"
        if "Analyze its purpose" in user or "Project Overview" in user:
            prompts_by_kind["root"].append(user)
            return "WT-ROOT"
        return "DW"

    asyncio.run(proj.analyze_summaries(ask=ask, use_cache=False))
    by_name = {t.method.qualified_name: t for t in proj.targets}
    assert by_name["Wallet#deposit"].what_todo == "WT-ROOT"        # raiz: README/plain
    assert by_name["Wallet#apply"].what_todo == "WT-PROPAGATED"    # callee: propagado
    # And the propagation prompt carried the caller's intent.
    assert any("WT-ROOT" in p and "Wallet#deposit" in p for p in prompts_by_kind["propagated"])


# --- item 3: class summaries + semantic hints ------------------------------ #
AMBIG_SRC = """\
class Sender
  def name; end
end

class Receiver
  def name; end
end

class Router
  def route(node)
    node.name
  end
end
"""


def test_class_summaries_computed_and_cached(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "test-model")
    proj = _project(tmp_path)
    calls = {"class": 0}

    async def ask(system, user):
        if "Ruby classes" in system:
            calls["class"] += 1
            return "CLASS-SUMMARY"
        return "x"

    asyncio.run(proj.analyze_summaries(ask=ask))
    assert proj.class_summaries == {"Wallet": "CLASS-SUMMARY"}
    assert calls["class"] == 1

    # Second run: class summaries come from the cache too.
    proj2 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj2.analyze_summaries(ask=ask))
    assert proj2.class_summaries == {"Wallet": "CLASS-SUMMARY"}
    assert calls["class"] == 1  # no new LLM call


def test_semantic_hint_added_when_structurally_ambiguous(tmp_path):
    proj = _project(tmp_path, src=AMBIG_SRC)
    route = next(t for t in proj.targets if t.method.name == "route")
    # Structural inference is ambiguous: both Sender and Receiver respond to name.
    assert "likely: Receiver, Sender" in route.judge

    proj.class_summaries = {
        "Sender": "sends messages to the network",
        "Receiver": "receives incoming node traffic by name",
        "Router": "routes nodes",
    }
    vocab = ["node", "name", "receives", "sends", "routes", "parameter", "responding"]

    def vec(text):
        t = text.lower()
        return [float(t.count(w)) for w in vocab]

    proj.build_rag(lambda docs: [vec(d) for d in docs], vec)
    assert "semantically closest class:" in route.judge
