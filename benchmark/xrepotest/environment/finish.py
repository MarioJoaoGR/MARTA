"""Record the repaired execution environment, independently of model/results."""
import hashlib
import json
from pathlib import Path

root = Path("/opt/xrepo")
projects = json.loads((root / "mutation-repair.json").read_text())
projects["hanami"].update(ruby_prefix="/opt/xrepo/ruby33",
                          bundle_config="/opt/xrepo/hanami-config")
# Existing project switches disable their CI reporting/whole-suite gate only.
# XRepoTest starts its own focal-method coverage independently in its wrapper.
projects["rom"]["env"] = {"COVERAGE": "false"}
projects["shoryuken"]["env"] = {"SIMPLECOV_DISABLED": "1"}
for name, item in projects.items():
    repo = Path("/app/repo_data") / name
    lock = repo / (item["gemfile"] + ".lock")
    item["lock_sha256"] = hashlib.sha256(lock.read_bytes()).hexdigest()
manifest = {"schema": 1, "base_image":
    "dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d",
    "hanami_ruby": "3.3.10", "other_ruby": "3.2.11", "projects": projects,
    "hanami_repair": json.loads((root / "hanami-config/repair.json").read_text()),
    "recipe": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
               for p in Path(__file__).parent.glob("*.py")}}
if len(projects) != 10:
    raise RuntimeError("Expected all ten repaired/verified project bundles")
(root / "environment.json").write_text(json.dumps(manifest, indent=2) + "\n")
