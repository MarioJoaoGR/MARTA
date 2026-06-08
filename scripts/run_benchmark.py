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
import subprocess
import sys
import time
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent.parent
CONFIG = REPO / "scripts" / "cm_benchmark.json"
HARNESS_DIR = REPO / "baselines" / "harness"
STATE = HARNESS_DIR / "state.json"
LOGS_DIR = HARNESS_DIR / "logs"

# Envs conda
ENVS = {
    "pynguin": "/opt/homebrew/Caskroom/miniconda/base/envs/pynguin_env",
    "coverup": "/opt/homebrew/Caskroom/miniconda/base/envs/coverup_env",
    "test4py_baseline": "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_baseline_env",
    "marta": "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env",
}

# Default timeouts (segundos)
TIMEOUTS = {
    "pynguin": 300,          # 5 min por módulo (headroom para Pynguin)
    "marta": 6 * 3600,       # 6h por projeto
    "test4py_baseline": 6 * 3600,
    "coverup": 6 * 3600,
}

# Order: Pynguin primeiro (rápido), MARTA, Test4Py-baseline. CoverUp depende
# de decisão da professora — desligado por defeito.
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

def _run(cmd: list[str], *, cwd: pathlib.Path, log_path: pathlib.Path,
         timeout: int, extra_env: dict | None = None) -> tuple[str, float, str]:
    """Corre ``cmd``, redireciona stdout+stderr para ``log_path``,
    devolve ``(status, elapsed_s, last_lines)``."""
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    try:
        with open(log_path, "w") as out:
            out.write(f"# $ {' '.join(shlex.quote(c) for c in cmd)}\n")
            out.write(f"# cwd: {cwd}\n")
            out.write(f"# timeout: {timeout}s\n")
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
        return "timeout", elapsed, f"after {timeout}s"
    except Exception as e:
        return "failed", time.time() - t0, repr(e)


def run_pynguin(proj: str, info: dict, state: dict) -> None:
    """Pynguin corre 1 vez por módulo. Cria entry no state por módulo
    para retomar de onde parou."""
    pynguin = ENVS["pynguin"] + "/bin/pynguin"
    project_path = info["project_path"]
    output_base = REPO / "baselines" / "Results_Pynguin" / proj
    output_base.mkdir(parents=True, exist_ok=True)

    for module in info["modules"]:
        key = f"pynguin/{proj}/{module}"
        if state.get(key, {}).get("status") in ("ok", "failed"):
            continue
        out_dir = output_base / module.replace(".", "_")
        out_dir.mkdir(parents=True, exist_ok=True)
        log_path = LOGS_DIR / "pynguin" / proj / f"{module}.log"
        cmd = [
            pynguin,
            "--project-path", project_path,
            "--output-path", str(out_dir),
            "--module-name", module,
            "--maximum-search-time", "60",
            "-v",
        ]
        log(f"  pynguin/{proj}/{module} …")
        status, elapsed, err = _run(
            cmd, cwd=REPO, log_path=log_path,
            timeout=TIMEOUTS["pynguin"],
            extra_env={"PYNGUIN_DANGER_AWARE": "1"},
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
    status, elapsed, err = _run(cmd, cwd=REPO, log_path=log_path, timeout=TIMEOUTS["marta"])
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
    status, elapsed, err = _run(cmd, cwd=base_cwd, log_path=log_path, timeout=TIMEOUTS["test4py_baseline"])
    state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
    save_state(state)
    log(f"  └─ {status} ({elapsed/60:.1f} min)")


def run_coverup(proj: str, info: dict, state: dict) -> None:
    """CoverUp: 1 run por projeto. Usa o LLM definido em COVERUP_MODEL.
    Desligado se COVERUP_MODEL não estiver definido."""
    key = f"coverup/{proj}"
    if state.get(key, {}).get("status") in ("ok", "failed"):
        return
    model = os.environ.get("COVERUP_MODEL")
    if not model:
        log(f"  coverup/{proj} … SKIP (COVERUP_MODEL não definido)")
        state[key] = {"status": "skipped", "elapsed_s": 0, "err": "COVERUP_MODEL não definido"}
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
    args = parser.parse_args()

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
    t0 = time.time()
    for tool in tools:
        log(f"━━━ {tool.upper()} ━━━")
        for proj, info in projects:
            try:
                RUNNERS[tool](proj, info, state)
            except KeyboardInterrupt:
                log("interrompido pelo utilizador")
                save_state(state)
                sys.exit(130)
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
