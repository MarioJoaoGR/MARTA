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
import os
import sys
import traceback

from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser(description="MARTA Ruby: generate RSpec tests")
    parser.add_argument("--project_path", type=str, required=True, help="Project root (cwd for RSpec)")
    parser.add_argument("--source_path", type=str, required=True, help="Source dir relative to project root")
    parser.add_argument("--num", type=int, default=3, help="Number of coverage-guided rounds")
    parser.add_argument("--limit", type=int, default=None, help="Only the first N method targets (smoke runs)")
    parser.add_argument("--no_rag", action="store_true", help="Skip embeddings/RAG (faster start, less context)")
    parser.add_argument("--no_cache", action="store_true", help="Ignore the analysis cache (recompute summaries)")
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
        proj = RubyProject(root_dir=args.project_path, source_dir=args.source_path).discover()
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
        print(f"✅ [MARTA Ruby] {ok}/{len(outcomes)} gerações com sucesso "
              f"({salvaged} via salvamento). Specs em "
              f"{os.path.join(args.project_path, GENERATED_SPEC_DIR)}")

        out_dir = args.output_dir or os.path.join(args.project_path, "run_results")
        path = recorder.end(out_dir, project_name)
        print(f"📊 Métricas em {path}")

    except Exception as e:
        print("\n🚨 ERRO CRÍTICO NA EXECUÇÃO RUBY!")
        traceback.print_exc()
        try:  # salvamento de emergência das métricas parciais, como o Python
            out_dir = args.output_dir or os.path.join(args.project_path, "run_results")
            proj._recorder().end(out_dir, project_name)
        except Exception:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()
