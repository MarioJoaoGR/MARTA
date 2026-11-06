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
import hashlib
import json
import os
import re
import shutil
import tempfile
import time
from collections import Counter
from contextlib import nullcontext
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional, Mapping
from types import MappingProxyType

from . import cache, coverage_runner, param_types, rag, readme, recorder as rec, ruby_ast, summaries
from .ablation import AblationOptions
from .analysis_state import AnalysisArchive, analysis_provenance
from .checkpoints import RoundCheckpoints, atomic_json, atomic_write, dependency_files, file_hash
from .backend import LanguageBackend, RubyBackend
from .generate import AskFn, GenOutcome, _default_ask, generate_spec_for_method
from .source_context import SourceContext, build_source_context
from .prompt_budget import PromptBudget, budget_provenance
from .retrieval_cache import PlannerRetrievalCache
from .evidence import evidence_policy, semantic_decision
from .class_context import build_class_context, POLICY as CLASS_CONTEXT_POLICY

# Default generation skips constructors; exact task selectors may request them.
SKIP_METHODS = {"initialize"}

# Bump when analysis prompts, definition identities, or cache semantics change.
ANALYSIS_SCHEMA = 8


class AnalysisResponseError(RuntimeError):
    """Analysis cannot continue with an empty or nontext LLM response."""


def _slice_lines(path: str, start: int, end: int) -> str:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return "\n".join(lines[start - 1:end])


def _sanitize(name: str) -> str:
    # Ruby method names can end in ? ! = — make a filesystem/spec-safe token.
    name = name.replace("?", "_q").replace("!", "_bang").replace("=", "_set")
    return re.sub(r"[^0-9A-Za-z_]", "_", name)


class _ClassEntry:
    """Adapter so class summaries fit the RubyFunctionDatabase target shape."""

    class _M:
        def __init__(self, qn):
            self.qualified_name = qn

    def __init__(self, qn: str, summary: str):
        self.method = self._M(qn)
        self.summary = summary
        self.done_what = ""


# Where generated specs live, relative to the project root — SEPARATE from the
# project's own spec/ (the Test4DT_tests analogue). Keeps tool output apart from
# the human suite so benchmark coverage measures ONLY generated tests.
GENERATED_SPEC_DIR = "marta_specs"
SPEC_NAMING_POLICY = "definition-sha256-v1-task-legacy"
SPEC_LABEL_CHARS = 96

# Character budget for focused source views. Auxiliary code is reduced first;
# a larger focal method is preserved intact and explicitly reported as over-limit.
# This is separate from the server context window and a whole-prompt token budget.
MAX_CONTEXT_CHARS = int(os.getenv("MARTA_MAX_CONTEXT_CHARS", "6000"))


@dataclass
class MethodTarget:
    method: ruby_ast.MethodInfo
    owner_class: Optional[ruby_ast.ClassInfo]
    file_path: str            # absolute path to the .rb file
    require_target: str       # e.g. "foo/bar" (relative to source_dir, no .rb)
    # Caminho do ficheiro relativo a source_dir, quando difere de require_target +
    # ".rb" (com load_paths: `deliver/lib/deliver/setup.rb` faz `require
    # "deliver/setup"`). É a chave que o helper de cobertura devolve.
    rel_path: str = ""
    # outros métodos da mesma classe (para a vista focada de context_source)
    siblings: List[ruby_ast.MethodInfo] = field(default_factory=list)
    spec_dir: str = GENERATED_SPEC_DIR
    done_what: str = ""       # implementation-view summary (item 3)
    what_todo: str = ""       # requirement-view summary, from README (item 7)
    summary: str = ""         # final merged summary, fed to the Planner context
    judge: str = ""           # inferred parameter types hint (item 5)
    task_id: Optional[str | int] = None

    @property
    def analysis_id(self) -> str:
        """Definition identity, independent of generation tasks/selectors."""
        return json.dumps([self.source_rel, self.method.qualified_name,
                           self.method.start_line, self.method.end_line],
                          ensure_ascii=True, separators=(",", ":"))

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
    def class_declaration(self) -> Optional[str]:
        cls = self.owner_class
        if cls is None:
            return None
        header = f"{cls.kind} {cls.qualified_name}"
        if cls.superclass:
            header += f" < {cls.superclass}"
        return header

    @property
    def class_code(self) -> str:
        """Class/module declaration and non-method statements, without method bodies."""
        if self.owner_class is None:
            return ""
        body = "\n".join(f"  {statement}" for statement in self.owner_class.body_statements)
        return self.class_declaration + ("\n" + body if body else "")

    @property
    def source_context(self) -> SourceContext:
        focal = _slice_lines(self.file_path, self.method.start_line, self.method.end_line)
        init = next((m for m in self.siblings if m.name == "initialize"), None)
        constructor = None
        if self.owner_class is not None and init is not None and self.method.name != "initialize":
            constructor = _slice_lines(self.file_path, init.start_line, init.end_line)
        return build_source_context(
            focal, self.method.qualified_name, limit=MAX_CONTEXT_CHARS,
            declaration=self.class_declaration,
            statements=self.owner_class.body_statements if self.owner_class else [],
            constructor=constructor)

    @property
    def context_source(self) -> str:
        """Source-only compatibility view; the complete focal method is never cut."""
        return self.source_context.source

    @property
    def _spec_stem(self) -> str:
        stem = os.path.splitext(os.path.basename(self.file_path))[0]
        owner = _sanitize(self.owner_class.qualified_name) if self.owner_class else "toplevel"
        base = f"{stem}__{owner}__{_sanitize(self.method.name)}"
        if self.task_id is not None:
            digest = hashlib.sha256(
                json.dumps([self.task_id, self.analysis_id]).encode()).hexdigest()[:20]
            return f"{base}__task_{digest}"
        # Human-readable labels are not identities: paths, singleton markers,
        # definition lines and sanitized Ruby names may otherwise collide.
        # Preserve the existing task branch above for frozen benchmark artifacts.
        label = _sanitize(base)[:SPEC_LABEL_CHARS]
        digest = hashlib.sha256(self.analysis_id.encode("utf-8")).hexdigest()
        return f"{label}__def_{digest}"

    @property
    def spec_path(self) -> str:
        return os.path.join(self.spec_dir, f"{self._spec_stem}_spec.rb")

    def spec_path_for_round(self, rnd: int) -> str:
        """One spec file per round (``..._r0_spec.rb``, ``..._r1_spec.rb``), so
        later rounds ADD coverage-targeted specs instead of overwriting — the
        Ruby analogue of MARTA's ``<prefix>_<round>.py`` accumulation."""
        return os.path.join(self.spec_dir, f"{self._spec_stem}_r{rnd}_spec.rb")

    @property
    def source_rel(self) -> str:
        """Path of the code file relative to source_dir — the key the coverage
        runner returns. Igual a ``require_target + ".rb"`` no caso simples; com
        load_paths os dois separam-se (`deliver/lib/deliver/setup.rb` pede-se por
        `deliver/setup`), e aí vale o ``rel_path``."""
        return self.rel_path or (self.require_target + ".rb")


class _AnalysisFunctionDatabase(rag.RubyFunctionDatabase):
    """Keep definition IDs in RAG without changing Ruby qualified names."""

    def _select(self, targets):
        docs, _ = super()._select(targets)
        # Keep the positional prefix expected by RubyFunctionDatabase.query.
        return docs, [f"{i}|{t.analysis_id}" for i, t in enumerate(self.targets)]

    def _pick(self, order, k, exclude):
        return [self.targets[i] for i in order
                if self.targets[i].analysis_id != exclude
                and self.targets[i].method.qualified_name != exclude][:k]


@dataclass
class RubyProject:
    root_dir: str             # project root (cwd for RSpec)
    source_dir: str           # dir containing the code under test, relative to root
    # Paridade com o get_output_root do Python: se definido, TODOS os outputs
    # (marta_specs/, caches) vão para esta pasta em vez de poluírem o projeto.
    # Run independente = output_root novo, exatamente como no lado Python.
    output_root: Optional[str] = None
    # Ficheiros-alvo (caminhos relativos a source_dir). Se definido, só os
    # métodos DESTES ficheiros viram alvos — o análogo do `modules` do
    # projects.json na MARTA Python (_targeted_file_messages). Por omissão,
    # os sumários e a análise estática continuam a ver todo o código fornecido.
    target_files: Optional[List[str]] = None
    # Ambiente de execução certificado pela camada 6 do dataset (vem do
    # `projetos.json` da camada 7). Sem ele, o comportamento de sempre: um só -I
    # (source_dir), sem porta de entrada, todos os .rb de source_dir analisados.
    #  - load_paths: pastas de carregamento, relativas a root_dir. Nos monorepos há
    #    uma por sub-gem (fastlane: 19). Decidem também o nome do `require`: o
    #    caminho do ficheiro sem o prefixo da pasta que o contém.
    #  - preload: a porta de entrada da gem, carregada antes de cada spec, tal como
    #    a camada 6 a carregou antes de certificar cada módulo.
    #  - code_files: os ficheiros que a camada 2 analisou, relativos a root_dir.
    #    Assim o grafo e o índice de tipos veem exatamente o que a camada 7 viu ao
    #    calcular os vizinhos de cada módulo.
    load_paths: Optional[List[str]] = None
    preload: Optional[str] = None
    code_files: Optional[List[str]] = None
    # Filtro por MÉTODO (nomes qualificados). Os alvos são por ficheiro, mas o
    # braço da ablação só precisa de repetir os métodos cujo prompt o grafo muda
    # (4601 dos 6898; ver benchmark/alvos_ablacao.py). Sem isto, repetia todos.
    method_names: Optional[List[str]] = None
    # Módulos que a camada 6 só certificou "com a biblioteca carregada": depois de
    # carregar TODA a biblioteca em três passagens (rb/ordem.rb). A porta de
    # entrada não chega para eles — o verificador mostrou-o nos 15 do corpus.
    #  - library_files: o que se carrega nessas passagens (relativo a root_dir)
    #  - library_targets: os ficheiros-alvo que precisam disso
    # Só os specs DESTES alvos pagam o carregamento; os outros não mudam.
    library_files: Optional[List[str]] = None
    library_targets: Optional[List[str]] = None

    # Authoritative generation selectors: source-relative file, exact Ruby
    # method name, 1-based inclusive definition lines, and opaque task_id.
    target_selectors: Optional[List[dict]] = None
    analysis_targets: List[MethodTarget] = field(default_factory=list)
    _ambiguous_qns: set = field(default_factory=set, init=False, repr=False)
    _loading_dependency_index: Optional[dict] = field(default=None, init=False, repr=False)
    _analysis_fingerprint_used: Optional[str] = field(default=None, init=False, repr=False)
    _planner_retrieval: PlannerRetrievalCache = field(default_factory=PlannerRetrievalCache, init=False, repr=False)
    last_analysis_archive: Optional[str] = field(default=None, init=False)

    files: List[str] = field(default_factory=list)          # absolute .rb paths
    targets: List[MethodTarget] = field(default_factory=list)
    rag_db: Optional[rag.RubyFunctionDatabase] = None
    type_index: Optional[param_types.ProjectTypeIndex] = None
    recorder: Optional[rec.RubyRecorder] = None
    call_graph: Optional[object] = None   # CallGraph (static), built in discover()
    code_changed: bool = True             # False on cg_cache hit (source unchanged)
    _class_definitions: dict = field(default_factory=dict, init=False, repr=False)
    class_files: Dict[str, str] = field(default_factory=dict)   # class qn -> abs path
    class_summaries: Dict[str, str] = field(default_factory=dict)  # class qn -> summary
    class_db: Optional[rag.RubyClassIndex] = None
    judge_decisions: Dict[str, dict] = field(default_factory=dict, init=False)
    backend: LanguageBackend = field(default_factory=RubyBackend)
    ablation_options: AblationOptions = field(default_factory=AblationOptions)
    subprocess_env: Optional[Mapping[str, str]] = field(default=None, repr=False)
    isolate_execution: bool = False
    generation_workers: int = 1
    round_barrier: bool = False
    _bound_env: Optional[Mapping[str, str]] = field(default=None, init=False, repr=False)

    def __post_init__(self):
        from .workers import validate_workers
        validate_workers(self)
        if self.subprocess_env is not None:
            self._execution_environment()

    def _execution_environment(self):
        if self._bound_env is None:
            env = os.environ if self.subprocess_env is None else self.subprocess_env
            if any(not isinstance(k, str) or not isinstance(v, str) for k, v in env.items()):
                raise TypeError("Subprocess environment keys and values must be strings")
            self._bound_env = MappingProxyType(dict(env))
        return self._bound_env

    @property
    def _coordinated_generation(self):
        return self.round_barrier or self.generation_workers > 1

    def _workspace(self):
        if self._coordinated_generation:
            from .workers import GenerationWorkers
            return GenerationWorkers(self)
        if not self.isolate_execution:
            return nullcontext(None)
        from .execution import GenerationWorkspace
        return GenerationWorkspace(self)


    def _planner_summary(self, target: MethodTarget) -> str:
        return target.summary if self.ablation_options.no_type_hints else target.planner_summary

    def _recorder(self) -> rec.RubyRecorder:
        if self.recorder is None:
            self.recorder = rec.RubyRecorder()
        return self.recorder

    def out_root(self) -> str:
        """Raiz dos outputs (specs gerados + caches). = get_output_root do
        Python: output_root quando definido, senão o próprio projeto (legacy)."""
        if self.output_root:
            os.makedirs(self.output_root, exist_ok=True)
            return self.output_root
        return self.root_dir

    def _spec_dir(self) -> str:
        return os.path.join(self.out_root(), GENERATED_SPEC_DIR) \
            if self.output_root else GENERATED_SPEC_DIR

    @property
    def abs_source(self) -> str:
        return os.path.join(self.root_dir, self.source_dir)

    def _load_path_list(self) -> List[str]:
        """Pastas de carregamento para o `-I`, relativas a root_dir. Sem ambiente
        declarado, só o source_dir — o comportamento de sempre.

        Com ambiente, a raiz do código entra TAMBÉM, e no fim: a camada 6 fazia
        `$LOAD_PATH.unshift(raiz)` depois das pastas, e é por isso que ficheiros
        fora de qualquer `lib/` (o `setup.rb` da kramdown, o `rakelib/` da pg)
        carregam. Sem a raiz, cinco módulos do corpus falhariam por causa do
        ambiente e não do código. Não entra no cálculo do nome do `require`, que
        usa só as pastas declaradas (ver _require_for)."""
        if not self.load_paths:
            return [self.source_dir]
        return list(self.load_paths) + [self.source_dir]

    def _apply_environment(self) -> None:
        """Bind execution paths and environment to this project's native backend."""
        # Own the native backend configuration even if a caller reused an instance.
        if type(self.backend) is RubyBackend:
            import copy
            self.backend = copy.copy(self.backend)
            self.backend.bind_environment(self._execution_environment())
        self.backend.extra_load_paths = self._load_path_list()
        self.backend.requires = [self.preload] if self.preload else []
        script = self._library_script()
        self.backend.coverage_requires = [script] if script else []

    def _library_script(self) -> Optional[str]:
        """Escreve o carregamento da biblioteca em três passagens, a mesma coisa
        que o rb/ordem.rb da camada 6 fez para certificar estes módulos, e devolve
        o caminho. None quando nenhum alvo precisa."""
        if not (self.library_files and self.library_targets):
            return None
        reqs = sorted({self._require_for(f) for f in self.library_files})
        linhas = ["# Gerado pela MARTA-Ruby: reproduz o rb/ordem.rb da camada 6.",
                  "# Três passagens, ignorando falhas: um módulo que falha na",
                  "# primeira pode passar depois de os irmãos definirem constantes.",
                  "ALVOS_BIBLIOTECA = ["]
        linhas += [f"  {json.dumps(r)}," for r in reqs]
        linhas += ["].freeze",
                   "3.times do",
                   "  ALVOS_BIBLIOTECA.each do |a|",
                   "    begin",
                   "      require a",
                   "    rescue Exception # rubocop:disable Lint/RescueException",
                   "      nil",
                   "    end",
                   "  end",
                   "end", ""]
        pasta = os.path.join(self.out_root(), ".marta_ruby_cache")
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, "biblioteca.rb")
        from pathlib import Path
        content = "\n".join(linhas)
        if not os.path.isfile(caminho) or Path(caminho).read_text(encoding="utf-8") != content:
            atomic_write(caminho, content)
        return os.path.abspath(caminho)

    def _extra_requires_for(self, t: "MethodTarget") -> Optional[List[str]]:
        """O `-r` extra que só os specs dos módulos certificados com a biblioteca
        carregada levam."""
        if self.library_targets and t.source_rel in self.library_targets:
            script = self._library_script()
            return [script] if script else None
        return None

    def _generation_loading_for(self, t: "MethodTarget", *, recorder=None) -> str:
        from .loading import loading_plan, loading_context
        from .dependencies import bundle_index
        recorder = recorder or self.recorder
        timer = recorder.medir("production_dependencies") if recorder else nullcontext()
        with timer:
            if self._loading_dependency_index is None:
                self._loading_dependency_index = bundle_index(self.root_dir, env=self._execution_environment())
            rel = os.path.join(self.source_dir, t.source_rel)
            plan = loading_plan(self.root_dir, rel, t.require_target, self._loading_dependency_index, env=self._execution_environment())
        if recorder is not None:
            recorder.evento(tipo="production_loading", metodo=t.method.qualified_name, plan=plan)
        return loading_context(plan)

    def _code_paths(self) -> List[str]:
        """Ficheiros a analisar: os do manifesto quando existe (exatamente os que
        a camada 2 leu, para o grafo ver o que a camada 7 viu), senão a descoberta
        do backend."""
        if self.code_files is None:
            return self.backend.discover_files(self.abs_source)
        return [p for p in (os.path.join(self.abs_source, rel) for rel in self.code_files)
                if os.path.isfile(p)]

    def _require_for(self, rel: str) -> str:
        """O nome por que o spec pede o ficheiro: tira o prefixo da PRIMEIRA pasta
        de carregamento que o contém, a mesma regra e a mesma ordem com que a
        camada 6 certificou o módulo. No fastlane, `deliver/lib/deliver/setup.rb`
        pede-se por `deliver/setup`, não pelo caminho inteiro."""
        for lp in (self.load_paths or []):
            pref = "" if lp in ("", ".") else lp.rstrip("/") + "/"
            if pref and rel.startswith(pref):
                return self.backend.module_ref(rel[len(pref):])
        return self.backend.module_ref(rel)

    def discover(self) -> "RubyProject":
        """Parse supplied production files and separate analysis from generation.

        Full context retains every parsed method, including constructors.
        Exact selectors are authoritative; otherwise legacy generation filters
        and the default constructor skip apply.
        """
        self.files = []
        self.targets = []
        self.analysis_targets = []
        self.class_files = {}
        self._class_definitions = {}
        self.class_summaries = {}
        self.judge_decisions = {}
        self._analysis_fingerprint_used = None
        self.last_analysis_archive = None
        self._planner_retrieval.clear()
        self._loading_dependency_index = None
        self.rag_db = self.class_db = None
        self.type_index = param_types.ProjectTypeIndex()
        self._apply_environment()
        # Métodos de TODOS os ficheiros (não só dos alvos): o grafo precisa do
        # projeto inteiro, e assim reaproveita-se este parse em vez de o repetir.
        all_methods: List = []
        for path in sorted(set(self._code_paths())):
            rel = os.path.relpath(path, self.abs_source)
            self.files.append(path)
            fp = self.backend.parse_file(path)
            self.type_index.add_file(fp)  # whole-project index for type inference
            all_methods.extend(fp.methods)
            classes_by_qn = {c.qualified_name: c for c in fp.classes}
            for c in fp.classes:
                self.class_files.setdefault(c.qualified_name, path)
                self._class_definitions.setdefault(c.qualified_name, []).append((path, c))
            require_target = self._require_for(rel)
            by_owner: Dict[str, List] = {}
            for m in fp.methods:
                if m.owner:
                    by_owner.setdefault(m.owner, []).append(m)
            for m in fp.methods:
                self.analysis_targets.append(MethodTarget(
                    method=m,
                    owner_class=classes_by_qn.get(m.owner) if m.owner else None,
                    file_path=path,
                    require_target=require_target,
                    rel_path=rel,
                    spec_dir=self._spec_dir(),
                    siblings=[s for s in by_owner.get(m.owner or "", []) if s is not m],
                ))
        counts = Counter(m.qualified_name for m in all_methods)
        self._ambiguous_qns = {qn for qn, count in counts.items() if count > 1}
        if self.target_selectors is not None:
            # The benchmark identifies exact methods by file, name and lines.
            self.targets = self._select_tasks(self.analysis_targets)
        else:
            # Otherwise, file/name filters select which methods receive tests.
            # Every method remains in analysis_targets for context construction.
            for target in self.analysis_targets:
                if target.method.name in SKIP_METHODS:
                    continue
                if self.target_files is not None and target.source_rel not in self.target_files:
                    continue
                if self.method_names is not None and target.method.qualified_name not in self.method_names:
                    continue
                self.targets.append(target)
        identities = Counter(t.analysis_id for t in self.analysis_targets)
        duplicates = [identity for identity, count in identities.items() if count > 1]
        if duplicates:
            # The parser has no column positions: repeated same-name defs on
            # one line cannot be safely distinguished by this identity format.
            raise ValueError(f"Ambiguous analysis definition identities: {duplicates!r}")
        # Keep additional declaration references only for the existing class
        # summary population, without retaining unrelated module/stub bodies.
        class_owners = {t.owner_class.qualified_name for t in self.analysis_targets
                        if t.owner_class is not None}
        self._class_definitions = {qn: values for qn, values in self._class_definitions.items()
                                  if qn in class_owners and self.type_index.classes[qn].kind == "class"}
        # Judge needs the full index (cross-file classes), so compute after.
        for t in self.analysis_targets:
            t.judge = self.type_index.judge_for_method(t.method)
        self._sync_generation_analysis()
        # Static call graph (item 6) — feeds cross-method done_what enrichment.
        # Cache keyed by source hash + RESOLVER_VERSION .
        from .call_graph import RESOLVER_VERSION
        src_hash = f"{cache.compute_source_hash(self.files)}:r{RESOLVER_VERSION}"
        cg_path = cache.call_graph_path(self.out_root())
        cached_cg = cache.load_call_graph(cg_path, src_hash)
        # code_changed espelha o Python: cache hit do grafo => source inalterado.
        self.code_changed = cached_cg is None
        if cached_cg is not None:
            from .call_graph import CallGraph
            self.call_graph = CallGraph.from_json(cached_cg)
        else:
            self.call_graph = self.backend.build_call_graph(
                self.files, methods=all_methods, index=self.type_index)
            if self.call_graph is not None:
                cache.save_call_graph(cg_path, src_hash, self.call_graph.to_json())
        return self

    def _select_tasks(self, analysis_targets: List[MethodTarget]) -> List[MethodTarget]:
        """Resolve every selector before analysis; never silently drop a task."""
        if not isinstance(self.target_selectors, list):
            raise ValueError("target_selectors must be a list")
        selected, task_ids = [], set()
        for selector in self.target_selectors:
            required = {"file", "start_line", "end_line", "name", "task_id"}
            if not isinstance(selector, dict) or not required <= selector.keys():
                raise ValueError(f"Invalid target selector: {selector!r}")
            file, name, task_id = (selector[k] for k in ("file", "name", "task_id"))
            start, end = selector["start_line"], selector["end_line"]
            if (not all(isinstance(v, str) and v for v in (file, name))
                    or type(task_id) not in (str, int) or str(task_id) == ""
                    or type(start) is not int or type(end) is not int
                    or start < 1 or end < start):
                raise ValueError(f"Invalid target selector: {selector!r}")
            file = os.path.normpath(file)
            if os.path.isabs(file) or file == ".." or file.startswith(".." + os.sep):
                raise ValueError(f"Task file must be source-relative: {file!r}")
            if str(task_id) in task_ids:
                raise ValueError(f"Duplicate task_id: {task_id!r}")
            task_ids.add(str(task_id))
            matches = [t for t in analysis_targets if t.source_rel == file
                       and t.method.name == name
                       and t.method.start_line == start and t.method.end_line == end]
            if len(matches) != 1:
                raise ValueError(f"Task {task_id!r}: expected exactly one definition, "
                                 f"found {len(matches)} for {selector!r}")
            # Separate task wrappers allow two tasks for the same definition.
            selected.append(replace(matches[0], task_id=task_id))
        return selected

    def _sync_generation_analysis(self) -> None:
        by_id = {t.analysis_id: t for t in self.analysis_targets}
        for t in self.targets:
            source = by_id.get(t.analysis_id)
            if source is not None and source is not t:
                for attr in ("done_what", "what_todo", "summary", "judge"):
                    setattr(t, attr, getattr(source, attr))

    def _analysis_path(self, model: str, enrich: bool, *, root_dir: Optional[str] = None) -> str:
        path = cache.cache_path(root_dir if root_dir is not None else self.out_root(),
                                model if enrich else f"{model}_sem_grafo")
        # Keep the established full-analysis cache name for compatible results.
        return path[:-5] + ".full_context.json"

    def _analysis_fingerprint(self, targets: List[MethodTarget], *, readme_snapshot=None, provenance=None) -> str:
        from .call_graph import RESOLVER_VERSION
        from .execution import ENVIRONMENT_KEYS
        readme_snapshot = readme_snapshot or readme.ReadmeOverviewCache(
            self.abs_source, project_root=self.root_dir)
        payload = {
            "schema": ANALYSIS_SCHEMA,
            "provenance": provenance if provenance is not None else analysis_provenance(),
            "scope": "full",
            "class_context_policy": CLASS_CONTEXT_POLICY,
            "ruby_execution_environment": {key: self._execution_environment().get(key) for key in ENVIRONMENT_KEYS},
            "methods": sorted(t.analysis_id for t in targets),
            "max_context_chars": MAX_CONTEXT_CHARS,
            "max_classes": None,
            "resolver": RESOLVER_VERSION,
            "readme_policy": readme.README_POLICY,
            "readmes": readme_snapshot.manifest_for([t.file_path for t in targets]),
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    @staticmethod
    def _load_analysis_bundle(path, source_hash, model, fingerprint, enrich):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            return None
        if (not isinstance(data, dict) or data.get("source_hash") != source_hash
                or data.get("model") != model or data.get("fingerprint") != fingerprint
                or data.get("enrich") is not enrich
                or not isinstance(data.get("targets"), dict)
                or not isinstance(data.get("classes"), dict)):
            return None
        if not all(isinstance(e, dict) and all(
                isinstance(e.get(key), str) and e[key].strip()
                for key in ("done_what", "what_todo", "summary", "done_what_passagem1"))
                for e in data["targets"].values()):
            return None
        if not all(isinstance(value, str) and value.strip() for value in data["classes"].values()):
            return None
        return data

    def _source_for(self, target: MethodTarget, phase: Optional[str] = None) -> str:
        view = target.source_context
        if view.reduced or view.over_limit:
            recorder = self._recorder()
            recorder.evento(tipo="source_context", fase=phase or recorder.fase_atual,
                            metodo=target.method.qualified_name, source=target.source_rel,
                            limit=view.limit, source_chars=len(view.source), method_chars=view.method_chars,
                            over_limit=view.over_limit,
                            omitted_class_statements=view.omitted_class_statements,
                            omitted_constructor=view.omitted_constructor,
                            omitted_class_declaration=view.omitted_class_declaration)
        return view.source

    async def generate_all(
        self,
        ask: Optional[AskFn] = None,
        max_attempts: int = 3,
        limit: Optional[int] = None,
    ) -> List[GenOutcome]:
        """Generate a spec per discovered method target (single round)."""
        outcomes: List[GenOutcome] = []
        targets = self.targets[:limit] if limit else self.targets
        self._validate_spec_paths(targets)
        recorder = self._recorder()
        from .workers import validate_workers
        if self._coordinated_generation and targets:
            ask = ask or _default_ask()
        validate_workers(self, ask)
        # The single-round API has no resume checkpoint, but shares the writer lock.
        lock = RoundCheckpoints(self.out_root(), {}, recorder.evento)
        with lock.locked(), self._workspace() as workspace:
            if self._coordinated_generation:
                if self._all_spec_paths():
                    self._measure_retained_suite([], workspace=workspace)
                jobs = [(t, t.spec_path, "First pass: Try to achieve maximum coverage.") for t in targets]
                outcomes = await workspace.generate_round(jobs, ask, max_attempts, recorder, 0)
                self._measure_retained_suite(outcomes, workspace=workspace)
            else:
                for t in targets:
                    outcomes.append(await self._generate_target(t, t.spec_path, ask, max_attempts, recorder, workspace))
            if workspace is not None:
                workspace.verify_inputs()
        return outcomes

    async def _generate_target(self, t, spec_path, ask, max_attempts, recorder,
                               workspace=None, coverage_info="First pass: Try to achieve maximum coverage.",
                               *, examples=None, publish=True):
        generate = workspace.generate if workspace is not None else generate_spec_for_method
        return await generate(
            method_qualified_name=t.method.qualified_name,
            describe_subject=t.describe_subject,
            method_source=self._source_for(t, "generation"),
            focal_source=t.source_context.mandatory_source,
            require_target=t.require_target,
            load_paths=self._load_path_list(),
            spec_path=spec_path,
            cwd=self.root_dir,
            ask=ask,
            summary=self._planner_summary(t),
            related=self._related_for(t, **({"recorder": recorder} if self._coordinated_generation else {})),
            max_attempts=self.ablation_options.attempts(max_attempts),
            coverage_info=coverage_info,
            recorder=recorder,
            backend=self.backend,

            error_help_fn=self._error_help_fn(t, **({"examples": examples} if examples is not None else {})),
            extra_requires=self._extra_requires_for(t),
            loading_context=self._generation_loading_for(t, **({"recorder": recorder} if self._coordinated_generation else {})),
            **({"publish": False} if not publish else {}),
        )

    async def analyze_summaries(
        self, ask: Optional[AskFn] = None, use_cache: bool = True,
        enrich: bool = True, reaproveitar_passagem1_de: Optional[str] = None,
    ) -> None:
        """Archive every analysis, independently of reusable-cache policy.

        With use_cache=False, neither whole bundles nor first-pass references
        are read and the previous reusable cache is preserved. Every completed
        result, including a cache hit or empty pool, has a separate bundle.
        """
        self._planner_retrieval.clear()
        archive = AnalysisArchive(self.out_root(), use_cache=use_cache, enrich=enrich)
        self.last_analysis_archive = str(archive.root)
        self._analysis_fingerprint_used = None
        with archive:
            # Resolve the real default client before fingerprinting, including
            # its dotenv configuration; injected callbacks never initialize it.
            if ask is None and self.analysis_targets:
                ask = _default_ask()
            model = os.getenv("MODEL", "default")
            provenance = analysis_provenance(ask)
            overviews = readme.ReadmeOverviewCache(self.abs_source, project_root=self.root_dir)
            fingerprint = self._analysis_fingerprint(
                self.analysis_targets, readme_snapshot=overviews, provenance=provenance)
            metadata = {"source_hash": cache.compute_source_hash(self.files), "model": model,
                        "fingerprint": fingerprint, "enrich": enrich, "schema": ANALYSIS_SCHEMA,
                        "provenance": provenance, "readme_policy": readme.README_POLICY,
                        "readmes": overviews.manifest_for([t.file_path for t in self.analysis_targets])}
            archive.annotate(**metadata)
            bundle, cache_hit = await self._analyze_summaries(
                ask=ask, use_cache=use_cache, enrich=enrich,
                reaproveitar_passagem1_de=reaproveitar_passagem1_de,
                metadata=metadata, overviews=overviews, archive=archive)
            if analysis_provenance(ask) != provenance:
                raise AnalysisResponseError("Analysis configuration changed during execution; no cache published")
            if cache.compute_source_hash(self.files) != metadata["source_hash"]:
                raise AnalysisResponseError("Production source changed during analysis; no cache published")
            # A no-cache analysis is evidence, not a replacement for old cache.
            # Save its complete result before publishing a reusable cache.
            atomic_json(archive.root / "bundle.json", bundle)
            if use_cache and not cache_hit:
                atomic_json(self._analysis_path(model, enrich), bundle)
            archive.complete(cache_hit=cache_hit)
            self._analysis_fingerprint_used = fingerprint
            self._recorder().evento(tipo="analysis_archive", archive=str(archive.root),
                                    cache_hit=cache_hit, fingerprint=fingerprint)

    async def _analyze_summaries(
        self,
        ask: Optional[AskFn] = None,
        use_cache: bool = True,
        enrich: bool = True,
        reaproveitar_passagem1_de: Optional[str] = None,
        *, metadata: dict, overviews: readme.ReadmeOverviewCache, archive: AnalysisArchive,
    ):
        """Populate each target's done_what / what_todo / summary before
        generation — the context-building phase MARTA runs in ``init()``.
        ``done_what`` is source-only until the call graph enriches it.

        Every supplied production method is analyzed, independently of the
        generation selection and limits. Generation uses self.targets.
        Cache validity includes sources, model, scope, exact analysis identities,
        README contents, schema and context limits. Graph arms use separate files.

        ``enrich=False`` é o braço da ablação: desliga os DOIS sítios onde o grafo
        entra (a 2ª passagem do done_what e a propagação do what_todo do chamador),
        que é tudo o que o grafo faz nesta fase. O resto do fluxo fica igual. A
        cache vai para um ficheiro próprio, senão um braço comia a do outro.
        """
        model = metadata["model"]
        src_hash = metadata["source_hash"]
        fingerprint = metadata["fingerprint"]
        readme_manifest = metadata["readmes"]
        path = self._analysis_path(model, enrich)

        # A fresh analysis (including a different graph arm) cannot inherit
        # requirements or semantic hints from an earlier analysis on this object.
        self.class_summaries = {}
        self.judge_decisions = {}
        self.rag_db = self.class_db = None
        for t in self.analysis_targets:
            t.done_what = t.what_todo = t.summary = ""
            t.judge = self.type_index.judge_for_method(t.method) if self.type_index else ""
        if use_cache:
            bundle = self._load_analysis_bundle(path, src_hash, model, fingerprint, enrich)
            cached = bundle["targets"] if bundle else {}
            if bundle is not None and all(t.analysis_id in cached for t in self.analysis_targets):
                for t in self.analysis_targets:
                    self._apply_cached(t, cached[t.analysis_id])
                self.class_summaries = bundle["classes"]
                self._sync_generation_analysis()
                return {**metadata, "targets": cached, "classes": self.class_summaries}, True
        if not self.analysis_targets:
            self._sync_generation_analysis()
            return {**metadata, "targets": {}, "classes": {}}, False

        r = self._recorder()
        ask = ask or _default_ask()
        budget = PromptBudget.from_ask(ask, r)
        # A Fase 1 são sete sub-fases e até agora media-se como um bloco só
        # ("collect_message"). Cada chamada fica etiquetada com a sua.
        tracked_ask = rec.token_tracking_ask(ask, r.score, r)

        async def checked_ask(system, user):
            try:
                response = await tracked_ask(system, user)
            except BaseException as error:
                archive.request(system, user, r, error={"type": type(error).__name__, "message": str(error)})
                raise
            archive.request(system, user, r, response=response)
            if not isinstance(response, str) or not response.strip():
                r.evento(tipo="analysis_invalid_response", fase=r.fase_atual,
                         response_type=type(response).__name__)
                raise AnalysisResponseError(
                    f"Invalid analysis response in {r.fase_atual}: expected nonempty text; "
                    "analysis stopped without saving an incomplete bundle")
            return response

        ask = checked_ask
        r.evento(tipo="analysis_readmes", policy=readme.README_POLICY, documents=readme_manifest)

        # Pass 1: source-only done_what (MARTA's no-call-graph branch).
        #
        # A passagem 1 só lê o código do método e não usa o grafo: sai igual nos
        # dois braços da ablação. Por isso o braço sem grafo vai buscá-la à cache
        # da execução normal (`reaproveitar_passagem1_de`) em vez de pagar a
        # chamada outra vez — uma por cada um dos 4601 métodos afetados. Só se
        # reaproveita o que bate certo com as mesmas fontes e o mesmo modelo.
        reaproveitada: Dict[str, str] = {}
        if reaproveitar_passagem1_de and use_cache:
            normal_bundle = self._load_analysis_bundle(
                reaproveitar_passagem1_de, src_hash, model, fingerprint, True)
            normal = normal_bundle["targets"] if normal_bundle else {}
            reaproveitada = {qn: e["done_what_passagem1"] for qn, e in normal.items()
                             if e.get("done_what_passagem1")}
        passagem1: Dict[str, str] = {}
        with r.fase("sumarios_passagem1"):
            for t in self.analysis_targets:
                qn = t.method.qualified_name
                if t.analysis_id in reaproveitada:
                    t.done_what = reaproveitada[t.analysis_id]
                else:
                    with r.contexto(metodo=qn):
                        t.done_what = await summaries.analyze_done_what(
                            ask, self._source_for(t), budget=budget,
                            focal_source=t.source_context.mandatory_source)
                passagem1[t.analysis_id] = t.done_what
        n_reap = sum(1 for t in self.analysis_targets if t.analysis_id in reaproveitada)
        if n_reap:
            print(f"♻️  [Ablação] passagem 1 reaproveitada da execução normal em "
                  f"{n_reap}/{len(self.analysis_targets)} métodos")
            r.evento(tipo="passagem1_reaproveitada", metodos=n_reap, alvos=len(self.analysis_targets))

        # Pass 2: enrich done_what of callers with their callees' done_what,
        # following the static call graph (the PyCG-driven enrichment). Only
        # methods that actually call project methods pay the extra LLM call.
        # Graph nodes only have qualified names. Omit ambiguous definitions
        # in BOTH directions rather than silently merging reopened methods.
        graph_policy = evidence_policy()
        supported_only = graph_policy["graph_context"] == "supported_only"
        r.evento(tipo="graph_context_policy", policy=graph_policy["graph_context"],
                 edges=len(self.call_graph.edges) if self.call_graph else 0,
                 supported_edges=sum(e.supported for e in self.call_graph.edges) if self.call_graph else 0)
        counts = Counter(t.method.qualified_name for t in self.analysis_targets)
        by_qn = {t.method.qualified_name: t for t in self.analysis_targets
                 if counts[t.method.qualified_name] == 1
                 and t.method.qualified_name not in self._ambiguous_qns}
        if self.call_graph is not None and enrich:
            # Esta é a fase que a ablação do grafo desliga: é aqui que o contexto
            # de um método passa a incluir o que os métodos chamados fazem.
            with r.fase("sumarios_passagem2"):
                for t in self.analysis_targets:
                    if t.method.qualified_name not in by_qn:
                        continue
                    called = [
                        f"{c}: {passagem1[by_qn[c].analysis_id]}\n{self.call_graph.evidence_label(t.method.qualified_name, c)}"
                        for c in self.call_graph.callees(t.method.qualified_name, supported_only=supported_only)
                        if c in by_qn and by_qn[c].done_what
                    ]
                    if called:
                        with r.contexto(metodo=t.method.qualified_name,
                                        chamados=len(called)):
                            t.done_what = await summaries.analyze_done_what(
                                ask, self._source_for(t), called_summaries=called, budget=budget,
                                focal_source=t.source_context.mandatory_source,
                            )

        # what_todo: raízes (sem callers) a partir do README; métodos chamados
        # herdam a perspetiva de requisito do chamador via grafo (porta do ramo
        # de propagação do analyze_what_todo). Ciclos/soltos caem no README.
        def _callers_of(t: MethodTarget) -> List[MethodTarget]:
            # A outra metade da ablação: sem grafo não há chamadores, logo todos os
            # métodos são raiz e o what_todo vem do README para todos.
            if (self.call_graph is None or not enrich
                    or t.method.qualified_name not in by_qn):
                return []
            names = self.call_graph.callers(t.method.qualified_name, supported_only=supported_only)
            names = sorted(names, key=lambda caller: (not self.call_graph.has_supported(caller, t.method.qualified_name), caller))
            return [by_qn[c] for c in names if c in by_qn]

        with r.fase("what_todo_raiz"):
            for t in self.analysis_targets:
                if not _callers_of(t):  # raiz
                    with r.contexto(metodo=t.method.qualified_name):
                        overview = await overviews.overview_for(ask, t.file_path, budget=budget)
                        t.what_todo = await readme.analyze_what_todo(
                            ask, self._source_for(t), overview, budget=budget,
                            focal_source=t.source_context.mandatory_source)

        # A outra metade do que a ablação do grafo desliga: sem arestas, todos os
        # métodos seriam raiz e o what_todo viria do README para todos.
        with r.fase("what_todo_propagado"):
            changed = True
            while changed:  # propaga pelas arestas até fixpoint
                changed = False
                for t in self.analysis_targets:
                    if t.what_todo:
                        continue
                    ready = [c for c in _callers_of(t) if c.what_todo]
                    if ready:
                        c = ready[0]
                        with r.contexto(metodo=t.method.qualified_name,
                                        chamador=c.method.qualified_name):
                            t.what_todo = await summaries.analyze_what_todo_from_caller(
                                ask, t.method.qualified_name, self._source_for(t),
                                c.method.qualified_name, c.what_todo, budget=budget,
                                focal_source=t.source_context.mandatory_source,
                                relationship=self.call_graph.evidence_label(c.method.qualified_name, t.method.qualified_name),
                            )
                        changed = True

        with r.fase("what_todo_fallback"):
            for t in self.analysis_targets:
                if not t.what_todo:  # ciclo sem raiz processada — fallback README
                    with r.contexto(metodo=t.method.qualified_name):
                        overview = await overviews.overview_for(ask, t.file_path, budget=budget)
                        t.what_todo = await readme.analyze_what_todo(
                            ask, self._source_for(t), overview, budget=budget,
                            focal_source=t.source_context.mandatory_source)

        # Merge final das duas perspetivas.
        with r.fase("sumario_final"):
            for t in self.analysis_targets:
                with r.contexto(metodo=t.method.qualified_name):
                    t.summary = await summaries.generate_summary(
                        ask, self._source_for(t), t.done_what, t.what_todo, budget=budget,
                        focal_source=t.source_context.mandatory_source,
                    )

        # Reuse source-only first-pass descriptions, not graph-enriched or
        # requirement summaries. Class evidence must not invent another graph arm.
        by_class = {}
        for target in self.analysis_targets:
            if target.owner_class is not None:
                by_class.setdefault(target.owner_class.qualified_name, []).append(target)
        with r.fase("sumarios_de_classe"):
            for qn, targets in by_class.items():
                cls = (self.type_index.classes if self.type_index else {}).get(qn)
                if cls is None or cls.kind != "class" or qn in self.class_summaries:
                    continue
                definitions = self._class_definitions.get(qn) or [
                    (t.file_path, t.owner_class) for t in targets]
                view = build_class_context(qn, definitions, targets, passagem1,
                                           root=self.root_dir, limit=MAX_CONTEXT_CHARS)
                with r.contexto(classe=qn):
                    r.evento(tipo="class_context", **view.metadata)
                    self.class_summaries[qn] = await summaries.analyze_class(
                        ask, view.core, budget=budget, class_evidence=list(view.records))

        entries = {
            t.analysis_id: {
                "done_what": t.done_what, "what_todo": t.what_todo,
                "summary": t.summary, "judge": t.judge,
                "done_what_passagem1": passagem1.get(t.analysis_id, ""),
            }
            for t in self.analysis_targets
        }
        self._sync_generation_analysis()
        return {**metadata, "targets": entries, "classes": self.class_summaries}, False

    @staticmethod
    def _apply_cached(t: MethodTarget, entry: dict) -> None:
        t.done_what = entry.get("done_what", "")
        t.what_todo = entry.get("what_todo", "")
        t.summary = entry.get("summary", "")
        if entry.get("judge"):
            t.judge = entry["judge"]

    def build_rag(self, embed_documents=None, embed_query=None, persist=True) -> None:
        """Index analysis-pool summaries for retrieval. Call after analyze_summaries.
        A custom embedder can be injected (tests); default is the real bge one.
        Also indexes class summaries and adds semantic type hints to ambiguous
        judges (the ``find_type_by_RAG`` analogue).

        Collections are persisted under ``.marta_ruby_cache/vectors/<scope>``.
        Sources, analysis settings, definition IDs, actual indexed text and the
        LLM/embedder identify reusable vectors. ``persist=False`` keeps them in
        memory (tests)."""
        self._planner_retrieval.clear()
        pdir = key = None
        if persist:
            pdir = os.path.join(cache.vectors_path(self.out_root()),
                                "full_context")
            documents = [(t.analysis_id, t.summary or t.done_what)
                         for t in self.analysis_targets]
            text_hash = hashlib.sha256(json.dumps(
                [documents, sorted(self.class_summaries.items())],
                ensure_ascii=True).encode()).hexdigest()
            key = cache.vectors_key(
                cache.compute_source_hash(self.files) + ":"
                + (self._analysis_fingerprint_used or self._analysis_fingerprint(self.analysis_targets)) + ":" + text_hash,
                os.getenv("MODEL", "default"),
                os.getenv("TRANSFORMER_PATH", "default"),
            )
        # Fase à parte: embeber os sumários é o custo que a cache de vetores veio
        # poupar, e no cluster corre em CPU (EMBED_DEVICE=cpu, para o Ollama ficar
        # com a GPU). Sem etiqueta própria, não havia como mostrar a poupança.
        self.class_db = None
        self.judge_decisions = {}
        with self._recorder().fase("rag"):
            self.rag_db = None
            if not self.ablation_options.no_method_retrieval:
                self.rag_db = _AnalysisFunctionDatabase(
                    embed_documents, embed_query, persist_dir=pdir, name="functions", key=key or "")
                self.rag_db.init(self.analysis_targets)
            if self.class_summaries and not self.ablation_options.no_type_hints:
                # Classes em NumPy, como o find_topK_message da Python (ver rag.py).
                self.class_db = rag.RubyClassIndex(
                    embed_documents, embed_query, persist_dir=pdir, key=key or "")
                self.class_db.init([_ClassEntry(qn, s) for qn, s in self.class_summaries.items()])
                self._augment_judge_semantic()
        if self.class_db is None and self.type_index is not None:
            # Do not retain a previous semantic choice after removing the index.
            for target in self.analysis_targets:
                target.judge = self.type_index.judge_for_method(target.method)
        self._sync_generation_analysis()
        if any(self.judge_decisions.values()):
            audit = tempfile.mkdtemp(prefix="judge_", dir=self._judge_archive_dir())
            atomic_json(os.path.join(audit, "report.json"), {
                "policy": evidence_policy(), "decisions": self.judge_decisions,
                "analysis_fingerprint": self._analysis_fingerprint_used,
                "vector_key": key,
                "interpretation": "Cosine similarity and structural compatibility are not calibrated type probabilities."})
        if persist and self.rag_db is not None and self.rag_db.reused:
            print("[rag] vetores reaproveitados do disco (sem re-embedding)")

    def _judge_archive_dir(self):
        directory = os.path.join(self.out_root(), "run_results", "judge_runs")
        os.makedirs(directory, exist_ok=True)
        return directory

    def _augment_judge_semantic(self) -> None:
        """Log compatible scores and abstain unless a declared policy accepts them."""
        if self.class_db is None or self.type_index is None:
            return
        policy = evidence_policy()
        scored_queries = {}  # Valid only for this frozen class-index pass.
        for target in self.analysis_targets:
            target.judge = self.type_index.judge_for_method(target.method)
            extra = []
            decisions = self.judge_decisions.setdefault(target.analysis_id, {})
            for pname, members in (target.method.param_members or {}).items():
                if not members:
                    continue
                candidates = self.type_index.candidates(set(members))
                scored = []
                if len(candidates) > 1 and hasattr(self.class_db, "query_scored"):
                    query = f"an object used as parameter `{pname}` responding to {', '.join(sorted(members))}"
                    key = (query, tuple(candidates))
                    if key in scored_queries:
                        scored = scored_queries[key]
                    else:
                        scored = self.class_db.query_scored(query, k=len(candidates), allowed=set(candidates))
                        if scored:  # Empty/transient results are not memoized.
                            scored_queries[key] = tuple(scored)
                decision = semantic_decision(candidates, scored, policy)
                decisions[pname] = decision
                self._recorder().evento(tipo="judge_decision", definition_id=target.analysis_id,
                                        parameter=pname, **decision)
                if decision["selected"] is not None:
                    extra.append(f"- `{pname}`: semantic candidate: {decision['selected']} "
                                 "(declared similarity/margin gates; heuristic, not a verified type)")
                else:
                    extra.append(f"- `{pname}`: semantic type unknown ({decision['reason']})")
            if extra:
                prefix = target.judge + "\n" if target.judge else "INFERRED PARAMETER TYPES:\n"
                target.judge = prefix + "\n".join(extra)

    def _related_for(self, t: MethodTarget, *, recorder=None) -> Optional[List[str]]:
        if self.ablation_options.no_method_retrieval or self.rag_db is None:
            self._planner_retrieval.clear()
            return None
        query = t.summary or t.done_what
        if not query:
            return None
        recorder = recorder or self._recorder()
        with recorder.medir("retrieval_estatico"):
            lines, hit, cacheable = self._planner_retrieval.related(
                self.rag_db, query, k=3, exclude=t.analysis_id)
        recorder.evento(tipo="planner_retrieval", fase="rag_related",
                        definition_id=t.analysis_id, cache_hit=hit, cacheable=cacheable,
                        query_sha256=hashlib.sha256(query.encode("utf-8")).hexdigest(),
                        k=3, results=len(lines or []))
        return lines

    def _example_passing_spec(self, t: MethodTarget, *, snapshot=None) -> Optional[str]:
        """Find only this definition's generated files, including selected tasks.

        Normal rounds have already archived uncertified old output. This lookup
        is not an independent test validator for arbitrary manually placed files.
        """
        stems = {t._spec_stem}
        # RAG indexes production definitions without task IDs; exact selectors
        # may generate several task-specific files for that same definition.
        stems.update(target._spec_stem for target in self.targets
                     if target.analysis_id == t.analysis_id)
        pattern = re.compile(r"(?:" + "|".join(re.escape(stem) for stem in sorted(stems))
                             + r")(?:_r[0-9]+)?_spec\.rb")
        directory = os.path.abspath(os.path.join(self.root_dir, t.spec_dir))
        try:
            names = sorted(snapshot.get(directory, {})) if snapshot is not None else sorted(os.listdir(directory))
        except OSError:
            return None
        for name in names:
            if not pattern.fullmatch(name):
                continue
            try:
                if snapshot is not None:
                    code = snapshot[directory][name]
                else:
                    with open(os.path.join(directory, name), encoding="utf-8") as stream:
                        code = stream.read()
                if code.strip():
                    return code
            except OSError:
                continue
        return None

    def _error_help_fn(self, t: MethodTarget, *, examples=None):
        """Error-directed RAG for the self-heal loop (generate_react_flow port):
        given the failure output, retrieve similar methods and, when available,
        one of their passing specs as a concrete example."""
        if self.ablation_options.no_method_retrieval or self.rag_db is None:
            return None

        database = self.rag_db
        def helper(error: str) -> str:
            hits = database.query(error[:400], k=3, exclude=t.analysis_id)[:2]
            if not hits:
                return ""
            blocks = ["SIMILAR TESTED METHODS THAT MIGHT HELP:"]
            for sf in hits:
                snippet = " ".join((sf.done_what or sf.summary or "no summary").split())[:200]
                blocks.append(f"- {sf.method.qualified_name}: {snippet}")
                example = (self._example_passing_spec(sf, snapshot=examples) if examples is not None
                           else self._example_passing_spec(sf))
                if example:
                    blocks.append(f"  Example passing spec:\n  ```ruby\n{example[:400]}\n  ```")
            return "\n\n" + "\n".join(blocks)

        return helper

    def _all_spec_paths(self) -> List[str]:
        """Every GENERATED spec (marta_specs/), never the project's own spec/ —
        benchmark coverage must reflect only what the tool produced."""
        specs = glob.glob(os.path.join(self.out_root(), GENERATED_SPEC_DIR, "**", "*.rb"),
                          recursive=True)
        return [os.path.relpath(s, self.root_dir) for s in sorted(specs)]

    def measure_coverage(self, *, workspace=None) -> Dict[int, coverage_runner.MethodCoverage]:
        """Run every generated spec under Coverage and synthesise per-method
        missing_lines. Keyed by target index. Targets whose source file has no
        coverage data (e.g. no passing spec yet) map to full-miss coverage."""
        spec_paths = self._all_spec_paths()
        by_target: Dict[int, coverage_runner.MethodCoverage] = {}
        if not spec_paths:
            return by_target
        result = (workspace.coverage(spec_paths) if workspace is not None else
                  self.backend.run_coverage(self.source_dir, spec_paths, cwd=self.root_dir))
        validation = getattr(result, "suite_result", None)
        self._recorder().evento(tipo="suite_validation", valid=bool(validation and validation.all_passed),
                                output=validation.output if validation else "missing validation report")
        if validation is None or not validation.all_passed:
            raise coverage_runner.SuiteValidationError(validation)
        for i, t in enumerate(self.targets):
            lines = result.files.get(t.source_rel)
            if lines:
                branches = getattr(result, "branches", {}).get(t.source_rel)
                methods = getattr(result, "methods", {}).get(t.source_rel)
                by_target[i] = self.backend.synthesize_coverage(
                    t.method, lines, branches, methods)
        return by_target

    def _measure_retained_suite(self, new_outcomes: List[GenOutcome], *, workspace=None):
        """Rollback new files until the accumulated suite passes in one process.

        Rejected code and diagnostics are archived outside the generated-spec
        directory. Existing files are never silently discarded. No extra LLM
        attempts are introduced by this acceptance gate.
        """
        pending = [o for o in new_outcomes if o.success and o.spec_path]
        while True:
            try:
                return self.measure_coverage(**({"workspace": workspace} if workspace is not None else {}))
            except coverage_runner.SuiteValidationError as exc:
                if not pending:
                    raise  # Invalid pre-existing suite needs explicit attention.
                outcome = pending.pop()
                path = os.path.join(self.root_dir, outcome.spec_path)
                archive = os.path.join(self.out_root(), "rejected_specs")
                os.makedirs(archive, exist_ok=True)
                destination = tempfile.mkdtemp(prefix="accumulated_", dir=archive)
                shutil.move(path, os.path.join(destination, os.path.basename(path)))
                with open(os.path.join(destination, "validation.txt"), "w", encoding="utf-8") as stream:
                    stream.write(str(exc))
                self._recorder().evento(tipo="suite_rollback", metodo=outcome.method,
                                        archived=destination, output=str(exc))
                outcome.success = False
                outcome.last_error = str(exc)
                outcome.spec_path = None
                outcome.spec_code = None

    def _validate_spec_paths(self, targets):
        paths = [os.path.normpath(os.path.join(self.root_dir, t.spec_path)) for t in targets]
        if len(paths) != len(set(paths)):
            raise ValueError("Generation targets collide on a spec path; "
                             "select distinct definition/task identities")

    def _generation_recipe(self, targets, ask, max_attempts, reuse_first_round):
        """Bind output to supplied sources, context, implementation and declared configuration."""
        from pathlib import Path
        from .workers import POLICY as WORKERS_POLICY
        source_files = sorted(set(self.files + [os.path.join(self.root_dir, path)
                                               for path in (self.library_files or [])]))
        dependencies = dependency_files(self.root_dir)
        client = getattr(ask, "__self__", None) or getattr(ask, "client", None)
        return {
            "sources": {os.path.relpath(path, self.root_dir): file_hash(path) for path in source_files},
            "dependencies": {os.path.relpath(path, self.root_dir): file_hash(path)
                             for path in dependencies},
            "implementation": {str(path.relative_to(Path(__file__).parent)): file_hash(path)
                               for path in sorted(Path(__file__).parent.rglob("*"))
                               if path.is_file() and path.suffix in (".py", ".rb")
                               and "tests" not in path.parts},
            "client_implementation": file_hash(Path(__file__).parents[1] / "gptapi.py"),
            "response_implementation": file_hash(Path(__file__).parents[1] / "llm_response.py"),
            "embedding_implementation": file_hash(Path(__file__).parents[1] / "embedding.py"),
            "model": os.getenv("MODEL", "default"),
            "generation_schedule": {"workers": self.generation_workers,
                                    "policy": WORKERS_POLICY if self._coordinated_generation else "sequential-live-examples-v1"},
            "spec_naming": SPEC_NAMING_POLICY,
            "evidence_policy": evidence_policy(),
            "prompt_budget": budget_provenance(ask),
            "client": {key: getattr(client, key, None) for key in
                       ("model_type", "temperature", "max_tokens", "reasoning_effort", "top_p",
                        "presence_penalty", "request_timeout")},
            "execution_workspace": "native-project-workspace-v1" if self.isolate_execution else "in-place",
            "environment": {key: self._execution_environment().get(key) for key in (
                "PATH", "MARTA_RUBY_ENV", "BUNDLE_APP_CONFIG", "RUBYLIB",
                "MARTA_RUBY_BIN", "MARTA_RSPEC_BIN", "GEM_HOME", "GEM_PATH", "BUNDLE_GEMFILE", "RUBYOPT")},
            "llm_environment": {key: os.getenv(key) for key in
                                ("LLM_MAX_TOKENS", "OLLAMA_CTX", "OLLAMA_CONTEXT_LENGTH", "TRANSFORMER_PATH")},
            "targets": [t.analysis_id + ":" + str(t.task_id) for _, t in targets],
            "analysis": [[t.analysis_id, t.done_what, t.what_todo, t.summary, t.judge]
                         for t in self.analysis_targets],
            "classes": dict(self.class_summaries),
            "loading": [[t.analysis_id, self._extra_requires_for(t), self._generation_loading_for(t)]
                        for _, t in targets],
            "load_paths": self._load_path_list(),
            "backend": type(self.backend).__module__ + "." + type(self.backend).__qualname__,
            "retrieval": type(self.rag_db).__module__ + "." + type(self.rag_db).__qualname__,
            "max_context_chars": MAX_CONTEXT_CHARS,
            "attempts": self.ablation_options.attempts(max_attempts),
            "ablations": self.ablation_options.as_dict(), "paired_seed": reuse_first_round,
        }

    async def generate_rounds(
        self, rounds: int = 3, ask: Optional[AskFn] = None,
        max_attempts: int = 3, limit: Optional[int] = None,
        reuse_first_round: bool = False,
    ) -> List[GenOutcome]:
        """Resume only completed validated rounds; preserve unfinished files as evidence.

        Existing output is re-executed before reuse. Terminal failed rounds are
        not resampled. A different configuration archives incompatible output;
        an edited or missing certified spec stops for explicit investigation.
        """
        if type(rounds) is not int or rounds < 1:
            raise ValueError("rounds must be a positive integer")
        if reuse_first_round and (not self.ablation_options.no_coverage_feedback
                                 or len(self.targets) != 1
                                 or self.ablation_options.no_repair
                                 or self.ablation_options.no_type_hints
                                 or self.ablation_options.no_method_retrieval):
            raise ValueError("First-round reuse requires one coverage-ablation target")
        ask = ask or _default_ask()
        from .workers import validate_workers
        validate_workers(self, ask)
        targets = list(enumerate(self.targets))
        if limit:
            targets = targets[:limit]
        self._validate_spec_paths([t for _, t in targets])
        checkpoints = RoundCheckpoints(self.out_root(),
            self._generation_recipe(targets, ask, max_attempts, reuse_first_round),
            self._recorder().evento)
        with checkpoints.locked():
            trusted = ([os.path.join(self.root_dir, self.targets[0].spec_path_for_round(0))]
                       if reuse_first_round else [])
            completed = checkpoints.prepare(rounds, trusted_seed=trusted)
            with self._workspace() as workspace:
                # Revalidate retained output in the same bound execution environment.
                cov = self._measure_retained_suite([], **({"workspace": workspace} if workspace is not None else {})) if completed else {}
                return await self._generate_rounds(
                    rounds, ask, max_attempts, limit, reuse_first_round,
                    checkpoints=checkpoints, completed=completed, initial_coverage=cov,
                    workspace=workspace)

    async def _generate_rounds(
        self,
        rounds: int = 3,
        ask: Optional[AskFn] = None,
        max_attempts: int = 3,
        limit: Optional[int] = None,
        reuse_first_round: bool = False,
        *, checkpoints: RoundCheckpoints, completed: int, initial_coverage: dict, workspace=None,
    ) -> List[GenOutcome]:
        """Coverage-guided multi-round generation — the Fase 2 loop.

        Round 0 generates for every target; after each round coverage is
        measured over all accumulated specs, and later rounds regenerate only
        methods with missing lines, feeding those lines back to the Planner.
        Returns newly generated outcomes. Explicit first-round reuse is only
        for a certified paired coverage ablation, including a no-spec seed;
        the adapter retains inherited outcomes/cost separately.
        """
        targets = list(enumerate(self.targets))
        if limit:
            targets = targets[:limit]
        outcomes: List[GenOutcome] = []
        cov: Dict[int, coverage_runner.MethodCoverage] = initial_coverage
        recorder = self._recorder()

        for rnd in range(completed, rounds):
            from .evaluation import cost_snapshot, round_observation
            round_started = time.monotonic()
            start_cost = cost_snapshot(recorder)
            before_cov = dict(cov)
            round_outcomes: List[GenOutcome] = []
            recorder.score.first_run = (rnd == 0)  # first_run metrics = round 0
            recorder.start_count_time(f"round_{rnd}")
            recorder.define_contexto(ronda=rnd)
            jobs = []
            for idx, t in targets:
                # The XRepo adapter has certified this completed normal round,
                # including a failed round with no spec. Do not retry either.
                if reuse_first_round and rnd == 0:
                    continue
                mc = cov.get(idx)
                if (not self.ablation_options.no_coverage_feedback
                        and rnd > 0 and mc is not None and mc.fully_covered):
                    continue  # already fully covered — skip, like the Python loop
                if self.ablation_options.no_coverage_feedback or rnd == 0 or mc is None:
                    coverage_info = "First pass: Try to achieve maximum coverage."
                else:
                    coverage_info = f"MISSING LINES TO COVER: {mc.format_missing_lines()}"
                jobs.append((t, t.spec_path_for_round(rnd), coverage_info))
            try:
                if self._coordinated_generation:
                    round_outcomes = await workspace.generate_round(jobs, ask, max_attempts, recorder, rnd)
                else:
                    for t, path, coverage_info in jobs:
                        round_outcomes.append(await self._generate_target(
                            t, path, ask, max_attempts, recorder, workspace, coverage_info))
                outcomes.extend(round_outcomes)
            finally:
                recorder.end_count_time(f"round_{rnd}")
            # A cobertura corre uma vez por ronda, sobre TODOS os specs acumulados
            # até aqui. No cluster isso é tempo com a GPU parada, por isso convém
            # estar medido à parte e não diluído no tempo da ronda.
            with recorder.medir("cobertura"):
                if workspace is not None:
                    workspace.verify_inputs()
                cov = self._measure_retained_suite(round_outcomes, **({"workspace": workspace} if workspace is not None else {}))
            checkpoints.commit(rnd, round_outcomes)
            recorder.evento(tipo="round_utility", **round_observation(
                targets, before_cov, cov, round_outcomes, start_cost, cost_snapshot(recorder),
                time.monotonic() - round_started))
            recorder.score.coverage.append(
                {t.method.qualified_name: (cov[i].covered_lines if i in cov else 0)
                 for i, t in targets}
            )
        return outcomes
