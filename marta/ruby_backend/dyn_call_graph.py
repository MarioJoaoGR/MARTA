"""Dynamic (TracePoint) call graph + static/dynamic comparison (item 6).

Runs a driver under ``marta_tracegraph.rb`` to observe real call edges, returned
in the same ``CallGraph`` shape as the static graph so the two can be compared
directly. See ``call_graph.py`` for the static side.
"""
from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from typing import List

from .call_graph import CallEdge, CallGraph
from .ruby_ast import RubyParseError, ruby_bin

_HELPER = os.path.join(os.path.dirname(__file__), "rb", "marta_tracegraph.rb")


def run_dynamic(source_dir: str, driver_path: str, cwd: str, timeout: int = 60) -> CallGraph:
    """Trace ``driver_path`` (which exercises the code under ``source_dir``) and
    build a CallGraph from the observed edges."""
    cwd = os.path.abspath(cwd)  # o filtro de caminhos no helper compara absolutos
    abs_source = source_dir if os.path.isabs(source_dir) else os.path.join(cwd, source_dir)
    try:
        proc = subprocess.run(
            [ruby_bin(), _HELPER, abs_source, driver_path],
            cwd=cwd, capture_output=True, text=True, timeout=timeout,
        )
    except FileNotFoundError as e:
        raise RubyParseError(f"Ruby binary '{ruby_bin()}' not found") from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("marta_tracegraph.rb timed out") from e
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RubyParseError(
            f"marta_tracegraph.rb emitted non-JSON (stderr: {proc.stderr[:300]})"
        ) from e

    edges: List[CallEdge] = []
    for caller, callees in data.get("edges", {}).items():
        for callee in callees:
            edges.append(CallEdge(caller, callee, 0, "dynamic"))
    g = CallGraph(edges=edges)
    g._index()
    return g


@dataclass
class GraphComparison:
    both: set          # edges (caller, callee) in both
    static_only: set   # static found, dynamic missed (over-approx or unexercised)
    dynamic_only: set  # dynamic found, static missed (dynamic dispatch / C-methods)

    @property
    def agreement(self) -> float:
        total = len(self.both) + len(self.static_only) + len(self.dynamic_only)
        return len(self.both) / total if total else 1.0

    def summary(self) -> str:
        return (
            f"agreement={self.agreement:.0%}  "
            f"both={len(self.both)}  "
            f"static_only={len(self.static_only)}  "
            f"dynamic_only={len(self.dynamic_only)}"
        )


def compare(static_graph: CallGraph, dynamic_graph: CallGraph) -> GraphComparison:
    s, d = static_graph.edge_set(), dynamic_graph.edge_set()
    return GraphComparison(both=s & d, static_only=s - d, dynamic_only=d - s)
