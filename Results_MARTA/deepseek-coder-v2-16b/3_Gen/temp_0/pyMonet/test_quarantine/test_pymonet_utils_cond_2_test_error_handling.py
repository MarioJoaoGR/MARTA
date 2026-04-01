
from typing import Callable, List, Tuple
import pytest
from pymonet.utils import cond

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("args, expected", [
    (4, 8),       # Test with even number
    (7, 21),      # Test with number greater than 5
    (3, None)     # Test without a matching condition
])
def test_cond(args, expected):
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, triple)
    ])
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
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________________ test_cond[4-8] ________________________________

args = 4, expected = 8

    @pytest.mark.parametrize("args, expected", [
        (4, 8),       # Test with even number
        (7, 21),      # Test with number greater than 5
        (3, None)     # Test without a matching condition
    ])
    def test_cond(args, expected):
        cond_func = cond([
            (is_even, double),
            (lambda n: n > 5, triple)
        ])
>       assert cond_func(*args) == expected
E       TypeError: pymonet.utils.cond.<locals>.result() argument after * must be an iterable, not int

pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py:25: TypeError
_______________________________ test_cond[7-21] ________________________________

args = 7, expected = 21

    @pytest.mark.parametrize("args, expected", [
        (4, 8),       # Test with even number
        (7, 21),      # Test with number greater than 5
        (3, None)     # Test without a matching condition
    ])
    def test_cond(args, expected):
        cond_func = cond([
            (is_even, double),
            (lambda n: n > 5, triple)
        ])
>       assert cond_func(*args) == expected
E       TypeError: pymonet.utils.cond.<locals>.result() argument after * must be an iterable, not int

pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py:25: TypeError
______________________________ test_cond[3-None] _______________________________

args = 3, expected = None

    @pytest.mark.parametrize("args, expected", [
        (4, 8),       # Test with even number
        (7, 21),      # Test with number greater than 5
        (3, None)     # Test without a matching condition
    ])
    def test_cond(args, expected):
        cond_func = cond([
            (is_even, double),
            (lambda n: n > 5, triple)
        ])
>       assert cond_func(*args) == expected
E       TypeError: pymonet.utils.cond.<locals>.result() argument after * must be an iterable, not int

pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py:25: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py::test_cond[4-8]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py::test_cond[7-21]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_cond_2_test_error_handling.py::test_cond[3-None]
============================== 3 failed in 0.08s ===============================
"""