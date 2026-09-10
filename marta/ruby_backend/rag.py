"""Function-level RAG over Ruby method summaries (item 4).

The Ruby counterpart to MARTA's ``function_database``: embed each method's
summary and, at generation time, retrieve semantically-related methods to feed
the Planner as inspiration (and, later, the self-heal loop). MARTA's embedding
stack (``embedding.py``: bge-large + chromadb) is language-agnostic — it embeds
summary text — so we reuse both the embedder and the store; only the indexed
objects differ (Ruby ``MethodTarget`` instead of Python ``FunctionMessage``).

Two deliberate differences from ``embedding.FunctionDatabase``, both recorded in
``PARIDADE.md`` §2:

* **The client is persistent, not ephemeral.** MARTA Python uses
  ``chromadb.Client(...)``, which keeps nothing, so every run re-embeds every
  summary. Here the collection lives under ``.marta_ruby_cache/vectors`` next to
  the analysis cache and is keyed on ``source hash | LLM model | embedder``: on
  an unchanged project the whole embedding pass is skipped. That is the actual
  cost, especially on the cluster where ``EMBED_DEVICE=cpu``.
* **The metric is cosine, not the chromadb default (L2).** The embedder does
  mean pooling and **does not normalise** (``embedding.py:43``), so on these
  vectors L2 and cosine do not rank alike. Cosine is what ``find_topK_message``
  uses in the same Python file, so this keeps the two paths consistent.

The embedder is injectable so the retrieval logic is testable without loading
torch/bge; without a ``persist_dir`` the collection is in-memory, as in Python.
"""
from __future__ import annotations

import re
import uuid
from typing import Callable, List, Optional, Sequence

EmbedDocs = Callable[[List[str]], Sequence[Sequence[float]]]
EmbedQuery = Callable[[str], Sequence[float]]


def _safe_name(name: str) -> str:
    """chromadb accepts 3-63 chars of [a-zA-Z0-9._-], starting and ending
    alphanumeric."""
    s = re.sub(r"[^0-9A-Za-z._-]", "_", name).strip("._-") or "col"
    return (s + "_col")[:63] if len(s) < 3 else s[:63]


class RubyFunctionDatabase:
    def __init__(
        self,
        embed_documents: Optional[EmbedDocs] = None,
        embed_query: Optional[EmbedQuery] = None,
        persist_dir: Optional[str] = None,
        name: str = "functions",
        key: str = "",
    ):
        self._embed_documents = embed_documents
        self._embed_query = embed_query
        self._persist_dir = persist_dir
        # In-memory collections are per-instance: MARTA Python hardcodes
        # 'functions_database', which would collide here because build_rag
        # creates two databases (methods and classes) in the same process.
        self._name = _safe_name(name if persist_dir else f"{name}-{uuid.uuid4().hex[:8]}")
        self._key = key
        self.targets: list = []
        self.reused = False          # True when the vectors came from disk
        self._collection = None

    def _ensure_embedder(self) -> None:
        if self._embed_documents is None or self._embed_query is None:
            from marta.embedding import embedder  # lazy: avoid torch unless used
            self._embed_documents = embedder.embed_documents
            self._embed_query = embedder.embed_query

    def _client(self):
        import chromadb  # lazy: chromadb pulls in a lot at import time
        if self._persist_dir:
            return chromadb.PersistentClient(path=self._persist_dir)
        return chromadb.EphemeralClient()

    @staticmethod
    def _text_of(target) -> str:
        return getattr(target, "summary", "") or getattr(target, "done_what", "") or ""

    def _open(self, ids: List[str]):
        """Return (collection, reusable). Reusable means the stored vectors were
        built from the same sources, the same LLM and the same embedder, and
        cover exactly these ids — so the embedding pass can be skipped."""
        client = self._client()
        # metadata is only applied on creation, so it records the key of the
        # vectors actually stored.
        meta = {"key": self._key, "hnsw:space": "cosine"}
        try:
            col = client.get_collection(self._name, embedding_function=None)
        except Exception:
            return client.create_collection(
                self._name, metadata=meta, embedding_function=None), False
        if (col.metadata or {}).get("key") == self._key and self._key:
            try:
                if col.get(include=[])["ids"] == ids:
                    return col, True
            except Exception:
                pass
        client.delete_collection(self._name)
        return client.create_collection(
            self._name, metadata=meta, embedding_function=None), False

    def init(self, targets: Sequence) -> "RubyFunctionDatabase":
        """Index the summary of every target that has one."""
        kept, docs = [], []
        for t in targets:
            text = self._text_of(t)
            if text:
                kept.append(t)
                docs.append(text)
        self.targets = kept
        self._collection = None
        self.reused = False
        if not docs:
            return self
        # The index is part of the id so a reordering invalidates the cache; the
        # name is there to make the stored collection readable.
        ids = [f"{n}|{getattr(t.method, 'qualified_name', '')}" for n, t in enumerate(kept)]
        col, reusable = self._open(ids)
        self._collection = col
        if reusable:
            self.reused = True
            return self
        self._ensure_embedder()
        vectors = [list(map(float, v)) for v in self._embed_documents(docs)]
        col.add(ids=ids, embeddings=vectors)
        return self

    def query(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List:
        """Top-k related targets for ``text``. ``exclude`` drops the target with
        that ``method.qualified_name`` (so a method doesn't retrieve itself)."""
        if self._collection is None or not text:
            return []
        self._ensure_embedder()
        q = list(map(float, self._embed_query(text)))
        # Over-fetch so we can drop the excluded self and still return k.
        n = min(k + (1 if exclude else 0), len(self.targets))
        try:
            res = self._collection.query(query_embeddings=[q], n_results=n)
        except Exception:
            return []
        out = []
        for ident in res["ids"][0]:
            t = self.targets[int(ident.split("|", 1)[0])]
            if exclude and t.method.qualified_name == exclude:
                continue
            out.append(t)
            if len(out) >= k:
                break
        return out

    def related_lines(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List[str]:
        """Retrieved methods as compact "name: summary" lines for the Planner
        context — the Ruby analogue of MARTA's related_block."""
        lines = []
        for t in self.query(text, k=k, exclude=exclude):
            snippet = " ".join(self._text_of(t).split())[:200]
            lines.append(f"{t.method.qualified_name}: {snippet}")
        return lines
