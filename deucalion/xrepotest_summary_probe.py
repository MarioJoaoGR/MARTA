"""One isolated budget diagnostic; never update benchmark results/checkpoints.

Recover the unchanged what_todo request from pinned sources and the original
README overview checkpoint. Stream one larger-budget request to separate files
so an interrupted diagnostic retains both thinking and final content.
"""
import argparse
import asyncio
import json
import os
from pathlib import Path
import tempfile
import time
from urllib.request import Request, urlopen

from benchmark.xrepotest.protocol import (
    atomic_json, code_fingerprint, digest, load_tasks, selectors, source_inventory,
)


def cached_overview_ask(calls, phase):
    async def ask(system, user):
        path = calls / (digest([phase, system, user]) + ".json")
        if not path.is_file():
            raise ValueError("Original README overview checkpoint missing: " + str(path))
        text = json.loads(path.read_text()).get("response")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Original README overview checkpoint is empty")
        return text
    return ask


async def recover(generation, repos, dataset, project, method, work):
    manifest = json.loads((generation / "experiment.json").read_text())
    if manifest.get("marta_code") != code_fingerprint():
        raise ValueError("Generation code differs from the original experiment")
    if manifest.get("thinking") != "on" or manifest.get("no_graph") is not False:
        raise ValueError("Expected the original thinking-on, graph-on run")
    for key, value in manifest.get("runtime_env", {}).items():
        if value:
            os.environ[key] = value
        else:
            os.environ.pop(key, None)
    os.environ["MODEL"] = manifest["model"]
    from benchmark.xrepotest.backend import XRepoBackend, XRepoProject
    from benchmark.xrepotest.runtime import project_environment
    from marta.ruby_backend import readme

    source = repos / project
    tasks = [t for t in load_tasks(dataset) if t["file_path"].split("/", 1)[0] == project]
    if not tasks:
        raise ValueError("Project has no official tasks")
    inventory = source_inventory(source, tasks)
    for field in ("source", "runtime"):
        if inventory[field + "_digest"] != manifest[field + "_hashes"][project]:
            raise ValueError("Pinned project " + field + " differs from the experiment")
    with project_environment(source, project):
        proj = XRepoProject(root_dir=str(source), source_dir=".", output_root=str(work),
                            code_files=inventory["code_files"], load_paths=inventory["load_paths"],
                            target_selectors=selectors(tasks), backend=XRepoBackend()).discover()
    matches = [t for t in proj.analysis_targets if t.method.qualified_name == method]
    if len(matches) != 1:
        raise ValueError("Expected exactly one production definition for " + method)
    target = matches[0]
    phase = "what_todo_raiz"
    events = [json.loads(line) for line in
              (generation / "analysis" / project / "events.jsonl").read_text().splitlines()]
    failures = [e for e in events if e.get("tipo") == "llm" and e.get("fase") == phase
                and e.get("metodo") == method]
    last = failures[-3:]
    if len(last) != 3 or not all(e.get("finish_reason") == "length" and
                               e.get("completion_tokens") == manifest["max_tokens"] and
                               e.get("caracteres_resposta") == 0 for e in last):
        raise ValueError("Expected three original empty output-limit responses")
    counts = {e["prompt_tokens"] for e in last}
    if len(counts) != 1:
        raise ValueError("Original attempts have different input token counts")
    calls = generation / "analysis" / project / "calls"
    overview = await readme.ReadmeOverviewCache(proj.abs_source).overview_for(
        cached_overview_ask(calls, phase), target.file_path)
    captured = []
    async def capture(system, user):
        captured.append((system, user))
        return "diagnostic capture only"
    await readme.analyze_what_todo(capture, target.context_source, overview)
    system, user = captured[0]
    key = digest([phase, system, user])
    if (calls / (key + ".json")).exists():
        raise ValueError("The request already has a valid checkpoint; diagnostic refused")
    return {"original_manifest": manifest, "original_manifest_digest": digest(manifest),
            "phase": phase, "project": project, "method": method,
            "analysis_id": target.analysis_id, "prompt_key": key,
            "original_prompt_tokens": counts.pop(), "original_failures": last,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}]}


def payload(capture, context, max_tokens):
    original = capture["original_manifest"]
    old_context = int(original["runtime_env"]["OLLAMA_CTX"])
    if max_tokens <= original["max_tokens"] or context <= old_context or max_tokens >= context:
        raise ValueError("Diagnostic requires larger budgets and output smaller than context")
    body = {"model": original["model"], "messages": capture["messages"],
            "temperature": original["temperature"], "reasoning_effort": "high",
            "max_tokens": max_tokens, "stream": True,
            "stream_options": {"include_usage": True}}
    for key in ("top_p", "presence_penalty"):
        if original.get(key) is not None:
            body[key] = original[key]
    return body


def stream_request(host, body, output, timeout):
    request = Request(host.rstrip("/") + "/v1/chat/completions",
                      data=json.dumps(body).encode(),
                      headers={"Content-Type": "application/json", "Authorization": "Bearer ollama"})
    start = time.monotonic()
    usage, finish, done = None, None, False
    thinking_chars = answer_chars = 0
    with (output / "thinking.txt").open("x") as thinking, \
            (output / "answer.txt").open("x") as answer, \
            (output / "stream.jsonl").open("x") as log, \
            urlopen(request, timeout=timeout) as response:
        for line in response:
            text = line.decode("utf-8").strip()
            if not text.startswith("data:"):
                continue
            data = text[5:].strip()
            if data == "[DONE]":
                done = True
                break
            chunk = json.loads(data)
            log.write(json.dumps(chunk, ensure_ascii=False) + "\n")
            log.flush()
            if chunk.get("error"):
                raise RuntimeError(str(chunk["error"]))
            if chunk.get("usage") is not None:
                usage = chunk["usage"]
            for choice in chunk.get("choices", []):
                delta = choice.get("delta", {})
                thought = delta.get("reasoning") or delta.get("reasoning_content") or ""
                content = delta.get("content") or ""
                thinking.write(thought)
                answer.write(content)
                thinking.flush()
                answer.flush()
                thinking_chars += len(thought)
                answer_chars += len(content)
                finish = choice.get("finish_reason") or finish
    if not done or not finish or usage is None:
        raise RuntimeError("Incomplete stream or missing server usage; partial files retained")
    return {"seconds": round(time.monotonic() - start, 3), "finish_reason": finish,
            "usage": usage, "thinking_characters": thinking_chars,
            "answer_characters": answer_chars,
            "usable_response": finish == "stop" and bool((output / "answer.txt").read_text().strip()),
            "note": "Characters are measured separately; no unreported reasoning-token split is inferred."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    parser.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    parser.add_argument("--project", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--capture-only", action="store_true")
    parser.add_argument("--host")
    parser.add_argument("--model-digest")
    parser.add_argument("--context", type=int, default=65536)
    parser.add_argument("--max-tokens", type=int, default=32768)
    args = parser.parse_args()
    generation, output = args.generation.resolve(), args.output.resolve()
    for source in (generation, args.repos.resolve()):
        if source == output or source in output.parents or output in source.parents:
            parser.error("Diagnostic and original trees must be separate")
    if args.capture_only:
        if args.host:
            parser.error("Capture mode never connects to a model")
        output.mkdir(parents=True, exist_ok=False)
        with tempfile.TemporaryDirectory(prefix="xrepo-summary-probe-") as work:
            capture = asyncio.run(recover(generation, args.repos, args.dataset,
                                          args.project, args.method, Path(work)))
        body = payload(capture, args.context, args.max_tokens)
        atomic_json(output / "request.json", {**capture, "request": body, "context": args.context,
                    "benchmark_write_policy": "No results or checkpoints are imported from this diagnostic"})
        print("Exact request recovered; original input {} tokens; diagnostic output {}, context {}".format(
            capture["original_prompt_tokens"], args.max_tokens, args.context), flush=True)
        return
    capture = json.loads((output / "request.json").read_text())
    if capture["request"] != payload(capture, capture["context"], capture["request"]["max_tokens"]):
        parser.error("Captured request was modified")
    if not args.host or args.model_digest != capture["original_manifest"]["model_digest"]:
        parser.error("An installed model with the original digest is required")
    if int(os.getenv("OLLAMA_CTX", "0")) != capture["context"]:
        parser.error("Server context differs from the diagnostic request")
    if digest(json.loads((generation / "experiment.json").read_text())) != capture["original_manifest_digest"]:
        parser.error("Original experiment changed after request capture")
    for name in ("thinking.txt", "answer.txt", "stream.jsonl", "result.json"):
        if (output / name).exists():
            parser.error("Diagnostic already attempted; automatic repeat refused")
    result = stream_request(args.host, capture["request"], output,
                            capture["original_manifest"]["request_timeout"])
    result["prompt_tokens_match_original"] = (
        result["usage"].get("prompt_tokens") == capture["original_prompt_tokens"])
    atomic_json(output / "result.json", result)
    print(json.dumps(result, indent=2), flush=True)
    print("Original benchmark unchanged. Diagnostic output: " + str(output), flush=True)


if __name__ == "__main__":
    main()
