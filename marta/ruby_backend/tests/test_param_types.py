"""Tests for parameter-type inference (item 5): member extraction + MRO + judge."""
import pytest

from marta.ruby_backend import param_types, project, runner
from marta.ruby_backend.ruby_ast import RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


PROJECT_SRC = """
module Loggable
  def log(msg); end
end

class User
  include Loggable
  def email; end
  def name; end
end

class Admin < User
  def permissions; end
end

class Notifier
  def send_to(user)
    user.email
    user.name
  end

  def audit(admin)
    admin.permissions
    admin.email
  end
end
"""


def _index():
    fp = parse_source(PROJECT_SRC, "app.rb")
    return fp, param_types.ProjectTypeIndex().add_file(fp)


def test_member_extraction_from_parser():
    fp, _ = _index()
    send_to = next(m for m in fp.methods if m.name == "send_to")
    assert set(send_to.param_members["user"]) == {"email", "name"}


def test_mro_includes_module_and_superclass():
    _, idx = _index()
    # Admin < User(include Loggable): responds to its own + inherited + mixin.
    assert idx.responds_to("Admin") >= {"permissions", "email", "name", "log"}


def test_candidate_type_from_members():
    _, idx = _index()
    # {email, name} -> User (and Admin, which inherits them)
    assert idx.candidates({"email", "name"}) == ["Admin", "User"]
    # permissions is only on Admin
    assert idx.candidates({"permissions", "email"}) == ["Admin"]


def test_judge_string_for_method():
    fp, idx = _index()
    audit = next(m for m in fp.methods if m.name == "audit")
    judge = idx.judge_for_method(audit)
    assert "`admin`" in judge
    assert "permissions" in judge and "email" in judge
    assert "likely: Admin" in judge


def test_discover_populates_judge_and_planner_summary(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.rb").write_text(PROJECT_SRC)
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    send_to = next(t for t in proj.targets if t.method.name == "send_to")
    assert "INFERRED PARAMETER TYPES" in send_to.judge
    assert "likely: Admin, User" in send_to.judge
    send_to.summary = "notifies a user"
    assert "notifies a user" in send_to.planner_summary
    assert "INFERRED PARAMETER TYPES" in send_to.planner_summary
