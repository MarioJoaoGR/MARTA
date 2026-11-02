"""One unscored original OpenAI request on a verified CPU runner with 8 threads."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

from deucalion.verify_ollama_cpu import verify, confirm_threads
from deucalion.xrepotest_cpu_threads_probe import query, recover
from deucalion.xrepotest_official_generate import atomic, PARAMETERS


def original_body(http_source, sdk_source):
    recorded = recover(sdk_source)
    expected = {key: value for key, value in recorded.items() if key not in ("timeout", "extra_body")}
    expected.update(recorded["extra_body"])
    with http_source.open() as source:
        for line in source:
            event = json.loads(line)
            if event.get("task_id") == 0:
                if event["body"] != expected:
                    raise ValueError("Original HTTP body and SDK request differ")
                return event["body"]
    raise ValueError("Original task 0 HTTP body not found")


def run(host, http_source, sdk_source, output, server_log):
    body = original_body(http_source, sdk_source)
    if output.exists():
        raise ValueError("Diagnostic output already exists")
    proof = verify(host, PARAMETERS["model"], 32768,
                   lambda path, payload=None: query(host, path, payload), 8, server_log)
    output.mkdir(parents=True)
    atomic(output / "cpu_proof.json", proof)
    atomic(output / "request.json", body)
    report = {"diagnostic_only": True, "included_in_benchmark": False, "task_id": 0,
              "cpu_threads": 8, "request_timeout": 1800,
              "http_body_sha256": hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest(),
              "transport": "original non-streaming OpenAI HTTP body; one attempt, no SDK retries"}
    atomic(output / "report.json", report)
    print("CPU request validation: 8 threads; original OpenAI body, thinking on, at most 1800s; no scores", flush=True)
    started = time.monotonic()
    with (output / "curl.log").open("w") as err:
        completed = subprocess.run(["curl", "--silent", "--show-error", "--max-time", "1800",
            "--header", "Content-Type: application/json", "--data-binary", "@-",
            "--output", str(output / "response.json"), "--write-out", "%{http_code}",
            host + "/v1/chat/completions"], input=json.dumps(body).encode(),
            stdout=subprocess.PIPE, stderr=err, timeout=1830)
    report.update(seconds=round(time.monotonic() - started, 3), curl_exit=completed.returncode,
                  http_status=completed.stdout.decode(errors="replace"))
    response_path = output / "response.json"
    try:
        response = json.loads(response_path.read_text())
    except (ValueError, OSError):
        response = {}
    choice = (response.get("choices") or [{}])[0]
    message = choice.get("message", {})
    report.update(finish_reason=choice.get("finish_reason"), usage=response.get("usage"),
                  answer_characters=len(message.get("content") or ""),
                  thinking_characters=len(message.get("reasoning") or message.get("reasoning_content") or ""))
    report["usable_response"] = (completed.returncode == 0 and report["http_status"] == "200"
                                 and bool((message.get("content") or "").strip())
                                 and choice.get("finish_reason") == "stop")
    report["confirmed_cpu_threads_after_request"] = confirm_threads(server_log, 8)
    atomic(output / "report.json", report)
    print(json.dumps(report, indent=2), flush=True)
    print("CPU request diagnostic complete; benchmark unchanged: " + str(output / "report.json"), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("http-source", "sdk-source", "output", "server-log"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--host", required=True)
    a = p.parse_args()
    run(a.host, a.http_source, a.sdk_source, a.output, a.server_log)


if __name__ == "__main__":
    main()
