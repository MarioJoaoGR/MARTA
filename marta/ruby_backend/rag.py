"""RAG sobre os sumários Ruby (item 4).

Contraparte do `function_database` da MARTA Python. A pilha de *embeddings*
(`embedding.py`: bge-large + chromadb) é agnóstica da linguagem — embebe texto —
por isso reutiliza-se tal e qual; muda só o que se indexa (`MethodTarget` em vez
de `FunctionMessage`).

**Dois índices, como na Python, e cada um com o mesmo armazenamento que lá tem:**

* `RubyFunctionDatabase` — sumários de MÉTODOS, em ChromaDB, como o
  `FunctionDatabase`. Responde a *"que métodos se parecem com este?"* e alimenta
  os `RELATED` do prompt do Planner.
* `RubyClassIndex` — sumários de CLASSES, em cosseno sobre NumPy, como o
  `find_topK_message`. Responde a *"que classe é este parâmetro?"* e alimenta o
  `_augment_judge_semantic`.

A única divergência face à Python, e está registada em `PARIDADE.md` §2, é a
**persistência**: lá os dois índices são reconstruídos a cada execução (o cliente
é `chromadb.Client(...)`, efémero), e mesmo com a cache de análise cheia os
sumários vinham do disco para serem embebidos outra vez. Aqui os dois ficam em
`.marta_ruby_cache/vectors`, validados por `hash das fontes | modelo LLM |
modelo de embeddings`, porque é aí que está o custo: no cluster o *embedding*
corre em CPU, para o Ollama ficar com a GPU sozinho.

Nota sobre a métrica: o `HuggingFaceEmbedder` faz *mean pooling* e **não
normaliza** (`embedding.py:43`). Em vetores não normalizados o L2 (omissão do
ChromaDB) não ordena como o cosseno, por isso a coleção é criada com
`hnsw:space: "cosine"` — que é o que o `find_topK_message` já usava do outro
lado.

O *embedder* é injetável, para a lógica de recuperação ser testável sem carregar
o torch.
"""
from __future__ import annotations

import os
import re
import uuid
from typing import Callable, List, Optional, Sequence

import numpy as np

EmbedDocs = Callable[[List[str]], Sequence[Sequence[float]]]
EmbedQuery = Callable[[str], Sequence[float]]


def _safe_name(name: str) -> str:
    """O chromadb aceita 3-63 caracteres de [a-zA-Z0-9._-], a começar e a acabar
    em alfanumérico."""
    s = re.sub(r"[^0-9A-Za-z._-]", "_", name).strip("._-") or "col"
    return (s + "_col")[:63] if len(s) < 3 else s[:63]


class _Indice:
    """O que os dois índices partilham: o embedder, a selecção dos alvos com
    sumário, e a formatação da resposta."""

    def __init__(
        self,
        embed_documents: Optional[EmbedDocs] = None,
        embed_query: Optional[EmbedQuery] = None,
        persist_dir: Optional[str] = None,
        key: str = "",
    ):
        self._embed_documents = embed_documents
        self._embed_query = embed_query
        self._persist_dir = persist_dir
        self._key = key
        self.targets: list = []
        self.reused = False          # True quando os vetores vieram do disco

    def _ensure_embedder(self) -> None:
        if self._embed_documents is None or self._embed_query is None:
            from marta.embedding import embedder  # tardio: evita o torch se não for usado
            self._embed_documents = embedder.embed_documents
            self._embed_query = embedder.embed_query

    @staticmethod
    def _text_of(target) -> str:
        return getattr(target, "summary", "") or getattr(target, "done_what", "") or ""

    def _select(self, targets: Sequence):
        """Guarda os alvos com sumário e devolve (textos, ids).

        O índice faz parte do id para uma reordenação invalidar o que está em
        disco; o nome vai atrás para a coleção ser legível a olho."""
        kept, docs = [], []
        for t in targets:
            text = self._text_of(t)
            if text:
                kept.append(t)
                docs.append(text)
        self.targets = kept
        self.reused = False
        ids = [f"{n}|{getattr(t.method, 'qualified_name', '')}" for n, t in enumerate(kept)]
        return docs, ids

    def _pick(self, ordem: Sequence[int], k: int, exclude: Optional[str]) -> List:
        """Dos índices já ordenados por semelhança, os k primeiros que não sejam
        o próprio."""
        out = []
        for i in ordem:
            t = self.targets[i]
            if exclude and t.method.qualified_name == exclude:
                continue
            out.append(t)
            if len(out) >= k:
                break
        return out

    def related_lines(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List[str]:
        """Os métodos recuperados como linhas "nome: sumário" para o contexto do
        Planner — o análogo do `related_block` da MARTA."""
        lines = []
        for t in self.query(text, k=k, exclude=exclude):
            snippet = " ".join(self._text_of(t).split())[:200]
            lines.append(f"{t.method.qualified_name}: {snippet}")
        return lines

    def query(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List:
        raise NotImplementedError


class RubyFunctionDatabase(_Indice):
    """Sumários de métodos em ChromaDB, como o `FunctionDatabase` da Python."""

    def __init__(self, embed_documents=None, embed_query=None,
                 persist_dir=None, name="functions", key=""):
        super().__init__(embed_documents, embed_query, persist_dir, key)
        # Em memória o nome é único por instância: a Python fixa
        # 'functions_database', o que aqui colidiria porque o build_rag cria
        # mais do que uma base no mesmo processo.
        self._name = _safe_name(name if persist_dir else f"{name}-{uuid.uuid4().hex[:8]}")
        self._collection = None

    def _client(self):
        import chromadb  # tardio: o chromadb arrasta muito no import
        if self._persist_dir:
            return chromadb.PersistentClient(path=self._persist_dir)
        return chromadb.EphemeralClient()

    def _open(self, ids: List[str]):
        """(coleção, reaproveitável). Reaproveitável = o que está guardado veio
        das mesmas fontes, do mesmo LLM e do mesmo embedder, e cobre exatamente
        estes ids."""
        client = self._client()
        # A metadata só se aplica na criação, por isso regista a chave dos
        # vetores que lá estão de facto.
        meta = {"key": self._key, "hnsw:space": "cosine"}
        try:
            col = client.get_collection(self._name, embedding_function=None)
        except Exception:
            return client.create_collection(
                self._name, metadata=meta, embedding_function=None), False
        if self._key and (col.metadata or {}).get("key") == self._key:
            try:
                if col.get(include=[])["ids"] == ids:
                    return col, True
            except Exception:
                pass
        client.delete_collection(self._name)
        return client.create_collection(
            self._name, metadata=meta, embedding_function=None), False

    def init(self, targets: Sequence) -> "RubyFunctionDatabase":
        docs, ids = self._select(targets)
        self._collection = None
        if not docs:
            return self
        col, reaproveitavel = self._open(ids)
        self._collection = col
        if reaproveitavel:
            self.reused = True
            return self
        self._ensure_embedder()
        vectors = [list(map(float, v)) for v in self._embed_documents(docs)]
        col.add(ids=ids, embeddings=vectors)
        return self

    def query(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List:
        if self._collection is None or not text:
            return []
        self._ensure_embedder()
        q = list(map(float, self._embed_query(text)))
        # Pede um a mais para poder deitar fora o próprio e ainda devolver k.
        n = min(k + (1 if exclude else 0), len(self.targets))
        try:
            res = self._collection.query(query_embeddings=[q], n_results=n)
        except Exception:
            return []
        return self._pick([int(i.split("|", 1)[0]) for i in res["ids"][0]], k, exclude)


class RubyClassIndex(_Indice):
    """Sumários de classes em cosseno sobre NumPy, como o `find_topK_message`.

    A MARTA Python usa NumPy aqui porque a pergunta é feita **uma vez por
    parâmetro ambíguo**, e com o ChromaDB cada chamada criava e apagava uma
    coleção (`embedding.py:95`). Aqui o índice é construído uma vez e depois só
    consultado, por isso esse custo não se põe — mas mantém-se o mesmo
    armazenamento, para as duas versões continuarem comparáveis.

    A matriz é guardada em `classes.npz` ao lado da coleção dos métodos.
    """

    FICHEIRO = "classes.npz"

    def __init__(self, embed_documents=None, embed_query=None,
                 persist_dir=None, key=""):
        super().__init__(embed_documents, embed_query, persist_dir, key)
        self._matrix: Optional[np.ndarray] = None

    def _path(self) -> Optional[str]:
        return os.path.join(self._persist_dir, self.FICHEIRO) if self._persist_dir else None

    def _load(self, ids: List[str]) -> Optional[np.ndarray]:
        p = self._path()
        if not p or not self._key or not os.path.exists(p):
            return None
        try:
            with np.load(p, allow_pickle=False) as z:
                if str(z["key"]) != self._key or list(z["ids"]) != ids:
                    return None
                return z["vectors"]
        except Exception:
            return None

    def _save(self, ids: List[str], matrix: np.ndarray) -> None:
        p = self._path()
        if not p or not self._key:
            return
        try:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            np.savez(p, vectors=matrix, ids=np.array(ids), key=np.array(self._key))
        except OSError:
            pass  # sem cache é mais lento, não é erro

    def init(self, targets: Sequence) -> "RubyClassIndex":
        docs, ids = self._select(targets)
        self._matrix = None
        if not docs:
            return self
        guardada = self._load(ids)
        if guardada is not None:
            self._matrix = guardada
            self.reused = True
            return self
        self._ensure_embedder()
        self._matrix = np.asarray(self._embed_documents(docs), dtype=float)
        self._save(ids, self._matrix)
        return self

    def query(self, text: str, k: int = 3, exclude: Optional[str] = None) -> List:
        if self._matrix is None or not text:
            return []
        self._ensure_embedder()
        q = np.asarray(self._embed_query(text), dtype=float)
        # Cosseno, igual ao helper do embedding.py.
        normas = np.linalg.norm(self._matrix, axis=1) + 1e-8
        sims = (self._matrix @ q) / (normas * (np.linalg.norm(q) + 1e-8))
        n = min(k + (1 if exclude else 0), len(self.targets))
        return self._pick(list(np.argsort(-sims)[:n]), k, exclude)
