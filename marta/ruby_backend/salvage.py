"""Salvage passing examples from a partially-failing spec (Option D, Ruby).

The Ruby analogue of ``Testcase.salvage_passing_tests``: when a generated spec
has some ``it`` blocks passing and others failing, keep the file but strip the
failing examples by source line range, preserving ``require``s, ``describe``
wrappers, ``let``s and helpers. Because RSpec identifies examples positionally
(``[1:2]``) rather than by name, we map each failed example's ``line_number``
(from ``rspec -f json``) onto the enclosing ``it`` block range reported by Prism.

The caller MUST re-run the trimmed spec: if it isn't fully green afterwards it
should be discarded, exactly as on the Python side.
"""
from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

from .ruby_ast import ExampleBlock, GroupBlock


def _blocks_for_lines(
    examples: List[ExampleBlock], failed_lines: Iterable[int]
) -> List[ExampleBlock]:
    """Innermost example block containing each failing line (an `it` may sit
    inside nested `describe`s, but the failing line points at the `it`)."""
    picked: List[ExampleBlock] = []
    seen = set()
    for ln in failed_lines:
        candidates = [ex for ex in examples if ex.contains(ln)]
        if not candidates:
            continue
        # Smallest range = innermost = the actual `it`.
        inner = min(candidates, key=lambda e: e.end_line - e.start_line)
        key = (inner.start_line, inner.end_line)
        if key not in seen:
            seen.add(key)
            picked.append(inner)
    return picked


def salvage_spec(
    spec_source: str,
    examples: List[ExampleBlock],
    failed_lines: List[int],
    groups: Optional[List[GroupBlock]] = None,
) -> Optional[Tuple[str, int]]:
    """Return ``(trimmed_source, removed_count)`` or None if salvage isn't safe.

    None when there are no examples, no failing lines map to a block, or every
    example would be removed (nothing left to keep). ``groups`` (describe/
    context blocks) left without any surviving example are removed too, so the
    trimmed spec has no empty husks.
    """
    if not examples or not failed_lines:
        return None
    to_remove = _blocks_for_lines(examples, failed_lines)
    if not to_remove:
        return None
    if len(to_remove) >= len(examples):
        return None  # nothing would survive

    remove_lines = set()
    for ex in to_remove:
        remove_lines.update(range(ex.start_line, ex.end_line + 1))

    # Drop groups with no surviving example inside their range. Ancestors of
    # survivors always intersect a surviving example, so they are kept.
    removed_keys = {(ex.start_line, ex.end_line) for ex in to_remove}
    surviving = [ex for ex in examples if (ex.start_line, ex.end_line) not in removed_keys]
    for g in groups or []:
        if not any(g.contains(ex.start_line) for ex in surviving):
            remove_lines.update(range(g.start_line, g.end_line + 1))

    lines = spec_source.splitlines()
    kept = [ln for i, ln in enumerate(lines, start=1) if i not in remove_lines]
    return "\n".join(kept), len(to_remove)


def salvage_minitest(
    test_source: str,
    test_methods: List,
    failed_lines: List[int],
) -> Optional[Tuple[str, int]]:
    """Option D for Minitest: drop failing ``def test_x`` methods by line range.

    Minitest tests are ordinary methods, so ``test_methods`` are the parser's
    ``MethodInfo`` entries whose name starts with ``test_`` — this is the same
    surgery the Python MARTA does on pytest functions, and simpler than the
    RSpec case (no block/group nesting to clean up).
    """
    tests = [m for m in test_methods if m.name.startswith("test_")]
    if not tests or not failed_lines:
        return None

    to_remove, seen = [], set()
    for ln in failed_lines:
        inner = [m for m in tests if m.start_line <= ln <= m.end_line]
        if not inner:
            continue
        m = min(inner, key=lambda x: x.end_line - x.start_line)
        key = (m.start_line, m.end_line)
        if key not in seen:
            seen.add(key)
            to_remove.append(m)
    if not to_remove or len(to_remove) >= len(tests):
        return None  # nothing maps, or nothing would survive

    remove_lines = set()
    for m in to_remove:
        remove_lines.update(range(m.start_line, m.end_line + 1))
    lines = test_source.splitlines()
    kept = [ln for i, ln in enumerate(lines, start=1) if i not in remove_lines]
    return "\n".join(kept), len(to_remove)
