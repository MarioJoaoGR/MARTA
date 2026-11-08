"""Real Ruby generation and suite validation across an interrupted method prefix."""
import asyncio
import json
from pathlib import Path

import pytest

from marta.ruby_backend.checkpoints import ResumeValidationError
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

pytestmark = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")

PLAN = '[{"name":"value", "desc":"check value", "setup":"none"}]'
FIRST = """require "calc"
$marta_checkpoint_fixture = :first
RSpec.describe Calc do
  it("checks a") { expect(Calc.a).to eq($marta_checkpoint_fixture) }
end
"""
FAILURE = """require "calc"
RSpec.describe Calc do
  it("fails b") { expect(Calc.b).to eq(:wrong) }
end
"""
LAST = """require "calc"
RSpec.describe Calc do
  it("checks c") { expect(Calc.c).to eq(:last) }
end
"""


@pytest.mark.parametrize("isolated", [False, True])
def test_resume_keeps_terminal_outcomes_and_revalidates_accumulated_suite(tmp_path, isolated):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/calc.rb").write_text(
        "class Calc; def self.a; :first; end; def self.b; :second; end; def self.c; :last; end; end"
    )

    def project():
        return RubyProject(str(tmp_path), "src", isolate_execution=isolated).discover()

    obj = project()
    replies = iter([PLAN, FIRST, PLAN, FAILURE])

    async def interrupted(system, user):
        reply = next(replies, None)
        if reply is None:
            raise RuntimeError("interrupted")
        return reply

    def run(obj, ask):
        return asyncio.run(obj.generate_rounds(rounds=1, max_attempts=1, ask=ask, resume_methods=True))

    with pytest.raises(RuntimeError, match="interrupted"):
        run(obj, interrupted)

    root = Path(obj.out_root()) / ".marta_generation"
    journal = root / "methods" / "0"
    first = json.loads((journal / "0.json").read_text())
    assert first["outcome"]["success"]
    assert not json.loads((journal / "1.json").read_text())["outcome"]["success"]
    assert not (root / "rounds.json").exists()

    async def unexpected(system, user):
        pytest.fail("An invalid journal must stop before another model request")

    path = journal / "0.json"
    path.write_text(json.dumps(dict(first, digest="corrupt")))
    with pytest.raises(ResumeValidationError, match="checksum"):
        run(project(), unexpected)
    path.write_text(json.dumps(first))

    # In the isolated case the later spec passes alone but breaks the
    # recovered spec when both files load in the final suite.
    last = '$marta_checkpoint_fixture = :last\n' + LAST if isolated else LAST
    replies = iter([PLAN, last])
    calls = []

    async def resumed(system, user):
        calls.append(user)
        return next(replies)

    obj = project()
    outcomes = run(obj, resumed)
    assert len(calls) == 2 and len(outcomes) == 1
    assert outcomes[0].method == "Calc.c" and outcomes[0].success is not isolated
    assert not journal.exists()
    certified = json.loads((root / "rounds.json").read_text())
    assert [(r["method"], r["success"]) for r in certified["rounds"][0]["outcomes"]] == [
        ("Calc.a", True), ("Calc.b", False), ("Calc.c", not isolated)
    ]
    assert len(certified["files"]) == (1 if isolated else 2)
    assert run(project(), unexpected) == []
