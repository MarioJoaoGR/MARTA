"""Métricas do backend Ruby (item 8), e a telemetria da execução.

Mantém os contadores da ``recorder.Score`` da MARTA Python (sintaxe, asserções,
correções, tipos de erro, cobertura por ronda, tokens), isolados em
``ruby_backend`` para não acoplar o fluxo Ruby ao singleton do Python.

Por cima disso há a telemetria, que o total de tokens não responde:

* **por fase** — a Fase 1 tem cinco sub-fases (done_what, o enriquecimento pelo
  grafo, o what_todo, o sumário final, as classes) e a geração tem três (plano,
  primeira escrita, reparação). Sem separar, não se sabe onde o tempo foi.
* **por chamada** — cada chamada ao modelo fica numa linha do ``eventos.jsonl``:
  fase, método, ronda, tentativa, tokens de entrada e saída, segundos, se a
  resposta foi cortada pelo limite e se houve erro. Escrito à medida (uma linha,
  um flush), para uma execução morta a meio deixar na mesma o que já mediu.
* **respostas cortadas e erros** — o ``gptapi`` devolve ``""`` quando a chamada
  falha, e o limite de tokens corta respostas sem avisar. As duas coisas
  contavam como chamada normal.
* **subprocessos Ruby** — ``ruby -c``, RSpec e cobertura. Numa geração real o
  modelo não é o único custo, e o tempo de GPU paga-se na mesma enquanto o RSpec
  corre.
"""
from __future__ import annotations

import json
import os
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional


def _fase_vazia() -> dict:
    return {"chamadas": 0, "prompt_tokens": 0, "completion_tokens": 0,
            "segundos_chamadas": 0.0, "segundos_total": 0.0,
            "cortadas": 0, "erros": 0}


@dataclass
class RubyScore:
    first_run: bool = True

    syntax_pass: int = 0
    syntax_error: int = 0
    syntax_fix_success: int = 0
    assertion_pass: int = 0
    assertion_error: int = 0
    assertion_fix_success: int = 0
    assertion_error_types: Dict[str, int] = field(default_factory=dict)

    first_syntax_pass: int = 0
    first_syntax_error: int = 0
    first_syntax_fix_success: int = 0
    first_assertion_pass: int = 0
    first_assertion_error: int = 0
    first_assertion_fix_success: int = 0
    first_assertion_error_types: Dict[str, int] = field(default_factory=dict)

    salvaged: int = 0
    coverage: List[dict] = field(default_factory=list)

    prompt_tokens: int = 0
    completion_tokens: int = 0
    llm_calls: int = 0
    # Chamadas que falharam (o gptapi devolve "" e o fluxo segue com resposta
    # vazia) e respostas cortadas pelo limite de tokens (finish_reason "length").
    llm_erros: int = 0
    llm_cortadas: int = 0
    # fase -> chamadas/tokens/segundos; tipo de subprocesso -> segundos e contagem
    por_fase: Dict[str, dict] = field(default_factory=dict)
    subprocessos: Dict[str, dict] = field(default_factory=dict)

    def _bump(self, name: str) -> None:
        setattr(self, name, getattr(self, name) + 1)
        if self.first_run:
            setattr(self, "first_" + name, getattr(self, "first_" + name) + 1)

    def add_syntax_pass(self) -> None:
        self._bump("syntax_pass")

    def add_syntax_error(self) -> None:
        self._bump("syntax_error")

    def add_syntax_fix_success(self) -> None:
        self._bump("syntax_fix_success")

    def add_assertion_pass(self) -> None:
        self._bump("assertion_pass")

    def add_assertion_error(self) -> None:
        self._bump("assertion_error")

    def add_assertion_fix_success(self) -> None:
        self._bump("assertion_fix_success")

    def add_salvaged(self) -> None:
        self.salvaged += 1

    def add_assertion_error_type(self, error_type: str) -> None:
        self.assertion_error_types[error_type] = self.assertion_error_types.get(error_type, 0) + 1
        if self.first_run:
            self.first_assertion_error_types[error_type] = (
                self.first_assertion_error_types.get(error_type, 0) + 1
            )

    def add_llm_call(self, prompt_tokens: int = 0, completion_tokens: int = 0,
                     fase: str = "?", segundos: float = 0.0,
                     cortada: bool = False, erro: bool = False) -> None:
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.llm_calls += 1
        if cortada:
            self.llm_cortadas += 1
        if erro:
            self.llm_erros += 1
        f = self.por_fase.setdefault(fase, _fase_vazia())
        f["chamadas"] += 1
        f["prompt_tokens"] += prompt_tokens
        f["completion_tokens"] += completion_tokens
        f["segundos_chamadas"] = round(f["segundos_chamadas"] + segundos, 3)
        f["cortadas"] += int(cortada)
        f["erros"] += int(erro)

    def add_tempo_fase(self, fase: str, segundos: float) -> None:
        f = self.por_fase.setdefault(fase, _fase_vazia())
        f["segundos_total"] = round(f["segundos_total"] + segundos, 3)

    def add_subprocesso(self, tipo: str, segundos: float) -> None:
        s = self.subprocessos.setdefault(tipo, {"execucoes": 0, "segundos": 0.0})
        s["execucoes"] += 1
        s["segundos"] = round(s["segundos"] + segundos, 3)

    def to_json(self) -> dict:
        d = asdict(self)
        d.pop("first_run", None)
        d["total_tokens"] = self.prompt_tokens + self.completion_tokens
        return d


def _python_side_tokens() -> tuple:
    """Current token tally of the Python gptapi singleton (which counts usage
    for every LLM call), or (0, 0) if the LLM stack isn't loaded."""
    try:
        from marta.recorder import recoder
        return recoder.score.prompt_tokens, recoder.score.completion_tokens
    except Exception:
        return (0, 0)


def _detalhe_da_ultima_chamada() -> dict:
    """O que o gptapi guardou da última chamada: razão de fim e erro. Vazio se a
    pilha do LLM não está carregada (testes com ``ask`` de mentira)."""
    try:
        from marta.gptapi import model
        return getattr(model, "last_call", None) or {}
    except Exception:
        return {}


def token_tracking_ask(ask, score: RubyScore, recorder: Optional["RubyRecorder"] = None):
    """Envolve um ``ask`` para creditar chamada, tokens, segundos, fase, respostas
    cortadas e erros. Aditivo: o gptapi não é tocado. Com um ``ask`` de mentira os
    tokens ficam a 0 e o resto continua a ser medido."""
    async def wrapped(system: str, user: str) -> str:
        fase = recorder.fase_atual if recorder is not None else "?"
        antes = _python_side_tokens()
        t0 = time.time()
        out = await ask(system, user)
        segundos = time.time() - t0
        depois = _python_side_tokens()
        detalhe = _detalhe_da_ultima_chamada()
        entrada, saida = depois[0] - antes[0], depois[1] - antes[1]
        cortada = detalhe.get("finish_reason") == "length"
        erro = bool(detalhe.get("erro"))
        score.add_llm_call(entrada, saida, fase=fase, segundos=segundos,
                           cortada=cortada, erro=erro)
        if recorder is not None:
            recorder.evento(tipo="llm", fase=fase, prompt_tokens=entrada,
                            completion_tokens=saida, segundos=round(segundos, 3),
                            cortada=cortada, erro=detalhe.get("erro"),
                            caracteres_resposta=len(out or ""))
        return out
    return wrapped


class RubyRecorder:
    def __init__(self, caminho_eventos: Optional[str] = None):
        self.start_time = time.time()
        self.times: Dict[str, float] = {}
        self.score = RubyScore()
        #: ficheiro JSONL com uma linha por chamada/subprocesso (opcional)
        self.caminho_eventos = caminho_eventos
        self._fases: List[str] = []
        self._contexto: Dict[str, object] = {}

    # ------------------------------------------------------------- fases --
    @property
    def fase_atual(self) -> str:
        return self._fases[-1] if self._fases else "?"

    @contextmanager
    def fase(self, nome: str):
        """Etiqueta tudo o que acontecer lá dentro, e mede o tempo de parede da
        fase (que inclui o Ruby e a espera, não só o modelo)."""
        self._fases.append(nome)
        t0 = time.time()
        try:
            yield
        finally:
            self._fases.pop()
            self.score.add_tempo_fase(nome, time.time() - t0)

    def define_contexto(self, **campos) -> None:
        """Fixa campos de contexto até nova ordem (a ronda, que dura um ciclo
        inteiro e não cabe num bloco `with` sem reindentar o ciclo todo)."""
        self._contexto.update({k: v for k, v in campos.items() if v is not None})

    @contextmanager
    def contexto(self, **campos):
        """Acrescenta campos aos eventos (método, ronda, tentativa)."""
        antes = dict(self._contexto)
        self._contexto.update({k: v for k, v in campos.items() if v is not None})
        try:
            yield
        finally:
            self._contexto = antes

    @contextmanager
    def medir(self, tipo: str):
        """Cronometra um subprocesso Ruby (ruby -c, rspec, cobertura)."""
        t0 = time.time()
        try:
            yield
        finally:
            segundos = time.time() - t0
            self.score.add_subprocesso(tipo, segundos)
            self.evento(tipo=tipo, fase=self.fase_atual, segundos=round(segundos, 3))

    # ---------------------------------------------------------- eventos --
    def evento(self, **campos) -> None:
        if not self.caminho_eventos:
            return
        linha = {"t": round(time.time() - self.start_time, 3), **self._contexto, **campos}
        try:
            os.makedirs(os.path.dirname(self.caminho_eventos) or ".", exist_ok=True)
            with open(self.caminho_eventos, "a", encoding="utf-8") as f:
                f.write(json.dumps(linha, ensure_ascii=False) + "\n")
        except OSError:
            pass  # telemetria nunca derruba a execução

    # ------------------------------------------------------------ tempos --
    def start_count_time(self, name: str) -> None:
        self.times[name] = time.time()

    def end_count_time(self, name: str) -> None:
        self.times[name] = time.time() - self.times[name]

    def to_json(self) -> dict:
        return {
            "time": time.time() - self.start_time,
            "times": self.times,
            **self.score.to_json(),
        }

    def end(self, out_dir: str, project_name: str) -> str:
        """Write ``<out_dir>/<project_name>.json`` and return its path."""
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"{project_name}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_json(), f, indent=2)
        return path
