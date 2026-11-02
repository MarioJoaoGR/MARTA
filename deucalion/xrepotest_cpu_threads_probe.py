"""CPU throughput diagnostic only: no task checkpoint, score or benchmark export."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from deucalion.xrepotest_official_generate import MODEL_DIGEST, PARAMETERS, atomic


def recover(path):
    with path.open() as source:
        for line in source:
            event = json.loads(line)
            if event.get("task_id") == 0:
                request = event["request"]
                for key in ("model", "temperature", "top_p", "presence_penalty", "max_tokens"):
                    if request.get(key) != PARAMETERS[key]:
                        raise ValueError("Recorded request differs: " + key)
                if request.get("timeout") != 1800 or request.get("extra_body") != {"reasoning_effort": "high"}:
                    raise ValueError("Recorded thinking/timeout differs")
                if not request.get("messages"):
                    raise ValueError("Missing original messages")
                return request
    raise ValueError("Original task 0 request not found")


def payload(request, threads):
    if threads not in (8, 16, 32):
        raise ValueError("Only the predeclared CPU thread counts are allowed")
    return {"model": request["model"], "messages": request["messages"],
            "think": "high", "stream": True, "keep_alive": -1,
            "options": {"num_ctx": 32768, "num_predict": request["max_tokens"],
                        "temperature": request["temperature"], "top_p": request["top_p"],
                        "presence_penalty": request["presence_penalty"],
                        "num_thread": threads, "num_gpu": 0}}


def stream_summary(path):
    result = {"done": False, "thinking_characters": 0, "answer_characters": 0}
    for line in path.read_text().splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("error"):
            result["error"] = event["error"]
        message = event.get("message", {})
        result["thinking_characters"] += len(message.get("thinking") or "")
        result["answer_characters"] += len(message.get("content") or "")
        if event.get("done"):
            result["done"] = True
            for key in ("done_reason", "eval_count", "eval_duration", "prompt_eval_count", "prompt_eval_duration"):
                result[key] = event.get(key)
    if result.get("eval_duration"):
        result["tokens_per_second"] = result["eval_count"] * 1e9 / result["eval_duration"]
    # Streaming chunks/characters are deliberately not interpreted as token counts.
    return result


def query(host, path, body=None):
    request = Request(host + path, data=json.dumps(body).encode() if body is not None else None,
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=600) as response:
        return json.load(response)


def run(host, source, output, server_log):
    url = urlparse(host)
    if url.scheme != "http" or url.hostname != "127.0.0.1" or url.path:
        raise ValueError("Only the private local Ollama server is allowed")
    original = recover(source)
    if output.exists():
        raise ValueError("Diagnostic directory already exists; never overwrite it")
    output.mkdir(parents=True)
    if query(host, "/api/version").get("version") != "0.30.7":
        raise ValueError("Wrong Ollama version")
    tags = query(host, "/api/tags").get("models", [])
    if not any(m.get("name") == PARAMETERS["model"] and m.get("digest") == MODEL_DIGEST for m in tags):
        raise ValueError("Pinned weights not present; no downloads allowed")
    report = {"diagnostic_only": True, "included_in_benchmark": False,
              "original_request_sha256": hashlib.sha256(json.dumps(original, sort_keys=True).encode()).hexdigest(),
              "sampling_parameters": PARAMETERS, "context_length": 32768,
              "measurement_seconds_per_case": 180,
              "transport": "native streaming chat, solely for CPU runtime diagnostics",
              "cases": []}
    atomic(output / "report.json", report)
    for threads in (8, 16, 32):
        case = output / str(threads)
        case.mkdir()
        body = payload(original, threads)
        atomic(case / "request.json", body)
        offset = server_log.stat().st_size
        load = query(host, "/api/generate", {"model": body["model"], "prompt": "", "stream": False,
                     "keep_alive": -1, "options": {"num_ctx": 32768, "num_thread": threads, "num_gpu": 0}})
        if load.get("done_reason") != "load" or load.get("eval_count", 0) or load.get("response"):
            raise ValueError("Expected a load-only call")
        loaded = [m for m in query(host, "/api/ps").get("models", []) if m.get("name") == body["model"]]
        if (len(loaded) != 1 or loaded[0].get("size_vram") != 0
                or loaded[0].get("digest") != MODEL_DIGEST or loaded[0].get("context_length") != 32768):
            raise ValueError("Runner is not the pinned CPU-only model")
        print("CPU diagnostic: {} threads; at most 180s of streaming; no scores".format(threads), flush=True)
        started = time.monotonic()
        with (case / "stream.jsonl").open("w") as out, (case / "curl.log").open("w") as err:
            completed = subprocess.run(["curl", "--silent", "--show-error", "--fail", "--no-buffer",
                "--max-time", "180", "--header", "Content-Type: application/json",
                "--data-binary", "@-", host + "/api/chat"], input=json.dumps(body).encode(),
                stdout=out, stderr=err, timeout=210)
        elapsed = time.monotonic() - started
        time.sleep(2)  # Allow the cancelled request to release its slot and print timing.
        with server_log.open("rb") as log:
            log.seek(offset)
            excerpt = log.read().decode(errors="replace")
        (case / "runner.log").write_text(excerpt)
        actual_threads = re.findall(r"system_info: n_threads =\s*(\d+)", excerpt)
        if not actual_threads or int(actual_threads[-1]) != threads:
            raise ValueError("Cannot confirm explicit runner threads in log")
        rates = [float(x) for x in re.findall(r"tg =\s*([0-9.]+) t/s", excerpt)]
        result = {"threads": threads, "confirmed_runner_threads": int(actual_threads[-1]),
                  "seconds": round(elapsed, 3), "curl_exit": completed.returncode,
                  "stream": stream_summary(case / "stream.jsonl"), "runner_reported_tokens_per_second": rates[-5:]}
        # Exit 28 is the diagnostic time boundary, not a benchmark failure or a retry.
        report["cases"].append(result)
        atomic(output / "report.json", report)
        print(json.dumps(result), flush=True)
        if completed.returncode not in (0, 28):
            raise RuntimeError("CPU diagnostic HTTP request failed; inspect curl.log")
    print("CPU diagnostic complete; original benchmark unchanged: " + str(output / "report.json"), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--host", required=True)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--server-log", type=Path, required=True)
    a = p.parse_args()
    run(a.host, a.source, a.output, a.server_log)


if __name__ == "__main__":
    main()
