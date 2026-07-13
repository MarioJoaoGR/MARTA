"""Parameter-type inference for the Ruby backend (item 5).

Ruby parameters are untyped (duck typing), so — like MARTA's ``ArgMessage`` /
``analyze_param_types`` — we infer a likely type from *behaviour*: the methods
invoked on a parameter (its "members", from the parser) are matched against the
methods each project class responds to (own + inherited via a linearised MRO of
superclass + ``include``/``prepend``). Classes that respond to every accessed
member are candidate types. The result is a compact "judge" hint fed to the
Planner, the analogue of ``FunctionMessage.judge``.

Static and best-effort: only project-defined classes/modules are resolved
(stdlib/gems are invisible), and metaprogrammed methods are missed — the same
class of limitation flagged for the call graph.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

from .ruby_ast import ClassInfo, FileParse, MethodInfo


@dataclass
class ProjectTypeIndex:
    classes: Dict[str, ClassInfo] = field(default_factory=dict)          # qn -> ClassInfo
    own_methods: Dict[str, Set[str]] = field(default_factory=dict)       # qn -> instance methods
    _by_short: Dict[str, str] = field(default_factory=dict)              # short name -> qn

    def add_file(self, fp: FileParse) -> "ProjectTypeIndex":
        for c in fp.classes:
            self.classes[c.qualified_name] = c
            self.own_methods.setdefault(c.qualified_name, set())
            self._by_short.setdefault(c.name, c.qualified_name)
        for m in fp.methods:
            if m.owner and not m.singleton:  # instance methods define the interface
                self.own_methods.setdefault(m.owner, set()).add(m.name)
        return self

    def _resolve(self, name: Optional[str]) -> Optional[str]:
        """Best-effort name -> qualified_name (exact, else last-segment match)."""
        if not name:
            return None
        if name in self.classes:
            return name
        short = name.split("::")[-1]
        return self._by_short.get(short)

    def ancestors(self, qn: str, _seen: Optional[Set[str]] = None) -> List[str]:
        """Linearised ancestors (self first): prepends, self, includes, then the
        superclass chain. Approximate but captures Ruby's mixin method lookup."""
        seen = _seen if _seen is not None else set()
        if qn in seen or qn not in self.classes:
            return []
        seen.add(qn)
        c = self.classes[qn]
        order: List[str] = []
        for mod in reversed(c.prepends):
            r = self._resolve(mod)
            if r:
                order += self.ancestors(r, seen)
        order.append(qn)
        for mod in reversed(c.includes):
            r = self._resolve(mod)
            if r:
                order += self.ancestors(r, seen)
        sup = self._resolve(c.superclass)
        if sup:
            order += self.ancestors(sup, seen)
        return order

    def responds_to(self, qn: str) -> Set[str]:
        methods: Set[str] = set()
        for anc in self.ancestors(qn):
            methods |= self.own_methods.get(anc, set())
        return methods

    def candidates(self, members: Set[str]) -> List[str]:
        """Project classes responding to every member accessed on a parameter."""
        if not members:
            return []
        return sorted(
            qn for qn, c in self.classes.items()
            if c.kind == "class" and members <= self.responds_to(qn)
        )

    def judge_for_method(self, method: MethodInfo) -> str:
        """One-line-per-parameter hint, or "" when nothing can be said."""
        lines: List[str] = []
        for pname, members in (method.param_members or {}).items():
            if not members:
                continue
            responds = ", ".join(sorted(members))
            cands = self.candidates(set(members))
            if cands:
                lines.append(f"- `{pname}` responds to [{responds}] -> likely: {', '.join(cands)}")
            else:
                lines.append(f"- `{pname}` responds to [{responds}]")
        if not lines:
            return ""
        return "INFERRED PARAMETER TYPES:\n" + "\n".join(lines)
