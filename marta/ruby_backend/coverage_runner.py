"""Per-method coverage synthesis for the Ruby backend (Fase 2).

Runs the generated specs under Ruby's Coverage module (``marta_coverage.rb``)
to get per-line hit counts, then intersects them with each method's line range
(from the Prism parser) to reproduce coverage.py's per-function ``missing_lines``
— the signal the coverage-guided ReAct loop targets on later rounds.

Why synthesise rather than read it off: Ruby's ``:methods`` coverage is only
hit/no-hit per method, not *which* lines are missing. The line ranges make the
missing-lines breakdown that Python gets natively. The ``:methods`` data is still
collected, because it answers a different question the lines cannot: was the
method ever INVOKED, or only loaded (see ``MethodCoverage.invoked``).
"""
from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .ruby_ast import MethodInfo, RubyParseError, ruby_bin

_HELPER = os.path.join(os.path.dirname(__file__), "rb", "marta_coverage.rb")


@dataclass
class MethodCoverage:
    """Coverage of one method, mirroring ``CoverageMessage``."""
    missing_lines: List[int] = field(default_factory=list)
    covered_lines: int = 0
    executable_lines: int = 0
    # Ramos não tomados, pela linha onde começam. Uma linha pode aparecer aqui e
    # NÃO estar em missing_lines: a linha do `if` executou, mas um dos seus lados
    # nunca correu. É exatamente o caso que a cobertura de linhas não vê.
    missing_branch_lines: List[int] = field(default_factory=list)
    covered_branches: int = 0
    total_branches: int = 0
    # O método chegou a ser CHAMADO? A linha do `def` executa quando o ficheiro é
    # carregado, por isso um método nunca chamado tem sempre essa linha coberta:
    # num de 2-3 linhas isso é metade da cobertura sem teste nenhum. None quando
    # a medição não trouxe dados de métodos. As linhas NÃO são corrigidas aqui:
    # qual das duas métricas se reporta é uma decisão, e as duas ficam gravadas.
    invoked: Optional[bool] = None

    @property
    def fully_covered(self) -> bool:
        return not self.missing_lines and not self.missing_branch_lines

    def format_missing_lines(self) -> str:
        """Collapse missing lines into ranges, e.g. "5-6, 8" — same format the
        Python side feeds the Planner as COVERAGE FEEDBACK. Ramos não tomados
        vão à parte, senão o Planner leria-os como linhas nunca executadas."""
        base = self._ranges(self.missing_lines)
        if self.missing_branch_lines:
            br = self._ranges(sorted(set(self.missing_branch_lines)))
            tail = f"branches not taken at line(s) {br}"
            return f"{base}; {tail}" if base else tail
        return base

    @staticmethod
    def _ranges(nums: List[int]) -> str:
        if not nums:
            return ""
        nums = sorted(nums)
        ranges: List[str] = []
        start = end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                ranges.append(f"{start}-{end}" if start != end else f"{start}")
                start = end = n
        ranges.append(f"{start}-{end}" if start != end else f"{start}")
        return ", ".join(ranges)


@dataclass
class CoverageResult:
    source_dir: str
    # relative-path -> per-line hit array (int hits, or None for non-executable)
    files: Dict[str, List[Optional[int]]] = field(default_factory=dict)
    # relative-path -> [[linha, execuções], ...] por ramo (0 = ramo não tomado)
    branches: Dict[str, List[List[int]]] = field(default_factory=dict)
    # relative-path -> [[linha do def, invocações], ...] por método
    methods: Dict[str, List[List[int]]] = field(default_factory=dict)


def run_line_coverage(
    source_dir: str,
    spec_paths: List[str],
    cwd: str,
    timeout: int = 120,
    isolated: bool = False,
    minitest: bool = False,
    load_paths: Optional[List[str]] = None,
    requires: Optional[List[str]] = None,
) -> CoverageResult:
    """Run specs under Coverage and return per-file per-line hit arrays.

    ``source_dir`` may be relative to ``cwd``; it is resolved to absolute and
    prepended to the load path so specs can ``require`` the code under test.
    ``isolated=True`` ignores the project's .rspec (for GENERATED specs, which
    are self-contained); leave False to measure human suites with their config.

    ``load_paths`` (extra, relative to ``cwd``) and ``requires`` (loaded before the
    specs) reproduce the environment the specs were generated in; without them a
    spec that was green during generation can fail to load when measured.
    """
    # cwd pode chegar relativo (ex.: CLI com --project_path relativo); o filtro
    # de caminhos no helper compara absolutos — absolutizar SEMPRE.
    cwd = os.path.abspath(cwd)
    abs_source = source_dir if os.path.isabs(source_dir) else os.path.join(cwd, source_dir)
    args = [ruby_bin(), _HELPER]
    if isolated:
        args.append("--isolated")
    if minitest:
        args.append("--minitest")
    for p in load_paths or []:
        args += ["--load-path", p if os.path.isabs(p) else os.path.join(cwd, p)]
    for r in requires or []:
        args += ["--require", r]
    args += [abs_source, *spec_paths]
    try:
        proc = subprocess.run(
            args, cwd=cwd, capture_output=True, text=True, errors='replace', timeout=timeout
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"Ruby binary '{ruby_bin()}' not found") from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("marta_coverage.rb timed out") from e

    # Projetos reais escrevem no stdout durante a suite (ex.: o spec_helper da
    # ruby-jwt imprime a versão do OpenSSL), o que corrompe um json.loads direto.
    # O nosso payload é o ÚLTIMO objeto JSON escrito — recorta-se defensivamente.
    data = None
    raw = proc.stdout.strip()
    if raw:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            start = raw.find('{"source_dir"')
            if start == -1:
                start = raw.find("{")
            end = raw.rfind("}")
            if start != -1 and end > start:
                try:
                    data = json.loads(raw[start:end + 1])
                except json.JSONDecodeError:
                    data = None
    if data is None:
        raise RubyParseError(
            f"marta_coverage.rb emitted non-JSON "
            f"(stdout[:200]: {raw[:200]!r}; stderr: {proc.stderr[:200]})"
        )
    # Helper wraps each file as {"lines": [...]}; unwrap to the bare hit array.
    entries = data.get("files", {})
    files = {rel: entry.get("lines", []) for rel, entry in entries.items()}
    branches = {rel: entry.get("branches", []) or [] for rel, entry in entries.items()}
    methods = {rel: entry.get("methods", []) or [] for rel, entry in entries.items()}
    return CoverageResult(source_dir=data.get("source_dir", abs_source),
                          files=files, branches=branches, methods=methods)


@dataclass
class FileCoverage:
    """Cobertura CONVENCIONAL de um ficheiro, a mesma regra do coverage.py.

    Denominador: todas as linhas executáveis do ficheiro inteiro — o topo do
    ficheiro, o corpo das classes, as linhas `def`, o `initialize`, e não só as
    linhas de dentro dos métodos-alvo. Numerador: as que correram pelo menos uma
    vez. É o que o `coverage report` do Python mostra como Stmts/Miss/Cover, e o
    que o CodaMosa e o CoverUp reportam por módulo.

    Consequência, igual nas duas linguagens: carregar o ficheiro já cobre as
    linhas que correm ao carregar (a linha `def`, as constantes, o `class`).
    """
    executable_lines: int = 0
    covered_lines: int = 0
    total_branches: int = 0
    covered_branches: int = 0

    @property
    def pct(self) -> float:
        return 100.0 * self.covered_lines / self.executable_lines if self.executable_lines else 0.0


def file_coverage(lines: Optional[List[Optional[int]]],
                  branches: Optional[List[List[int]]] = None) -> FileCoverage:
    """Cobertura convencional de um ficheiro a partir do array de linhas do
    Coverage do Ruby (null = não executável, 0 = não correu, >0 = correu)."""
    fc = FileCoverage()
    for hit in lines or []:
        if hit is None:
            continue
        fc.executable_lines += 1
        if hit > 0:
            fc.covered_lines += 1
    for entry in branches or []:
        if entry and len(entry) >= 2:
            fc.total_branches += 1
            if entry[1]:
                fc.covered_branches += 1
    return fc


def synthesize(method: MethodInfo, lines: List[Optional[int]],
               branches: Optional[List[List[int]]] = None,
               methods: Optional[List[List[int]]] = None) -> MethodCoverage:
    """Per-method missing_lines (e ramos) from a file's coverage arrays.

    Executable lines are those with a non-null entry within the method's
    ``[start_line, end_line]`` range; missing = executable with 0 hits.

    Os ramos vêm como pares ``[linha, execuções]`` do ficheiro inteiro e são
    atribuídos ao método pelo mesmo intervalo de linhas. Isto acrescenta sinal
    real: um ``if`` cuja linha executou conta como linha coberta, mas se o lado
    ``else`` nunca correu há aqui um ramo por tomar que a cobertura de linhas
    não mostrava.

    ``methods`` (pares ``[linha do def, invocações]``) só preenche ``invoked``;
    não altera as contagens de linhas.
    """
    missing: List[int] = []
    covered = 0
    executable = 0
    for line_no in range(method.start_line, method.end_line + 1):
        idx = line_no - 1
        if idx < 0 or idx >= len(lines):
            continue
        hit = lines[idx]
        if hit is None:
            continue  # non-executable
        executable += 1
        if hit == 0:
            missing.append(line_no)
        else:
            covered += 1

    missing_br: List[int] = []
    cov_br = tot_br = 0
    for entry in (branches or []):
        if not entry or len(entry) < 2:
            continue
        b_line, b_hits = entry[0], entry[1]
        if not (method.start_line <= b_line <= method.end_line):
            continue
        tot_br += 1
        if b_hits:
            cov_br += 1
        else:
            missing_br.append(b_line)

    invoked: Optional[bool] = None
    if methods is not None:
        counts = [m[1] for m in methods
                  if m and len(m) >= 2 and m[0] == method.start_line]
        invoked = (max(counts) > 0) if counts else None

    return MethodCoverage(missing_lines=missing, covered_lines=covered,
                          executable_lines=executable,
                          missing_branch_lines=missing_br,
                          covered_branches=cov_br, total_branches=tot_br,
                          invoked=invoked)
