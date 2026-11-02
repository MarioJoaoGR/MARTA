# Repair with previous test, plan and observed diagnosis

Implemented on 2026-11-02, following strict suite validation (`4061bcd30`).
This changes new generation requests. It does not migrate frozen paper runs or
modify the external XRepoTest evaluator and its recorded results.

## What each repair receives

- The effective JSON plan used for this target and coverage round, with a stable plan ID.
- The complete latest nonempty generated test, labelled with its attempt number.
- The current failure stage and category, validation status, process status, and
  individual example identities/statuses/locations when a coherent report exists.
- The previous test's own diagnosis when the latest response was empty and thus
  did not create or execute a replacement test.
- The existing target source, loading guidance, bounded failure output and
  error-directed retrieval when enabled.

For example, if attempt 1 has one passing and one failing example, attempt 2 is
empty and attempt 3 repairs the code, the third request receives code from attempt
1, that code's validation results, and a separately labelled empty-response
failure from attempt 2. It does not present the old execution as evidence about
an empty replacement.

The first Developer request is unchanged. Repair still returns a complete spec
file, but its instruction asks for targeted corrections that preserve passing
examples, meaningful assertions and planned scenarios. This instruction is not a
semantic guarantee: the runner still cannot prove an assertion is useful, and
quality gains require a controlled model-based evaluation.

## Diagnosis and provenance

`repair.py` builds deterministic diagnostics from runner evidence. Syntax and
empty-response failures have no invented execution counts. RSpec exception
classes distinguish assertion, missing method/constant, loading, argument, type
and other execution failures; different categories can be reported as mixed.
Outside-example failures, invalid reports and process timeouts remain distinct.
Error keywords are not treated as proof of a failure's category. No project- or
framework-integration-specific repair recipes are added.

`repair_context` events record the effective plan ID, source attempt, previous
code hash and current failure stage/category. Existing validation events retain
the corresponding candidate code and output. This makes contexts traceable
without another model call to classify errors.

The same generation budgets, coverage rounds, retrieval policies, salvage and
strict final-suite validation apply. Transport failures keep their existing
handling; no hidden retries or larger output budgets are introduced.

## Bounds and remaining work

The existing raw-error compression still applies. The previous test and effective
plan are supplied intact; this delivery does not silently truncate either. A
complete token-budget policy for all context blocks remains separate work.
Preserving the last nonempty candidate for a later repair does not introduce a
new salvage attempt after an empty response exhausts the configured budget.

Planner schema validation, focal-source preservation, bounded summary propagation,
atomic resume and other backlog items remain pending. The next experiments must
use a distinct run/configuration fingerprint; old paper measurements remain a
record of their original prompts and implementation.

## Verification

The regression tests use real local Ruby/RSpec execution and injected model
responses. They cover execution and syntax failures, initial/intermediate empty
responses, latest-code updates, unchanged attempt counts, typed diagnostics,
process timeouts and stable plan identities. Existing adapter and ablation tests
check that loading guidance, retrieval and no-repair controls remain compatible.
No model-quality improvement is inferred from these offline checks alone.
