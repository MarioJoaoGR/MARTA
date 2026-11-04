"""Whole-message budgets with explicit counting and optional-context reduction."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from functools import lru_cache
import os
from pathlib import Path
import sys
from typing import Any, Callable

from .checkpoints import digest, file_hash

POLICY = "whole-prompt-budget-v1"
DEFAULT_CONTEXT = 16384  # Client policy, not discovery of a server's context window.
DEFAULT_OUTPUT = 2048   # Existing default of MyGPT; explicit client limits win.
DEFAULT_MARGIN = 256


class BudgetConfigurationError(ValueError):
    pass


class PromptBudgetExceeded(RuntimeError):
    pass


class UTF8Estimate:
    name = "utf8-bytes-plus-64-estimate"
    exact = False
    identity = {"mode": name, "exact_for_template": False}

    def __call__(self, system, user):
        return len(system.encode("utf-8")) + len(user.encode("utf-8")) + 64


@lru_cache(maxsize=2)
def _local_tokenizer(path, fingerprint):
    try:
        from transformers import AutoTokenizer
        return AutoTokenizer.from_pretrained(path, local_files_only=True, trust_remote_code=False)
    except Exception as error:
        raise BudgetConfigurationError(
            "Cannot load the configured local chat tokenizer; no download or fallback attempted") from error


class LocalChatCounter:
    exact = True  # Exact for this local template; server/template matching is the caller's contract.
    name = "local-chat-template"

    def __init__(self, path, thinking=None):
        root = Path(path)
        if not root.is_dir():
            raise BudgetConfigurationError("MARTA_TOKENIZER_PATH must be an existing local directory")
        names = ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json",
                 "config.json", "vocab.json", "vocab.txt", "merges.txt", "chat_template.jinja",
                 "added_tokens.json", "tokenizer.model", "spiece.model", "sentencepiece.bpe.model")
        files = {name: file_hash(root/name) for name in names if (root/name).is_file()}
        files.update({str(item.relative_to(root)): file_hash(item)
                      for item in sorted((root / "chat_templates").glob("*.jinja")) if item.is_file()})
        if not files:
            raise BudgetConfigurationError("No tokenizer metadata found in MARTA_TOKENIZER_PATH")
        self.path = str(root.resolve())
        self.identity = {"mode": self.name, "path": self.path, "files": files,
                         "thinking": thinking, "exact_for_template": True}
        self.thinking = thinking

    def __call__(self, system, user):
        tokenizer = _local_tokenizer(self.path, digest(self.identity))
        kwargs = {"tokenize": True, "add_generation_prompt": True}
        if self.thinking is not None:
            kwargs["enable_thinking"] = self.thinking
        try:
            ids = tokenizer.apply_chat_template(
                [{"role": "system", "content": system}, {"role": "user", "content": user}], **kwargs)
        except Exception as error:
            raise BudgetConfigurationError("Configured tokenizer cannot render this chat template") from error
        return len(ids)


@dataclass(frozen=True)
class OptionalPart:
    name: str
    full: Any
    minimum: Any = ""
    compact: bool = True


@dataclass(frozen=True)
class PromptBudget:
    context_tokens: int
    output_tokens: int
    margin_tokens: int = DEFAULT_MARGIN
    counter: Callable = field(default_factory=UTF8Estimate, compare=False, repr=False)
    recorder: Any = field(default=None, compare=False, repr=False)
    window_source: str = "explicit"

    def __post_init__(self):
        if (type(self.context_tokens) is not int or self.context_tokens <= 0
                or type(self.output_tokens) is not int or self.output_tokens <= 0
                or type(self.margin_tokens) is not int or self.margin_tokens < 0
                or self.output_tokens + self.margin_tokens >= self.context_tokens):
            raise BudgetConfigurationError("Context must exceed the positive output reserve plus nonnegative margin")

    @property
    def input_limit(self):
        return self.context_tokens - self.output_tokens - self.margin_tokens

    @property
    def identity(self):
        return {"policy": POLICY, "context_tokens": self.context_tokens,
                "output_tokens": self.output_tokens, "margin_tokens": self.margin_tokens,
                "window_source": self.window_source,
                "counter": getattr(self.counter, "identity", {"mode": type(self.counter).__qualname__,
                                                              "exact_for_template": bool(getattr(self.counter, "exact", False))})}

    @classmethod
    def from_ask(cls, ask=None, recorder=None):
        client = getattr(ask, "client", None) or getattr(ask, "__self__", None)
        if client is None:
            loaded = getattr(sys.modules.get("marta.gptapi"), "model", None)
            if loaded is not None and ("MODEL" not in os.environ or
                    getattr(loaded, "model_type", os.getenv("MODEL")) == os.getenv("MODEL")):
                client = loaded
        supplied = getattr(ask, "prompt_budget", None) or getattr(client, "prompt_budget", None)
        def number(value, label):
            try:
                return int(value)
            except (TypeError, ValueError) as error:
                raise BudgetConfigurationError(label + " must be an integer") from error
        windows = {name: number(os.environ[name], name) for name in
                   ("MARTA_CONTEXT_TOKENS", "OLLAMA_CTX", "OLLAMA_CONTEXT_LENGTH") if os.getenv(name)}
        if any(value <= 0 for value in windows.values()):
            raise BudgetConfigurationError("Declared context windows must be positive")
        window = min(windows.values()) if windows else DEFAULT_CONTEXT
        cap = getattr(client, "max_tokens", "missing")
        if type(cap) not in (int, float, bool, type(None), str):
            cap = "missing"  # Opaque test/callback objects do not declare a cap.
        if cap == "missing":
            cap = number(os.getenv("LLM_MAX_TOKENS", str(
                supplied.output_tokens if isinstance(supplied, cls) else DEFAULT_OUTPUT)), "LLM_MAX_TOKENS")
        if type(cap) is not int or cap <= 0:
            raise BudgetConfigurationError("A finite positive output cap is required for whole-prompt budgeting")
        declared_reserve = number(os.getenv("MARTA_OUTPUT_RESERVE", str(cap)), "MARTA_OUTPUT_RESERVE")
        if declared_reserve <= 0:
            raise BudgetConfigurationError("MARTA_OUTPUT_RESERVE must be positive")
        declared_margin = number(os.environ["MARTA_CONTEXT_MARGIN"], "MARTA_CONTEXT_MARGIN") if os.getenv("MARTA_CONTEXT_MARGIN") else None
        if declared_margin is not None and declared_margin < 0:
            raise BudgetConfigurationError("MARTA_CONTEXT_MARGIN must be nonnegative")
        if isinstance(supplied, cls):
            if windows and supplied.context_tokens > window:
                raise BudgetConfigurationError("Supplied prompt budget exceeds a declared context window")
            if declared_margin is not None and supplied.margin_tokens < declared_margin:
                raise BudgetConfigurationError("Supplied prompt budget does not preserve the declared margin")
            if supplied.output_tokens < max(cap, declared_reserve):
                raise BudgetConfigurationError("Supplied prompt budget reserves less than the client output cap")
            if os.getenv("MARTA_REQUIRE_EXACT_TOKENS", "0") == "1" and not getattr(supplied.counter, "exact", False):
                raise BudgetConfigurationError("Exact token counting requires a matching local tokenizer or supplied exact counter")
            return replace(supplied, recorder=recorder)
        reserve = max(cap, declared_reserve)
        margin = declared_margin if declared_margin is not None else DEFAULT_MARGIN
        path = os.getenv("MARTA_TOKENIZER_PATH")
        effort = getattr(client, "reasoning_effort", None)
        thinking = None if effort is None else effort != "none"
        counter = LocalChatCounter(path, thinking) if path else UTF8Estimate()
        if os.getenv("MARTA_REQUIRE_EXACT_TOKENS", "0") == "1" and not counter.exact:
            raise BudgetConfigurationError("Exact token counting requires a matching local tokenizer or supplied PromptBudget")
        return cls(window, reserve, margin, counter, recorder,
                   "declared:" + ",".join(sorted(windows)) if windows else "client-default-unverified-server")

    def render(self, system, builder, parts=()):
        """Try complete context first, then reduce parts in declared low-priority order.

        Atomic parts can only switch to their explicit fallback. Compact prose
        and lists retain a prefix; code/plans/previous tests stay in the builder's
        mandatory closure, or in an atomic source part whose fallback is focal code.
        """
        parts = list(parts)
        values = {p.name: list(p.full) if isinstance(p.full, list) else p.full for p in parts}
        if len(values) != len(parts):
            raise ValueError("Optional prompt-part names must be unique")
        def render():
            text = builder(values)
            reduced = [p.name for p in parts if values[p.name] != p.full]
            if reduced:
                text += "\n\n[MARTA context budget: optional context reduced: " + ", ".join(reduced) + ".]"
            count = self.counter(system, text)
            if type(count) is not int or count < 0:
                raise BudgetConfigurationError("Prompt counter must return a nonnegative integer")
            return text, count
        original_text, original_count = render()
        def finish(text, count, fits):
            if self.recorder is not None:
                self.recorder.evento(tipo="prompt_budget", fase=self.recorder.fase_atual,
                    **self.identity, input_limit=self.input_limit, original_input=original_count,
                    selected_input=count, fits=fits,
                    original_request_sha256=digest([system, original_text]),
                    selected_request_sha256=digest([system, text]),
                    reduced=[{"name": p.name, "original_size": len(p.full), "selected_size": len(values[p.name])}
                             for p in parts if values[p.name] != p.full])
            if not fits:
                raise PromptBudgetExceeded(
                    f"Mandatory prompt requires {count} input units, budget {self.input_limit}; "
                    f"output reserve {self.output_tokens}, margin {self.margin_tokens}. "
                    "No model request was sent; focal code, original plan and previous test were preserved.")
            return text
        if original_count <= self.input_limit:
            return finish(original_text, original_count, True)
        for part in parts:
            if part.full == part.minimum:
                continue
            values[part.name] = part.minimum
            text, count = render()
            if count > self.input_limit:
                continue
            # Keep as much of this optional part as the complete rendered request
            # permits. Every candidate is recounted; BPE non-monotonicity may be
            # conservative, but the accepted candidate always actually fits.
            if part.compact and isinstance(part.full, (str, list)) and part.full[:len(part.minimum)] == part.minimum:
                low, high = len(part.minimum), len(part.full)
                best = part.minimum
                while low <= high:
                    middle = (low + high) // 2
                    values[part.name] = part.full[:middle]
                    candidate, size = render()
                    if size <= self.input_limit:
                        best = values[part.name]
                        low = middle + 1
                    else:
                        high = middle - 1
                values[part.name] = best
                text, count = render()
            return finish(text, count, count <= self.input_limit)
        text, count = render()
        return finish(text, count, False)


def budget_provenance(ask=None):
    return PromptBudget.from_ask(ask).identity
