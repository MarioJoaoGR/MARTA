import asyncio
import sys
import traceback
from dotenv import load_dotenv
import argparse
import os
from test4dt.config import config
from test4dt.message import ProjectMessage
from test4dt.recorder import recoder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_path", type=str, help="Project path", required=True)
    parser.add_argument("--source_path", type=str, help="Source path", required=True)
    parser.add_argument("--num", type=int, help="The number of rounds for which you want to generate test cases.", default=3)
    parser.add_argument("--type", type=bool, help="Output the extract type of function paras", default=False)
    parser.add_argument("--run_benchmark", type=bool, help="Project under test is in projects.json", default=True)

    load_dotenv()
    args = parser.parse_args()
    base_dir: str = args.project_path
    source_dir: str = args.source_path
    config.need_extract_type = args.type
    config.run_benchmark = args.run_benchmark

    project_name = base_dir.split(os.path.sep)[-1]

    # --- INÍCIO DO BLOCO DE SEGURANÇA PARA O DEUCALION ---
    try:
        recoder.start_count_time('collect_message')
        project = ProjectMessage(base_dir, source_dir)
        asyncio.run(project.init())
        recoder.end_count_time('collect_message')

        for i in range(args.num):
            recoder.start_count_time(f'run_{i}')
            project.generate_once()
            project.get_coverage_message()
            recoder.score.first_run = False
            recoder.end_count_time(f'run_{i}')

        recoder.end(project_name=project_name)

    except Exception as e:
        print("\n🚨 ERRO CRÍTICO DURANTE A EXECUÇÃO DA BASELINE!")
        traceback.print_exc()
        
        # Tentativa de salvamento de emergência: guarda os resultados parciais antes de morrer
        try:
            print("A tentar guardar os resultados gerados até ao momento do erro...")
            recoder.end(project_name=project_name)
        except Exception:
            pass
            
        print("A libertar o GPU do Deucalion...")
        sys.exit(1) # Mata o processo imediatamente com código de erro

if __name__ == "__main__":
    main()