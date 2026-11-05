"""Per-request identity/usage and task-local context; no network or model."""
import asyncio
from dataclasses import FrozenInstanceError
import json
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.llm_response import ChatReply
from marta.ruby_backend.recorder import RubyRecorder, token_tracking_ask
from marta.ruby_backend.requests import RubyAsk, client_request


def test_reply_is_immutable_and_details_are_independent():
    result = ChatReply("code", 10, 4, "stop")
    with pytest.raises(FrozenInstanceError):
        result.text = "changed"
    details = result.details()
    details["prompt_tokens"] = 999
    assert result.details()["prompt_tokens"] == 10


@pytest.mark.parametrize("incoming,outgoing", [(None, None), (10, None), (-1, 2), (True, 2)])
def test_missing_or_invalid_usage_stays_explicitly_unknown(incoming, outgoing):
    assert ChatReply("code", incoming, outgoing).details()["usage_reported"] is False


def test_opaque_callbacks_do_not_inherit_global_tokens_or_errors(monkeypatch):
    from marta.recorder import recoder
    monkeypatch.setitem(sys.modules, "marta.gptapi", SimpleNamespace(model=SimpleNamespace(
        last_call={"erro": "unrelated failure", "finish_reason": "length"})))
    async def opaque(system, user):
        recoder.score.add_tokens(100, 50)  # Simulate unrelated legacy/global work.
        return "code"
    recorder = RubyRecorder()
    assert asyncio.run(token_tracking_ask(opaque, recorder.score)("s", "u")) == "code"
    assert recorder.score.prompt_tokens == recorder.score.completion_tokens == 0
    assert recorder.score.llm_erros == recorder.score.llm_cortadas == 0
    assert recorder.score.llm_usage_unknown_calls == 1


@pytest.mark.parametrize("second_error", [False, True])
def test_overlapping_native_calls_keep_their_own_metadata_and_phase(tmp_path, second_error):
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    class Client:
        response_api = True
        last_call = {"prompt_tokens": 999, "finish_reason": "length", "erro": "stale legacy"}
        async def aask_result(self, system, user):
            if user == "A":
                entered.set()
                await finished.wait()
                return ChatReply("answer A", 10, 3, "length")
            await entered.wait()
            finished.set()
            return ChatReply("" if second_error else "answer B", 20, 7, "stop",
                             "fixture failure" if second_error else None)
    native = RubyAsk(Client())
    ask = token_tracking_ask(native, recorder.score, recorder)
    async def worker(name):
        with recorder.contexto(metodo=name):
            with recorder.fase("phase_" + name):
                return await ask("system", name)
    async def run():
        nonlocal entered, finished
        entered, finished = asyncio.Event(), asyncio.Event()
        recorder.define_contexto(ronda=2)
        result = await asyncio.gather(worker("A"), worker("B"))
        assert recorder._contexto == {"ronda": 2} and recorder.fase_atual == "?"
        assert native.last_call is None  # Child metadata never enters the parent task.
        return result
    entered = finished = None
    assert asyncio.run(run()) == ["answer A", "" if second_error else "answer B"]
    rows = {e["metodo"]: e for e in map(json.loads, (tmp_path / "events.jsonl").read_text().splitlines())}
    assert rows["A"]["prompt_tokens"] == 10 and rows["A"]["fase"] == "phase_A"
    assert rows["B"]["prompt_tokens"] == 20 and rows["B"]["fase"] == "phase_B"
    assert rows["A"]["cortada"] and not rows["B"]["cortada"]
    assert all(row["ronda"] == 2 and row["usage_reported"] for row in rows.values())
    assert recorder.score.llm_calls == 2 and recorder.score.prompt_tokens == 30
    assert recorder.score.llm_erros == int(second_error)


def test_cancellation_clears_metadata_and_restores_context(tmp_path):
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    class Client:
        response_api = True
        async def aask_result(self, system, user):
            if user == "first":
                return ChatReply("code", 2, 1, "stop")
            raise asyncio.CancelledError()
    native = RubyAsk(Client())
    ask = token_tracking_ask(native, recorder.score, recorder)
    async def run():
        with recorder.contexto(metodo="outer"):
            with recorder.fase("outer"):
                await ask("s", "first")
                with pytest.raises(asyncio.CancelledError):
                    with recorder.contexto(metodo="cancelled"):
                        with recorder.fase("inner"):
                            await ask("s", "second")
                assert native.last_call is None
                assert recorder.fase_atual == "outer" and recorder._contexto == {"metodo": "outer"}
    asyncio.run(run())
    assert recorder.score.llm_calls == 1 and recorder.score.prompt_tokens == 2
    assert recorder.score.llm_interrupted_requests == 1
    events = list(map(json.loads, (tmp_path / "events.jsonl").read_text().splitlines()))
    assert events[-1]["tipo"] == "llm_interrupted" and events[-1]["cancelled"]
    assert events[-1]["metodo"] == "cancelled"


def test_response_api_contract_failure_does_not_fall_back_or_retry():
    class Client:
        response_api = True
        aask = Mock(side_effect=AssertionError("no legacy fallback"))
        async def aask_result(self, system, user):
            return {"text": "invalid contract"}
    with pytest.raises(TypeError, match="ChatReply"):
        asyncio.run(client_request(Client(), "s", "u"))


def test_legacy_client_uses_its_own_metadata_and_is_marked_legacy():
    class Client:
        last_call = {"prompt_tokens": 10, "completion_tokens": 2}
        async def aask(self, system, user):
            return "legacy code"
    text, detail = asyncio.run(client_request(Client(), "s", "u"))
    assert text == "legacy code" and detail["prompt_tokens"] == 10
    assert detail["metrics_source"] == "legacy_client_last_call"
    assert not detail["usage_reported"]


def fake_http_client(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    import httpx
    from openai import OpenAI
    from marta.gptapi import MyGPT
    client = MyGPT.__new__(MyGPT)
    client.model_type, client.temperature, client.max_tokens = "fixture:1b", 0.6, 16384
    client.reasoning_effort, client.top_p, client.presence_penalty = "high", 0.95, 0
    client.last_call = None
    captured = []
    def reply(request):
        captured.append(json.loads(request.content))
        return httpx.Response(200, json={"id": "fixture", "object": "chat.completion", "created": 0,
            "model": "fixture:1b", "choices": [{"index": 0, "finish_reason": "stop",
                "message": {"role": "assistant", "content": "final code", "reasoning": "not final content"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 4, "total_tokens": 14}})
    client.client = OpenAI(api_key="fixture", base_url="http://offline.invalid/v1", max_retries=0,
        http_client=httpx.Client(transport=httpx.MockTransport(reply)))
    return client, captured


def test_new_and_legacy_http_bodies_match_without_global_credit_from_new_api(tmp_path, monkeypatch):
    from marta.recorder import recoder
    client, captured = fake_http_client(tmp_path, monkeypatch)
    credit = Mock()
    monkeypatch.setattr(recoder.score, "add_tokens", credit)
    messages = [{"role": "system", "content": "s"}, {"role": "user", "content": "u"}]
    try:
        reply = client.chat_result(messages)
        assert reply == ChatReply("final code", 10, 4, "stop")
        assert client.last_call is None
        credit.assert_not_called()
        assert client.chat(messages) == "final code"
        credit.assert_called_once_with(10, 4)
        assert captured[0] == captured[1]
        assert captured[0]["reasoning_effort"] == "high" and captured[0]["max_tokens"] == 16384
    finally:
        client.client.close()


def test_async_response_api_uses_same_limiter_and_http_request(tmp_path, monkeypatch):
    client, captured = fake_http_client(tmp_path, monkeypatch)
    class Limiter:
        entered = 0
        async def __aenter__(self):
            self.entered += 1
        async def __aexit__(self, *args):
            pass
    client.limiter = Limiter()
    try:
        reply = asyncio.run(client.aask_result("s", "u"))
        assert reply.text == "final code" and client.limiter.entered == 1
        assert len(captured) == 1 and client.last_call is None
    finally:
        client.client.close()


def test_structured_error_is_local_and_does_not_credit_legacy_state(tmp_path, monkeypatch):
    client, _ = fake_http_client(tmp_path, monkeypatch)
    monkeypatch.setattr(client.client.chat.completions, "create", Mock(side_effect=RuntimeError("fixture failure")))
    try:
        reply = client.chat_result([])
        assert reply.text == "" and "fixture failure" in reply.error
        assert not reply.details()["usage_reported"] and client.last_call is None
    finally:
        client.client.close()


def test_native_tracking_consumes_reply_without_using_mutable_last_call():
    class Client:
        response_api = True
        async def aask_result(self, system, user):
            return ChatReply("code", 7, 2, "stop")
    native = RubyAsk(Client())
    recorder = RubyRecorder()
    async def run():
        assert await token_tracking_ask(native, recorder.score)("s", "u") == "code"
        assert native.last_call is None
    asyncio.run(run())
    assert recorder.score.prompt_tokens == 7 and recorder.score.llm_usage_unknown_calls == 0


def test_default_ruby_ask_selects_response_api_without_legacy_client_call(monkeypatch):
    from unittest.mock import AsyncMock
    from marta.ruby_backend.generate import _default_ask
    client = SimpleNamespace(response_api=True,
        aask_result=AsyncMock(return_value=ChatReply("native code", 11, 5, "stop")),
        aask=AsyncMock(side_effect=AssertionError("no legacy call")))
    monkeypatch.setitem(sys.modules, "marta.gptapi", SimpleNamespace(model=client))
    ask = _default_ask()
    recorder = RubyRecorder()
    assert isinstance(ask, RubyAsk) and ask.client is client
    assert asyncio.run(token_tracking_ask(ask, recorder.score)("s", "u")) == "native code"
    assert recorder.score.prompt_tokens == 11
    client.aask.assert_not_awaited()
    client.aask_result.assert_awaited_once_with("s", "u")
