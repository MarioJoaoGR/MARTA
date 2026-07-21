"""Python wrapper over the Prism-based Ruby parser helper (``rb/marta_parse.rb``).

Runs the helper as a subprocess and returns a language-neutral structural view
of a Ruby file — classes/modules and methods, each with source line ranges and
typed parameters. This is the Ruby counterpart to what Python's ``ast`` gives
the original MARTA; the line ranges are what later lets us synthesise per-method
missing-lines out of SimpleCov's per-line hits.

The Ruby binary defaults to ``$MARTA_RUBY_BIN`` or ``ruby`` on PATH; point it at
an rbenv/asdf shim (Ruby >= 3.3, which ships Prism) if ``ruby`` is older.
"""
from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from typing import Dict, List, Optional

_HELPER = os.path.join(os.path.dirname(__file__), "rb", "marta_parse.rb")

# Parameter kinds emitted by the helper, in Ruby terms.
PARAM_KINDS = {"req", "opt", "rest", "keyreq", "key", "keyrest", "block"}


@dataclass
class ParamInfo:
    name: Optional[str]
    kind: str  # one of PARAM_KINDS


@dataclass
class MethodInfo:
    name: str
    owner: Optional[str]       # enclosing class/module qualified name, or None (top-level)
    singleton: bool            # True for `def self.x` / `def Klass.x`
    start_line: int
    end_line: int
    params: List[ParamInfo] = field(default_factory=list)
    # param name -> methods invoked on it in the body (duck-typing "members")
    param_members: Dict[str, List[str]] = field(default_factory=dict)
    # every call made in the body: {name, recv, recv_name, line} (call graph)
    calls: List[dict] = field(default_factory=list)

    @property
    def qualified_name(self) -> str:
        """`Owner#name` for instance methods, `Owner.name` for singletons,
        bare `name` for top-level defs — mirrors how a reader refers to it."""
        if self.owner is None:
            return self.name
        sep = "." if self.singleton else "#"
        return f"{self.owner}{sep}{self.name}"


@dataclass
class ClassInfo:
    name: str
    qualified_name: str
    kind: str                  # "class" | "module"
    superclass: Optional[str]
    start_line: int
    end_line: int
    includes: List[str] = field(default_factory=list)
    extends: List[str] = field(default_factory=list)
    prepends: List[str] = field(default_factory=list)
    attributes: List[str] = field(default_factory=list)  # attr_* reader/writer methods
    # statements do corpo que nao sao metodos (constantes, attr_*, include):
    # o "class stub" para o prompt (== non_method_statements do Python)
    body_statements: List[str] = field(default_factory=list)
    # receiver token ("@bank" / getter "bank") -> methods invoked on it in the
    # class body (duck-typing interface of collaborator objects)
    receiver_members: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class ExampleBlock:
    """An RSpec `it`/`specify`/... block, with its source line range. Used by
    the salvage step to remove failing examples by line range (the Ruby analogue
    of removing failing `def`s in ``salvage_passing_tests``)."""
    name: str                  # "it", "specify", ...
    description: Optional[str]
    start_line: int
    end_line: int

    def contains(self, line: int) -> bool:
        return self.start_line <= line <= self.end_line


@dataclass
class GroupBlock:
    """An RSpec `describe`/`context` block. Salvage removes groups left with no
    surviving examples (avoids empty `context "..." do end` husks)."""
    name: str                  # "describe" | "context"
    description: Optional[str]
    start_line: int
    end_line: int

    def contains(self, line: int) -> bool:
        return self.start_line <= line <= self.end_line


@dataclass
class FileParse:
    path: str
    classes: List[ClassInfo] = field(default_factory=list)
    methods: List[MethodInfo] = field(default_factory=list)
    examples: List[ExampleBlock] = field(default_factory=list)
    groups: List[GroupBlock] = field(default_factory=list)
    errors: List[dict] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


class RubyParseError(RuntimeError):
    """The helper itself failed to run (missing Ruby/Prism, crash) — distinct
    from a *syntax* error in the analysed file, which comes back in ``errors``."""


def ruby_bin() -> str:
    return os.getenv("MARTA_RUBY_BIN", "ruby")


def _from_json(data: dict) -> FileParse:
    classes = [
        ClassInfo(
            name=c["name"],
            qualified_name=c["qualified_name"],
            kind=c["kind"],
            superclass=c.get("superclass"),
            start_line=c["start_line"],
            end_line=c["end_line"],
            includes=c.get("includes", []),
            extends=c.get("extends", []),
            prepends=c.get("prepends", []),
            attributes=c.get("attributes", []),
            receiver_members=c.get("receiver_members", {}),
            body_statements=c.get("body_statements", []),
        )
        for c in data.get("classes", [])
    ]
    methods = [
        MethodInfo(
            name=m["name"],
            owner=m.get("owner"),
            singleton=m.get("singleton", False),
            start_line=m["start_line"],
            end_line=m["end_line"],
            params=[ParamInfo(name=p.get("name"), kind=p["kind"]) for p in m.get("params", [])],
            param_members=m.get("param_members", {}),
            calls=m.get("calls", []),
        )
        for m in data.get("methods", [])
    ]
    examples = [
        ExampleBlock(
            name=e["name"],
            description=e.get("description"),
            start_line=e["start_line"],
            end_line=e["end_line"],
        )
        for e in data.get("examples", [])
    ]
    groups = [
        GroupBlock(
            name=g["name"],
            description=g.get("description"),
            start_line=g["start_line"],
            end_line=g["end_line"],
        )
        for g in data.get("groups", [])
    ]
    return FileParse(
        path=data.get("path", ""),
        classes=classes,
        methods=methods,
        examples=examples,
        groups=groups,
        errors=data.get("errors", []),
    )


def _run(args: List[str], stdin: Optional[str] = None) -> dict:
    try:
        proc = subprocess.run(
            [ruby_bin(), _HELPER, *args],
            input=stdin,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError as e:
        raise RubyParseError(
            f"Ruby binary '{ruby_bin()}' not found. Set MARTA_RUBY_BIN to a "
            f"Ruby >= 3.3 (ships Prism)."
        ) from e
    except subprocess.TimeoutExpired as e:
        raise RubyParseError("marta_parse.rb timed out") from e
    if proc.returncode != 0:
        raise RubyParseError(
            f"marta_parse.rb exited {proc.returncode}: {proc.stderr.strip()}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RubyParseError(f"marta_parse.rb emitted non-JSON: {proc.stdout[:200]}") from e


def parse_file(path: str) -> FileParse:
    """Structural parse of a Ruby file on disk."""
    return _from_json(_run([path]))


def parse_source(source: str, name: str = "(source)") -> FileParse:
    """Structural parse of Ruby source held in memory."""
    return _from_json(_run(["--stdin", name], stdin=source))
