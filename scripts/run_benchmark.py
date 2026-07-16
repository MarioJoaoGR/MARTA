#!/usr/bin/env python3
"""
Harness do benchmark CM (486 módulos × 27 projetos × N ferramentas).

Funcionalidades:

- Corre cada ferramenta sequencialmente sobre os 27 projetos:
    * Pynguin → 486 invocações curtas (1 por módulo)
    * MARTA → 27 invocações longas (1 por projeto, filtrado por projects.json)
    * Test4Py-baseline → 27 invocações longas (igual à MARTA)
    * CoverUp → 27 invocações longas (1 por projeto)
- Resume-friendly: state.json regista o que já foi feito.
- Logs por (tool, projeto, módulo) em ``baselines/harness/logs/``.
- Outputs vão para ``baselines/Results_<TOOL>/<project>/``.
- Timeout configurável por (tool, projeto). Default 6h.

Uso (corre tudo em background, persistente)::

    nohup python scripts/run_benchmark.py > harness.out 2>&1 &
    tail -f harness.out

Subsets para debug::

    python scripts/run_benchmark.py --tools pynguin --projects codetiming
    python scripts/run_benchmark.py --dry-run
    python scripts/run_benchmark.py --tools marta,test4py_baseline

Estado: ``baselines/harness/state.json`` ↔ key ``"<tool>/<project>"``.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shlex
import shutil
import subprocess
import signal
import sys
import time
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent.parent
CONFIG = REPO / "scripts" / "cm_benchmark.json"
HARNESS_DIR = REPO / "baselines" / "harness"
STATE = HARNESS_DIR / "state.json"
LOGS_DIR = HARNESS_DIR / "logs"

# Envs conda — defaults para Mac local. Overridable via env vars
# (ENV_PYNGUIN, ENV_COVERUP, ENV_TEST4PY_BASELINE, ENV_MARTA) para que o
# Deucalion (paths em /opt/conda/envs/...) funcione sem editar este ficheiro.
ENVS = {
    "pynguin": os.environ.get(
        "ENV_PYNGUIN",
        "/opt/homebrew/Caskroom/miniconda/base/envs/pynguin_env"),
    "coverup": os.environ.get(
        "ENV_COVERUP",
        "/opt/homebrew/Caskroom/miniconda/base/envs/coverup_env"),
    "test4py_baseline": os.environ.get(
        "ENV_TEST4PY_BASELINE",
        "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_baseline_env"),
    "marta": os.environ.get(
        "ENV_MARTA",
        "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env"),
}

# Default timeouts (segundos). None = sem timeout (corre até acabar ou falhar).
# Pynguin é search-based determinístico → timeout faz sentido para apertar
# o budget. LLM tools dependem do tamanho do projeto (ansible >> codetiming)
# e do throughput do Ollama; default sem timeout para evitar matar runs
# legítimas. Cada um pode ser sobreposto via --timeout-<tool> (segundos).
TIMEOUTS = {
    "pynguin": 300,          # 5 min por módulo
    "marta": None,           # sem timeout
    "test4py_baseline": None,
    "coverup": None,
}

# Order: Pynguin primeiro (rápido), MARTA, Test4Py-baseline.
# CoverUp NÃO está aqui por defeito: optámos por comparar contra os números
# publicados no paper FSE 2025 do CoverUp (mesmo benchmark CM/CodaMosa,
# GPT-4o no paper deles) em vez de re-correr localmente. Razões:
#   1. Nenhum LLM local cumpre simultaneamente (a) function calling
#      correcto sem loops, (b) qualidade de output decente, e (c) velocidade
#      suficiente para o benchmark de 486 módulos (ver bake-off em
#      baselines/BASELINES_README.md).
#   2. Re-correr CoverUp com GPT-4o via API paga (~$30-150) não foi a
#      escolha do utilizador.
# Se mudares de ideias: re-clonar baselines/coverup, recriar coverup_env,
# adicionar "coverup" a DEFAULT_TOOLS ou via --tools.
DEFAULT_TOOLS = ["pynguin", "marta", "test4py_baseline"]

# Ordem de projetos: menores primeiro (validar harness), ansible último.
PROJECT_ORDER_KEY = lambda info: len(info["modules"])


# ────────────────────────────────────────────────────────────────────────────
# State (checkpoint)
# ────────────────────────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    HARNESS_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


# ────────────────────────────────────────────────────────────────────────────
# Populadores de projects.json para MARTA e Test4Py-baseline
# ────────────────────────────────────────────────────────────────────────────

def populate_projects_json(cm: dict) -> None:
    """Garante que ambos os projects.json (MARTA + Test4Py-baseline) têm
    as listas CM dos 27 projetos. Adiciona; não remove entradas pré-existentes
    para preservar configurações manuais (ex.: paper #1 antigo)."""
    for path in [
        REPO / "projects.json",
        REPO / "baselines" / "test4py-baseline" / "projects.json",
    ]:
        try:
            existing = json.loads(path.read_text())
        except FileNotFoundError:
            existing = {}
        merged = dict(existing)
        for proj, info in cm.items():
            merged[proj] = info["modules"]
        path.write_text(json.dumps(merged, indent=2) + "\n")


# ────────────────────────────────────────────────────────────────────────────
# Runners (um por tool)
# ────────────────────────────────────────────────────────────────────────────

SANDBOX_ROOT = HARNESS_DIR / "sandbox"


def _sandbox(name: str, link_from: pathlib.Path) -> pathlib.Path:
    """cwd isolado para correr uma tool, sem poluir o repo.

    Pynguin/MARTA/test4dt EXECUTAM os testes gerados, que correm código dos
    projetos-alvo (cookiecutter, etc.) — esse código cria ficheiros/dirs no
    cwd. Com cwd=REPO isso enche o repo de milhares de ficheiros-lixo. Aqui
    damos um cwd descartável (limpo a cada projeto) e symlinkamos os ficheiros
    que as tools leem relativamente (``projects.json``, ``.env``)."""
    sb = SANDBOX_ROOT / name
    # rmtree limpa o lixo do projeto anterior (evita acumular inodes).
    if sb.exists() or sb.is_symlink():
        shutil.rmtree(sb, ignore_errors=True)
    sb.mkdir(parents=True, exist_ok=True)
    # COPIAR (não symlink): os testes correm com PYNGUIN_DANGER_AWARE=1 e podem
    # tentar escrever/apagar ficheiros no cwd. Com cópia, só afetam o sandbox
    # descartável; os originais (projects.json regenerado a cada run, .env com
    # credenciais) ficam protegidos.
    for fname in ("projects.json", ".env"):
        src = link_from / fname
        if src.exists():
            shutil.copy2(src, sb / fname)
    return sb


def _pythonpath_env(*dirs) -> dict:
    """extra_env com PYTHONPATH = dirs (na ordem dada) + PYTHONPATH existente.

    Usado para injetar as deps pesadas instaladas via `pip install --target`
    (em PYDEPS_MARTA / PYDEPS_BASELINE) + o diretório do pacote (marta/ ou
    test4dt/) sem as ter instaladas no env. Em Deucalion o overlay/fakeroot
    não funcionam, por isso as deps vêm por PYTHONPATH."""
    parts = [str(d) for d in dirs if d]
    existing = os.environ.get("PYTHONPATH", "")
    if existing:
        parts.append(existing)
    return {"PYTHONPATH": os.pathsep.join(parts)}


def _run(cmd: list[str], *, cwd: pathlib.Path, log_path: pathlib.Path,
         timeout: int | None, extra_env: dict | None = None) -> tuple[str, float, str]:
    """Corre ``cmd``, redireciona stdout+stderr para ``log_path``,
    devolve ``(status, elapsed_s, last_lines)``. ``timeout=None`` → sem limite."""
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    timeout_label = f"{timeout}s" if timeout else "sem limite"
    try:
        with open(log_path, "w") as out:
            out.write(f"# $ {' '.join(shlex.quote(c) for c in cmd)}\n")
            out.write(f"# cwd: {cwd}\n")
            out.write(f"# timeout: {timeout_label}\n")
            out.write(f"# started: {datetime.now(timezone.utc).isoformat()}\n\n")
            out.flush()
            r = subprocess.run(
                cmd, cwd=str(cwd), env=env,
                stdout=out, stderr=subprocess.STDOUT,
                timeout=timeout,
            )
        elapsed = time.time() - t0
        if r.returncode == 0:
            return "ok", elapsed, ""
        return "failed", elapsed, f"returncode={r.returncode}"
    except subprocess.TimeoutExpired:
        elapsed = time.time() - t0
        return "timeout", elapsed, f"after {timeout_label}"
    except Exception as e:
        return "failed", time.time() - t0, repr(e)


def _import_root(project_path: str, source_path: str) -> str:
    """Raiz de sys.path para importar os módulos do projeto.

    Se source_path for um CONTAINER (sem __init__.py — ex.: ansible/lib,
    black/src), os módulos (ansible.cli.adhoc, blib2to3.*) só são importáveis a
    partir de project_path/source_path. Sem isto o Pynguin corria com
    --project-path=project_path e dava ModuleNotFoundError → falhava 237/237 no
    ansible (e 6/6 no black). Se source_path for o próprio pacote (codetiming/),
    devolve project_path → comportamento inalterado nos 25 projetos normais."""
    src_full = os.path.join(project_path, source_path) if source_path else project_path
    if source_path and not os.path.exists(os.path.join(src_full, "__init__.py")):
        return src_full
    return project_path


def run_pynguin(proj: str, info: dict, state: dict) -> None:
    """Pynguin corre 1 vez por módulo. Cria entry no state por módulo
    para retomar de onde parou."""
    pynguin = ENVS["pynguin"] + "/bin/pynguin"
    project_path = _import_root(info["project_path"], info["source_path"])
    output_base = REPO / "baselines" / "Results_Pynguin" / proj
    output_base.mkdir(parents=True, exist_ok=True)
    # cwd descartável: os módulos executados pelo Pynguin criam ficheiros no cwd.
    sandbox = _sandbox("pynguin", REPO)

    for module in info["modules"]:
        key = f"pynguin/{proj}/{module}"
        if state.get(key, {}).get("status") in ("ok", "failed"):
            continue
        out_dir = output_base / module.replace(".", "_")
        out_dir.mkdir(parents=True, exist_ok=True)
        log_path = LOGS_DIR / "pynguin" / proj / f"{module}.log"
        # Budget de busca: 600s = o padrão do CodaMosa (MESMO benchmark) e do próprio
        # paper do Pynguin. Antes usávamos 60s (1/10!) → baseline subvalorizada.
        # Algoritmo: vazio = default do Pynguin = DynaMOSA, que o paper do Pynguin
        # mostra ser o MELHOR (Fig.2: DynaMOSA 68.0% > MOSA 67.8%) → Pynguin no seu
        # melhor = comparação justa. PYNGUIN_ALGORITHM=MOSA p/ replicar o CodaMosa.
        search_time = os.environ.get("PYNGUIN_SEARCH_TIME", "600")
        algorithm = os.environ.get("PYNGUIN_ALGORITHM", "")  # "" = DynaMOSA (default)
        cmd = [
            pynguin,
            "--project-path", project_path,
            "--output-path", str(out_dir),
            "--module-name", module,
            "--maximum-search-time", search_time,
            "-v",
        ]
        if algorithm:
            cmd += ["--algorithm", algorithm]
        log(f"  pynguin/{proj}/{module} …")
        # PYDEPS_SUT: deps do SUT em falta no env (regex, stringcase, invoke,
        # urllib3<2 do httpie) instaladas via pip --target e injetadas no
        # PYTHONPATH (precede o site-packages → também faz override de versão).
        # Necessário para a comparação ser justa (o CoverdUp/CM tinha-as).
        extra_env = {"PYNGUIN_DANGER_AWARE": "1"}
        extra_env.update(_pythonpath_env(os.environ.get("PYDEPS_SUT")))
        # kill timeout TEM de exceder a busca (600s) + overhead (arranque, geração
        # de asserts). Senão o subprocesso era morto a meio da busca.
        kill_timeout = max(TIMEOUTS["pynguin"], int(search_time) + 300)
        status, elapsed, err = _run(
            cmd, cwd=sandbox, log_path=log_path,
            timeout=kill_timeout,
            extra_env=extra_env,
        )
        state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
        save_state(state)
        log(f"  └─ {status} ({elapsed:.0f}s)")


def run_marta(proj: str, info: dict, state: dict) -> None:
    """MARTA: 1 run por projeto. projects.json filtra para os módulos CM."""
    key = f"marta/{proj}"
    if state.get(key, {}).get("status") in ("ok", "failed"):
        return
    python = ENVS["marta"] + "/bin/python"
    out_dir = REPO / "baselines" / "Results_MARTA"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / "marta" / f"{proj}.log"
    cmd = [
        python, "-m", "marta.start_react",
        "--project_path", info["project_path"],
        "--source_path", info["source_path"],
        "--output_dir", str(out_dir),
        "--num", "3",
    ]
    log(f"  marta/{proj} ({len(info['modules'])} módulos) …")
    # cwd descartável (com symlink projects.json + .env); PYTHONPATH dá
    # acesso ao pacote marta/ (REPO) + deps pesadas (PYDEPS_MARTA).
    sandbox = _sandbox("marta", REPO)
    extra_env = _pythonpath_env(os.environ.get("PYDEPS_SUT"), os.environ.get("PYDEPS_MARTA"), REPO)
    status, elapsed, err = _run(cmd, cwd=sandbox, log_path=log_path,
                                timeout=TIMEOUTS["marta"], extra_env=extra_env)
    state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
    save_state(state)
    log(f"  └─ {status} ({elapsed/60:.1f} min)")


def run_test4py_baseline(proj: str, info: dict, state: dict) -> None:
    """Test4Py-baseline: 1 run por projeto, mesma lógica que a MARTA."""
    key = f"test4py_baseline/{proj}"
    if state.get(key, {}).get("status") in ("ok", "failed"):
        return
    python = ENVS["test4py_baseline"] + "/bin/python"
    base_cwd = REPO / "baselines" / "test4py-baseline"
    out_dir = REPO / "baselines" / "Results_Test4PyBaseline"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / "test4py_baseline" / f"{proj}.log"
    cmd = [
        python, "-m", "test4dt.start",
        "--project_path", info["project_path"],
        "--source_path", info["source_path"],
        "--output_dir", str(out_dir),
        "--num", "3",
    ]
    log(f"  test4py_baseline/{proj} ({len(info['modules'])} módulos) …")
    # cwd descartável (symlink projects.json + .env do test4py-baseline);
    # PYTHONPATH = pacote test4dt/ (base_cwd) + deps. PYDEPS_BASELINE estava
    # INCOMPLETO (faltava aiolimiter, etc.) e a baseline nunca tinha corrido.
    # test4dt é fork do marta → mesmas deps de terceiros; juntamos PYDEPS_MARTA
    # (completo) para preencher as que faltam. Ordem: BASELINE ganha onde tem,
    # MARTA preenche o resto. Não há conflito de package (o source test4dt vem
    # só de base_cwd; os pydeps são só libs de terceiros via pip --target).
    sandbox = _sandbox("test4py_baseline", base_cwd)
    extra_env = _pythonpath_env(os.environ.get("PYDEPS_SUT"), os.environ.get("PYDEPS_BASELINE"),
                                os.environ.get("PYDEPS_MARTA"), base_cwd)
    status, elapsed, err = _run(cmd, cwd=sandbox, log_path=log_path,
                                timeout=TIMEOUTS["test4py_baseline"], extra_env=extra_env)
    state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
    save_state(state)
    log(f"  └─ {status} ({elapsed/60:.1f} min)")


def run_coverup(proj: str, info: dict, state: dict) -> None:
    """CoverUp: 1 run por projeto.

    Default: ``ollama_chat/gpt-oss:20b`` — escolhido após bake-off de 9
    LLMs locais como o único que produz coverage decente (96% em codetiming._
    timers smoke). Foi a escolha do utilizador apesar de crashar em runs
    longos por context window overflow + thinking mode token-hungry;
    estes crashes são recuperáveis via state.json + CoverUp checkpoint.

    Setup geral é MIXED: deepseek-coder-v2:16b para MARTA/Test4Py (rápido,
    no-tools), gpt-oss:20b para CoverUp (única opção local com qualidade).
    Apples-to-apples imperfeito; documentado em Threats to Validity.

    O prefixo ``ollama_chat/`` é crítico para o LiteLLM extrair o content
    correctamente do endpoint /api/chat do Ollama.

    Bake-off completo (em codetiming._timers, ordenado por viabilidade):
      - gpt-oss:20b           → 96% cov (ESCOLHIDO; crashes recuperáveis)
      - mistral-small:24b     → 76% cov estável mas 3-4x mais lento na MARTA
      - granite3.1-dense:8b   → 62% cov, baixa qualidade
      - llama3.1:8b           → loop infinito em tools
      - qwen2.5-coder 14B/32B → loop infinito em tools
      - mistral-nemo:12b      → alucina tools fictícias
      - command-r:35b         → Ollama tools wrapping devolve content vazio
      - DeepSeek-Coder, Codestral → não suportam tools via Ollama

    Override com COVERUP_MODEL=<ollama_chat/MODEL>. COVERUP_MODEL=skip
    desactiva CoverUp."""
    key = f"coverup/{proj}"
    if state.get(key, {}).get("status") in ("ok", "failed"):
        return
    model = os.environ.get("COVERUP_MODEL", "ollama_chat/gpt-oss:20b")
    if model.lower() == "skip":
        log(f"  coverup/{proj} … SKIP (COVERUP_MODEL=skip)")
        state[key] = {"status": "skipped", "elapsed_s": 0, "err": "COVERUP_MODEL=skip"}
        save_state(state)
        return
    coverup = ENVS["coverup"] + "/bin/coverup"
    project_path = pathlib.Path(info["project_path"])
    source_root = project_path / info["source_path"]
    # Lista de ficheiros .py que correspondem aos módulos CM
    files = []
    for mod in info["modules"]:
        rel = mod.replace(".", "/") + ".py"
        f = source_root / rel
        if f.exists():
            files.append(str(f.relative_to(project_path)))
    if not files:
        state[key] = {"status": "failed", "elapsed_s": 0, "err": "nenhum ficheiro encontrado"}
        save_state(state)
        return
    out_dir = REPO / "baselines" / "Results_CoverUp" / proj
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / "coverup" / f"{proj}.log"
    cmd = [
        coverup,
        "--package-dir", info["source_path"],
        "--tests-dir", str(out_dir),
        "--model", model,
        "--branch-coverage",
        "--max-attempts", "3",
        "--log-file", str(out_dir / "coverup.log"),
        *files,
    ]
    extra_env = {"OLLAMA_API_BASE": os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")}
    log(f"  coverup/{proj} ({len(files)} ficheiros, modelo={model}) …")
    status, elapsed, err = _run(
        cmd, cwd=project_path, log_path=log_path,
        timeout=TIMEOUTS["coverup"], extra_env=extra_env,
    )
    state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
    save_state(state)
    log(f"  └─ {status} ({elapsed/60:.1f} min)")


RUNNERS = {
    "pynguin": run_pynguin,
    "marta": run_marta,
    "test4py_baseline": run_test4py_baseline,
    "coverup": run_coverup,
}


# ────────────────────────────────────────────────────────────────────────────
# Main loop
# ────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tools", default=",".join(DEFAULT_TOOLS),
                        help="tools separadas por vírgula (default: pynguin,marta,test4py_baseline)")
    parser.add_argument("--projects", default=None,
                        help="subset de projetos (default: todos os 27)")
    parser.add_argument("--dry-run", action="store_true",
                        help="mostra o plano sem executar")
    parser.add_argument("--reset", action="store_true",
                        help="apaga state.json antes de começar")
    parser.add_argument("--timeout-pynguin", type=int, default=None,
                        help=f"timeout do Pynguin em segundos (default: {TIMEOUTS['pynguin']})")
    parser.add_argument("--timeout-marta", type=int, default=None,
                        help="timeout da MARTA em segundos (default: sem limite)")
    parser.add_argument("--timeout-test4py-baseline", type=int, default=None,
                        help="timeout do Test4Py-baseline em segundos (default: sem limite)")
    parser.add_argument("--timeout-coverup", type=int, default=None,
                        help="timeout do CoverUp em segundos (default: sem limite)")
    args = parser.parse_args()

    # Overrides de timeout (None na CLI → manter default da tabela)
    for tool, cli in [
        ("pynguin", args.timeout_pynguin),
        ("marta", args.timeout_marta),
        ("test4py_baseline", args.timeout_test4py_baseline),
        ("coverup", args.timeout_coverup),
    ]:
        if cli is not None:
            # 0 ou negativo significa "sem limite"
            TIMEOUTS[tool] = cli if cli > 0 else None

    cm = json.loads(CONFIG.read_text())

    populate_projects_json(cm)
    log(f"projects.json populados ({len(cm)} projetos)")

    tools = [t.strip() for t in args.tools.split(",") if t.strip()]
    for t in tools:
        if t not in RUNNERS:
            print(f"❌ tool desconhecida: {t}")
            sys.exit(2)

    # Ordem dos projetos: smaller-first para validar o harness depressa
    projects = sorted(cm.items(), key=lambda kv: PROJECT_ORDER_KEY(kv[1]))
    if args.projects:
        wanted = set(args.projects.split(","))
        projects = [(n, info) for n, info in projects if n in wanted]

    log(f"vai correr {len(tools)} tools × {len(projects)} projetos")
    for n, info in projects:
        log(f"  • {n}: {len(info['modules'])} módulos (source={info['source_path']})")

    if args.dry_run:
        log("(dry-run; a sair)")
        return

    if args.reset and STATE.exists():
        STATE.unlink()
        log("state.json apagado (reset)")

    state = load_state()

    # SIGTERM handler: SLURM (e outros batch systems) enviam SIGTERM ~30s
    # antes de SIGKILL. Convertemos em KeyboardInterrupt para o ciclo
    # principal apanhar, gravar o state e sair com exit code 143 (= 128 + 15).
    # Da próxima run, o resume salta o que está "ok" e re-tenta o resto.
    def _on_terminate(signum, _frame):
        log(f"signal {signum} recebido — a gravar state e sair limpo")
        raise KeyboardInterrupt(f"signal {signum}")

    signal.signal(signal.SIGTERM, _on_terminate)

    t0 = time.time()
    for tool in tools:
        log(f"━━━ {tool.upper()} ━━━")
        for proj, info in projects:
            try:
                RUNNERS[tool](proj, info, state)
            except KeyboardInterrupt as e:
                msg = str(e) or "interrompido pelo utilizador"
                log(f"interrompido ({msg}) — state gravado, sair")
                save_state(state)
                sys.exit(143 if "signal 15" in msg else 130)
            except Exception as e:
                log(f"  ❌ erro inesperado em {tool}/{proj}: {e!r}")
                state[f"{tool}/{proj}"] = {"status": "failed", "elapsed_s": 0, "err": repr(e)}
                save_state(state)

    # Sumário final
    by_status = {}
    for v in state.values():
        s = v.get("status", "?")
        by_status[s] = by_status.get(s, 0) + 1
    log("━━━ SUMÁRIO ━━━")
    for s, n in sorted(by_status.items()):
        log(f"  {s}: {n}")
    log(f"tempo total: {(time.time()-t0)/60:.1f} min")


if __name__ == "__main__":
    main()
