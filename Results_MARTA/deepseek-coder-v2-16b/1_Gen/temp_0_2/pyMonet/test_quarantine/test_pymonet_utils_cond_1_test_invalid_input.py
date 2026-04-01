
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("condition_list, args, expected", [
    ([(is_even, double), (lambda x: x > 5, triple)], 4, 8),
    ([(is_even, double), (lambda x: x > 5, triple)], 7, 21),
])
def test_cond(condition_list, args, expected):
    cond_func = cond(condition_list)
    assert cond_func(*args) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_utils_cond_1_test_invalid_input.py FF [100%]

=================================== FAILURES ===================================
________________________ test_cond[condition_list0-4-8] ________________________

condition_list = [(<function is_even at 0x7fea44afdc60>, <function double at 0x7fea44afd6c0>), (<function <lambda> at 0x7fea44afe980>, <function triple at 0x7fea44afd9e0>)]
args = 4, expected = 8

    @pytest.mark.parametrize("condition_list, args, expected", [
        ([(is_even, double), (lambda x: x > 5, triple)], 4, 8),
        ([(is_even, double), (lambda x: x > 5, triple)], 7, 21),
    ])
    def test_cond(condition_list, args, expected):
        cond_func = cond(condition_list)
>       assert cond_func(*args) == expected
E       TypeError: pymonet.utils.cond.<locals>.result() argument after * must be an iterable, not int

pyMonet/Test4DT_tests/test_pymonet_utils_cond_1_test_invalid_input.py:21: TypeError
_______________________ test_cond[condition_list1-7-21] ________________________

condition_list = [(<function is_even at 0x7fea44afdc60>, <function double at 0x7fea44afd6c0>), (<function <lambda> at 0x7fea44aff560>, <function triple at 0x7fea44afd9e0>)]
args = 7, expected = 21

    @pytest.mark.parametrize("condition_list, args, expected", [
        ([(is_even, double), (lambda x: x > 5, triple)], 4, 8),
        ([(is_even, double), (lambda x: x > 5, triple)], 7, 21),
    ])
    def test_cond(condition_list, args, expected):
        cond_func = cond(condition_list)
>       assert cond_func(*args) == expected
E       TypeError: pymonet.utils.cond.<locals>.result() argument after * must be an iterable, not int

pyMonet/Test4DT_tests/test_pymonet_utils_cond_1_test_invalid_input.py:21: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_1_test_invalid_input.py::test_cond[condition_list0-4-8]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_1_test_invalid_input.py::test_cond[condition_list1-7-21]
============================== 2 failed in 0.07s ===============================
"""