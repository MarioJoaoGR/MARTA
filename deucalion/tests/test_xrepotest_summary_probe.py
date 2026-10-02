import asyncio
import io
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from deucalion import xrepotest_summary_probe as probe
from benchmark.xrepotest.protocol import digest


def capture():
    return {"original_manifest": {"model": "qwen3.6:35b", "temperature": 0.6,
             "top_p": 0.95, "presence_penalty": 0, "max_tokens": 16384,
             "runtime_env": {"OLLAMA_CTX": "32768"}},
            "messages": [{"role": "system", "content": "unchanged system"},
                         {"role": "user", "content": "unchanged source"}]}


def test_probe_changes_only_budgets_and_transport_preserving_prompt_and_thinking():
    original = capture()
    body = probe.payload(original, 65536, 32768)
    assert body["messages"] is original["messages"]
    assert body["model"] == "qwen3.6:35b"
    assert (body["temperature"], body["top_p"], body["presence_penalty"]) == (0.6, 0.95, 0)
    assert body["reasoning_effort"] == "high" and body["max_tokens"] == 32768
    assert original["original_manifest"]["max_tokens"] == 16384


@pytest.mark.parametrize("context,tokens", [(32768,32768),(65536,16384),(65536,65536)])
def test_inadequate_budget_is_rejected(context, tokens):
    with pytest.raises(ValueError, match="larger budgets"):
        probe.payload(capture(), context, tokens)


def test_readme_overview_is_exact_cached_prompt_without_writes(tmp_path):
    key = digest(["what_todo_raiz", "system", "readme"])
    p = tmp_path / (key + ".json")
    p.write_text(json.dumps({"response": "original overview"}))
    before = p.read_bytes()
    ask = probe.cached_overview_ask(tmp_path, "what_todo_raiz")
    assert asyncio.run(ask("system", "readme")) == "original overview"
    assert p.read_bytes() == before
    with pytest.raises(ValueError, match="missing"):
        asyncio.run(ask("system", "different README"))
    assert len(list(tmp_path.iterdir())) == 1


def sse(chunks, done=True):
    text = "".join("data: " + json.dumps(c) + "\n\n" for c in chunks)
    return io.BytesIO((text + ("data: [DONE]\n\n" if done else "")).encode())


def test_stream_preserves_reasoning_final_answer_and_server_usage(tmp_path, monkeypatch):
    requests = []
    def reply(request, timeout):
        requests.append((request, timeout))
        return sse([
            {"choices": [{"delta": {"reasoning": "first thought "}}]},
            {"choices": [{"delta": {"reasoning_content": "second thought"}}]},
            {"choices": [{"delta": {"content": "final summary"}, "finish_reason": "stop"}]},
            {"choices": [], "usage": {"prompt_tokens": 374, "completion_tokens": 2000}},
        ])
    monkeypatch.setattr(probe, "urlopen", reply)
    result = probe.stream_request("http://localhost:123", probe.payload(capture(),65536,32768),tmp_path,1800)
    assert len(requests) == 1 and requests[0][1] == 1800
    assert (tmp_path / "thinking.txt").read_text() == "first thought second thought"
    assert (tmp_path / "answer.txt").read_text() == "final summary"
    assert result["usable_response"] and result["usage"]["completion_tokens"] == 2000
    assert "reasoning_tokens" not in result
    with pytest.raises(FileExistsError):
        probe.stream_request("http://localhost:123",{},tmp_path,1800)
    assert len(requests) == 1


def test_empty_length_is_a_diagnostic_failure_not_usable_summary(tmp_path, monkeypatch):
    monkeypatch.setattr(probe,"urlopen",lambda *a,**kw:sse([
        {"choices":[{"delta":{"reasoning":"repeated thinking"},"finish_reason":"length"}],
         "usage":{"prompt_tokens":374,"completion_tokens":32768}}]))
    result=probe.stream_request("http://localhost:123",{},tmp_path,1800)
    assert not result["usable_response"] and result["finish_reason"] == "length"
    assert (tmp_path / "thinking.txt").read_text() == "repeated thinking"
    assert (tmp_path / "answer.txt").read_text() == ""


def test_interrupted_stream_retains_partial_thinking_without_success(tmp_path, monkeypatch):
    monkeypatch.setattr(probe,"urlopen",lambda *a,**kw:sse([
        {"choices":[{"delta":{"reasoning":"partial thought"}}]}],done=False))
    with pytest.raises(RuntimeError,match="Incomplete stream"):
        probe.stream_request("http://localhost:123",{},tmp_path,1800)
    assert (tmp_path / "thinking.txt").read_text() == "partial thought"
    assert not (tmp_path / "result.json").exists()


def test_recover_uses_original_readme_and_method_without_model_or_checkpoint_write(tmp_path,monkeypatch):
    from benchmark.xrepotest import backend, runtime
    from marta.ruby_backend import readme
    generation=tmp_path / "generation"
    calls=generation / "analysis/repo/calls"
    calls.mkdir(parents=True)
    source=tmp_path / "repos/repo"
    (source / "lib").mkdir(parents=True)
    focal=source / "lib/a.rb"
    focal.write_text("def foo; end")
    (source / "README.md").write_text("Original README")
    original={**capture()["original_manifest"],"marta_code":"code","thinking":"on","no_graph":False,
              "source_hashes":{"repo":"source"},"runtime_hashes":{"repo":"runtime"}}
    (generation / "experiment.json").write_text(json.dumps(original))
    failures=[{"tipo":"llm","fase":"what_todo_raiz","metodo":"A#foo","finish_reason":"length",
               "completion_tokens":16384,"caracteres_resposta":0,"prompt_tokens":374}]*3
    (calls.parent / "events.jsonl").write_text("".join(json.dumps(e)+"\n" for e in failures))
    async def save_overview(system,user):
        (calls / (digest(["what_todo_raiz",system,user])+".json")).write_text(
            json.dumps({"response":"Cached original overview"}))
    asyncio.run(readme.analyze_readme(save_overview,"Original README"))
    monkeypatch.setattr(probe,"code_fingerprint",lambda:"code")
    monkeypatch.setattr(probe,"load_tasks",lambda _: [{"file_path":"repo/lib/a.rb"}])
    monkeypatch.setattr(probe,"selectors",lambda _: [])
    monkeypatch.setattr(probe,"source_inventory",lambda *a:{"source_digest":"source","runtime_digest":"runtime",
                        "code_files":["lib/a.rb"],"load_paths":["lib"]})
    target=SimpleNamespace(method=SimpleNamespace(qualified_name="A#foo"),file_path=str(focal),
                           context_source="EXACT METHOD CONTEXT",analysis_id="identity")
    class Project:
        def __init__(self,**kw): self.abs_source=kw["root_dir"]; self.analysis_targets=[target]
        def discover(self): return self
    monkeypatch.setattr(backend,"XRepoProject",Project)
    monkeypatch.setattr(runtime,"project_environment",lambda *a:__import__('contextlib').nullcontext())
    before={str(p):p.read_bytes() for p in generation.rglob('*') if p.is_file()}
    result=asyncio.run(probe.recover(generation,tmp_path/'repos',Path('unused'),'repo','A#foo',tmp_path/'work'))
    assert "Cached original overview" in result["messages"][1]["content"]
    assert "EXACT METHOD CONTEXT" in result["messages"][1]["content"]
    assert result["original_prompt_tokens"] == 374
    assert before == {str(p):p.read_bytes() for p in generation.rglob('*') if p.is_file()}
    with pytest.raises(ValueError,match="exactly one"):
        asyncio.run(probe.recover(generation,tmp_path/'repos',Path('unused'),'repo','missing',tmp_path/'work'))


def test_probe_wrapper_has_no_chaining_and_mounts_original_generation_read_only():
    text=(Path(__file__).resolve().parents[1]/'run_xrepotest_summary_probe_gpu.sh').read_text()
    assert '#SBATCH --time=00:20:00' in text
    assert '--bind "$RUN/generation:$GEN:ro"' in text
    assert 'trap - USR1' in text and 'sbatch' not in text
    assert text.index('--capture-only') < text.index('ollama serve')
    assert 'benchmark.xrepotest.run ' not in text
