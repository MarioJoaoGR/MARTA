"""Request-local Ruby transport facade and explicit legacy-client compatibility."""
from contextvars import ContextVar

from marta.llm_response import ChatReply


async def client_request(client, system, user):
    if getattr(client, "response_api", False) is True:
        result = await client.aask_result(system, user)
        if not isinstance(result, ChatReply):
            raise TypeError("aask_result must return ChatReply")
        return result.text, result.details()
    # Explicitly legacy: valid for sequential adapters, not a concurrency proof.
    text = await client.aask(system, user)
    details = dict(getattr(client, "last_call", None) or {})
    details.setdefault("usage_reported", False)
    details["metrics_source"] = "legacy_client_last_call"
    return text, details


class RubyAsk:
    def __init__(self, client):
        self.client = client
        self._last = ContextVar("ruby_request_detail", default=None)

    @property
    def response_api(self):
        return getattr(self.client, "response_api", False) is True

    async def aask_result(self, system, user):
        result = await self.client.aask_result(system, user)
        if not isinstance(result, ChatReply):
            raise TypeError("aask_result must return ChatReply")
        return result

    @property
    def last_call(self):
        value = self._last.get()
        return dict(value) if value is not None else None

    async def __call__(self, system, user):
        self._last.set(None)
        text, details = await client_request(self.client, system, user)
        self._last.set(details)
        return text if isinstance(text, str) else ""
