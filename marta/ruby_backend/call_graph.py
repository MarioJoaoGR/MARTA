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

# Bump whenever the resolver's behaviour changes: it participates in the
# cg_cache key so stale graphs are rebuilt automatically (bit us on sondagem 1).
RESOLVER_VERSION = 2


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

    def to_json(self) -> dict:
        return {"edges": [[e.caller, e.callee, e.line, e.kind] for e in self.edges]}

    def to_dot(self, name: str = "callgraph", strip_prefix: str = "") -> str:
        """O grafo em DOT (Graphviz), para poder ser desenhado por ferramenta
        padrão em vez de à mão. As folhas — métodos que não chamam ninguém —
        ficam a cinzento, que é o que distingue o fim de um caminho.

            dot -Tpng grafo.dot -o grafo.png
        """
        def rot(qn: str) -> str:
            return qn[len(strip_prefix):] if strip_prefix and qn.startswith(strip_prefix) else qn

        nos = {e.caller for e in self.edges} | {e.callee for e in self.edges}
        linhas = [f'digraph {name} {{',
                  '  rankdir=LR;',
                  '  node [shape=box, style="rounded,filled", fontname="Helvetica",'
                  ' fontsize=10, fillcolor="#ffffff", color="#3f6ea8"];',
                  '  edge [color="#8aa6c4", arrowsize=0.7];']
        for n in sorted(nos):
            folha = not self.uses.get(n)
            extra = ' fillcolor="#eef3fb" color="#9db6d4"' if folha else ""
            linhas.append(f'  "{rot(n)}" [{extra.strip()}];' if extra else f'  "{rot(n)}";')
        for e in sorted(self.edges, key=lambda x: (x.caller, x.callee)):
            linhas.append(f'  "{rot(e.caller)}" -> "{rot(e.callee)}";')
        linhas.append("}")
        return "\n".join(linhas)

    @classmethod
    def from_json(cls, data: dict) -> "CallGraph":
        g = cls(edges=[CallEdge(c, ce, ln, k) for c, ce, ln, k in data.get("edges", [])])
        g._index()
        return g


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

        def _instance_lookup(cqn: str, name: str) -> Optional[str]:
            """First ancestor of cqn defining `name`, as an existing target."""
            for anc in type_index.ancestors(cqn):
                if name in instance_methods.get(anc, set()):
                    cand = f"{anc}#{name}"
                    if cand in exists:
                        return cand
            return None

        # Duck-typed collaborators (ivar/getter/lvar): cap the candidate fan-out
        # so one generic member (e.g. `==`) doesn't edge to the whole project.
        MAX_CANDIDATES = 5

        def _duck_targets(members, name) -> List[str]:
            if not members:
                return []
            cands = type_index.candidates(set(members))
            if not cands or len(cands) > MAX_CANDIDATES:
                return []
            out = []
            for cqn in cands:
                t = _instance_lookup(cqn, name)
                if t:
                    out.append(t)
            return out

        def resolve(caller: MethodInfo, call: dict) -> List[str]:
            name, recv, rname = call["name"], call["recv"], call.get("recv_name")
            owner_cls = type_index.classes.get(caller.owner) if caller.owner else None
            if recv in ("none", "self"):
                if caller.owner:
                    t = _instance_lookup(caller.owner, name)
                    if t:
                        return [t]
                return [name] if name in toplevel else []
            if recv == "const":
                cqn = type_index._resolve(rname)
                if not cqn:
                    return []
                if name == "new":
                    cand = f"{cqn}#initialize"
                    return [cand] if cand in exists else []
                return [f"{cqn}.{name}"] if name in singleton.get(cqn, set()) else []
            if recv == "selfclass":
                # self.class.new -> Owner#initialize; self.class.foo -> Owner.foo
                if not caller.owner:
                    return []
                if name == "new":
                    cand = f"{caller.owner}#initialize"
                    return [cand] if cand in exists else []
                return [f"{caller.owner}.{name}"] if name in singleton.get(caller.owner, set()) else []
            if recv == "lvar":
                return _duck_targets((caller.param_members or {}).get(rname), name)
            if recv in ("ivar", "getter"):
                # Collaborator held in an ivar (or exposed via a zero-arg getter):
                # type it by the interface used on it across the whole class.
                if owner_cls is None:
                    return []
                return _duck_targets(owner_cls.receiver_members.get(rname), name)
            return []

        edges: List[CallEdge] = []
        seen = set()
        for m in methods:
            for call in m.calls:
                for target in resolve(m, call):
                    if target == m.qualified_name:
                        continue
                    key = (m.qualified_name, target)
                    if key not in seen:
                        seen.add(key)
                        edges.append(CallEdge(m.qualified_name, target, call.get("line", 0), call["recv"]))
        g = CallGraph(edges=edges)
        g._index()
        return g
