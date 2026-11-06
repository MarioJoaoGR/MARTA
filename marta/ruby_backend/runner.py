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


# Carregado com -r antes de cada spec (ver o próprio ficheiro): impede que o
# to_json substituído pelo ActiveSupport rebente o relatório JSON do RSpec.
_GUARD = os.path.join(os.path.dirname(__file__), "rb", "marta_rspec_guard.rb")


def rspec_bin(env=None) -> str:
    env = os.environ if env is None else env
    override = env.get("MARTA_RSPEC_BIN")
    if override:
        return override
    # O venv de Ruby (scripts/ruby_env.sh) é o sítio onde o rspec deve viver: nada
    # nosso é instalado no store global do rbenv. Procurá-lo aqui ANTES do irmão
    # do `ruby` faz a ferramenta funcionar com o venv activo mesmo sem
    # MARTA_RSPEC_BIN definido.
    venv = env.get("MARTA_RUBY_ENV")
    if venv:
        candidate = os.path.join(venv, "bin", "rspec")
        if os.path.exists(candidate):
            return candidate
    resolved = shutil.which(ruby_bin(env), path=env.get("PATH", os.defpath)) or ruby_bin(env)
    sibling = os.path.join(os.path.dirname(os.path.abspath(resolved)), "rspec")
    return sibling if os.path.exists(sibling) else "rspec"


# --------------------------------------------------------------------------- #
# Syntax check
# --------------------------------------------------------------------------- #
def syntax_check(source: str, timeout: int = 15, *, env=None) -> Optional[str]:
    """Return None if ``source`` is syntactically valid Ruby, else the error.

    Mirrors ``find_syntax_error``: cheap, parse-only, no execution.
    """
    try:
        proc = subprocess.run(
            [ruby_bin(env), "-c"],
            input=source,
            capture_output=True,
            text=True, errors='replace',
            timeout=timeout, env=env,
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"Ruby binary '{ruby_bin(env)}' not found") from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("ruby -c timed out") from e
    if proc.returncode == 0:
        return None
    msg = (proc.stderr or proc.stdout).strip()
    return msg or "syntax error"


def syntax_check_file(path: str, timeout: int = 15, *, env=None) -> Optional[str]:
    with open(path, "r", encoding="utf-8") as f:
        return syntax_check(f.read(), timeout=timeout, env=env)


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
    exception_class: Optional[str] = None


@dataclass
class RSpecResult:
    all_passed: bool
    examples: List[ExampleResult] = field(default_factory=list)
    output: str = ""
    # errors that happened outside any example (e.g. a require that blew up)
    load_error: bool = False
    exit_code: Optional[int] = None
    report_valid: bool = False
    validation_error: Optional[str] = None
    timed_out: bool = False

    @property
    def results(self) -> Dict[str, str]:
        """{id: status} — the analogue of pytest's {nodeid: outcome}."""
        return {e.id: e.status for e in self.examples}

    @property
    def failed(self) -> List[ExampleResult]:
        return [e for e in self.examples if e.status == "failed"]


def _extract_json(stdout: str) -> Optional[dict]:
    """Read an object, tolerating console text around a formatter payload."""
    stdout = stdout.strip()
    if not stdout:
        return None
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        start, end = stdout.find("{"), stdout.rfind("}")
        if start == -1 or end <= start:
            return None
        try:
            data = json.loads(stdout[start:end + 1])
        except json.JSONDecodeError:
            return None
    return data if isinstance(data, dict) else None


def rspec_result(data, exit_code: Optional[int], output: str = "", *,
                 interrupted: bool = False) -> RSpecResult:
    """Validate the formatter report independently of the process exit code.

    At least one example must actually pass. Pending examples are retained as
    pending, but cannot make a pending-only suite successful. Incomplete or
    contradictory reports and interrupted runs never certify generated tests.
    """
    examples = []
    summary = {}
    problem = None
    try:
        if not isinstance(data, dict):
            raise ValueError("missing RSpec JSON object")
        rows, summary = data.get("examples"), data.get("summary")
        if not isinstance(rows, list) or not isinstance(summary, dict):
            raise ValueError("missing RSpec examples or summary")
        fields = ("example_count", "failure_count", "pending_count", "errors_outside_of_examples_count")
        if any(type(summary.get(key)) is not int or summary[key] < 0 for key in fields):
            raise ValueError("invalid or missing RSpec summary counts")
        ids = set()
        for row in rows:
            if (not isinstance(row, dict) or not isinstance(row.get("status"), str)
                    or row["status"] not in {"passed", "failed", "pending"}):
                raise ValueError("invalid or incomplete RSpec example")
            identity = row.get("id")
            if not isinstance(identity, str) or not identity or identity in ids:
                raise ValueError("missing or duplicate RSpec example identity")
            ids.add(identity)
            exception = row.get("exception") or {}
            if not isinstance(exception, dict):
                raise ValueError("invalid RSpec exception")
            examples.append(ExampleResult(
                id=identity, full_description=row.get("full_description", ""),
                status=row["status"], line_number=row.get("line_number"),
                message=exception.get("message"),
                exception_class=exception.get("class") if isinstance(exception.get("class"), str) else None))
        if (summary["example_count"] != len(examples)
                or summary["failure_count"] != sum(e.status == "failed" for e in examples)
                or summary["pending_count"] != sum(e.status == "pending" for e in examples)):
            raise ValueError("RSpec summary does not match its example results")
    except ValueError as exc:
        problem = str(exc)
    report_valid = problem is None
    load_error = (not report_valid or bool(summary.get("errors_outside_of_examples_count")))
    if problem is None:
        if interrupted:
            problem = "RSpec execution was interrupted"
        elif type(exit_code) is not int or exit_code != 0:
            problem = f"RSpec exited with status {exit_code}"
        elif load_error:
            problem = "RSpec reported errors outside examples"
        elif any(e.status == "failed" for e in examples):
            problem = "RSpec reported failing examples despite exit status zero"
        elif not any(e.status == "passed" for e in examples):
            problem = "RSpec executed no passing examples"
    if problem:
        output = (output.rstrip() + "\n[MARTA validation] " + problem).lstrip()
    return RSpecResult(all_passed=problem is None, examples=examples, output=output,
                       load_error=load_error, exit_code=exit_code,
                       report_valid=report_valid, validation_error=problem)


def run_rspec(
    spec_path: str,
    load_paths: Optional[List[str]] = None,
    cwd: Optional[str] = None,
    timeout: int = 60,
    requires: Optional[List[str]] = None,
    use_bundle: bool = False,
    isolated: bool = True,
    use_guard: bool = True,
    *, env=None,
) -> RSpecResult:
    """Run one spec file under ``rspec -f json`` and parse the results.

    ``load_paths`` become ``-I`` flags (the ``PYTHONPATH`` analogue) so the spec
    can ``require`` the code under test. ``requires`` become ``-r`` flags, loaded
    before the spec: the gem's entry point, as in the environment the dataset
    certified. Success requires a complete, consistent formatter report, at
    least one passing example, no failures/load errors, and exit status zero.
    """
    # -O /dev/null: a "vacina" (analoga ao -c /dev/null do pytest na MARTA
    # Python) — ignora o .rspec do projeto-alvo, para os specs gerados serem
    # auto-contidos e nao dependerem do spec_helper/config da suite humana.
    # O JSON vai para FICHEIRO (-o), não para o stdout. O código sob teste escreve
    # no stdout ao ser carregado — a `httparty` traz um exemplo que tenta ligar-se
    # à rede e imprime o relatório do erro, com chavetas lá dentro. Isso corrompia
    # o JSON e um spec verde era lido como falha de carregamento.
    import tempfile
    fd, json_path = tempfile.mkstemp(prefix="marta_rspec_", suffix=".json")
    os.close(fd)
    # Dois formatos: o progress (texto legível, com as falhas e os backtraces) no
    # stdout, para o erro que volta ao modelo; o json no ficheiro, para ler os
    # resultados. O -o aplica-se ao formato anterior (o json).
    args = ["bundle", "exec", "rspec"] if use_bundle else [rspec_bin(env)]
    if isolated:
        args += ["-O", os.devnull]
    args += ["-f", "progress", "-f", "json", "-o", json_path]
    if use_guard:
        args += ["-r", _GUARD]
    for p in load_paths or []:
        args += ["-I", p]
    for r in requires or []:
        args += ["-r", r]
    args.append(spec_path)

    try:
        proc = subprocess.run(
            args, cwd=cwd, capture_output=True, text=True, errors='replace', timeout=timeout, env=env
        )
    except FileNotFoundError as e:
        os.unlink(json_path)
        raise RubyParseError(f"rspec binary '{rspec_bin(env)}' not found") from e
    except subprocess.TimeoutExpired:
        os.unlink(json_path)
        return RSpecResult(all_passed=False, output="time exceeded",
                           validation_error="RSpec timed out", timed_out=True)

    try:
        with open(json_path, encoding="utf-8", errors="replace") as f:
            bruto = f.read()
    except OSError:
        bruto = ""
    finally:
        try:
            os.unlink(json_path)
        except OSError:
            pass
    # Fallback ao stdout: versões antigas do rspec, ou um -o que não pegou.
    data = _extract_json(bruto) or _extract_json(proc.stdout)
    # O texto do erro que volta ao modelo na reparação é o relatório legível do
    # RSpec (stdout) e o stderr, o análogo do texto do pytest na MARTA Python.
    # Antes ia o JSON inteiro: com os backtraces de todos os exemplos em JSON, uma
    # falha grande enchia a janela de 16k tokens e o modelo recebia um prompt
    # cortado (visto no piloto do Deucalion: prompt 16383 tokens, resposta 1).
    # Se o stdout vier vazio (não devia, com o progress), fica o JSON.
    full_output = "\n".join(
        x for x in (proc.stdout.strip(), proc.stderr.strip()) if x) or bruto.strip()

    return rspec_result(data, proc.returncode, full_output)
