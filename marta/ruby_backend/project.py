"""Project-level orchestration for the Ruby backend (Fase 1 MVP).

The lightweight Ruby analogue of ``ProjectMessage``: discover ``*.rb`` files
under a source directory, parse each with Prism, and drive
``generate_spec_for_method`` over their methods. It reuses the language-agnostic
pieces (the LLM via the injected ``ask``) and stays out of the stabilised Python
flow — the ``LanguageBackend`` interface can be formalised on top of this later.

Load-path / require resolution (the ``PYTHONPATH``/import-root analogue):
``-I <source_dir>`` is put on RSpec's load path and each spec does
``require "<path-relative-to-source-dir, without .rb>"``.
"""
from __future__ import annotations

import glob
import os
import re
from dataclasses import dataclass, field
from typing import List, Optional

from . import ruby_ast
from .generate import AskFn, GenOutcome, generate_spec_for_method

# Methods we never target directly: exercised indirectly as construction context.
SKIP_METHODS = {"initialize"}


def _slice_lines(path: str, start: int, end: int) -> str:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return "\n".join(lines[start - 1:end])


def _sanitize(name: str) -> str:
    # Ruby method names can end in ? ! = — make a filesystem/spec-safe token.
    name = name.replace("?", "_q").replace("!", "_bang").replace("=", "_set")
    return re.sub(r"[^0-9A-Za-z_]", "_", name)


@dataclass
class MethodTarget:
    method: ruby_ast.MethodInfo
    owner_class: Optional[ruby_ast.ClassInfo]
    file_path: str            # absolute path to the .rb file
    require_target: str       # e.g. "foo/bar" (relative to source_dir, no .rb)

    @property
    def describe_subject(self) -> str:
        """What follows ``RSpec.describe``. The owning class for methods on a
        class; a quoted string for top-level defs."""
        if self.owner_class is not None:
            return self.owner_class.qualified_name
        return f'"{self.method.name}"'

    @property
    def context_source(self) -> str:
        """Source shown to the LLM as the code under test: the whole owning
        class (so it knows how to construct it) or just the method."""
        if self.owner_class is not None:
            return _slice_lines(
                self.file_path, self.owner_class.start_line, self.owner_class.end_line
            )
        return _slice_lines(self.file_path, self.method.start_line, self.method.end_line)

    @property
    def spec_path(self) -> str:
        stem = os.path.splitext(os.path.basename(self.file_path))[0]
        owner = _sanitize(self.owner_class.qualified_name) if self.owner_class else "toplevel"
        return os.path.join("spec", f"{stem}__{owner}__{_sanitize(self.method.name)}_spec.rb")


@dataclass
class RubyProject:
    root_dir: str             # project root (cwd for RSpec)
    source_dir: str           # dir containing the code under test, relative to root

    files: List[str] = field(default_factory=list)          # absolute .rb paths
    targets: List[MethodTarget] = field(default_factory=list)

    @property
    def abs_source(self) -> str:
        return os.path.join(self.root_dir, self.source_dir)

    def discover(self) -> "RubyProject":
        """Find *.rb under source_dir (excluding spec/) and build method targets."""
        self.files = []
        self.targets = []
        pattern = os.path.join(self.abs_source, "**", "*.rb")
        for path in sorted(glob.glob(pattern, recursive=True)):
            rel = os.path.relpath(path, self.abs_source)
            if rel.split(os.sep)[0] == "spec":
                continue
            self.files.append(path)
            fp = ruby_ast.parse_file(path)
            classes_by_qn = {c.qualified_name: c for c in fp.classes}
            require_target = os.path.splitext(rel)[0]
            for m in fp.methods:
                if m.name in SKIP_METHODS:
                    continue
                self.targets.append(
                    MethodTarget(
                        method=m,
                        owner_class=classes_by_qn.get(m.owner) if m.owner else None,
                        file_path=path,
                        require_target=require_target,
                    )
                )
        return self

    async def generate_all(
        self,
        ask: Optional[AskFn] = None,
        max_attempts: int = 3,
        limit: Optional[int] = None,
    ) -> List[GenOutcome]:
        """Generate a spec per discovered method target. Returns the outcomes."""
        outcomes: List[GenOutcome] = []
        targets = self.targets[:limit] if limit else self.targets
        for t in targets:
            outcome = await generate_spec_for_method(
                method_qualified_name=t.method.qualified_name,
                describe_subject=t.describe_subject,
                method_source=t.context_source,
                require_target=t.require_target,
                load_paths=[self.source_dir],
                spec_path=t.spec_path,
                cwd=self.root_dir,
                ask=ask,
                max_attempts=max_attempts,
            )
            outcomes.append(outcome)
        return outcomes
