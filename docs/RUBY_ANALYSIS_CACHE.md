# Analysis provenance and evidence archives

Implemented on 2026-11-04 after project-root README context (`2b073ad4a`).
These are new cache/execution semantics, not migrations of frozen paper runs.

## Analysis validity

This delivery introduced `ANALYSIS_SCHEMA=6`; the later
[whole-prompt budget](RUBY_PROMPT_BUDGET.md) advances it to 7 and adds the effective
budget/counter to provenance. In addition to sources, analysis scope, exact definition
IDs, README snapshots, resolver and focused-code limits, the fingerprint now
includes an explicit analysis provenance object:

- SHA-256 of the analysis prompt-builder modules and their runtime string constants.
  Changes to a summary/requirement prompt invalidate old summaries without relying
  only on a manually incremented schema. Generation-only prompt constants are
  outside this analysis prompt set.
- Implementation hashes for analysis orchestration, source-context construction,
  the provenance policy and the configured LLM client implementation.
- Configured model name, available client name and caller-declared model digest.
- Available client parameters: temperature, output cap, reasoning effort, top-p,
  presence penalty and request timeout; relevant declared context/output settings.

The real default client is resolved before capturing configuration, including
its existing dotenv behavior. No inference or model download is needed to inspect
these settings. Injected callbacks do not initialize that default client. Client
wrappers can expose their actual client through `.client`; bound client methods
also expose their configuration. The existing matching loaded global client is
used when no explicit client is available. Opaque callbacks must declare their
configuration rather than assume that arbitrary behavior can be inferred.

API keys and endpoint URLs are not persisted in this provenance. A rotating local
server port does not invalidate analysis. Missing client fields remain unknown;
they are not silently asserted to be a particular model's effective defaults.
A missing weight digest is recorded as `unavailable`. `MARTA_MODEL_DIGEST`, or a
client's `model_digest`, supplies a declaration, not automatic weight attestation.
The XRepoTest adapter passes along its existing model-digest argument; its outer
cluster/model manifest still owns verification of that installed model.

Before publishing results, analysis checks that captured client/prompt provenance
and production-source hashes have not changed during execution. A detected change
fails with evidence retained and no mixed-input cache publication. README bodies
retain the separate immutable snapshot behavior from the preceding delivery.

## Reusable cache versus archive

The reusable bundle path remains
`<output>/.marta_ruby_cache/analysis_<model>[...].full_context.json`.
Every analysis invocation independently creates:

```text
<output>/run_results/analysis_runs/analysis_<unique>/
    manifest.json
    bundle.json          # only once the analysis has a complete result
    responses.jsonl      # present when logical requests were made
```

`last_analysis_archive` exposes the directory on the project object, and the
recorder emits an `analysis_archive` event on completion. The existing ignored
`run_results` directory contains these generated artifacts without mixing them
with reusable cache.

| Invocation | Reuse | Reusable cache | Independent evidence |
|---|---|---|---|
| Valid cache hit | Apply the compatible complete bundle | Preserve it | New complete archive, `cache_hit=true`, zero new requests |
| Cache enabled, miss | Run analysis | Publish the new complete bundle atomically | Full bundle, provenance and logical responses |
| `use_cache=False` / CLI `--no_cache` | Recompute, including source-only summaries even with an explicit reference | Neither read nor replace the previous cache | New complete bundle and responses |
| Failure or cancellation | Stop; do not buy extra attempts | No incomplete analysis replaces a valid bundle | Failure/interruption manifest and available responses |

The no-cache result does not become the next reusable result automatically: an
ordinary later call may still reuse the earlier valid cache. Independent model
trials should use independent output directories. Archives are never consulted
as a fallback cache. This distinction prevents an archival feature from silently
repeating or selecting better scientific outcomes.

`responses.jsonl` retains complete returned text, a hash of the system/user
request, phase/method context and errors. It does not duplicate full prompt/source
bodies. These are logical calls after any supplied wrapper; existing XRepoTest
physical-attempt telemetry/retry accounting remains authoritative and is not
counted a second time. External wrappers may have their own checkpoint semantics;
core `use_cache=False` cannot bypass an opaque callback's internal implementation.

Manifest states are `running`, `complete`, `failed` and `interrupted`. Catchable
failures preserve the response history and final error; forced process termination
can leave `running` and a partial final JSONL line. The final request count is
written when the manifest is finalized. A staging bundle may exist if later I/O
fails, so the completion manifest, not file existence alone, certifies completion.
Archives add evidence, not per-request automatic recovery or model retries.

## Embedding caches

Document/class vector keys and XRepoTest query-vector keys now incorporate the
same configured embedding provenance: model/path, embedding and retrieval code,
selected local tokenizer/configuration file hashes, and optional declarations
`MARTA_EMBEDDING_DIGEST` and `MARTA_EMBEDDING_RECIPE`. This avoids reusing vectors
computed with a changed implementation or declared custom recipe. Query-cache
mismatches are explicitly rejected; normal index validity rejects old vector keys.

This metadata inspection does not import Transformers or download/load a model.
Large weight files are not hashed, and undeclared custom callback semantics cannot
be inferred. Local configuration hashes and model tags alone do not certify that
weights are immutable. Pin the actual provider/weights externally when that claim
is required, and declare a custom recipe when injecting embedding callbacks.

The vector identity uses the fingerprint actually accepted by the last completed
analysis rather than reconstructing a different analysis recipe after the fact.
The XRepoTest registered-analysis reuse path retains the same key construction and
continues to verify its reference manifests. Original references remain read-only.
Frozen experiments must keep their original implementation/manifests; old runs
are not relabelled as executions of this policy or silently upgraded.

## Evidence and remaining work

Regressions exercise cache reuse without new model calls, changed prompts without
schema edits, effective parameter/digest changes, default-client initialization,
full no-cache archives, preservation of old cache, source-only reference bypass,
failed/cancelled analyses, empty pools, mid-analysis mutations, embedding metadata
changes, query-key mismatches and omission of API credentials from provenance.
Existing real Chroma/NumPy reference-reuse and generation tests also run offline.

The synthesis algorithm, generation budgets and external evaluation formulas do
not change. Automatic request-level recovery and concurrent client/recorder isolation remain
separate work. The later [whole-prompt budget](RUBY_PROMPT_BUDGET.md) now supplies
the budget, with its documented counting limitations. Quality improvement is not inferred
from these engineering regression checks.
