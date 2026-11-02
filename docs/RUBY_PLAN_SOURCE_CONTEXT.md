# Validated plans and complete focal-method source

Implemented on 2026-11-02, following repair context (`3476c2e36`).
These are new generation/analysis policies. Frozen paper results and external
benchmark metric definitions are not rewritten or migrated.

## Planner contract and fallback

The accepted plan is a top-level JSON list of one to three distinct scenarios.
Each object contains exactly `name`, `desc` and `setup`, all nonempty strings.
Leading/trailing field whitespace is normalized; inner text, brackets, Unicode
and code fences inside setup text are preserved. Missing/extra fields, duplicate
object keys or scenario names, wrong types and incomplete JSON are rejected.
Fenced JSON and prose surrounding a complete array remain supported.

The maximum of three scenarios matches the Planner template. The normalized JSON
has a 6000-character resource limit. This initial bound follows the scale of the
existing focused-code and error-text bounds; it is not a scientific quality
threshold or a whole-prompt token guarantee. Limits can be supplied explicitly
to `planning.validate_plan`; invalid limit configuration raises an error rather
than being attributed to the model.

Invalid plans use the existing single basic scenario. The whole plan is replaced;
we do not silently keep an arbitrary valid subset or truncate descriptions.
There is no extra Planner request or increased Developer attempt budget.
`plan_validation` events retain the response text, reason and effective plan;
`GenOutcome.plan_fallback` and `plan_validation_error` expose the decision to
callers. `generate.parse_plan` remains available as the list-returning API.

## Focused source contract

The complete focal method is reserved before any auxiliary code. If the original
view fits the character budget, it remains complete. Otherwise, fitting priority
is the class/module declaration, a whole constructor, then whole non-method class
statements in their original order. An oversized constant does not block later
short declarations. Omissions are explicit and no statement is cut in half.
The output order remains class context, constructor, focal method.

The class/module declaration reflects the parser's actual kind. A constructor
that is itself the focal target is not duplicated. Top-level methods are also
preserved in full.

If the mandatory focal view (including its identification marker when applicable)
alone exceeds `MARTA_MAX_CONTEXT_CHARS`, it remains intact and is marked over-limit;
auxiliary context is omitted. The configured limit must be positive. This is a
local character budget, not the LLM's token window. Neither context-window nor
output-token settings are enlarged by this change. A complete token budget for
all prompt blocks remains future work; a genuinely oversized request can still
be rejected by the model server.

`MethodTarget.source_context` exposes omission counts and over-limit status;
`context_source` retains its string-returning interface. `source_context` telemetry
records reductions/excess in both analysis and generation. Full-production analysis
scope and generation selectors are unchanged.

## Cache and evidence

`ANALYSIS_SCHEMA` moves from 2 to 3 because source-context construction changed.
Old analysis bundles are not silently reused as current summaries. Newly generated
summaries and indexed texts therefore reflect the new source policy. Frozen
experiments must retain their original code/configuration; this is not a reason
to relabel historical runs as executions of the improved tool.

Regression tests reproduce malformed plans and large class/constructor contexts,
verify fallback provenance and unchanged request counts, and ensure the focal
method's tail survives. Other tests cover full-production analysis, exact task
selection, cache invalidation and compatibility with the repair context.
No online model-quality gain is inferred from these offline checks.
