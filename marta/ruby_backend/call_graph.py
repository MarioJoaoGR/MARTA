"""Call graph for the Ruby backend (item 6).

Two implementations, so we can compare precision/coverage and keep the best:

* ``StaticCallGraph`` — resolves each call recorded by the parser to a target
  method, best-effort, using the class/MRO index and parameter-type inference we
  already have. Static and deterministic (no execution), the faithful analogue
  of PyCG — and, like PyCG, it cannot see through fully dynamic dispatch.
* ``DynamicCallGraph`` (in ``dyn_call_graph.py``) — observes real calls at
  runtime via TracePoint.

Both expose the same shape: ``uses`` (caller -> callees) and ``used`` (reverse),
keyed by method qualified name, which is what enriches ``done_what`` and
propagates ``what_todo``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Set

from .param_types import ProjectTypeIndex
from .ruby_ast import MethodInfo


@dataclass(frozen=True)
class CallEdge:
    caller: str            # qualified name
    callee: str            # qualified name
    line: int
    kind: str              # how it resolved: self | toplevel | const | lvar


@dataclass
class CallGraph:
    edges: List[CallEdge] = field(default_factory=list)
    uses: Dict[str, List[str]] = field(default_factory=dict)   # caller -> callees
    used: Dict[str, List[str]] = field(default_factory=dict)   # callee -> callers

    def _index(self) -> None:
        self.uses, self.used = {}, {}
        for e in self.edges:
            self.uses.setdefault(e.caller, [])
            if e.callee not in self.uses[e.caller]:
                self.uses[e.caller].append(e.callee)
            self.used.setdefault(e.callee, [])
            if e.caller not in self.used[e.callee]:
                self.used[e.callee].append(e.caller)

    def callees(self, method_qn: str) -> List[str]:
        return self.uses.get(method_qn, [])

    def callers(self, method_qn: str) -> List[str]:
        return self.used.get(method_qn, [])

    def edge_set(self):
        return {(e.caller, e.callee) for e in self.edges}


class StaticCallGraph:
    """Best-effort static resolution over the parser's per-method call records."""

    @classmethod
    def build(cls, methods: Sequence[MethodInfo], type_index: ProjectTypeIndex) -> CallGraph:
        instance_methods: Dict[str, Set[str]] = dict(type_index.own_methods)  # qn -> names
        singleton: Dict[str, Set[str]] = {}
        toplevel: Set[str] = set()
        exists: Set[str] = set()
        by_qn: Dict[str, MethodInfo] = {}
        for m in methods:
            exists.add(m.qualified_name)
            by_qn[m.qualified_name] = m
            if m.owner is None:
                toplevel.add(m.name)
            elif m.singleton:
                singleton.setdefault(m.owner, set()).add(m.name)
        # attr_reader/accessor methods are real instance methods (no def node) —
        # register them as valid call targets so edges to accessors resolve.
        for qn, names in instance_methods.items():
            for name in names:
                exists.add(f"{qn}#{name}")

        def resolve(caller: MethodInfo, call: dict) -> Optional[str]:
            name, recv, rname = call["name"], call["recv"], call.get("recv_name")
            if recv in ("none", "self"):
                if caller.owner:
                    for anc in type_index.ancestors(caller.owner):
                        if name in instance_methods.get(anc, set()):
                            cand = f"{anc}#{name}"
                            if cand in exists:
                                return cand
                if name in toplevel:
                    return name
                return None
            if recv == "const":
                cqn = type_index._resolve(rname)
                if not cqn:
                    return None
                if name == "new":
                    cand = f"{cqn}#initialize"
                    return cand if cand in exists else None
                if name in singleton.get(cqn, set()):
                    return f"{cqn}.{name}"
                return None
            if recv == "lvar":
                members = (caller.param_members or {}).get(rname)
                if not members:
                    return None
                for cqn in type_index.candidates(set(members)):
                    for anc in type_index.ancestors(cqn):
                        if name in instance_methods.get(anc, set()):
                            cand = f"{anc}#{name}"
                            if cand in exists:
                                return cand
                return None
            return None

        edges: List[CallEdge] = []
        seen = set()
        for m in methods:
            for call in m.calls:
                target = resolve(m, call)
                if target and target != m.qualified_name:
                    key = (m.qualified_name, target)
                    if key not in seen:
                        seen.add(key)
                        edges.append(CallEdge(m.qualified_name, target, call.get("line", 0), call["recv"]))
        g = CallGraph(edges=edges)
        g._index()
        return g
