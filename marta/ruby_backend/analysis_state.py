"""Analysis provenance and append-only evidence, independent of reusable caches."""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import tempfile

from . import readme, summaries
from .checkpoints import atomic_json, digest, file_hash
from .prompt_budget import budget_provenance

PROVENANCE_POLICY = "analysis-provenance-v1"
CLIENT_FIELDS = ("temperature", "max_tokens", "reasoning_effort", "top_p",
                 "presence_penalty", "request_timeout")


def _scalar(value):
    return value if type(value) in (str, int, float, bool, type(None)) else None


def analysis_provenance(ask=None):
    """Read only declared/loaded configuration; never initialize or query a model.

    Wrappers such as XRepoTest's SummaryCheckpoints expose their actual client.
    An opaque injected callback must declare its settings to identify them.
    """
    configured = os.getenv("MODEL", "default")
    client = getattr(ask, "client", None) or getattr(ask, "__self__", None)
    if client is None:
        loaded = getattr(sys.modules.get("marta.gptapi"), "model", None)
        if loaded is not None and ("MODEL" not in os.environ
                                  or getattr(loaded, "model_type", configured) == configured):
            client = loaded
    parameters = {name: _scalar(getattr(client, name)) for name in CLIENT_FIELDS
                  if client is not None and hasattr(client, name)
                  and type(getattr(client, name)) in (str, int, float, bool, type(None))}
    declared_digest = _scalar(getattr(client, "model_digest", None)) if client is not None else None
    declared_digest = declared_digest or os.getenv("MARTA_MODEL_DIGEST")
    directory = Path(__file__).parent
    prompt_modules = {"summaries": summaries, "readme": readme}
    prompts = {name: {"module_sha256": file_hash(module.__file__),
                      "constants_sha256": digest({key: value for key, value in vars(module).items()
                                                  if key.isupper() and isinstance(value, str)})}
               for name, module in prompt_modules.items()}
    return {
        "policy": PROVENANCE_POLICY,
        "prompts": prompts,
        "implementation": {name: file_hash(directory / name) for name in
                           ("project.py", "source_context.py", "analysis_state.py", "prompt_budget.py")},
        "client_implementation": file_hash(directory.parent / "gptapi.py"),
        "model": {"configured_name": configured,
                  "client_name": _scalar(getattr(client, "model_type", None)),
                  "digest": declared_digest, "digest_status": "caller_declared" if declared_digest else "unavailable"},
        "client_parameters": parameters,
        "prompt_budget": budget_provenance(ask),
        "runtime": {key: os.getenv(key) for key in
                    ("LLM_MAX_TOKENS", "OLLAMA_CTX", "OLLAMA_CONTEXT_LENGTH", "MARTA_MAX_CONTEXT_CHARS")},
    }


def embedding_provenance(model):
    """Identify the configured embedding recipe without loading Transformers.

    Local metadata is hashed; large weight files are not scanned or claimed
    immutable. A supplied digest/recipe is explicitly caller-declared.
    """
    directory = Path(__file__).parent
    local = Path(model)
    names = ("config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json",
             "vocab.txt", "vocab.json", "merges.txt", "model.safetensors.index.json")
    return {"policy": "embedding-provenance-v1", "configured_model": model,
            "implementation": {name: file_hash(directory / name) for name in ("rag.py", "analysis_state.py")},
            "embedding_implementation": file_hash(directory.parent / "embedding.py"),
            "declared_digest": os.getenv("MARTA_EMBEDDING_DIGEST"),
            "declared_recipe": os.getenv("MARTA_EMBEDDING_RECIPE"),
            "local_metadata": {name: file_hash(local / name) for name in names
                               if model and local.is_dir() and (local / name).is_file()}}


class AnalysisArchive:
    """Unique local evidence directory per invocation, never a cache lookup source."""

    def __init__(self, output, *, use_cache, enrich):
        parent = Path(output) / "run_results" / "analysis_runs"
        parent.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="analysis_", dir=parent))
        self.manifest = {"status": "running", "use_cache": use_cache, "enrich": enrich,
                         "started_at": datetime.now(timezone.utc).isoformat(), "requests": 0}
        self._save()

    def _save(self):
        atomic_json(self.root / "manifest.json", self.manifest)

    def annotate(self, **values):
        self.manifest.update(values)
        self._save()

    def request(self, system, user, recorder, *, response=None, error=None):
        entry = {"request_sha256": digest([system, user]), "phase": recorder.fase_atual,
                 "context": dict(recorder._contexto),
                 "response": response if isinstance(response, str) else None,
                 "response_type": type(response).__name__, "error": error}
        with (self.root / "responses.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(entry, ensure_ascii=True) + "\n")
            stream.flush()
        self.manifest["requests"] += 1

    def complete(self, *, cache_hit):
        if not (self.root / "bundle.json").is_file():
            raise RuntimeError("Cannot complete an analysis without its bundle")
        self.annotate(status="complete", cache_hit=cache_hit,
                      finished_at=datetime.now(timezone.utc).isoformat())

    def __enter__(self):
        return self

    def __exit__(self, kind, error, traceback):
        if kind is not None:
            interrupted = issubclass(kind, (KeyboardInterrupt, asyncio.CancelledError))
            self.annotate(status="interrupted" if interrupted else "failed",
                          error={"type": kind.__name__, "message": str(error)},
                          finished_at=datetime.now(timezone.utc).isoformat())
        elif self.manifest["status"] != "complete":
            self.annotate(status="failed", error={"type": "IncompleteAnalysis", "message": "No complete bundle"})
            raise RuntimeError("Analysis did not commit its evidence bundle")
        return False
