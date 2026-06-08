#!/usr/bin/env python3
"""
Instala os 27 projetos do benchmark CM em cada um dos envs conda das tools.

Cada projeto-alvo precisa de estar pip-installed para os testes gerados
poderem importar o módulo (ex.: ``import codetiming`` num teste do Pynguin).

Faz ``pip install --no-build-isolation`` para acelerar e ``--no-deps`` para
evitar puxar deps transitivas (que podem conflituar com as deps fixas dos
ambientes das ferramentas).

Reporta sucesso/falha por (env, projeto) num JSON state.

Uso::

    python scripts/prepare_envs.py
    python scripts/prepare_envs.py --envs pynguin_env --projects codetiming
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
CONFIG = REPO / "scripts" / "cm_benchmark.json"
STATE = REPO / "baselines" / "harness" / "envs_state.json"

CONDA_ENVS = {
    "pynguin_env": "/opt/homebrew/Caskroom/miniconda/base/envs/pynguin_env",
    "coverup_env": "/opt/homebrew/Caskroom/miniconda/base/envs/coverup_env",
    "test4py_baseline_env": "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_baseline_env",
    "test4py_env": "/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env",
}


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2) + "\n")


BUILD_PREP = ["pip", "setuptools", "wheel", "flit_core", "build", "hatchling"]


def ensure_build_tools(env_path: str) -> None:
    """Garante que os build backends comuns (flit_core, hatchling, setuptools)
    estão instalados no env. Idempotente."""
    pip = f"{env_path}/bin/pip"
    subprocess.run([pip, "install", "-U", "-q", *BUILD_PREP],
                   capture_output=True, text=True, timeout=120)


def pip_install_project(env_path: str, project_path: str, timeout: int = 600) -> tuple[str, str]:
    """Tenta instalar ``project_path`` em ``env_path`` COM as suas deps de
    runtime (necessárias para os testes gerados conseguirem importar o
    package). Devolve (status, mensagem).
    """
    pip = f"{env_path}/bin/pip"
    cmd = [pip, "install", project_path]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.returncode == 0:
            return ("ok", "")
        return ("failed", r.stderr.strip().splitlines()[-1] if r.stderr else "(no stderr)")
    except subprocess.TimeoutExpired:
        return ("timeout", f"timeout após {timeout}s")
    except Exception as e:
        return ("failed", str(e))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--envs", default=None, help="lista de envs (default: todos)")
    parser.add_argument("--projects", default=None, help="lista de projetos (default: todos)")
    parser.add_argument("--force", action="store_true", help="reinstalar mesmo se 'ok' no state")
    args = parser.parse_args()

    cfg = json.loads(CONFIG.read_text())
    state = load_state()

    envs = args.envs.split(",") if args.envs else list(CONDA_ENVS)
    projects = args.projects.split(",") if args.projects else list(cfg)

    total = len(envs) * len(projects)
    done = 0
    t0 = time.time()
    for env in envs:
        if env not in CONDA_ENVS:
            print(f"⚠️  env desconhecido: {env}")
            continue
        env_path = CONDA_ENVS[env]
        print(f"\n=== {env}: garantir build backends ===")
        ensure_build_tools(env_path)
        for proj in projects:
            done += 1
            key = f"{env}/{proj}"
            if not args.force and state.get(key, {}).get("status") == "ok":
                print(f"[{done}/{total}] skip {key} (ok)")
                continue
            if proj not in cfg:
                print(f"[{done}/{total}] skip {key} (projeto não está no CM)")
                continue
            project_path = cfg[proj]["project_path"]
            print(f"[{done}/{total}] instalar {key} ...", end=" ", flush=True)
            t = time.time()
            status, msg = pip_install_project(env_path, project_path)
            elapsed = time.time() - t
            state[key] = {
                "status": status,
                "elapsed_s": round(elapsed, 1),
                "msg": msg,
            }
            save_state(state)
            print(f"{status} ({elapsed:.1f}s)")
            if status == "failed":
                print(f"        ↳ {msg[:200]}")

    # Sumário
    summary = {"ok": 0, "failed": 0, "timeout": 0}
    for v in state.values():
        s = v.get("status")
        if s in summary:
            summary[s] += 1
    total_time = time.time() - t0
    print(f"\n--- Sumário ({total_time:.0f}s total) ---")
    for k, v in summary.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
