"""Bounded class evidence from existing parse facts and source-only summaries.

No source reads, parsing, retrieval, embedding or model calls. Record selection
is deterministic, prioritizes construction, and keeps reopened declarations.
"""
from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import chain
from pathlib import Path

POLICY = "class-source-evidence-v1"
SUMMARY_EXCERPT_CHARS = 320  # Prose only; never slice a Ruby statement/signature.


@dataclass(frozen=True)
class ClassContext:
    core: str
    records: tuple
    metadata: dict

    @property
    def text(self):
        return "\n\n".join((self.core, *self.records))


def _round_robin(targets, root):
    groups = defaultdict(deque)
    for target in sorted(targets, key=lambda t: (str(Path(t.file_path).relative_to(root)),
                                                t.method.start_line, t.method.end_line, t.analysis_id)):
        groups[str(Path(target.file_path).relative_to(root))].append(target)
    names = deque(sorted(groups))
    while names:
        name = names.popleft()
        yield groups[name].popleft()
        if groups[name]:
            names.append(name)


def build_class_context(qualified_name, definitions, targets, source_summaries, *, root, limit):
    """One local character cap, then the caller's whole-message token budget.

    Short method descriptions replace a raw first-40 signature list. All methods
    are eligible; a record that does not fit can fall back to parser facts, and
    never prevents a later smaller record from being considered.
    """
    if type(limit) is not int or limit < 1:
        raise ValueError("Class context limit must be a positive integer")
    root = Path(root)
    targets = sorted(targets, key=lambda t: t.analysis_id)
    # Deduplicate repeated references from fallback method owners, not distinct
    # parser nodes. Two reopenings can even share a source line/range.
    seen, declarations = set(), []
    for path, cls in definitions:
        relative = str(Path(path).relative_to(root))
        identity = (relative, id(cls))
        if identity not in seen:
            seen.add(identity)
            declarations.append((relative, cls.start_line, cls.end_line, cls.kind, cls.superclass, cls))
    declarations.sort(key=lambda item: (item[0], item[1], item[2], item[3], item[4] or "",
                                        tuple(item[5].body_statements)))
    statements = [(item, text) for item in declarations for text in item[5].body_statements]
    totals = {"declarations": len(declarations), "methods": len(targets), "statements": len(statements)}
    selected = dict.fromkeys(totals, 0)
    descriptions = 0

    def core(counts):
        return (f"CLASS: {qualified_name}\nPartial static project evidence; not executable class source.\n"
                + "; ".join(f"{name}: {counts[name]} prepared / {total} available" for name, total in totals.items())
                + ". Prepared counts precede whole-request reduction. Missing evidence is unknown; "
                "reopenings are not resolved to a runtime winner.")

    # The all-counts form reserves at least as many digits as any final count.
    reserved = len(core(totals))
    records, used = [], reserved
    def add(kind, full, fallback=None):
        nonlocal used
        for text in (full, fallback):
            if text is not None and used + 2 + len(text) <= limit:
                records.append(text)
                used += 2 + len(text)
                selected[kind] += 1
                return text == full
        return None

    for key in declarations:
        path, start, end, kind, parent, _ = key
        declaration = f"{kind} {qualified_name}" + (f" < {parent}" if parent else "")
        add("declarations", f"Declaration {path}:{start}-{end}: {declaration}")

    constructors = [t for t in targets if t.method.name == "initialize" and not t.method.singleton]
    others = [t for t in targets if t.method.name != "initialize" or t.method.singleton]
    for target in chain(_round_robin(constructors, root), _round_robin(others, root)):
        method = target.method
        relative = Path(target.file_path).relative_to(root)
        params = ", ".join(f"{p.name if p.name is not None else '<unnamed>'} [{p.kind}]" for p in method.params)
        facts = (f"Method {method.qualified_name} @ {relative}:{method.start_line}-{method.end_line}\n"
                 f"Parser-reported parameters: {params or '(none recorded)'}. Defaults/visibility not inferred.")
        description = source_summaries.get(target.analysis_id, "").strip()
        if description:
            excerpt = description[:SUMMARY_EXCERPT_CHARS]
            if len(description) > len(excerpt):
                excerpt += " … [incomplete excerpt]"
            full = facts + "\nGenerated source-only implementation description (not runtime proof): " + excerpt
            if add("methods", full, facts) is True:
                descriptions += 1
        else:
            add("methods", facts)

    for key, statement in statements:
        add("statements", f"Source body statement from {key[0]}:{key[1]}-{key[2]} (not executed):\n{statement}")

    text_core = core(selected)
    metadata = {"policy": POLICY, "limit_chars": limit, "available": totals,
                "prepared": dict(selected), "omitted": {k: totals[k] - selected[k] for k in totals},
                "method_descriptions": descriptions,
                "description_source": "done_what_passage1_source_only",
                "summary_excerpt_chars": SUMMARY_EXCERPT_CHARS,
                "prepared_chars": len(text_core) + sum(2 + len(r) for r in records),
                "over_limit": len(text_core) + sum(2 + len(r) for r in records) > limit}
    return ClassContext(text_core, tuple(records), metadata)
