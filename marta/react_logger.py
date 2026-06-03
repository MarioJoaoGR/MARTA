import os
import datetime
from marta.config import config


def _log_file():
    """Resolve o caminho do log conforme config.output_dir (se definido).

    - Sem --output_dir: legacy → ./react_history.txt no CWD.
    - Com --output_dir: {output_dir}/react_history.txt (criado se necessário).
    """
    if config.output_dir:
        os.makedirs(config.output_dir, exist_ok=True)
        return os.path.join(config.output_dir, "react_history.txt")
    return "react_history.txt"


# Compat para imports antigos (avaliado lazy ao chamar funções)
LOG_FILE = "react_history.txt"


def clear_log():
    """Limpa o ficheiro de log no início da execução."""
    with open(_log_file(), "w", encoding="utf-8") as f:
        f.write(f"=== INÍCIO DA EXECUÇÃO REACT: {datetime.datetime.now()} ===\n\n")

def log(tag, message):
    """
    Escreve uma mensagem no ficheiro e também mostra no terminal (para saberes que não encravou).
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    formatted_msg = f"[{timestamp}] [{tag}] {message}"
    
    # 1. Escreve no Ficheiro
    with open(_log_file(), "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")
    
    # 2. Mostra no Terminal (Opcional, mas bom para saber que está vivo)
    print(formatted_msg)

def log_block(tag, content):
    """Loga blocos grandes (JSONs, Código) de forma formatada."""
    with open(_log_file(), "a", encoding="utf-8") as f:
        f.write(f"\n--- INÍCIO BLOCO ({tag}) ---\n")
        f.write(str(content))
        f.write(f"\n--- FIM BLOCO ---\n\n")