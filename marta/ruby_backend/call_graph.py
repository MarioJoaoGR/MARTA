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

from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional, Sequence, Set
from collections import Counter

from .param_types import ProjectTypeIndex
from .ruby_ast import MethodInfo

# Bump whenever the resolver's behaviour changes: it participates in the
# cg_cache key so stale graphs are rebuilt automatically (bit us on sondagem 1).
RESOLVER_VERSION = 3


@dataclass(frozen=True)
class CallEdge:
    caller: str            # qualified name
    callee: str            # qualified name
    line: int
    kind: str              # receiver syntax, not a confidence level
    evidence: str = "legacy_unknown"
    receiver_candidates: tuple = ()

    @property
    def supported(self) -> bool:
        # Supported by the project lookup model / an observed execution, not a
        # proof of dispatch for every possible Ruby runtime or input.
        return self.evidence in ("static_lookup", "runtime_observed")


@dataclass
class CallGraph:
    edges: List[CallEdge] = field(default_factory=list)
    uses: Dict[str, List[str]] = field(default_factory=dict)   # caller -> callees
    used: Dict[str, List[str]] = field(default_factory=dict)   # callee -> callers

    _pair_edges: dict = field(default_factory=dict, init=False, repr=False)
    _supported_uses: dict = field(default_factory=dict, init=False, repr=False)
    _supported_used: dict = field(default_factory=dict, init=False, repr=False)
    _supported_pairs: set = field(default_factory=set, init=False, repr=False)

    def _index(self) -> None:
        self.uses, self.used = {}, {}
        self._pair_edges, self._supported_uses, self._supported_used = {}, {}, {}
        self._supported_pairs = set()
        for e in self.edges:
            self._pair_edges.setdefault((e.caller, e.callee), []).append(e)
            if e.supported and (e.caller, e.callee) not in self._supported_pairs:
                self._supported_uses.setdefault(e.caller, []).append(e.callee)
                self._supported_used.setdefault(e.callee, []).append(e.caller)
                self._supported_pairs.add((e.caller, e.callee))
            self.uses.setdefault(e.caller, [])
            if e.callee not in self.uses[e.caller]:
                self.uses[e.caller].append(e.callee)
            self.used.setdefault(e.callee, [])
            if e.caller not in self.used[e.callee]:
                self.used[e.callee].append(e.caller)

    def callees(self, method_qn: str, *, supported_only=False) -> List[str]:
        if not supported_only:
            return self.uses.get(method_qn, [])
        return self._supported_uses.get(method_qn, [])

    def callers(self, method_qn: str, *, supported_only=False) -> List[str]:
        if not supported_only:
            return self.used.get(method_qn, [])
        return self._supported_used.get(method_qn, [])

    def has_supported(self, caller, callee):
        return (caller, callee) in self._supported_pairs

    def evidence_label(self, caller, callee):
        edges = self._pair_edges.get((caller, callee), [])
        kinds = sorted({e.evidence for e in edges}) or ["legacy_unknown"]
        candidates = sorted({name for e in edges for name in e.receiver_candidates})
        owner = callee.split("#", 1)[0] if "#" in callee else callee.rsplit(".", 1)[0]
        detail = "; receiver candidates: " + ", ".join(candidates) if candidates and candidates != [owner] else ""
        return "[graph evidence: " + ", ".join(kinds) + detail + "]"

    def edge_set(self):
        return {(e.caller, e.callee) for e in self.edges}

    def to_json(self) -> dict:
        return {"edges": [asdict(e) for e in self.edges]}

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
            style = "" if e.supported else ' [style=dashed, label="' + e.evidence + '"]'
            linhas.append(f'  "{rot(e.caller)}" -> "{rot(e.callee)}"{style};')
        linhas.append("}")
        return "\n".join(linhas)

    @classmethod
    def from_json(cls, data: dict) -> "CallGraph":
        edges = []
        for record in data.get("edges", []):
            if isinstance(record, dict):
                record = {**record, "receiver_candidates": tuple(record.get("receiver_candidates", []))}
                edges.append(CallEdge(**record))
            else:
                edges.append(CallEdge(*record))  # Old four-field records stay unknown.
        g = cls(edges=edges)
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

        def _duck_targets(members, name):
            if not members:
                return []
            candidates = type_index.candidates(set(members))
            if not candidates or len(candidates) > MAX_CANDIDATES:
                return []
            evidence = "duck_unique" if len(candidates) == 1 else "duck_ambiguous"
            return [(target, evidence, tuple(candidates)) for candidate in candidates
                    if (target := _instance_lookup(candidate, name))]

        def singleton_target(owner, name, evidence, candidates=()):
            if name in singleton.get(owner, set()):
                return [(f"{owner}.{name}", evidence, candidates)]
            if name == "new":
                target = _instance_lookup(owner, "initialize")
                return [(target, "constructor_mapping", candidates)] if target else []
            return []

        def resolve(caller: MethodInfo, call: dict):
            name, recv, rname = call["name"], call["recv"], call.get("recv_name")
            owner_cls = type_index.classes.get(caller.owner) if caller.owner else None
            if recv in ("none", "self"):
                if caller.owner:
                    if caller.singleton:
                        found = singleton_target(caller.owner, name, "static_lookup")
                    else:
                        target = _instance_lookup(caller.owner, name)
                        found = [(target, "static_lookup", ())] if target else []
                    if found:
                        return found
                if name in toplevel:
                    return [(name, "implicit_global_fallback" if caller.owner else "static_lookup", ())]
                return []
            if recv == "const":
                candidates = type_index.resolve_candidates(rname)
                if not candidates or len(candidates) > MAX_CANDIDATES:
                    return []
                evidence = ("constant_ambiguous" if len(candidates) > 1 else
                            "static_lookup" if rname.removeprefix("::") == candidates[0] else "constant_short_fallback")
                return [result for owner in candidates
                        for result in singleton_target(owner, name, evidence, tuple(candidates))]
            if recv == "selfclass":
                # self.class inside an instance method is only a runtime type
                # candidate; inside a singleton method it is Class, not Owner.
                if caller.owner and not caller.singleton:
                    return singleton_target(caller.owner, name, "selfclass_inferred", (caller.owner,))
                return []
            if recv == "lvar":
                return _duck_targets((caller.param_members or {}).get(rname), name)
            if recv in ("ivar", "getter") and owner_cls is not None:
                return _duck_targets(owner_cls.receiver_members.get(rname), name)
            return []

        counts = Counter(method.qualified_name for method in methods)
        edges: List[CallEdge] = []
        seen = set()
        for method in methods:
            for call in method.calls:
                for target, evidence, candidates in resolve(method, call):
                    if target == method.qualified_name:
                        continue
                    if counts[target] > 1 or counts[method.qualified_name] > 1:
                        evidence = "ambiguous_definition"
                    key = (method.qualified_name, target, call.get("line", 0), call["recv"], evidence, candidates)
                    if key not in seen:
                        seen.add(key)
                        edges.append(CallEdge(*key))
        g = CallGraph(edges=edges)
        g._index()
        return g
