"""Production-only hints for loading a Ruby target's owning gem.

This is prompt context, never a hidden executor preload. No test helpers or
benchmark answers are read. Ambiguous entry points remain explicit failures.
"""
from pathlib import Path
import json
import re

LOADING_POLICY = "gemspec-entry-before-focal-v1"

# Optional integration libraries do not always require their host themselves.
# These namespace/require aliases describe dependency APIs, not benchmark tasks.
# Apply an alias only when the dependency is declared AND the focal production
# file (or a namespace ancestor) references it. Every resulting recipe is probed.
INTEGRATION_LOADERS = {
    "Rails": ("railties", "rails"),
    "Selenium::WebDriver": ("selenium-webdriver", "selenium-webdriver"),
    "Dry::System": ("dry-system", "dry/system"),
}


def _integration_requires(root, package, source, specs):
    metadata = "\n".join(s.read_text() for s in specs)
    declared = set(re.findall(r'add_(?:runtime_|development_)?dependency\s*\(?\s*["\']([^"\']+)', metadata))
    files = {source}
    ancestor = source.parent
    while ancestor != root and root in ancestor.parents:
        namespace = ancestor.with_suffix(".rb")
        if namespace.is_file():
            files.add(namespace)
        ancestor = ancestor.parent
    # A focal subclass can depend on a production base class in another file.
    # Follow explicit qualified constants to conventional lib paths; never
    # inspect spec helpers or installed dependency source for test answers.
    pending = list(files)
    texts = []
    while pending:
        text = pending.pop().read_text()
        texts.append(text)
        for constant in re.findall(r'\b[A-Z]\w*(?:::[A-Z]\w*)+', text):
            name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', constant.replace("::", "/"))
            name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name).lower()
            dependency = package / "lib" / (name + ".rb")
            if dependency.is_file() and dependency not in files:
                files.add(dependency)
                pending.append(dependency)
    production = "\n".join(texts)
    return [require for namespace, (gem, require) in INTEGRATION_LOADERS.items()
            if gem in declared and re.search(r"\b" + re.escape(namespace) + r"\b", production)]


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
    integrations = _integration_requires(root, package, source, specs)
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
    requires = list(dict.fromkeys(integrations + ([entry] if entry else []) + parents + [focal_require]))
    return {"policy": LOADING_POLICY, "entry": entry, "focal": focal_require,
            "requires": requires, "entry_file": candidates.get(entry),
            "package": str(package.relative_to(root)), "candidates": candidates,
            "integrations": integrations}


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
        "These requires must be in the spec itself; the executor does not preload them.\n"
        "For configuration, prefer the library's real defaults and configuration objects; "
        "do not replace them with an OpenStruct/double containing guessed fields. "
        "If initialization fails, check the production configuration and constructor. "
        "Do not invent missing classes, claim that an API was removed without evidence, "
        "or replace the library's initialization with stubs."
    )
