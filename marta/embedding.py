import os
import re
import numpy as np
from dotenv import load_dotenv
from langchain_core.embeddings import Embeddings
from transformers import AutoTokenizer, AutoModel
import torch
from typing import List
import chromadb
from chromadb.config import Settings


class HuggingFaceEmbedder(Embeddings):
    def embed_query(self, text: str) -> List[float]:
        """Embed query text.

        Args:
            text: Text to embed.

        Returns:
            Embedding as a list of floats.
        """
        text = self.embed_instruction + text.replace("\n", " ")

        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512, **self.encode_kwargs)
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)

        embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()

        return embedding.tolist()

    def __init__(self, model_name_or_path: str, embed_instruction: str = "", show_progress: bool = False,
                 encode_kwargs=None):
        if encode_kwargs is None:
            encode_kwargs = {}
        self.embed_instruction = embed_instruction
        self.show_progress = show_progress
        self.encode_kwargs = encode_kwargs
        # EMBED_DEVICE força o device (ex: 'cpu' no Deucalion, para o Ollama ter
        # a GPU sozinho — torch + llama.cpp na mesma GPU sem MPS mata o throughput).
        _dev = os.environ.get("EMBED_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = torch.device(_dev)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, local_files_only=True)
        self.model = AutoModel.from_pretrained(model_name_or_path, local_files_only=True).to(self.device)

    @staticmethod
    def _masked_mean(last_hidden_state, attention_mask):
        """Mean pooling que IGNORA os tokens de padding.

        Crucial para que o embedding em lote seja idêntico ao de item único:
        o `embed_query` não usa padding, por isso a sua média plana == média
        mascarada. Já em lote há padding, e uma média plana (dim=1) poluiria o
        vetor com tokens de padding → vetores fora do espaço das queries."""
        mask = attention_mask.unsqueeze(-1).type_as(last_hidden_state)
        summed = (last_hidden_state * mask).sum(dim=1)
        counts = mask.sum(dim=1).clamp(min=1e-9)
        return summed / counts

    def embed_documents(self, texts: List[str], batch_size: int = 32) -> List[List[float]]:
        """Embedding em lote (uma passagem por chunk) com pooling mascarado.

        Equivale a chamar embed_query item-a-item, mas com muito menos forwards
        no modelo. Faz chunking para limitar o pico de memória em projetos com
        muitas funções/classes."""
        texts = [self.embed_instruction + t.replace("\n", " ") for t in texts]
        all_embeddings: List[List[float]] = []
        for start in range(0, len(texts), batch_size):
            chunk = texts[start:start + batch_size]
            inputs = self.tokenizer(chunk, padding=True, truncation=True,
                                    return_tensors="pt", max_length=512, **self.encode_kwargs)
            inputs = {key: value.to(self.device) for key, value in inputs.items()}
            with torch.no_grad():
                outputs = self.model(**inputs)
            pooled = self._masked_mean(outputs.last_hidden_state, inputs["attention_mask"])
            all_embeddings.extend(pooled.tolist())
        return all_embeddings


def find_topK_message(name, messages, query_vector, k=1):
    """Top-k por similaridade de cosseno em numpy.

    Antes criava/apagava uma coleção ChromaDB a cada chamada (uma por
    parâmetro analisado) — overhead enorme no caminho quente. Como os vetores
    das classes já estão pré-computados (embedding_class_summary), basta um
    produto interno em memória. `name` mantém-se na assinatura por
    compatibilidade mas já não é usado.
    """
    # Só considera mensagens com vetor válido; sem candidatos, devolve o input.
    candidates = [m for m in messages if getattr(m, 'vector', None) is not None]
    if not candidates:
        return messages

    mat = np.asarray([m.vector for m in candidates], dtype=np.float32)
    q = np.asarray(query_vector, dtype=np.float32)

    mat_norms = np.linalg.norm(mat, axis=1) + 1e-8
    q_norm = np.linalg.norm(q) + 1e-8
    sims = (mat @ q) / (mat_norms * q_norm)

    top_idx = np.argsort(-sims)[:k]
    return [candidates[i] for i in top_idx]


class FunctionDatabase:
    def __init__(self):
        self.collection = client.create_collection('functions_database')
        self.functions = []

    def init(self, project):
        ids = []
        summaries = []
        for file_message in project.file_messages:
            for function in file_message.functions:
                if function.summary is None:
                    continue
                ids.append(str(len(self.functions)))
                self.functions.append(function)
                summaries.append(function.summary)
        if not summaries:
            return
        # Embedding em lote (uma passagem por chunk) em vez de N forwards.
        vectors = embedder.embed_documents(summaries)
        self.collection.add(
            embeddings=vectors,
            ids=ids
        )

    def query(self, query, k=3):
        query_vector = embedder.embed_query(query)
        try:
            results = self.collection.query(
                query_embeddings=[query_vector],
                n_results=k
            )
        except RuntimeError:
            return []

        top_k = []
        for index in results['ids'][0]:
            top_k.append(self.functions[int(index)])
        return top_k


load_dotenv()
embedder = HuggingFaceEmbedder(model_name_or_path=os.getenv('TRANSFORMER_PATH') or '')
# anonymized_telemetry=False: a telemetria posthog do chromadb está partida
# (capture() com assinatura errada) e, em queries RAG via asyncio.to_thread,
# o batched_events dá KeyError que MATA o processo a meio (perdeu o httpie aos
# 170 min). Desligá-la remove o crash sem afetar funcionalidade.
client = chromadb.Client(Settings(anonymized_telemetry=False))
function_database = FunctionDatabase()
