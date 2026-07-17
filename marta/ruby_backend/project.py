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
from typing import Dict, List, Optional

from . import cache, coverage_runner, param_types, rag, readme, recorder as rec, ruby_ast, summaries
from .backend import LanguageBackend, RubyBackend
from .generate import AskFn, GenOutcome, _default_ask, generate_spec_for_method

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
    done_what: str = ""       # implementation-view summary (item 3)
    what_todo: str = ""       # requirement-view summary, from README (item 7)
    summary: str = ""         # final merged summary, fed to the Planner context
    judge: str = ""           # inferred parameter types hint (item 5)

    @property
    def planner_summary(self) -> str:
        """Summary + inferred param types, as fed to the Planner context."""
        return f"{self.summary}\n\n{self.judge}".strip() if self.judge else self.summary

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
    def _spec_stem(self) -> str:
        stem = os.path.splitext(os.path.basename(self.file_path))[0]
        owner = _sanitize(self.owner_class.qualified_name) if self.owner_class else "toplevel"
        return f"{stem}__{owner}__{_sanitize(self.method.name)}"

    @property
    def spec_path(self) -> str:
        return os.path.join("spec", f"{self._spec_stem}_spec.rb")

    def spec_path_for_round(self, rnd: int) -> str:
        """One spec file per round (``..._r0_spec.rb``, ``..._r1_spec.rb``), so
        later rounds ADD coverage-targeted specs instead of overwriting — the
        Ruby analogue of MARTA's ``<prefix>_<round>.py`` accumulation."""
        return os.path.join("spec", f"{self._spec_stem}_r{rnd}_spec.rb")

    @property
    def source_rel(self) -> str:
        """Path of the code file relative to source_dir (= require_target + .rb).
        Matches the keys returned by the coverage runner."""
        return self.require_target + ".rb"


@dataclass
class RubyProject:
    root_dir: str             # project root (cwd for RSpec)
    source_dir: str           # dir containing the code under test, relative to root

    files: List[str] = field(default_factory=list)          # absolute .rb paths
    targets: List[MethodTarget] = field(default_factory=list)
    rag_db: Optional[rag.RubyFunctionDatabase] = None
    type_index: Optional[param_types.ProjectTypeIndex] = None
    recorder: Optional[rec.RubyRecorder] = None
    call_graph: Optional[object] = None   # CallGraph (static), built in discover()
    code_changed: bool = True             # False on cg_cache hit (source unchanged)
    backend: LanguageBackend = field(default_factory=RubyBackend)

    def _recorder(self) -> rec.RubyRecorder:
        if self.recorder is None:
            self.recorder = rec.RubyRecorder()
        return self.recorder

    @property
    def abs_source(self) -> str:
        return os.path.join(self.root_dir, self.source_dir)

    def discover(self) -> "RubyProject":
        """Find *.rb under source_dir (excluding spec/) and build method targets."""
        self.files = []
        self.targets = []
        self.type_index = param_types.ProjectTypeIndex()
        for path in self.backend.discover_files(self.abs_source):
            rel = os.path.relpath(path, self.abs_source)
            self.files.append(path)
            fp = self.backend.parse_file(path)
            self.type_index.add_file(fp)  # whole-project index for type inference
            classes_by_qn = {c.qualified_name: c for c in fp.classes}
            require_target = self.backend.module_ref(rel)
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
        # Judge needs the full index (cross-file classes), so compute after.
        for t in self.targets:
            t.judge = self.type_index.judge_for_method(t.method)
        # Static call graph (item 6) — feeds cross-method done_what enrichment.
        # Cached by source hash (cg_cache); rebuilt only when the source changes.
        src_hash = cache.compute_source_hash(self.files)
        cg_path = cache.call_graph_path(self.root_dir)
        cached_cg = cache.load_call_graph(cg_path, src_hash)
        # code_changed espelha o Python: cache hit do grafo => source inalterado.
        self.code_changed = cached_cg is None
        if cached_cg is not None:
            from .call_graph import CallGraph
            self.call_graph = CallGraph.from_json(cached_cg)
        else:
            self.call_graph = self.backend.build_call_graph(self.files)
            if self.call_graph is not None:
                cache.save_call_graph(cg_path, src_hash, self.call_graph.to_json())
        return self

    async def generate_all(
        self,
        ask: Optional[AskFn] = None,
        max_attempts: int = 3,
        limit: Optional[int] = None,
    ) -> List[GenOutcome]:
        """Generate a spec per discovered method target (single round)."""
        outcomes: List[GenOutcome] = []
        targets = self.targets[:limit] if limit else self.targets
        recorder = self._recorder()
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
                summary=t.planner_summary,
                related=self._related_for(t),
                max_attempts=max_attempts,
                recorder=recorder,
                backend=self.backend,

                error_help_fn=self._error_help_fn(t),
            )
            outcomes.append(outcome)
        return outcomes

    async def analyze_summaries(
        self,
        ask: Optional[AskFn] = None,
        limit: Optional[int] = None,
        use_cache: bool = True,
    ) -> None:
        """Populate each target's done_what / what_todo / summary before
        generation — the context-building phase MARTA runs in ``init()``.
        ``done_what`` is source-only until the call graph enriches it.

        Cached by source hash + model: on an unchanged project the whole LLM
        summary phase is skipped (``load_analysis_cache`` analogue).
        """
        targets = self.targets[:limit] if limit else self.targets
        model = os.getenv("MODEL", "default")
        src_hash = cache.compute_source_hash(self.files)
        path = cache.cache_path(self.root_dir, model)

        if use_cache:
            cached = cache.load_analysis(path, src_hash, model)
            if cached is not None and all(t.method.qualified_name in cached for t in targets):
                for t in targets:
                    self._apply_cached(t, cached[t.method.qualified_name])
                return

        ask = ask or _default_ask()
        ask = rec.token_tracking_ask(ask, self._recorder().score)
        overviews = readme.ReadmeOverviewCache(self.abs_source)

        # Pass 1: source-only done_what (MARTA's no-call-graph branch).
        for t in targets:
            t.done_what = await summaries.analyze_done_what(ask, t.context_source)

        # Pass 2: enrich done_what of callers with their callees' done_what,
        # following the static call graph (the PyCG-driven enrichment). Only
        # methods that actually call project methods pay the extra LLM call.
        if self.call_graph is not None:
            by_qn = {t.method.qualified_name: t for t in targets}
            for t in targets:
                called = [
                    f"{by_qn[c].method.qualified_name}: {by_qn[c].done_what}"
                    for c in self.call_graph.callees(t.method.qualified_name)
                    if c in by_qn and by_qn[c].done_what
                ]
                if called:
                    t.done_what = await summaries.analyze_done_what(
                        ask, t.context_source, called_summaries=called
                    )

        # what_todo (README) + final merged summary.
        for t in targets:
            overview = await overviews.overview_for(ask, t.file_path)
            t.what_todo = await readme.analyze_what_todo(ask, t.context_source, overview)
            t.summary = await summaries.generate_summary(
                ask, t.context_source, t.done_what, t.what_todo
            )
        if use_cache:
            cache.save_analysis(path, src_hash, model, {
                t.method.qualified_name: {
                    "done_what": t.done_what, "what_todo": t.what_todo,
                    "summary": t.summary, "judge": t.judge,
                }
                for t in targets
            })

    @staticmethod
    def _apply_cached(t: MethodTarget, entry: dict) -> None:
        t.done_what = entry.get("done_what", "")
        t.what_todo = entry.get("what_todo", "")
        t.summary = entry.get("summary", "")
        if entry.get("judge"):
            t.judge = entry["judge"]

    def build_rag(self, embed_documents=None, embed_query=None) -> None:
        """Index target summaries for retrieval. Call after analyze_summaries.
        A custom embedder can be injected (tests); default is the real bge one."""
        self.rag_db = rag.RubyFunctionDatabase(embed_documents, embed_query)
        self.rag_db.init(self.targets)

    def _related_for(self, t: MethodTarget) -> Optional[List[str]]:
        if self.rag_db is None:
            return None
        query = t.summary or t.done_what
        if not query:
            return None
        return self.rag_db.related_lines(query, k=3, exclude=t.method.qualified_name) or None

    def _example_passing_spec(self, t: MethodTarget) -> Optional[str]:
        """First spec already on disk for this target (kept specs are green)."""
        files = sorted(glob.glob(os.path.join(self.root_dir, "spec", f"{t._spec_stem}*_spec.rb")))
        for f in files:
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    return fh.read()
            except OSError:
                continue
        return None

    def _error_help_fn(self, t: MethodTarget):
        """Error-directed RAG for the self-heal loop (generate_react_flow port):
        given the failure output, retrieve similar methods and, when available,
        one of their passing specs as a concrete example."""
        if self.rag_db is None:
            return None

        def helper(error: str) -> str:
            hits = self.rag_db.query(error[:400], k=3, exclude=t.method.qualified_name)[:2]
            if not hits:
                return ""
            blocks = ["SIMILAR TESTED METHODS THAT MIGHT HELP:"]
            for sf in hits:
                snippet = " ".join((sf.done_what or sf.summary or "no summary").split())[:200]
                blocks.append(f"- {sf.method.qualified_name}: {snippet}")
                example = self._example_passing_spec(sf)
                if example:
                    blocks.append(f"  Example passing spec:\n  ```ruby\n{example[:400]}\n  ```")
            return "\n\n" + "\n".join(blocks)

        return helper

    def _all_spec_paths(self) -> List[str]:
        specs = glob.glob(os.path.join(self.root_dir, "spec", "**", "*.rb"), recursive=True)
        return [os.path.relpath(s, self.root_dir) for s in sorted(specs)]

    def measure_coverage(self) -> Dict[int, coverage_runner.MethodCoverage]:
        """Run every generated spec under Coverage and synthesise per-method
        missing_lines. Keyed by target index. Targets whose source file has no
        coverage data (e.g. no passing spec yet) map to full-miss coverage."""
        spec_paths = self._all_spec_paths()
        by_target: Dict[int, coverage_runner.MethodCoverage] = {}
        if not spec_paths:
            return by_target
        result = self.backend.run_coverage(self.source_dir, spec_paths, cwd=self.root_dir)
        for i, t in enumerate(self.targets):
            lines = result.files.get(t.source_rel)
            if lines:
                by_target[i] = self.backend.synthesize_coverage(t.method, lines)
        return by_target

    async def generate_rounds(
        self,
        rounds: int = 3,
        ask: Optional[AskFn] = None,
        max_attempts: int = 3,
        limit: Optional[int] = None,
    ) -> List[GenOutcome]:
        """Coverage-guided multi-round generation — the Fase 2 loop.

        Round 0 generates for every target; after each round coverage is
        measured over all accumulated specs, and later rounds regenerate only
        methods with missing lines, feeding those lines back to the Planner.
        Returns the flat list of per-round outcomes.
        """
        targets = list(enumerate(self.targets))
        if limit:
            targets = targets[:limit]
        outcomes: List[GenOutcome] = []
        cov: Dict[int, coverage_runner.MethodCoverage] = {}
        recorder = self._recorder()

        for rnd in range(rounds):
            recorder.score.first_run = (rnd == 0)  # first_run metrics = round 0
            recorder.start_count_time(f"round_{rnd}")
            for idx, t in targets:
                mc = cov.get(idx)
                if rnd > 0 and mc is not None and mc.fully_covered:
                    continue  # already fully covered — skip, like the Python loop
                # Skip resume-safe (porta o skip round-aware do Python): se o
                # código não mudou e o spec DESTA ronda já existe (run retomado),
                # não regenera — o ficheiro em disco conta para a cobertura via
                # _all_spec_paths(). Rondas por fazer continuam normalmente.
                round_spec = os.path.join(self.root_dir, t.spec_path_for_round(rnd))
                if not self.code_changed and os.path.exists(round_spec):
                    print(f"[SKIP] Spec de '{t.method.qualified_name}' já existe (ronda {rnd}), a saltar...")
                    continue
                if rnd == 0 or mc is None:
                    coverage_info = "First pass: Try to achieve maximum coverage."
                else:
                    coverage_info = f"MISSING LINES TO COVER: {mc.format_missing_lines()}"
                outcome = await generate_spec_for_method(
                    method_qualified_name=t.method.qualified_name,
                    describe_subject=t.describe_subject,
                    method_source=t.context_source,
                    require_target=t.require_target,
                    load_paths=[self.source_dir],
                    spec_path=t.spec_path_for_round(rnd),
                    cwd=self.root_dir,
                    ask=ask,
                    summary=t.planner_summary,
                    related=self._related_for(t),
                    max_attempts=max_attempts,
                    coverage_info=coverage_info,
                    recorder=recorder,
                    backend=self.backend,

                    error_help_fn=self._error_help_fn(t),
                )
                outcomes.append(outcome)
            recorder.end_count_time(f"round_{rnd}")
            cov = self.measure_coverage()
            recorder.score.coverage.append(
                {t.method.qualified_name: (cov[i].covered_lines if i in cov else 0)
                 for i, t in targets}
            )
        return outcomes
