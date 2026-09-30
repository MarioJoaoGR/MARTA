"""Infer dependency entry points from frozen Bundler metadata and Prism facts.

No per-library mapping, library execution, test source, download or installation.
Namespace matches with multiple providers are reported instead of guessed.
"""
import json
from itertools import product
import os
from pathlib import Path
import re
import subprocess

from .ruby_ast import ruby_bin

HELPER = Path(__file__).parent / "rb/marta_dependencies.rb"
POLICY = "bundle-production-namespaces-v1"


def _query(mode, root, payload=None):
    # Parsing must not inherit a caller's -rbundler/setup: Prism need not be a
    # dependency of the SUT. Bundle metadata itself still uses Bundler.setup.
    env = dict(os.environ)
    env.pop("RUBYOPT", None)
    result = subprocess.run([ruby_bin(), str(HELPER), mode], cwd=root, env=env,
                            input=json.dumps(payload) if payload is not None else None,
                            capture_output=True, text=True, timeout=120)
    if result.returncode:
        raise RuntimeError(f"Dependency inspection failed ({mode}): {result.stderr[-3000:]}")
    return json.loads(result.stdout)


def bundle_index(root):
    root = Path(root).resolve()
    gemfile = Path(os.environ.get("BUNDLE_GEMFILE", root / "Gemfile")).resolve()
    if not gemfile.is_relative_to(root) or not gemfile.is_file():
        return {"policy": POLICY, "entries": []}
    specs = _query("--bundle", root)
    entries = []
    for spec in specs:
        package = Path(spec["gem_path"]).resolve()
        # Own source is handled by the production entry/namespace loader.
        if package == root or package.is_relative_to(root) and "vendor" not in package.relative_to(root).parts:
            continue
        for entry in spec["entries"]:
            entries.append({**entry, "gem": spec["gem"], "version": spec["version"], "roots": spec["roots"]})
    return {"policy": POLICY, "entries": entries}


def snake_namespace(name):
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name.replace("::", "/"))
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def namespace_paths(name):
    # Libraries use both snake_case and compact lowercase filenames. Each
    # choice must exist and declare the exact namespace; names alone are not
    # proof. Bound mixed combinations, retaining both uniform styles first.
    parts = name.split("::")
    choices = [tuple(dict.fromkeys((snake_namespace(part), part.lower()))) for part in parts]
    names = [snake_namespace(name), "/".join(part.lower() for part in parts)]
    for i, combination in enumerate(product(*choices)):
        if i >= 128:
            break
        names.append("/".join(combination))
    return list(dict.fromkeys(names))


def namespace_index(index, facts, root):
    """Verify conventional namespace files inside the bundle's require paths.

    A gem that merely reopens another library's class is not credited as its
    provider because an unrelated entry file mentions that namespace.
    """
    namespaces = {"::".join(ref.split("::")[:n]) for ref in facts["references"]
                  for n in range(1, len(ref.split("::")) + 1)}
    paths = {}
    candidates = []
    for entry in index["entries"]:
        definitions = {}
        for namespace in sorted(namespaces):
            for lib in entry["roots"]:
                for relative in namespace_paths(namespace):
                    path = Path(lib) / (relative + ".rb")
                    if path.is_file() and path.resolve().is_relative_to(Path(lib).resolve()):
                        paths[str(path)] = None
                        definitions.setdefault(namespace, []).append(str(path))
        candidates.append({**entry, "definitions": definitions})
    evidence = _query("--files", root, {"files": sorted(paths)}) if paths else {}
    for entry in candidates:
        entry["definitions"] = {name: [p for p in files if name in evidence[p]["definitions"]
                                        and not evidence[p]["errors"]]
                                for name, files in entry["definitions"].items()}
        entry["definitions"] = {k: v for k, v in entry["definitions"].items() if v}
    return {"policy": POLICY, "entries": candidates}


def source_references(root, source, package, parents):
    root, source, package = (Path(p).resolve() for p in (root, source, package))
    lib = package / "lib"
    pending = {source}
    pending.update(lib / (p + ".rb") for p in parents)
    seen, references = set(), set()
    while pending:
        batch = sorted({str(p.resolve()) for p in pending if p.is_file()
                        and p.resolve().is_relative_to(root) and str(p.resolve()) not in seen})
        pending = set()
        if not batch:
            break
        for path, facts in _query("--files", root, {"files": batch}).items():
            seen.add(path)
            if facts["errors"]:
                raise ValueError(f"Production dependency references have parse errors: {path}")
            references.update(facts["references"])
            # Follow explicit local constants to conventional production lib
            # paths, including a superclass in a different file. No spec tree.
            for name in facts["references"]:
                if "::" not in name:
                    continue
                for relative in namespace_paths(name):
                    candidate = lib / (relative + ".rb")
                    if candidate.is_file() and str(candidate.resolve()) not in seen:
                        pending.add(candidate)
    return {"references": sorted(references), "production_files": sorted(seen)}


def resolve(index, facts, root=None):
    if root is not None:
        index = namespace_index(index, facts, root)
    resolved, ambiguous = {}, {}
    for reference in facts["references"]:
        matches = []
        for entry in index["entries"]:
            for namespace, paths in entry["definitions"].items():
                if reference == namespace or reference.startswith(namespace + "::"):
                    matches.append((len(namespace.split("::")), entry, namespace, paths))
        if not matches:
            continue
        depth = max(m[0] for m in matches)
        best = [m for m in matches if m[0] == depth]
        providers = {(m[1]["gem"], m[1]["require"], m[1]["path"]) for m in best}
        if len(providers) != 1:
            ambiguous[reference] = sorted({(m[1]["gem"], m[1]["require"]) for m in best})
            continue
        _, entry, namespace, paths = best[0]
        key = (entry["gem"], entry["require"], entry["path"])
        item = resolved.setdefault(key, {k: entry[k] for k in ("gem", "version", "require", "path")})
        item.setdefault("evidence", []).append({"reference": reference, "namespace": namespace,
                                                "definition_files": paths})
    return {"policy": POLICY, "resolved": [resolved[k] for k in sorted(resolved)],
            "ambiguous": ambiguous, "production_files": facts["production_files"]}
