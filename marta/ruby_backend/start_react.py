"""CLI entry point for the Ruby backend — mirrors ``marta.start_react``.

    python -m marta.ruby_backend.start_react \
        --project_path /path/to/ruby_project --source_path src --num 3

Runs the full pipeline: discover -> context (summaries/README/types, cached by
source hash) -> RAG -> coverage-guided multi-round generation. Specs land in
``<project_path>/spec/``; run metrics in ``<project_path>/run_results/``.

Requires Ruby >= 3.3 with RSpec (set MARTA_RUBY_BIN / MARTA_RSPEC_BIN, e.g. the
rbenv 3.4 binaries) and the LLM configured via .env (ollama etc.).
"""
import argparse
import asyncio
import functools
import os
import sys
import traceback

from dotenv import load_dotenv

# Progresso tem de aparecer mesmo com stdout redirecionado para ficheiro (runs
# em background/SLURM); sem isto o output fica no buffer e a run parece pendurada.
print = functools.partial(print, flush=True)  # noqa: A001


def main():
    parser = argparse.ArgumentParser(description="MARTA Ruby: generate RSpec tests")
    parser.add_argument("--project_path", type=str, required=True, help="Project root (cwd for RSpec)")
    parser.add_argument("--source_path", type=str, required=True, help="Source dir relative to project root")
    parser.add_argument("--num", type=int, default=3, help="Number of coverage-guided rounds")
    parser.add_argument("--limit", type=int, default=None, help="Only the first N method targets (smoke runs)")
    parser.add_argument("--no_rag", action="store_true", help="Skip embeddings/RAG (faster start, less context)")
    parser.add_argument("--no_cache", action="store_true", help="Ignore the analysis cache (recompute summaries)")
    parser.add_argument(
        "--targets", type=str, default=None,
        help="Ficheiro JSON com os ficheiros-alvo deste projeto (ver "
             "benchmark/select_targets.py). Sem ele, todos os ficheiros são alvo.")
    parser.add_argument(
        "--output_dir", type=str, default=None,
        help="Where to write run_results (default: <project_path>/run_results)",
    )
    load_dotenv()
    args = parser.parse_args()

    from marta.ruby_backend import runner
    from marta.ruby_backend.project import RubyProject
    from marta.ruby_backend.ruby_ast import RubyParseError

    # Fail fast, with a clear message, if the Ruby toolchain isn't reachable.
    try:
        if runner.syntax_check("def x; end") is not None:
            raise RubyParseError("ruby -c failed on trivial input")
    except RubyParseError as e:
        print(f"❌ Toolchain Ruby indisponível: {e}")
        print("   Define MARTA_RUBY_BIN/MARTA_RSPEC_BIN (Ruby >= 3.3 com RSpec).")
        sys.exit(2)

    project_name = os.path.abspath(args.project_path).rstrip(os.sep).split(os.sep)[-1]
    print(f"🚀 [MARTA Ruby] A iniciar análise para o projeto: {project_name}")

    try:
        # Semântica do --output_dir IGUAL ao Python (get_output_root): outputs
        # (marta_specs/, caches, run_results) vão para {output_dir}/{projeto}/,
        # sem poluir o projeto. Run independente = output_dir novo.
        output_root = None
        if args.output_dir:
            output_root = os.path.join(os.path.abspath(args.output_dir), project_name)
        target_files = None
        if args.targets:
            import json as _json
            with open(args.targets, encoding="utf-8") as _f:
                target_files = [e["file"] if isinstance(e, dict) else e
                                for e in _json.load(_f)]
            print(f"🎯 [Alvos] {len(target_files)} ficheiros selecionados "
                  f"(seleção de alvos ativa)")
        proj = RubyProject(root_dir=args.project_path, source_dir=args.source_path,
                           output_root=output_root, target_files=target_files).discover()
        print(f"🔍 [Contexto] {len(proj.files)} ficheiros, {len(proj.targets)} métodos-alvo; "
              f"grafo: {len(proj.call_graph.edges) if proj.call_graph else 0} arestas "
              f"({'source inalterado' if not proj.code_changed else 'source novo/alterado'})")
        if not proj.targets:
            print(f"❌ Nenhum método-alvo em {os.path.join(args.project_path, args.source_path)} "
                  f"— confirma --project_path/--source_path.")
            sys.exit(2)

        recorder = proj._recorder()

        # Um único event loop para todo o fluxo async (evita re-uso do
        # AsyncLimiter do gptapi entre loops distintos).
        async def _pipeline():
            recorder.start_count_time("collect_message")
            await proj.analyze_summaries(limit=args.limit, use_cache=not args.no_cache)
            if not args.no_rag:
                print("🧠 [RAG] A indexar summaries (bge)...")
                proj.build_rag()
            recorder.end_count_time("collect_message")
            print(f"🔄 [ReAct Loop] {args.num} ronda(s) guiadas por cobertura...")
            return await proj.generate_rounds(rounds=args.num, limit=args.limit)

        outcomes = asyncio.run(_pipeline())

        from marta.ruby_backend.project import GENERATED_SPEC_DIR
        ok = sum(1 for o in outcomes if o.success)
        salvaged = sum(1 for o in outcomes if o.salvaged)
        specs_at = os.path.join(proj.out_root(), GENERATED_SPEC_DIR)
        print(f"✅ [MARTA Ruby] {ok}/{len(outcomes)} gerações com sucesso "
              f"({salvaged} via salvamento). Specs em {specs_at}")

        out_dir = os.path.join(output_root, "run_results") if output_root \
            else os.path.join(args.project_path, "run_results")
        path = recorder.end(out_dir, project_name)
        print(f"📊 Métricas em {path}")

    except Exception as e:
        print("\n🚨 ERRO CRÍTICO NA EXECUÇÃO RUBY!")
        traceback.print_exc()
        try:  # salvamento de emergência das métricas parciais, como o Python
            out_dir = os.path.join(output_root, "run_results") if output_root \
                else os.path.join(args.project_path, "run_results")
            proj._recorder().end(out_dir, project_name)
        except Exception:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()
