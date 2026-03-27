import os
import datetime

# Define o nome do ficheiro de log
LOG_FILE = "react_history.txt"

def clear_log():
    """Limpa o ficheiro de log no início da execução."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"=== INÍCIO DA EXECUÇÃO REACT: {datetime.datetime.now()} ===\n\n")

def log(tag, message):
    """
    Escreve uma mensagem no ficheiro e também mostra no terminal (para saberes que não encravou).
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    formatted_msg = f"[{timestamp}] [{tag}] {message}"
    
    # 1. Escreve no Ficheiro
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")
    
    # 2. Mostra no Terminal (Opcional, mas bom para saber que está vivo)
    print(formatted_msg)

def log_block(tag, content):
    """Loga blocos grandes (JSONs, Código) de forma formatada."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- INÍCIO BLOCO ({tag}) ---\n")
        f.write(str(content))
        f.write(f"\n--- FIM BLOCO ---\n\n")