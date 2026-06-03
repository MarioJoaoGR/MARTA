import asyncio
import sys
import traceback
from dotenv import load_dotenv
import argparse
import os
from marta.config import config
from marta.react_logger import clear_log, log
from marta.recorder import recoder

def main():
    # --- CONFIGURAÇÃO DE ARGUMENTOS ---
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_path", type=str, help="Project path", required=True)
    parser.add_argument("--source_path", type=str, help="Source path", required=True)
    parser.add_argument("--num", type=int, help="The number of rounds for which you want to generate test cases.", default=3)
    parser.add_argument("--type", type=bool, help="Output the extract type of function paras", default=False)
    parser.add_argument("--run_benchmark", type=bool, help="Project under test is in projects.json", default=True)
    parser.add_argument(
        "--output_dir",
        type=str,
        default=None,
        help=(
            "Pasta-base onde escrever TODOS os outputs (Test4DT_tests, "
            "test_quarantine, coverage.json, caches, run_results, "
            "react_history.txt). Se omitida, escreve dentro do source "
            "do projeto (comportamento legacy)."
        ),
    )

    load_dotenv()
    args = parser.parse_args()
    base_dir: str = args.project_path
    source_dir: str = args.source_path
    config.need_extract_type = args.type
    config.run_benchmark = args.run_benchmark
    if args.output_dir:
        config.output_dir = os.path.abspath(args.output_dir)
        os.makedirs(config.output_dir, exist_ok=True)

    project_name = base_dir.split(os.path.sep)[-1]

    # --- O DESVIO REACT ---
    from marta.message_react import ProjectMessage

    # --- INÍCIO DO BLOCO DE SEGURANÇA PARA O DEUCALION ---
    try:
        # --- EXECUÇÃO ---
        print(f"🚀 [Modo ReAct] A iniciar análise para o projeto: {project_name}")

        clear_log() 
        log("SYSTEM", f"Projeto: {project_name}")

        recoder.start_count_time('collect_message')
        project = ProjectMessage(base_dir, source_dir)

        print("🔍 [Contexto] A analisar Call Graph e Tipos (PyCG)...")
        asyncio.run(project.init())
        recoder.end_count_time('collect_message')

        for i in range(args.num):
            print(f"🔄 [ReAct Loop] Ronda {i+1} de {args.num}...")
            recoder.start_count_time(f'run_{i}')
            
            project.generate_once()
            project.get_coverage_message()
            
            recoder.score.first_run = False
            recoder.end_count_time(f'run_{i}')

        recoder.end(project_name=project_name)
        print("✅ [Modo ReAct] Execução terminada.")

    except Exception as e:
        print("\n🚨 ERRO CRÍTICO DURANTE A EXECUÇÃO DO REACT!")
        traceback.print_exc()
        
        # Guarda o erro no ficheiro de logs para analisares depois
        log("SYSTEM", f"ERRO CRÍTICO (FALHA NO DEUCALION): {str(e)}")
        
        # Tentativa de salvamento de emergência: guarda os resultados parciais
        try:
            print("A tentar guardar os resultados gerados até ao momento do erro...")
            recoder.end(project_name=project_name)
        except Exception:
            pass
            
        print("A libertar o GPU do Deucalion...")
        sys.exit(1) # Mata o processo imediatamente com código de erro

if __name__ == "__main__":
    main()