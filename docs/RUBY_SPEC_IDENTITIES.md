# Definition-based generated-spec identities

Implemented on 2026-11-04, following validated round recovery (`1939c60f3`).

## Naming contract

Ordinary generated filenames retain a readable label and append `__def_` plus
all 64 hexadecimal characters of SHA-256 over `MethodTarget.analysis_id` encoded
as UTF-8. That existing canonical identity includes the source-relative file,
Ruby qualified method name (including instance/singleton distinction), and the
inclusive start/end lines of the definition.

The label is sanitized to ASCII and bounded to 96 characters before the digest.
Thus deeply namespaced classes, long method names and Unicode/glob characters in
source filenames do not produce unbounded or ambiguous output basenames. The
usual endings remain `_spec.rb` for the unconditional helper and `_rN_spec.rb`
for generation rounds. Output roots and absolute checkout paths are excluded
from definition identity; changing source locations/definition lines changes it.
Adding another selected target does not rename an existing definition's output.

This separates methods in identically named files, instance/singleton methods,
reopened definitions on different lines, and distinct Ruby names collapsed by
sanitization. Both `generate_all` and `generate_rounds` reject duplicate final
paths before generation requests, including accidental repeated exact targets.
The parser still cannot distinguish same-name definitions sharing the same
inclusive line range; discovery continues to reject those ambiguous identities.

The pre-existing `__task_<20-hex>` naming branch is unchanged, byte for byte.
Official tasks retain their task-ID-plus-definition identity and historical names.

## RAG example lookup

The normal project's repair-example lookup matches the exact definition stem
followed only by `_spec.rb` or `_r<digits>_spec.rb`. It no longer accepts arbitrary
prefix neighbours. Directory lookup treats glob characters literally. Empty or
unreadable matching files are skipped.

Production RAG entries have no task ID. For selected tasks, the lookup also accepts
only the known task stems whose `analysis_id` equals that production definition.
It never broadens the lookup to another file with the same method name. XRepoTest
continues to disable reuse of another task's generated answers through its own
project override.

This lookup is not an independent validator for manually placed files. Normal
round generation uses its existing validation and checkpoint/archive gates before
retaining output; the unconditional `generate_all` helper remains unconditional.

## Existing output and checkpoints

The generation recipe explicitly records
`spec_naming=definition-sha256-v1-task-legacy`; implementation hashes also change.
Existing generation checkpoints with a different recipe are incompatible. Normal
round recovery archives their old files/checkpoint with a reason and regenerates
under the new policy. It does not silently certify or rename an old file.

Use a fresh output directory for an independent experiment. Frozen papers must
retain their code/manifests and output. No frozen artifacts, official tasks,
model settings, prompts, attempt budgets or evaluation formulas were changed.
Analysis summaries remain reusable under their existing independent cache rules;
this filename change does not require new summary calls by itself.

## Verification

Regressions exercise the formerly colliding definitions, filename length/ASCII,
stability across checkouts and output roots, unchanged official task names,
exact RAG lookup and selected-task mapping. Both public generation entry points
produce separate passing files for the colliding cases, with real Ruby/RSpec and
scripted Planner/Dev responses. Joint coverage validation executes both files;
no extra model attempts are introduced by naming.

The backlog now distinguishes completed engineering fixes from remaining context,
cache, retrieval, mutation and thesis work. The pre-review notes are preserved
verbatim in `docs/archive/ruby-improvements-before-2026-10-04.md`.
