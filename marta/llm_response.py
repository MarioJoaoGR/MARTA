"""Immutable per-request output; no global client or usage counters."""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ChatReply:
    text: Optional[str]
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    finish_reason: Optional[str] = None
    error: Optional[str] = None

    def details(self):
        reported = all(type(value) is int and value >= 0
                       for value in (self.prompt_tokens, self.completion_tokens))
        return {"prompt_tokens": self.prompt_tokens if type(self.prompt_tokens) is int and self.prompt_tokens >= 0 else 0,
                "completion_tokens": self.completion_tokens if type(self.completion_tokens) is int and self.completion_tokens >= 0 else 0,
                "finish_reason": self.finish_reason, "erro": self.error,
                "usage_reported": reported, "metrics_source": "request_response"}
