# MARTA — Supplementary Material

Material referenced in the Data Availability Statement of the paper and omitted from it
for space. Everything here is reproduced from the extended version of the manuscript.

All exchanges below are *illustrative*: they use a small worked example (`process_payment`)
to show the shape of each prompt and response. The prompts as actually issued are
constructed at run time in `marta/message_react.py`.

## 1. Agent exchanges

### A. Planner Agent exchange

Illustrative anatomy of the Planner Agent exchange: the prompt injects role-playing,
source code and inferred types while the agent returns a JSON test plan. The `COVERAGE
FEEDBACK` field is present only in outer-loop rounds, where it redirects the same QA
Lead persona toward the unexecuted lines.

```text
[SYSTEM]:
You are a QA Lead. Analyze the function
and output a Test Plan in JSON format.
--------------------
[USER]:
CONTEXT:
Function Name: process_payment | Module: billing

SOURCE CODE:
def process_payment(account, amount: float) -> bool:
    """ Processes a payment and deducts it. """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return account.deduct(amount)

INFERRED TYPES & USAGE:
- `account`: inferred as `billing.Account`
  (uses method `deduct`)

COVERAGE FEEDBACK:        <- outer-loop rounds only
MISSING LINES TO COVER: 45

TASK: Generate 3 distinct test scenarios covering
happy path, edge cases and error handling.
CRITICAL: scenarios MUST execute the missing lines.

OUTPUT FORMAT: Return ONLY a raw JSON list.
--------------------
[PLANNER OUTPUT]:
[
 {"name": "test_valid_payment",
  "desc": "Standard input, positive amount.",
  "setup": "Mock account whose deduct() returns True"},
 {"name": "test_invalid_amount",
  "desc": "Negative amount must raise ValueError.",
  "setup": "Mock a minimal account object"}
]
```

### B. Assertion Agent exchange

Illustrative Assertion Agent exchange. From the JSON plan, the agent emits a single,
complete Pytest file with one independent test per scenario in one inference call,
declaring shared mocks once. Note how it translates a logical "raises" outcome into a
proper `pytest.raises` context manager.

```text
[SYSTEM]:
You are a Pytest Expert. Write valid python code.
--------------------
[USER]:
Write a SINGLE pytest file containing one independent
test function for EACH of these scenarios:
  1. test_valid_payment: standard positive amount.
  2. test_invalid_amount: negative amount raises error.

FUNCTION CODE:
def process_payment(account, amount: float) -> bool: ...

RULES:
1. Output ONLY python code in a ```python``` block
   (a complete test file).
2. Import correctly from module 'billing'.
3. One independent, function-based test per scenario.
--------------------
[ASSERTION AGENT OUTPUT]:
import pytest
from billing import process_payment

class MockAccount:
    def deduct(self, amount): return True

def test_valid_payment():
    acc = MockAccount()
    assert process_payment(acc, 50.0) is True

def test_invalid_amount():
    acc = MockAccount()
    with pytest.raises(ValueError, match="Amount must be positive"):
        process_payment(acc, -10.0)
```

### C. ReAct repair exchange

Illustrative exchange of the ReAct self-healing inner loop. The Assertion Agent receives
the raw Pytest failure log for the generated file and autonomously rewrites it to
capture the correct exception.

```text

```

### D. Generated suites compared across the three tools

Tests generated for `string_utils.validation.is_number` by the three systems (16B model;
excerpts, reformatted for space). Both LLM-driven pipelines exercise the function with
concrete inputs and assert its return value, while the search-based generator reaches it
once and records only that some input raises. This example is illustrative rather than
representative: it was selected to show the difference in oracle form that the aggregate
rates reported in this section measure across the full corpus.

```text
# ---- MARTA -----------------------------------------------------
def test_valid_numbers():
    assert is_number('123') == True
    assert is_number('123.45') == True
    assert is_number('-123.45e6') == True

def test_invalid_inputs():
    assert is_number('abc') == False
    assert is_number('123abc') == False
    assert is_number('12.34e56f') == False   # malformed exponent

def test_error_handling():
    with pytest.raises(TypeError):
        is_number(None)

# ---- Test4Py (single-prompt) -----------------------------------
def test_valid_positive_integer():
    assert is_number('42') == True

def test_valid_negative_decimal():
    assert is_number('-9.12') == True

def test_valid_scientific_notation():
    assert is_number('1e3') == True

def test_invalid_string():
    assert is_number('1 2 3') == False

# ---- Pynguin (search-based) ------------------------------------
def test_case_6():
    bool_0 = False
    with pytest.raises(module_1.InvalidInputError):
        module_0.is_number(bool_0)
# Pynguin emits one module-level suite; its remaining cases
# target other functions in the same module.
```

## 2. Per-phase inference cost

Decoupling generation into two agents plus a repair loop could reasonably be expected to
multiply inference cost, since it introduces a planning call the single-prompt
architecture does not make. It does not: the planning call is amortized because the
Assertion Agent emits one complete file per function in a single inference call rather
than one call per scenario and the outer loop regenerates only functions with remaining
uncovered lines. MARTA's generation phase costs 0.63x the baseline's.

The saving does not carry to the total. MARTA infers parameter types during context
building, whereas the baseline defers the same work into generation, so MARTA's Phase 1
costs 2.7x the baseline's and end to end it is 21% more expensive (13.4 against 11.1 GPU-
hours; 28.6M against 23.3M tokens). The architecture makes generation cheaper and
context building dearer. To mitigate this, MARTA persists the call graph, the generated
summaries and the vector index to disk, keyed by a content hash of the source, so an
unchanged project restores Phase 1 from cache and re-incurs no LLM cost. The heavier
context-building step is therefore paid once per version of the code under test rather
than on every run.

These figures were measured on a nine-project subset. Pynguin performs no inference and
is excluded, its cost is CPU search time (300 s per module).

We report cost for completeness rather than as an objective. MARTA was not designed to
minimise inference cost or suite size, but to produce tests that meaningfully verify the
code under test.

**Why the paper reports only the end-to-end figure.** The submitted paper gives the 21%
end-to-end difference but not the 0.63x generation-phase ratio above. The two systems draw
the boundary between context building and generation differently: MARTA infers parameter
types eagerly during Phase 1, whereas the single-prompt baseline defers the same work into
generation. That is the same work billed to different phases, so a per-phase split
flatters whichever tool moves work out of the phase being compared. The end-to-end
total is unaffected by where the boundary falls, which is why it is the figure we report.

