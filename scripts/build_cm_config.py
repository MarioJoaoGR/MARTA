#!/usr/bin/env python3
"""
Gera ``scripts/cm_benchmark.json`` a partir do ficheiro oficial
``modules_base_and_name.csv`` do CodaMosa/CoverUp.

Para cada um dos 27 projetos CM, extrai:
- ``project_path``: caminho absoluto para a pasta do projeto
- ``source_path``: subdir relativo do source dentro do projeto
- ``modules``: lista de módulos qualificados (ex.: ``codetiming._timers``)

Esta config é depois consumida pelo ``run_benchmark.py`` e também usada
para popular o ``projects.json`` da MARTA e do Test4Py-baseline.

Uso::

    python scripts/build_cm_config.py
"""
from __future__ import annotations

import collections
import csv
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = REPO / "baselines" / "codamosa" / "replication" / "scripts" / "modules_base_and_name.csv"
TEST_APPS = REPO / "baselines" / "codamosa" / "replication" / "test-apps"
OUT_PATH = REPO / "scripts" / "cm_benchmark.json"


def parse_csv():
    """Itera o CSV. Cada linha é ``test-apps/PROJ[/subdir],module.name``."""
    with open(CSV_PATH) as f:
        for row in csv.reader(f):
            if not row or len(row) != 2:
                continue
            csv_path, module = row[0].strip(), row[1].strip()
            yield csv_path, module


def derive_source_path(csv_path: str, module: str, project_name: str) -> str:
    """Decide o ``source_path`` para um projeto.

    Regra:
    - Se o CSV path tem subdir (ex.: ``test-apps/ansible/lib``), usa-o
      (``lib``).
    - Caso contrário, ``source_path`` = primeiro segmento do nome do módulo
      (ex.: ``codetiming._timers`` → ``codetiming``).
    """
    parts = csv_path.split("/")
    if len(parts) > 2:
        return "/".join(parts[2:])
    return module.split(".")[0]


def main():
    projects = collections.defaultdict(
        lambda: {"project_path": None, "source_path": None, "modules": []}
    )

    for csv_path, module in parse_csv():
        parts = csv_path.split("/")
        project_name = parts[1]
        proj = projects[project_name]
        if proj["project_path"] is None:
            proj["project_path"] = str(TEST_APPS / project_name)
            proj["source_path"] = derive_source_path(csv_path, module, project_name)
        proj["modules"].append(module)

    # Sanity checks
    print(f"Total projetos:  {len(projects)}")
    print(f"Total módulos:   {sum(len(p['modules']) for p in projects.values())}")
    print("Top 5 por nº de módulos:")
    for name, info in sorted(projects.items(), key=lambda x: -len(x[1]["modules"]))[:5]:
        print(f"  {name:12s}  {len(info['modules']):4d} módulos  (source: {info['source_path']})")

    # Validar que project_path e source_path existem no disco
    missing = []
    for name, info in projects.items():
        src_root = pathlib.Path(info["project_path"]) / info["source_path"]
        if not src_root.is_dir():
            missing.append((name, str(src_root)))
    if missing:
        print(f"\n⚠️  source_path inválido em {len(missing)} projetos:")
        for name, path in missing[:10]:
            print(f"  {name}: {path}")

    # Ordenar dict por nome do projeto para output determinístico
    out = {name: projects[name] for name in sorted(projects)}
    OUT_PATH.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n✅ Escrito {OUT_PATH.relative_to(REPO)} ({OUT_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
