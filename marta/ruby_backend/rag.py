"""Function-level RAG over Ruby method summaries (item 4).

The Ruby counterpart to MARTA's ``function_database``: embed each method's
summary and, at generation time, retrieve semantically-related methods to feed
the Planner as inspiration (and, later, the self-heal loop). MARTA's embedding
stack (``embedding.py``: bge-large + chromadb) is language-agnostic — it embeds
summary text — so we reuse the exact same embedder; only the stored objects
differ (Ruby ``MethodTarget`` instead of Python ``FunctionMessage``).

The embedder is injectable (defaults to ``marta.embedding.embedder``) so the
retrieval logic is unit-testable without loading torch/bge. Retrieval is plain
cosine top-k, mirroring the chromadb query MARTA performs.
"""
from __future__ import annotations

from typing import Callable, List, Optional, Sequence

import numpy as np

EmbedDocs = Callable[[List[str]], Sequence[Sequence[float]]]
EmbedQuery = Callable[[str], Sequence[float]]


def _cosine_topk(matrix: np.ndarray, q: np.ndarray, k: int) -> List[int]:
    """Indices of the k rows most cosine-similar to q (same as embedding.py)."""
    mat_norms = np.linalg.norm(matrix, axis=1) + 1e-8
    q_norm = np.linalg.norm(q) + 1e-8
    sims = (matrix @ q) / (mat_norms * q_norm)
    return list(np.argsort(-sims)[:k])


class RubyFunctionDatabase:
    def __init__(
        self,
        embed_documents: Optional[EmbedDocs] = None,
        embed_query: Optional[EmbedQuery] = None,
    ):
        self._embed_documents = embed_documents
        self._embed_query = embed_query
        self.targets: list = []
        self._matrix: Optional[np.ndarray] = None

    def _ensure_embedder(self) -> None:
        if self._embed_documents is None or self._embed_query is None:
            from marta.embedding import embedder  # lazy: avoid torch unless used
            self._embed_documents = embedder.embed_documents
            self._embed_query = embedder.embed_query

    @staticmethod
    def _text_of(target) -> str:
        return getattr(target, "summary", "") or getattr(target, "done_what", "") or ""

    def init(self, targets: Sequence) -> "RubyFunctionDatabase":
        """Embed the summary of every target that has one."""
        kept, docs = [], []
        for t in targets:
            text = self._text_of(t)
            if text:
                kept.append(t)
                docs.append(text)
        self.targets = kept
        if not docs:
            self._matrix = None
            return self
        self._ensure_embedder()
        self._matrix = np.asarray(self._embed_documents(docs), dtype=float)
        return self

    def query(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List:
        """Top-k related targets for ``text``. ``exclude`` drops the target with
        that ``method.qualified_name`` (so a method doesn't retrieve itself)."""
        if self._matrix is None or not text:
            return []
        self._ensure_embedder()
        q = np.asarray(self._embed_query(text), dtype=float)
        # Over-fetch so we can drop the excluded self and still return k.
        idx = _cosine_topk(self._matrix, q, k + (1 if exclude else 0))
        out = []
        for i in idx:
            t = self.targets[i]
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
