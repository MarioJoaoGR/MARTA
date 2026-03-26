
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

def is_even(n): 
    return n % 2 == 0

def double(n): 
    return n * 2

def triple(n): 
    return n * 3

# Define the test cases
@pytest.mark.parametrize("condition_list, args, expected", [
    ([(is_even, double)], [4], 8),  # Example 1: Using `is_even` and `double`
    ([(is_even, double)], [7], 21),  # Example 2: Using `is_even` and `double`, with a different argument
    ([(is_even, double), (lambda x: x > 5, triple)], [4], 8),  # Example 3: Using multiple conditions and execute functions
])
def test_cond(condition_list, args, expected):
    result = cond(condition_list)(*args)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py .F.                   [100%]

=================================== FAILURES ===================================
_____________________ test_cond[condition_list1-args1-21] ______________________

condition_list = [(<function is_even at 0x7f56148d9580>, <function double at 0x7f56148d8d60>)]
args = [7], expected = 21

    @pytest.mark.parametrize("condition_list, args, expected", [
        ([(is_even, double)], [4], 8),  # Example 1: Using `is_even` and `double`
        ([(is_even, double)], [7], 21),  # Example 2: Using `is_even` and `double`, with a different argument
        ([(is_even, double), (lambda x: x > 5, triple)], [4], 8),  # Example 3: Using multiple conditions and execute functions
    ])
    def test_cond(condition_list, args, expected):
        result = cond(condition_list)(*args)
>       assert result == expected
E       assert None == 21

pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_0.py::test_cond[condition_list1-args1-21]
========================= 1 failed, 2 passed in 0.06s ==========================
"""