"""Per-method coverage synthesis for the Ruby backend (Fase 2).

Runs the generated specs under Ruby's Coverage module (``marta_coverage.rb``)
to get per-line hit counts, then intersects them with each method's line range
(from the Prism parser) to reproduce coverage.py's per-function ``missing_lines``
— the signal the coverage-guided ReAct loop targets on later rounds.

Why synthesise rather than read it off: Ruby's ``:methods`` coverage is only
hit/no-hit per method, not *which* lines are missing. The line ranges make the
missing-lines breakdown that Python gets natively.
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

    @property
    def fully_covered(self) -> bool:
        return not self.missing_lines

    def format_missing_lines(self) -> str:
        """Collapse missing lines into ranges, e.g. "5-6, 8" — same format the
        Python side feeds the Planner as COVERAGE FEEDBACK."""
        if not self.missing_lines:
            return ""
        nums = sorted(self.missing_lines)
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


def run_line_coverage(
    source_dir: str,
    spec_paths: List[str],
    cwd: str,
    timeout: int = 120,
    isolated: bool = False,
    minitest: bool = False,
) -> CoverageResult:
    """Run specs under Coverage and return per-file per-line hit arrays.

    ``source_dir`` may be relative to ``cwd``; it is resolved to absolute and
    prepended to the load path so specs can ``require`` the code under test.
    ``isolated=True`` ignores the project's .rspec (for GENERATED specs, which
    are self-contained); leave False to measure human suites with their config.
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
    args += [abs_source, *spec_paths]
    try:
        proc = subprocess.run(
            args, cwd=cwd, capture_output=True, text=True, timeout=timeout
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"Ruby binary '{ruby_bin()}' not found") from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("marta_coverage.rb timed out") from e

    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RubyParseError(
            f"marta_coverage.rb emitted non-JSON (stderr: {proc.stderr[:300]})"
        ) from e
    # Helper wraps each file as {"lines": [...]}; unwrap to the bare hit array.
    files = {rel: entry.get("lines", []) for rel, entry in data.get("files", {}).items()}
    return CoverageResult(source_dir=data.get("source_dir", abs_source), files=files)


def synthesize(method: MethodInfo, lines: List[Optional[int]]) -> MethodCoverage:
    """Per-method missing_lines from a file's per-line hit array.

    Executable lines are those with a non-null entry within the method's
    ``[start_line, end_line]`` range; missing = executable with 0 hits.
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
    return MethodCoverage(missing_lines=missing, covered_lines=covered, executable_lines=executable)
