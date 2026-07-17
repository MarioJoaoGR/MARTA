"""Lightweight, self-contained metrics recorder for the Ruby backend (item 8).

Mirrors the metrics of MARTA's ``recorder.Score`` — syntax/assertion pass/error/
fix counts (with first-round variants), assertion error types, per-round
coverage, and LLM call/token tallies — but stays isolated in ``ruby_backend``
(the chosen design) so it doesn't couple the Ruby flow to the Python singleton.
Wired in optionally: pass a ``RubyRecorder`` to the generation flow, or omit it.
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from typing import Dict, List


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

    def add_llm_call(self, prompt_tokens: int = 0, completion_tokens: int = 0) -> None:
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.llm_calls += 1

    def to_json(self) -> dict:
        d = asdict(self)
        d.pop("first_run", None)
        d["total_tokens"] = self.prompt_tokens + self.completion_tokens
        return d


class RubyRecorder:
    def __init__(self):
        self.start_time = time.time()
        self.times: Dict[str, float] = {}
        self.score = RubyScore()

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
