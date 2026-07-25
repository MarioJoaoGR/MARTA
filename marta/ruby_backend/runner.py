"""Syntax check and RSpec execution for the Ruby backend.

The Ruby counterparts to MARTA's ``Testcase.find_syntax_error`` (``ast.parse``)
and ``run_pytest_with_results`` (``pytest --json-report``):

* ``syntax_check`` shells out to ``ruby -c`` — instantaneous, catches every
  ``SyntaxError`` the way ``ast.parse`` does (import/name errors surface later,
  when RSpec actually runs, with more actionable tracebacks).
* ``run_rspec`` runs ``rspec -f json`` and maps ``examples[] -> {id: status}``,
  the analogue of pytest's ``{nodeid: outcome}``. Load path (``-I``) plays the
  role of ``PYTHONPATH`` so specs can ``require`` the code under test.

Binaries come from ``$MARTA_RUBY_BIN`` / ``$MARTA_RSPEC_BIN`` (defaulting to the
executable sitting next to the Ruby, else ``ruby``/``rspec`` on PATH), so a
pinned rbenv/asdf Ruby is used consistently.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .ruby_ast import RubyParseError, ruby_bin


def rspec_bin() -> str:
    override = os.getenv("MARTA_RSPEC_BIN")
    if override:
        return override
    resolved = shutil.which(ruby_bin()) or ruby_bin()
    sibling = os.path.join(os.path.dirname(os.path.abspath(resolved)), "rspec")
    return sibling if os.path.exists(sibling) else "rspec"


# --------------------------------------------------------------------------- #
# Syntax check
# --------------------------------------------------------------------------- #
def syntax_check(source: str, timeout: int = 15) -> Optional[str]:
    """Return None if ``source`` is syntactically valid Ruby, else the error.

    Mirrors ``find_syntax_error``: cheap, parse-only, no execution.
    """
    try:
        proc = subprocess.run(
            [ruby_bin(), "-c"],
            input=source,
            capture_output=True,
            text=True, errors='replace',
            timeout=timeout,
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"Ruby binary '{ruby_bin()}' not found") from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("ruby -c timed out") from e
    if proc.returncode == 0:
        return None
    msg = (proc.stderr or proc.stdout).strip()
    return msg or "syntax error"


def syntax_check_file(path: str, timeout: int = 15) -> Optional[str]:
    with open(path, "r", encoding="utf-8") as f:
        return syntax_check(f.read(), timeout=timeout)


# --------------------------------------------------------------------------- #
# RSpec runner
# --------------------------------------------------------------------------- #
@dataclass
class ExampleResult:
    id: str                       # e.g. "./spec/foo_spec.rb[1:2]"
    full_description: str
    status: str                   # "passed" | "failed" | "pending"
    line_number: Optional[int]
    message: Optional[str]        # exception message on failure, else None


@dataclass
class RSpecResult:
    all_passed: bool
    examples: List[ExampleResult] = field(default_factory=list)
    output: str = ""
    # errors that happened outside any example (e.g. a require that blew up)
    load_error: bool = False

    @property
    def results(self) -> Dict[str, str]:
        """{id: status} — the analogue of pytest's {nodeid: outcome}."""
        return {e.id: e.status for e in self.examples}

    @property
    def failed(self) -> List[ExampleResult]:
        return [e for e in self.examples if e.status == "failed"]


def _extract_json(stdout: str) -> Optional[dict]:
    """RSpec's json formatter writes pure JSON to stdout, but a stray warning
    can precede it — carve out the object defensively."""
    stdout = stdout.strip()
    if not stdout:
        return None
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        start, end = stdout.find("{"), stdout.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(stdout[start:end + 1])
            except json.JSONDecodeError:
                return None
    return None


def run_rspec(
    spec_path: str,
    load_paths: Optional[List[str]] = None,
    cwd: Optional[str] = None,
    timeout: int = 60,
) -> RSpecResult:
    """Run one spec file under ``rspec -f json`` and parse the results.

    ``load_paths`` become ``-I`` flags (the ``PYTHONPATH`` analogue) so the spec
    can ``require`` the code under test. ``all_passed`` follows RSpec's exit code
    (0 only when every example passed and nothing errored outside examples).
    """
    # -O /dev/null: a "vacina" (analoga ao -c /dev/null do pytest na MARTA
    # Python) — ignora o .rspec do projeto-alvo, para os specs gerados serem
    # auto-contidos e nao dependerem do spec_helper/config da suite humana.
    args = [rspec_bin(), "-O", os.devnull, "-f", "json"]
    for p in load_paths or []:
        args += ["-I", p]
    args.append(spec_path)

    try:
        proc = subprocess.run(
            args, cwd=cwd, capture_output=True, text=True, errors='replace', timeout=timeout
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"rspec binary '{rspec_bin()}' not found") from e
    except subprocess.TimeoutExpired:
        return RSpecResult(all_passed=False, output="time exceeded")

    data = _extract_json(proc.stdout)
    full_output = (proc.stdout + "\n" + proc.stderr).strip()

    if data is None:
        # No parseable JSON: a hard failure (usually a load/require error).
        return RSpecResult(all_passed=False, output=full_output, load_error=True)

    examples = [
        ExampleResult(
            id=ex.get("id", ""),
            full_description=ex.get("full_description", ""),
            status=ex.get("status", ""),
            line_number=ex.get("line_number"),
            message=(ex.get("exception") or {}).get("message"),
        )
        for ex in data.get("examples", [])
    ]
    summary = data.get("summary", {})
    load_error = summary.get("errors_outside_of_examples_count", 0) > 0
    return RSpecResult(
        all_passed=(proc.returncode == 0),
        examples=examples,
        output=full_output,
        load_error=load_error,
    )
