"""The ``LanguageBackend`` interface and its Ruby implementation (item 9).

Formalises the language-specific surface the orchestrator programs against —
discovery, parsing, syntax check, test runner, coverage, salvage, prompts and
(optionally) a call graph. The ReAct loop and project orchestration call
``backend.*`` instead of importing Ruby modules directly, so the flow is
language-agnostic and a second language would only need a new backend.

Deliberately low-risk and self-contained: this lives inside ``ruby_backend`` and
does NOT touch the stabilised Python MARTA. A future ``PythonBackend`` could
implement the same ABC, but that (and any refactor of the Python flow) is out of
scope — the Python tool stays exactly as it is.
"""
from __future__ import annotations

import glob
import os
from abc import ABC, abstractmethod
from types import ModuleType
from typing import Any, List, Optional, Tuple

from . import coverage_runner, prompts as ruby_prompts, runner, salvage
from . import ruby_ast
from .coverage_runner import CoverageResult, MethodCoverage
from .ruby_ast import ExampleBlock, FileParse, MethodInfo
from .runner import RSpecResult


class LanguageBackend(ABC):
    """Everything language-specific, behind one surface. Return types are the
    contract dataclasses (FileParse, RSpecResult, CoverageResult, ...); another
    language's backend would return structurally-equivalent objects."""

    #: source file extension glob and the directory tests live in
    source_glob: str = "*"
    test_dir: str = "test"

    @abstractmethod
    def discover_files(self, abs_source: str) -> List[str]: ...

    @abstractmethod
    def parse_file(self, path: str) -> FileParse: ...

    @abstractmethod
    def parse_source(self, source: str, name: str = "(source)") -> FileParse: ...

    @abstractmethod
    def module_ref(self, source_rel: str) -> str:
        """How a test refers to the code under test (e.g. require target)."""

    @abstractmethod
    def syntax_check(self, source: str) -> Optional[str]: ...

    @abstractmethod
    def run_tests(self, test_path: str, load_paths: List[str], cwd: str) -> RSpecResult: ...

    @abstractmethod
    def run_coverage(self, source_dir: str, test_paths: List[str], cwd: str) -> CoverageResult: ...

    @abstractmethod
    def synthesize_coverage(self, method: MethodInfo, lines: List[Optional[int]]) -> MethodCoverage: ...

    @abstractmethod
    def salvage(
        self,
        test_source: str,
        examples: List[ExampleBlock],
        failed_lines: List[int],
        groups=None,
    ) -> Optional[Tuple[str, int]]: ...

    @abstractmethod
    def build_call_graph(self, files: List[str]) -> Optional[Any]:
        """Static call graph over ``files`` (``CallGraph``), or None if the
        backend has none."""

    @property
    @abstractmethod
    def prompts(self) -> ModuleType:
        """Module exposing the Planner/Dev prompt builders + code extractor."""


class RubyBackend(LanguageBackend):
    """Ruby/RSpec implementation, delegating to the ruby_backend modules."""

    source_glob = "*.rb"
    test_dir = "spec"

    def discover_files(self, abs_source: str) -> List[str]:
        pattern = os.path.join(abs_source, "**", self.source_glob)
        files = []
        for path in sorted(glob.glob(pattern, recursive=True)):
            rel = os.path.relpath(path, abs_source)
            if rel.split(os.sep)[0] == self.test_dir:
                continue  # skip spec/ — those are tests, not code under test
            files.append(path)
        return files

    def parse_file(self, path: str) -> FileParse:
        return ruby_ast.parse_file(path)

    def parse_source(self, source: str, name: str = "(source)") -> FileParse:
        return ruby_ast.parse_source(source, name)

    def module_ref(self, source_rel: str) -> str:
        # foo/bar.rb -> foo/bar  (require "foo/bar" with -I on the source dir)
        return os.path.splitext(source_rel)[0]

    def syntax_check(self, source: str) -> Optional[str]:
        return runner.syntax_check(source)

    def run_tests(self, test_path: str, load_paths: List[str], cwd: str) -> RSpecResult:
        return runner.run_rspec(test_path, load_paths=load_paths, cwd=cwd)

    def run_coverage(self, source_dir: str, test_paths: List[str], cwd: str) -> CoverageResult:
        # Generated specs are self-contained -> isolate from the project .rspec.
        return coverage_runner.run_line_coverage(source_dir, test_paths, cwd=cwd, isolated=True)

    def synthesize_coverage(self, method: MethodInfo, lines: List[Optional[int]]) -> MethodCoverage:
        return coverage_runner.synthesize(method, lines)

    def salvage(
        self,
        test_source: str,
        examples: List[ExampleBlock],
        failed_lines: List[int],
        groups=None,
    ) -> Optional[Tuple[str, int]]:
        return salvage.salvage_spec(test_source, examples, failed_lines, groups)

    def build_call_graph(self, files: List[str]) -> Optional[Any]:
        # Static resolution over the parsed methods (see call_graph.py).
        from .call_graph import StaticCallGraph
        from .param_types import ProjectTypeIndex
        methods = []
        index = ProjectTypeIndex()
        for f in files:
            fp = self.parse_file(f)
            index.add_file(fp)
            methods.extend(fp.methods)
        return StaticCallGraph.build(methods, index)

    @property
    def prompts(self) -> ModuleType:
        return ruby_prompts
