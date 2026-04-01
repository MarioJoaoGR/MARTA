
import pytest
from pytutils.iters import dedupe

def some_function(iterable):
    return list(set(iterable))  # Ensure uniqueness by converting to set and back to list

@pytest.mark.parametrize("input_data, expected", [
    ([1, 2, 3, 2, 1], [1, 2, 3]),
    (["a", "b", "a", "c"], ["a", "b", "c"]),
    ((1, 2, 3, 2, 1), [1, 2, 3]),
])
def test_dedupe_edge_case(input_data, expected):
    @dedupe(some_function, instance=None, args=(input_data,), kwargs={})
    def wrapped_function(iterable):
        return iterable
    
    result = wrapped_function(input_data)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py FF [ 66%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________ test_dedupe_edge_case[input_data0-expected0] _________________

input_data = [1, 2, 3, 2, 1], expected = [1, 2, 3]

    @pytest.mark.parametrize("input_data, expected", [
        ([1, 2, 3, 2, 1], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ((1, 2, 3, 2, 1), [1, 2, 3]),
    ])
    def test_dedupe_edge_case(input_data, expected):
>       @dedupe(some_function, instance=None, args=(input_data,), kwargs={})

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/iters.py:75: in dedupe
    gen = f(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable = <function test_dedupe_edge_case.<locals>.wrapped_function at 0x7fa7d435f9c0>

    def some_function(iterable):
>       return list(set(iterable))  # Ensure uniqueness by converting to set and back to list
E       TypeError: 'function' object is not iterable

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:6: TypeError
_________________ test_dedupe_edge_case[input_data1-expected1] _________________

input_data = ['a', 'b', 'a', 'c'], expected = ['a', 'b', 'c']

    @pytest.mark.parametrize("input_data, expected", [
        ([1, 2, 3, 2, 1], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ((1, 2, 3, 2, 1), [1, 2, 3]),
    ])
    def test_dedupe_edge_case(input_data, expected):
>       @dedupe(some_function, instance=None, args=(input_data,), kwargs={})

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/iters.py:75: in dedupe
    gen = f(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable = <function test_dedupe_edge_case.<locals>.wrapped_function at 0x7fa7d435fe20>

    def some_function(iterable):
>       return list(set(iterable))  # Ensure uniqueness by converting to set and back to list
E       TypeError: 'function' object is not iterable

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:6: TypeError
_________________ test_dedupe_edge_case[input_data2-expected2] _________________

input_data = (1, 2, 3, 2, 1), expected = [1, 2, 3]

    @pytest.mark.parametrize("input_data, expected", [
        ([1, 2, 3, 2, 1], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ((1, 2, 3, 2, 1), [1, 2, 3]),
    ])
    def test_dedupe_edge_case(input_data, expected):
>       @dedupe(some_function, instance=None, args=(input_data,), kwargs={})

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/iters.py:75: in dedupe
    gen = f(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable = <function test_dedupe_edge_case.<locals>.wrapped_function at 0x7fa7d437c2c0>

    def some_function(iterable):
>       return list(set(iterable))  # Ensure uniqueness by converting to set and back to list
E       TypeError: 'function' object is not iterable

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py::test_dedupe_edge_case[input_data0-expected0]
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py::test_dedupe_edge_case[input_data1-expected1]
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_1_test_edge_case.py::test_dedupe_edge_case[input_data2-expected2]
============================== 3 failed in 0.07s ===============================
"""