"""Focused source views: the focal method is mandatory, auxiliary code is optional."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

_NOTICE = "# ... optional context omitted; focal method preserved in full."


@dataclass(frozen=True)
class SourceContext:
    source: str
    limit: int
    method_chars: int
    omitted_class_statements: int = 0
    omitted_constructor: bool = False
    omitted_class_declaration: bool = False
    mandatory_source: str = ""

    @property
    def over_limit(self) -> bool:
        return len(self.source) > self.limit

    @property
    def reduced(self) -> bool:
        return bool(self.omitted_class_statements or self.omitted_constructor
                    or self.omitted_class_declaration)


def build_source_context(focal: str, qualified_name: str, *, limit: int,
                         declaration: Optional[str] = None,
                         statements: Optional[List[str]] = None,
                         constructor: Optional[str] = None) -> SourceContext:
    """Keep whole components, reserving the focal code before any auxiliary text.

    Fitting priority is declaration, constructor, then class statements in source
    order. A large statement does not block later small ones. If the focal view
    alone exceeds the local character limit it remains intact and over_limit is
    true. This limit is not a model-token-window guarantee.
    """
    if limit < 1:
        raise ValueError("source context limit must be positive")
    statements = list(statements or [])
    focal_block = (f"# --- MÉTODO A ANALISAR: {qualified_name} ---\n{focal}"
                   if declaration is not None else focal)

    def render(header=None, body=(), init=None, notice=""):
        parts = []
        if header is not None:
            stub = header + ("\n" + "\n".join("  " + text for text in body) if body else "")
            parts.append("# --- contexto: a classe onde o método vive (sem corpos) ---\n" + stub)
        if init:
            parts.append("# --- construtor ---\n" + init)
        if notice:
            parts.append(notice)
        parts.append(focal_block)
        return "\n\n".join(parts)

    mandatory = render()
    if len(mandatory) > limit:
        return SourceContext(mandatory, limit, len(focal),
                             omitted_class_statements=len(statements),
                             omitted_constructor=bool(constructor),
                             omitted_class_declaration=declaration is not None, mandatory_source=mandatory)
    full = render(declaration, statements, constructor)
    if len(full) <= limit:
        return SourceContext(full, limit, len(focal), mandatory_source=mandatory)
    notice = ""  # Fit useful code before adding a human-readable omission notice.
    header, body, init = None, [], None
    if declaration is not None and len(render(declaration, notice=notice)) <= limit:
        header = declaration
    if constructor and len(render(header, init=constructor, notice=notice)) <= limit:
        init = constructor
    for statement in statements:
        if header is not None and len(render(header, [*body, statement], init, notice)) <= limit:
            body.append(statement)
    if len(render(header, body, init, _NOTICE)) <= limit:
        notice = _NOTICE
    return SourceContext(render(header, body, init, notice), limit, len(focal),
                         omitted_class_statements=len(statements) - len(body),
                         omitted_constructor=bool(constructor and init is None),
                         omitted_class_declaration=bool(declaration is not None and header is None), mandatory_source=mandatory)
