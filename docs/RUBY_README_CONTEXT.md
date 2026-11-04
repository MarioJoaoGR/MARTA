# Project-root README context and cache consistency

Implemented on 2026-11-04 after definition-based spec identities (`f384cb252`).

## Selection

Project orchestration now supplies both the code root and the project root to
README selection. Given `source_dir=lib`, the search continues from each source
file through its parent directories up to the project root, inclusive. It still
prefers the nearest README, so a monorepo component can override root-level docs.
The existing filename order stays `README.md`, `README.markdown`, `README.rdoc`,
then `README`.

A project with no matching README continues with code-only requirement analysis.
It does not inherit documentation from a parent checkout or another project.
Paths and symlinks are resolved; a source or README resolving outside the project
boundary is not a source of project documentation. A skipped external README can
still fall back to an eligible README inside the project.

Two-argument `nearest_readme(file_path, abs_source)` and
`ReadmeOverviewCache(abs_source)` callers preserve their existing supplied
source-root boundary. New keyword `project_root` enables the broader project
scope; `RubyProject` passes its own `root_dir` explicitly. No CLI flag is needed.

## One snapshot for cache and prompts

Before testing cache validity, analysis snapshots the selected document for every
production source file. Each snapshot retains its exact UTF-8 contents and SHA-256.
The fingerprint includes the source-file-to-README mapping, relative README path,
content hash, and selection policy. The eventual overview prompt reads the same
snapshot; each distinct document receives at most one overview request in that
analysis. A missing README is also remembered for that snapshot.

Editing a README while the analysis is running therefore does not produce a
bundle whose fingerprint refers to different documentation from the prompts.
The current analysis uses the captured snapshot; a subsequent analysis sees the
new contents and invalidates the earlier cache. Adding or removing a nearer
README also invalidates selection, even if its bytes equal the former document.
Editing an unused, shadowed ancestor README does not require regeneration.
Unreadable or non-UTF-8 selected documents fail explicitly; this change does not
silently substitute different requirements.

`ANALYSIS_SCHEMA` is now 5. New bundles add `readme_policy` and `readmes` for audit;
`analysis_readmes` telemetry records paths/hashes, not the README bodies. Bundles
using an older fingerprint are not silently reused under the new context rule.
The bundle filename and its existing atomic write remain unchanged.

## Scope and next work

These are new analysis semantics. Existing paper results and frozen experiment
manifests are not migrated or rerun. A new analysis can use root documentation
that was previously invisible; source-only summaries still use their existing
source-only prompts, and nearest-overview context feeds the same requirement
and merge stages as before. No token/output limits, synthesis policy, retry
budgets, evaluation formulas or generation selectors changed.

This closes the README boundary and its cache/prompt consistency issue only.
Prompt/model/embedding provenance still needs the broader cache work from A3.
`use_cache=False` still recomputes without writing a new bundle; separating
reusable cache from an always-saved analysis archive remains A4. Per-call analysis
recovery and a complete token budget remain separate tasks.

## Verification

Offline regressions cover root discovery from nested source directories,
monorepo overrides and fallback, project boundaries and symlinks, legacy callers,
exact UTF-8/CRLF snapshots, missing-document snapshots, the requirement prompt,
audit metadata, cache reuse and invalidation, and edits during analysis.
Analysis integration tests use real Ruby parsing and scripted model responses;
there are no live LLM calls or installations.
