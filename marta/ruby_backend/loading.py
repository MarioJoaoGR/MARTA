"""Production-only hints for loading a Ruby target's owning gem.

This is prompt context, never a hidden executor preload. No test helpers or
benchmark answers are read. Ambiguous entry points remain explicit failures.
"""
from pathlib import Path
import json
import re

LOADING_POLICY = "gemspec-entry-before-focal-v2"


def loading_plan(root, source_rel, focal_require):
    root = Path(root).resolve()
    source = (root / source_rel).resolve()
    if not source.is_relative_to(root) or not source.is_file():
        raise ValueError(f"Target is not a source file inside the project: {source_rel}")
    package = source.parent
    specs = []
    while package == root or root in package.parents:
        specs = sorted(package.glob("*.gemspec"))
        if specs or package == root:
            break
        package = package.parent
    candidates = {}
    for spec in specs:
        # Conventional require names are verified against actual production
        # files. Do not execute the gemspec or infer APIs from the gem name.
        for entry in dict.fromkeys((spec.stem, spec.stem.replace("-", "/"),
                                    spec.stem.replace("-", "_"))):
            path = package / "lib" / (entry + ".rb")
            if re.fullmatch(r"[\w/.-]+", entry) and path.is_file():
                candidates[entry] = str(path.relative_to(root))
                break
    matching = [e for e in candidates if focal_require == e or focal_require.startswith(e + "/")]
    if matching:
        entry = max(matching, key=len)
    elif len(candidates) == 1:
        entry = next(iter(candidates))
    else:
        entry = None
    parents = []
    ancestor = source.parent
    lib = package / "lib"
    while ancestor == lib or lib in ancestor.parents:
        namespace = ancestor.with_suffix(".rb")
        if namespace.is_file() and namespace.is_relative_to(lib):
            parents.append(str(namespace.relative_to(lib).with_suffix("")))
        if ancestor == lib:
            break
        ancestor = ancestor.parent
    parents.reverse()
    requires = list(dict.fromkeys(([entry] if entry else []) + parents + [focal_require]))
    return {"policy": LOADING_POLICY, "entry": entry, "focal": focal_require,
            "requires": requires, "entry_file": candidates.get(entry),
            "package": str(package.relative_to(root)), "candidates": candidates}


def loading_context(plan):
    if not plan["entry"]:
        return ""
    code = "\n".join("require " + json.dumps(r) for r in plan["requires"])
    return (
        "PRODUCTION LOADING CONTEXT:\n"
        f"The owning gem has an entry file at {plan['entry_file']}. "
        "An internal source file may not initialize the library on its own.\n"
        "Begin the exported spec with these requires, in this order:\n"
        f"```ruby\n{code}\n```\n"
        "These requires must be in the spec itself; the executor does not preload them."
    )
