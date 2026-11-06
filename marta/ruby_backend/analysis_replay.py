"""Explicit prefix recovery from an inactive, compatible analysis journal.

Never searches for a better answer or replays completed analyses. No model calls.
"""
from collections import deque
import fcntl
import hashlib
import json
from pathlib import Path

from .checkpoints import digest

ARCHIVE_POLICY = "analysis-journal-v2"
POLICY = "exact-analysis-prefix-v1"


class AnalysisRecoveryError(RuntimeError):
    pass


class AnalysisReplay:
    def __init__(self, source, expected):
        self.source = Path(source).resolve()
        try:
            with (self.source / "writer.lock").open("r") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                manifest = json.loads((self.source / "manifest.json").read_text())
                if (not isinstance(manifest, dict) or manifest.get("archive_policy") != ARCHIVE_POLICY
                        or manifest.get("status") not in ("failed", "interrupted", "running")
                        or manifest.get("use_cache") is not True):
                    raise AnalysisRecoveryError("Recovery requires an incomplete, cache-enabled v2 analysis archive")
                source_error = manifest.get("error")
                if isinstance(source_error, dict) and source_error.get("type") == "AnalysisRecoveryError":
                    raise AnalysisRecoveryError("A refused recovery is not a new recovery source")
                if any(key not in manifest or manifest[key] != value for key, value in expected.items()):
                    raise AnalysisRecoveryError("Analysis recovery inputs, order or configuration differ")
                path = self.source / "responses.jsonl"
                raw = path.read_bytes() if path.exists() else b""
        except BlockingIOError as error:
            raise AnalysisRecoveryError("Analysis recovery source is still owned by a writer") from error
        except (OSError, ValueError, TypeError) as error:
            raise AnalysisRecoveryError("Analysis recovery archive is unavailable or malformed") from error
        self.records = deque()
        failed = False
        for index, line in enumerate(raw.splitlines(keepends=True), 1):
            if not line.endswith(b"\n"):
                break  # A crash may leave only the final record incomplete.
            try:
                entry = json.loads(line)
                if (failed or not isinstance(entry, dict) or type(entry.get("sequence")) is not int
                        or entry["sequence"] != index
                        or not isinstance(entry.get("context"), dict)
                        or not isinstance(entry.get("request_sha256"), str)
                        or len(entry["request_sha256"]) != 64
                        or type(entry.get("response_accepted")) is not bool):
                    raise ValueError("invalid journal entry")
                accepted = entry.get("error") is None and isinstance(entry.get("response"), str) and bool(entry["response"].strip())
                if accepted != entry["response_accepted"]:
                    raise ValueError("inconsistent response status")
                if entry["response_accepted"]:
                    response = entry.get("response")
                    if (not isinstance(response, str) or not response.strip()
                            or entry.get("error") is not None
                            or entry.get("response_sha256") != digest(response)):
                        raise ValueError("invalid accepted response")
                    self.records.append(entry)
                else:
                    failed = True  # The failed request itself is never replayed.
            except (ValueError, TypeError, KeyError) as error:
                raise AnalysisRecoveryError(f"Malformed analysis journal at record {index}") from error
        upstream = manifest.get("recovery")
        if upstream is not None:
            if (not isinstance(upstream, dict) or type(upstream.get("eligible_prefix")) is not int
                    or upstream["eligible_prefix"] < 0):
                raise AnalysisRecoveryError("Malformed upstream recovery audit")
            inherited = sum(entry.get("replayed_from") is not None for entry in self.records)
            if inherited < upstream["eligible_prefix"]:
                raise AnalysisRecoveryError("Inherited prefix was not fully preserved; resume the original source archive")
        self.audit = {"policy": POLICY, "source": str(self.source),
                      "manifest_sha256": digest(manifest),
                      "journal_sha256": hashlib.sha256(raw).hexdigest(),
                      "eligible_prefix": len(self.records)}

    def take(self, system, user, recorder):
        if not self.records:
            return None
        entry = self.records[0]
        if (entry["request_sha256"] != digest([system, user])
                or entry.get("phase") != recorder.fase_atual
                or digest(entry["context"]) != digest(dict(recorder._contexto))):
            raise AnalysisRecoveryError("Analysis request differs from the saved prefix; recovery stopped")
        return self.records.popleft()

    def verify_consumed(self):
        if self.records:
            raise AnalysisRecoveryError("Analysis ended before consuming the saved request prefix")
