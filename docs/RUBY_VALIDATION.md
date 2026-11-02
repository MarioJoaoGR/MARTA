# Ruby validation after the paper

Implemented on 2026-11-02, starting from the consolidated `main` at `adfb5017b`.
This is a new generation policy, not a correction to the published measurements.
Frozen paper suites, external metrics and experiment manifests are not modified.

## Acceptance contract

`runner.run_rspec` now requires all of the following:

- An RSpec JSON object containing examples and a complete numeric summary.
- Unique example identities and recognized example statuses.
- Agreement between summary counts and the individual example results.
- At least one passed example, zero failed examples and zero errors outside examples.
- Process exit code zero. Interrupted or incomplete reports are rejected.

Pending examples remain visible as pending. They do not count as passed, and a
pending-only suite is rejected. Passing examples alongside pending examples are
allowed if all other checks hold. An executed example is not proof of a useful
assertion or of focal invocation; those remain separate quality measurements.

The result retains `exit_code`, `report_valid` and `validation_error` alongside
example statuses and diagnostic output. A malformed report is an unsuccessful
validation, not a parser crash or an opportunity to salvage an unverified suite.

## Coverage and accumulated suites

The Ruby coverage helper reports the RSpec formatter data and runner status in
`test_result`, alongside unchanged line, branch and method-hit observations.
Raw coverage remains available even if assertions fail. `CoverageResult.suite_result`
records whether that execution certified a usable suite. Minitest keeps its
existing raw-coverage path and does not acquire an RSpec validation claim.

`RubyProject.measure_coverage` refuses to use missing or unsuccessful RSpec
validation as successful generation feedback. Application `SystemExit` still
propagates with its original status; the helper still emits observed coverage.
The report uses the existing ActiveSupport-compatible serialization path.

At the end of each generation round, the accumulated suite is checked together,
using the backend's execution environment. The XRepoTest adapter consequently
checks the concatenated suite at its final staging path.

If a newly added round makes the accumulated suite invalid, new candidates are
removed in reverse generation order until the remaining suite passes. This is a
conservative rollback, not minimal fault localization: in a multi-target round it
can reject a harmless recent candidate before reaching the conflicting one.
Each rejected candidate and its diagnostics are retained under `rejected_specs/`,
outside the directory searched for accepted specs. Its `GenOutcome` becomes
unsuccessful. `suite_validation` and `suite_rollback` events record this decision.
There are no additional model requests or enlarged attempt budgets.

Invalid pre-existing suites are preserved and raise an explicit validation error;
they are not silently deleted or accepted merely because their files exist.
Atomic resume and stronger output identities remain separate backlog items.

## Regression checks

`marta/ruby_backend/tests/test_suite_validation.py` covers empty and pending-only
suites, hidden failures with exit status zero, early exit, outside-example errors,
malformed/inconsistent reports, accumulated-suite conflicts, preservation of old
files and ActiveSupport JSON compatibility. These use fixtures and simulated LLM
responses, not live inference or benchmark tasks.

The other runner, coverage, generation, adapter and cluster tests must continue to
pass. The existing XRepoTest mutation-support tests use its prepared container
because the local development environment lacks the Ruby Tree-sitter grammar.

## Remaining work

This delivery closes the acceptance and joint-suite validation issues only.
It does not yet add previous test/plan context to repair, validate the Planner
scenario schema, preserve focal code when limiting context, bound summary
propagation, redesign cache provenance, or improve graph/retrieval policies.
The paper remains a measurement of its frozen implementation and artifacts.
