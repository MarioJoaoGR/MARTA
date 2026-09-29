"""Full production context and exact benchmark tasks; no Ruby/LLM required.

Uses unittest so this suite also runs without installing pytest or chromadb.
The parser/graph backend and Chroma client are fakes; summary prompts, analysis,
RAG identity/embedding reuse and generation orchestration are real code.
"""
import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from marta.ruby_backend import cache, project
from marta.ruby_backend.backend import RubyBackend
from marta.ruby_backend.call_graph import CallEdge, CallGraph
from marta.ruby_backend.ruby_ast import ClassInfo, FileParse, MethodInfo


class FakeBackend(RubyBackend):
    def __init__(self):
        self.parsed = {}
        self.edges = [CallEdge("A#x", "B#y", 6, "const")]
        self.graph_methods = []

    def discover_files(self, abs_source):
        return list(self.parsed)

    def parse_file(self, path):
        return self.parsed[path]

    def build_call_graph(self, files, methods=None, index=None):
        self.graph_methods = list(methods)
        graph = CallGraph(edges=list(self.edges))
        graph._index()
        return graph


class MemoryCollection:
    def __init__(self, metadata):
        self.metadata = metadata
        self.ids = []

    def get(self, include):
        return {"ids": self.ids}

    def add(self, ids, embeddings):
        assert len(set(ids)) == len(ids), "RAG IDs collided"
        assert len(ids) == len(embeddings)
        self.ids = ids

    def query(self, query_embeddings, n_results):
        return {"ids": [self.ids[:n_results]]}


class MemoryClient:
    def __init__(self):
        self.collections = {}

    def get_collection(self, name, embedding_function):
        return self.collections[name]

    def create_collection(self, name, metadata, embedding_function):
        col = MemoryCollection(metadata)
        self.collections[name] = col
        return col

    def delete_collection(self, name):
        del self.collections[name]


class FullContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.backend = FakeBackend()
        self.calls = []
        self.embed_calls = []
        self.clients = {}
        self.add_file("a.rb", "A", [("initialize", 2, 4), ("x", 5, 7)])
        self.add_file("b.rb", "B", [("y", 2, 4)])
        patches = [
            patch.dict("os.environ", {"MODEL": "fake-model", "TRANSFORMER_PATH": "fake-embed"}),
            patch.object(project, "_default_ask", side_effect=AssertionError("Live LLM forbidden")),
            patch.object(project.rec, "_python_side_tokens", return_value=(0, 0)),
            patch.object(project.rec, "_detalhe_da_ultima_chamada", return_value={}),
            patch.object(project._AnalysisFunctionDatabase, "_client", autospec=True,
                         side_effect=lambda db: self.clients.setdefault(db._persist_dir, MemoryClient())),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def add_file(self, rel, owner, methods):
        path = self.root / "lib" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        end = max(m[2] for m in methods) + 1
        lines = [""] * end
        lines[0], lines[-1] = f"class {owner}", "end"
        parsed = []
        for entry in methods:
            name, start, stop = entry[:3]
            singleton = bool(entry[3]) if len(entry) > 3 else False
            lines[start - 1] = f"  def {'self.' if singleton else ''}{name}"
            if stop > start:
                lines[start] = f"    :{Path(rel).stem}"
                lines[stop - 1] = "  end"
            parsed.append(MethodInfo(name, owner, singleton, start, stop))
        path.write_text("\n".join(lines) + "\n")
        cls = ClassInfo(owner, owner, "class", None, 1, end)
        self.backend.parsed[str(path)] = FileParse(str(path), classes=[cls], methods=parsed)

    def make(self, **kwargs):
        return project.RubyProject(root_dir=str(self.root), source_dir="lib",
                                   backend=self.backend, **kwargs).discover()

    @staticmethod
    def selector(file="a.rb", name="x", start=5, end=7, task_id="task-x"):
        return dict(file=file, name=name, start_line=start, end_line=end, task_id=task_id)

    async def ask(self, system, user):
        self.calls.append((system, user))
        return f"summary-{len(self.calls)}"

    def analyze(self, proj, **kwargs):
        asyncio.run(proj.analyze_summaries(ask=self.ask, **kwargs))

    def embed(self, docs):
        self.embed_calls.append(list(docs))
        return [[float(len(d)), 1.0] for d in docs]

    def rag(self, proj):
        proj.build_rag(self.embed, lambda text: [float(len(text)), 1.0])

    def test_default_analysis_includes_helpers_and_constructors_outside_generation(self):
        proj = self.make(target_files=["a.rb"], method_names=["A#x", "A#initialize"])
        self.assertEqual([t.method.qualified_name for t in proj.targets], ["A#x"])
        self.assertEqual({t.method.qualified_name for t in proj.analysis_targets},
                         {"A#initialize", "A#x", "B#y"})
        self.assertIs(proj.analysis_targets[1], proj.targets[0])
        self.assertEqual(proj.targets[0].spec_path, "marta_specs/a__A__x_spec.rb")
        self.assertEqual(len(proj.files), 2)

    def test_full_pool_context_reaches_selected_generation(self):
        proj = self.make(target_files=["a.rb"], method_names=["A#x"])
        self.analyze(proj)
        self.assertEqual(len(proj.analysis_targets), 3)
        self.assertEqual([t.method.qualified_name for t in proj.targets], ["A#x"])
        self.assertTrue(all(t.summary and t.what_todo for t in proj.analysis_targets))
        self.assertEqual(set(proj.class_summaries), {"A", "B"})
        helper = next(t for t in proj.analysis_targets if t.method.name == "y")
        self.assertTrue(any(f"B#y: {helper.done_what}" in user for _, user in self.calls))
        self.assertEqual(proj.recorder.score.por_fase["what_todo_propagado"]["chamadas"], 1)
        self.rag(proj)
        self.assertEqual(len(proj.rag_db.targets), 3)
        fake_generate = AsyncMock(return_value=project.GenOutcome("A#x", True, 1))
        with patch.object(project, "generate_spec_for_method", fake_generate):
            asyncio.run(proj.generate_all(ask=self.ask))
        self.assertEqual(fake_generate.await_count, 1)
        self.assertEqual(fake_generate.call_args.kwargs["method_qualified_name"], "A#x")
        self.assertEqual(fake_generate.call_args.kwargs["summary"], proj.targets[0].planner_summary)
        self.assertTrue(any("B#y" in item for item in fake_generate.call_args.kwargs["related"]))

    def test_exact_constructor_selectors_override_legacy_filters(self):
        selectors = [self.selector(name="initialize", start=2, end=4, task_id=42),
                     self.selector(name="initialize", start=2, end=4, task_id="second")]
        proj = self.make(target_selectors=selectors,
                         target_files=[], method_names=[])
        self.assertEqual([t.task_id for t in proj.targets], [42, "second"])
        self.assertEqual(len(proj.analysis_targets), 3)
        self.assertEqual(len({t.spec_path for t in proj.targets}), 2)
        for t in proj.targets:
            self.assertEqual(t.context_source.count("def initialize"), 1)
            self.assertTrue(all(s is not t.method for s in t.siblings))
        self.analyze(proj)
        init = proj.analysis_targets[0]
        self.assertTrue(all(t.summary == init.summary for t in proj.targets))
        again = self.make(target_selectors=selectors)
        self.analyze(again)
        self.assertEqual([t.spec_path for t in again.targets], [t.spec_path for t in proj.targets])
        self.assertEqual([t.summary for t in again.targets], [init.summary, init.summary])

    def test_selectors_resolve_file_lines_and_name_exactly(self):
        for changed in [dict(file="missing.rb"), dict(name="A#x"), dict(start_line=6),
                        dict(end_line=6), dict(name="initialize")]:
            selector = self.selector()
            selector.update(changed)
            with self.subTest(changed=changed), self.assertRaisesRegex(ValueError, "found 0"):
                self.make(target_selectors=[self.selector(),
                          dict(selector, task_id="bad")])
        self.assertFalse(self.calls)
        proj = self.make(target_selectors=[self.selector(file="./a.rb")])
        self.assertEqual(proj.targets[0].method.name, "x")

    def test_ambiguous_or_invalid_selectors_fail(self):
        fp = self.backend.parsed[str(self.root / "lib/a.rb")]
        fp.methods.append(MethodInfo("x", "Other", False, 5, 7))
        with self.assertRaisesRegex(ValueError, "found 2"):
            self.make(target_selectors=[self.selector()])
        fp.methods.pop()
        for selectors in [{}, [None], [{}], [dict(self.selector(), file="../a.rb")],
                          [dict(self.selector(), file="/a.rb")],
                          [dict(self.selector(), start_line=True)],
                          [dict(self.selector(), end_line=0)],
                          [dict(self.selector(), task_id="")],
                          [self.selector(), self.selector()]]:
            with self.subTest(selectors=selectors), self.assertRaises(ValueError):
                self.make(target_selectors=selectors)

    def test_empty_selectors_still_allow_full_analysis(self):
        proj = self.make(target_selectors=[])
        self.assertEqual(proj.targets, [])
        self.analyze(proj)
        self.assertTrue(all(t.summary for t in proj.analysis_targets))
        empty = self.make(code_files=[], target_selectors=[])
        self.assertEqual(empty.analysis_targets, [])
        before = len(self.calls)
        self.analyze(empty)
        self.assertEqual(len(self.calls), before)

    def test_generation_selection_changes_reuse_complete_analysis(self):
        first = self.make(method_names=["A#x"])
        self.analyze(first)
        before = len(self.calls)
        changed = self.make(target_selectors=[
            self.selector(file="b.rb", name="y", start=2, end=4)])
        self.analyze(changed)
        self.assertEqual(len(self.calls), before)
        self.assertTrue(changed.targets[0].summary)
        self.assertEqual({t.method.qualified_name for t in changed.analysis_targets},
                         {"A#initialize", "A#x", "B#y"})
        self.analyze(self.make(method_names=["B#y"]))
        self.assertEqual(len(self.calls), before)

    def test_narrower_production_inventory_cannot_supply_complete_cache(self):
        narrow = self.make(code_files=["a.rb"])
        self.analyze(narrow)
        self.assertEqual(len(narrow.analysis_targets), 2)
        before = len(self.calls)
        complete = self.make()
        self.analyze(complete)
        self.assertGreater(len(self.calls), before)
        self.assertEqual(len(complete.analysis_targets), 3)
        self.assertTrue(all(t.summary for t in complete.analysis_targets))

    def test_cache_invalidates_for_schema_context_readme_and_source(self):
        self.analyze(self.make())
        for attr in ("ANALYSIS_SCHEMA", "MAX_CONTEXT_CHARS"):
            before = len(self.calls)
            with patch.object(project, attr, getattr(project, attr) + 1):
                self.analyze(self.make())
            self.assertGreater(len(self.calls), before)
            self.analyze(self.make())
        before = len(self.calls)
        (self.root / "lib/README.md").write_text("New project requirements")
        self.analyze(self.make())
        self.assertGreater(len(self.calls), before)
        before = len(self.calls)
        source = self.root / "lib/b.rb"
        source.write_text(source.read_text().replace(":b", ":changed"))
        self.analyze(self.make())
        self.assertGreater(len(self.calls), before)

    def test_legacy_unversioned_cache_is_not_accepted(self):
        proj = self.make()
        cache.save_analysis(proj._analysis_path("fake-model", True),
                            cache.compute_source_hash(proj.files), "fake-model",
                            {t.method.qualified_name: {"summary": "stale"} for t in proj.targets})
        self.analyze(proj)
        self.assertTrue(self.calls)
        self.assertTrue(all(t.summary != "stale" for t in proj.targets))

    def test_graph_arms_separate_files_and_reset_requirements(self):
        proj = self.make()
        self.analyze(proj)
        first = {t.analysis_id: t.what_todo for t in proj.analysis_targets}
        before = len(self.calls)
        self.analyze(proj, enrich=False)
        self.assertGreater(len(self.calls), before)
        self.assertTrue(all(t.what_todo != first[t.analysis_id] for t in proj.analysis_targets))
        self.assertTrue(Path(proj._analysis_path("fake-model", True)).exists())
        self.assertTrue(Path(proj._analysis_path("fake-model", False)).exists())
        before = len(self.calls)
        self.analyze(proj, enrich=False)
        self.assertEqual(len(self.calls), before)

    def test_full_context_pass_one_reuse_is_validated(self):
        normal = self.make()
        self.analyze(normal)
        other = self.make()
        self.analyze(other, enrich=False,
                     reaproveitar_passagem1_de=normal._analysis_path("fake-model", True))
        self.assertEqual(other.recorder.score.por_fase.get(
            "sumarios_passagem1", {}).get("chamadas", 0), 0)
        # A smaller production inventory cannot supply a complete pass-one cache.
        legacy = self.make(code_files=["a.rb"])
        self.analyze(legacy)
        fresh = self.make()
        self.analyze(fresh, use_cache=False, enrich=False,
                     reaproveitar_passagem1_de=legacy._analysis_path("fake-model", True))
        self.assertEqual(fresh.recorder.score.por_fase["sumarios_passagem1"]["chamadas"], 3)

    def test_cli_ablation_reuses_default_full_analysis_from_normal_output(self):
        from marta.ruby_backend import runner, start_react

        output = self.root / "outputs"
        normal = self.make(output_root=str(output / "sample"), method_names=["A#x"])
        self.analyze(normal)
        ablation = self.make(output_root=str(output / "sample_sem_grafo"),
                             method_names=["A#x"])
        analyze = ablation.analyze_summaries

        async def with_fake_model(**kwargs):
            await analyze(ask=self.ask, **kwargs)

        argv = ["marta", "--project_path", str(self.root), "--source_path", "lib",
                "--project_name", "sample", "--output_dir", str(output),
                "--no_graph_enrich", "--no_rag", "--limit", "1"]
        with patch("sys.argv", argv), patch.object(start_react, "load_dotenv"), \
                patch.object(project, "RubyProject", return_value=ablation), \
                patch.object(ablation, "discover", return_value=ablation), \
                patch.object(runner, "syntax_check", return_value=None), \
                patch.object(ablation, "analyze_summaries", side_effect=with_fake_model) as summary_call, \
                patch.object(ablation, "generate_rounds", new_callable=AsyncMock,
                             return_value=[]) as generation:
            start_react.main()

        self.assertEqual(summary_call.call_args.kwargs["reaproveitar_passagem1_de"],
                         normal._analysis_path("fake-model", True))
        self.assertEqual(ablation.recorder.score.por_fase.get(
            "sumarios_passagem1", {}).get("chamadas", 0), 0)
        self.assertEqual(len(ablation.analysis_targets), 3)
        self.assertTrue(all(t.summary for t in ablation.analysis_targets))
        generation.assert_awaited_once_with(rounds=3, limit=1)

    def test_duplicate_names_do_not_merge_cache_graph_or_rag(self):
        self.add_file("c.rb", "B", [("y", 2, 4)])
        self.backend.edges.append(CallEdge("B#y", "A#initialize", 3, "const"))
        proj = self.make()
        self.analyze(proj)
        entries = json.loads(Path(proj._analysis_path("fake-model", True)).read_text())["targets"]
        self.assertEqual(len(entries), 4)
        self.assertEqual(proj.recorder.score.por_fase.get("sumarios_passagem2", {}).get("chamadas", 0), 0)
        self.assertEqual(proj.recorder.score.por_fase.get("what_todo_propagado", {}).get("chamadas", 0), 0)
        duplicate = [t for t in proj.analysis_targets if t.method.qualified_name == "B#y"]
        self.assertEqual(len({t.summary for t in duplicate}), 2)
        before = len(self.calls)
        again = self.make()
        self.analyze(again)
        self.assertEqual(len(self.calls), before)
        self.assertEqual([t.summary for t in again.analysis_targets],
                         [t.summary for t in proj.analysis_targets])
        self.rag(again)
        ids = again.rag_db._collection.ids
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(t.analysis_id in ids[i] for i, t in enumerate(again.analysis_targets)))
        hits = again.rag_db.query("error", k=4, exclude=duplicate[0].analysis_id)
        self.assertNotIn(duplicate[0].analysis_id, [t.analysis_id for t in hits])
        self.assertIn(duplicate[1].analysis_id, [t.analysis_id for t in hits])

    def test_duplicate_names_outside_generation_selection_are_also_ambiguous(self):
        self.add_file("c.rb", "B", [("y", 2, 4)])
        proj = self.make(target_files=["a.rb", "b.rb"])
        self.analyze(proj)
        self.assertEqual(proj.recorder.score.por_fase.get("sumarios_passagem2", {}).get("chamadas", 0), 0)

    def test_instance_singleton_and_duplicate_task_names_have_unique_specs(self):
        self.add_file("c.rb", "C", [("go", 2, 4), ("go", 5, 7, True)])
        selectors = [self.selector("c.rb", "go", 2, 4, "a/b"),
                     self.selector("c.rb", "go", 5, 7, "a_b")]
        proj = self.make(target_selectors=selectors)
        self.assertEqual([t.method.qualified_name for t in proj.targets], ["C#go", "C.go"])
        self.assertEqual(len({t.spec_path_for_round(0) for t in proj.targets}), 2)

    def test_focal_initialize_never_includes_another_initialize(self):
        self.add_file("c.rb", "C", [("initialize", 2, 4), ("initialize", 5, 7)])
        proj = self.make(target_selectors=[
            self.selector("c.rb", "initialize", 5, 7)])
        self.assertEqual(proj.targets[0].context_source.count("def initialize"), 1)

    def test_vectors_reuse_only_when_text_and_identity_match(self):
        proj = self.make()
        self.analyze(proj)
        self.rag(proj)
        first = len(self.embed_calls)
        self.rag(proj)
        self.assertTrue(proj.rag_db.reused)
        self.assertTrue(proj.class_db.reused)
        self.assertEqual(len(self.embed_calls), first)
        proj.analysis_targets[0].summary += " changed"
        self.rag(proj)
        self.assertFalse(proj.rag_db.reused)
        self.assertGreater(len(self.embed_calls), first)
        first = len(self.embed_calls)
        proj.class_summaries["A"] += " changed"
        self.rag(proj)
        self.assertFalse(proj.class_db.reused)
        self.assertGreater(len(self.embed_calls), first)
        old_key = proj.rag_db._key
        proj.analysis_targets[0].rel_path = "another/a.rb"
        self.rag(proj)
        self.assertNotEqual(proj.rag_db._key, old_key)

    def test_full_context_respects_supplied_production_inventory(self):
        self.add_file("unselected.rb", "Outside", [("other", 2, 4)])
        proj = self.make(code_files=["a.rb", "b.rb"],
                         target_selectors=[self.selector()])
        self.assertEqual(len(proj.files), 2)
        self.assertEqual(len(proj.analysis_targets), 3)
        self.assertNotIn("Outside", proj.type_index.classes)

    def test_indistinguishable_analysis_definitions_fail_instead_of_merging(self):
        fp = self.backend.parsed[str(self.root / "lib/b.rb")]
        fp.methods.append(MethodInfo("y", "B", False, 2, 4))
        with self.assertRaisesRegex(ValueError, "Ambiguous analysis definition"):
            self.make(target_selectors=[self.selector()])

    def test_rounds_and_limit_only_generate_selected_tasks_in_selector_order(self):
        proj = self.make(target_selectors=[
            self.selector("b.rb", "y", 2, 4, "first"), self.selector(task_id="second")])
        self.analyze(proj)
        fake_generate = AsyncMock(return_value=project.GenOutcome("B#y", True, 1))
        with patch.object(project, "generate_spec_for_method", fake_generate), \
                patch.object(proj, "measure_coverage", return_value={}):
            outcomes = asyncio.run(proj.generate_rounds(rounds=2, limit=1, ask=self.ask))
        self.assertEqual(len(outcomes), 2)
        self.assertEqual([call.kwargs["method_qualified_name"]
                          for call in fake_generate.call_args_list], ["B#y", "B#y"])
        self.assertTrue(all(t.summary for t in proj.analysis_targets))
        self.assertEqual([t.task_id for t in proj.targets], ["first", "second"])

    def test_semantic_hints_cover_analysis_pool_and_sync_to_task_wrappers(self):
        for fp in self.backend.parsed.values():
            for method in fp.methods:
                method.param_members = {"node": ["unknown_member"]}
        proj = self.make(target_selectors=[self.selector()])
        self.analyze(proj)
        self.rag(proj)
        self.assertTrue(all("semantically closest class" in t.judge for t in proj.analysis_targets))
        target = proj.targets[0]
        analyzed = next(t for t in proj.analysis_targets if t.analysis_id == target.analysis_id)
        self.assertEqual(target.judge, analyzed.judge)
        self.rag(proj)
        self.assertEqual(target.judge.count("semantically closest class"), 1)

    def test_enrichment_uses_frozen_pass_one_summaries(self):
        self.backend.edges = [CallEdge("A#initialize", "A#x", 3, "self"),
                              CallEdge("A#x", "A#initialize", 6, "self")]
        proj = self.make()
        self.analyze(proj)
        enriched_prompts = [u for system, u in self.calls if "other methods it calls" in system]
        self.assertEqual(len(enriched_prompts), 2)
        # initialize is enriched first, but x must receive its original summary.
        self.assertIn("A#initialize: summary-1", enriched_prompts[1])


if __name__ == "__main__":
    unittest.main()
