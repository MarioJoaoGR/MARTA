# Nonempty analysis and validated round checkpoints

Implemented on 2026-11-03 after the plan/source and repair-context deliveries.
This is a new execution policy. Frozen paper runs, results and external metric
formulas are not migrated or rerun by this change.

## Analysis must make progress

Every actual analysis response must be a nonempty string: source summaries,
callee enrichment, README overview, root/propagated/fallback intent, final merge
and class summaries. Whitespace, `None` and nontext values raise
`AnalysisResponseError` immediately, with phase/method context in the recorder.
An absent README still means no overview request; it is not an error.

Previously an empty propagated intent left a method unresolved while setting the
loop's `changed` flag, so the same request could repeat indefinitely. A successful
propagation now necessarily fills that intent. Cycles retain the existing README
fallback, subject to the same response contract. We keep LLM synthesis and the
first-pass snapshot used for callee enrichment.

This guard adds no retry, token-budget increase or synthetic summary. Existing
XRepoTest exact-request checkpoints still own their established truncation retries;
the core guard does not count or repeat their physical calls again. Ordinary CLI
analysis still has no per-request recovery checkpoint: after a failed fresh
analysis, successful earlier requests may need repeating. That remains separate
from generation round recovery.

`ANALYSIS_SCHEMA` is 4. Empty required fields in a cached bundle are rejected.
Complete bundles and generated Ruby files are written to a same-directory temporary
file, flushed and replaced atomically. A failed analysis never replaces a prior
complete bundle; `use_cache=False` still does not save a new bundle. Changing that
option's archival semantics remains a separate task.

Telemetry only reads already-loaded Python client modules. It does not initialize
the global client or load `.env` as a side effect of an injected/offline request.

## What a generation checkpoint certifies

`generate_rounds` owns `<output>/.marta_generation/rounds.json`. After a whole round
has passed the accumulated-suite gate (including any existing conservative
rollback), it atomically records the round's outcomes and SHA-256 hashes of all
retained specs. A completed failed attempt is recorded too, including rounds that
leave no tests. An advisory POSIX writer lock covers generation and revalidation
across awaits; a second MARTA writer fails before modifying round output.

A resumed call first verifies those hashes and re-executes the retained suite in
the current Ruby environment. Previously completed rounds, including terminal
failures, are skipped without another model attempt. Further rounds may be added;
requesting fewer rounds than the completed checkpoint is rejected. Return values
continue to contain newly generated outcomes only; historical outcomes are in the
checkpoint. Resume validation costs Ruby execution time, not model tokens.

The recipe binds the supplied production files and library-loading files,
Gemfiles/lockfiles/gemspecs, selected definition/task identities, analyzed context,
class summaries, loading context, backend/retrieval kind, effective attempt budget,
ablation flags, declared model/client parameters, relevant runtime settings and
implementation hashes. Dependency discovery prunes installed gems and output
archives. A rotating local server port is not a generation-policy change.

This is a conservative compatibility check, not a model-weight attestation or
complete environment image. Custom injected clients must keep their declared
configuration stable; undeclared behavior changes cannot be inferred from a
callback. Ordinary CLI model tags are not immutable digests, and custom embedding
providers/index provenance still need their separate cache manifest. Frozen XRepoTest
experiments additionally retain their stronger outer model/image/code manifests.

## Interrupted, legacy and incompatible output

- Ruby files without a compatible completed-round checkpoint are archived under
  `<output>/rejected_specs/resume_*/`, with a reason file. They cannot enter coverage
  as accepted tests just because they exist. The previous checkpoint is preserved
  there too when the recipe is incompatible or malformed.
- On an interrupted later round, completed earlier rounds survive. Only the files
  outside that last committed snapshot are archived; the interrupted round restarts.
  This boundary is a round, not an individual method. Already attempted methods in
  an uncommitted multi-method round can therefore be repeated, with their old files
  retained as evidence. Per-method recovery is future work.
- A hash change or disappearance of a previously certified spec stops with
  `ResumeValidationError`; failure in the current test environment stops with
  `SuiteValidationError`. Neither case buys fresh attempts to improve an old result.
  Investigate the preserved output or choose a new output directory explicitly.
- A changed source/configuration archives incompatible output and starts a fresh
  compatible ledger. Use a new `output_root` for independent experiments; keep the
  original code and directories for frozen paper results.
- Colliding ordinary spec paths are detected before round-generation requests.
  Exact task selectors already provide distinct task paths. Automatic renaming of
  all legacy spec identities remains separate work.

The explicit paired first-round ablation contract remains supported, including
its certified no-spec seed. The adapter certifies that external seed; the core
then runs its accumulated-suite gate and records the imported round. The outer
XRepoTest adapter continues to archive/restart an interrupted task as a whole.

`generate_all` remains an unconditional one-round helper, with atomic spec writes;
it does not claim checkpoint recovery. The normal CLI uses `generate_rounds`.
External evaluators and mutation-score formulas are unchanged.

## Verification

Offline regressions cover invalid responses in every analysis phase, bounded
propagation, cycles, corrupt bundles, preservation after a failed atomic replace,
legacy empty/pending/failing specs, successful and failed resume, configuration
changes, edited/deleted certified files, interrupted rounds, interrupted suite
gates, writer exclusion, paired first-round reuse and spec-path collisions.
They use simulated model responses and real Ruby/RSpec fixtures. No live inference
or quality gain over paper results is claimed.
