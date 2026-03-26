
import pytest
from pytutils.iters import dedupe

# Example function to be wrapped for testing
def some_function(*args, **kwargs):
    # Some implementation
    return [1, 2, 3, 4]  # Example iterable to be deduplicated

# Test cases for the dedupe decorator
@pytest.mark.parametrize("f, instance, args, kwargs", [
    (some_function, None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
    (lambda *args, **kwargs: [1, 2, 3, 4], None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
])
def test_dedupe(f, instance, args, kwargs):
    # Call the dedupe function with the provided arguments
    deduped_output = dedupe(f, instance, *args, **kwargs)
    
    # Convert to a set to remove duplicates and then back to a list for comparison
    expected_deduped = list(set([item for item in f(*args, **kwargs)]))
    
    # Assert that the deduplicated output matches the expected deduplicated result
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py FF                [100%]

=================================== FAILURES ===================================
________________ test_dedupe[some_function-None-args0-kwargs0] _________________

f = <function some_function at 0x7f335d8e9260>, instance = None
args = ('arg1', 'arg2'), kwargs = {'kwarg1': 'value'}

    @pytest.mark.parametrize("f, instance, args, kwargs", [
        (some_function, None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
        (lambda *args, **kwargs: [1, 2, 3, 4], None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
    ])
    def test_dedupe(f, instance, args, kwargs):
        # Call the dedupe function with the provided arguments
        deduped_output = dedupe(f, instance, *args, **kwargs)
    
        # Convert to a set to remove duplicates and then back to a list for comparison
        expected_deduped = list(set([item for item in f(*args, **kwargs)]))
    
        # Assert that the deduplicated output matches the expected deduplicated result
>       assert sorted(list(deduped_output)) == sorted(expected_deduped), "Dedupe function failed to remove duplicates"
E       TypeError: 'function' object is not iterable

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py:23: TypeError
___________________ test_dedupe[<lambda>-None-args1-kwargs1] ___________________

f = <function <lambda> at 0x7f335d947600>, instance = None
args = ('arg1', 'arg2'), kwargs = {'kwarg1': 'value'}

    @pytest.mark.parametrize("f, instance, args, kwargs", [
        (some_function, None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
        (lambda *args, **kwargs: [1, 2, 3, 4], None, ('arg1', 'arg2'), {'kwarg1': 'value'}),
    ])
    def test_dedupe(f, instance, args, kwargs):
        # Call the dedupe function with the provided arguments
        deduped_output = dedupe(f, instance, *args, **kwargs)
    
        # Convert to a set to remove duplicates and then back to a list for comparison
        expected_deduped = list(set([item for item in f(*args, **kwargs)]))
    
        # Assert that the deduplicated output matches the expected deduplicated result
>       assert sorted(list(deduped_output)) == sorted(expected_deduped), "Dedupe function failed to remove duplicates"
E       TypeError: 'function' object is not iterable

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py:23: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py::test_dedupe[some_function-None-args0-kwargs0]
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py::test_dedupe[<lambda>-None-args1-kwargs1]
============================== 2 failed in 0.06s ===============================
"""