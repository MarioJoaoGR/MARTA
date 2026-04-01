
import pytest
from functools import reduce
from pymonet.utils import compose  # Assuming this module contains the `compose` function

# Define the functions for testing
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

@pytest.mark.parametrize("value, functions, expected", [
    (5, [add_one, multiply_by_two], 12),
    (3, [lambda x: x + 1, lambda x: x * 2], 8),
    (0, [], 0),
    (10, [lambda x: x ** 2], 100)
])
def test_compose(value, functions, expected):
    assert compose(value, *functions) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pyMonet/Test4DT_tests/test_pymonet_utils_compose_1_test_edge_cases.py FF [ 50%]
..                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_compose[5-functions0-12] _________________________

value = 5
functions = [<function add_one at 0x7f638cec3060>, <function multiply_by_two at 0x7f638cec3ec0>]
expected = 12

    @pytest.mark.parametrize("value, functions, expected", [
        (5, [add_one, multiply_by_two], 12),
        (3, [lambda x: x + 1, lambda x: x * 2], 8),
        (0, [], 0),
        (10, [lambda x: x ** 2], 100)
    ])
    def test_compose(value, functions, expected):
>       assert compose(value, *functions) == expected
E       assert 11 == 12
E        +  where 11 = compose(5, *[<function add_one at 0x7f638cec3060>, <function multiply_by_two at 0x7f638cec3ec0>])

pyMonet/Test4DT_tests/test_pymonet_utils_compose_1_test_edge_cases.py:20: AssertionError
_________________________ test_compose[3-functions1-8] _________________________

value = 3
functions = [<function <lambda> at 0x7f638cec3600>, <function <lambda> at 0x7f638cec34c0>]
expected = 8

    @pytest.mark.parametrize("value, functions, expected", [
        (5, [add_one, multiply_by_two], 12),
        (3, [lambda x: x + 1, lambda x: x * 2], 8),
        (0, [], 0),
        (10, [lambda x: x ** 2], 100)
    ])
    def test_compose(value, functions, expected):
>       assert compose(value, *functions) == expected
E       assert 7 == 8
E        +  where 7 = compose(3, *[<function <lambda> at 0x7f638cec3600>, <function <lambda> at 0x7f638cec34c0>])

pyMonet/Test4DT_tests/test_pymonet_utils_compose_1_test_edge_cases.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_compose_1_test_edge_cases.py::test_compose[5-functions0-12]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_compose_1_test_edge_cases.py::test_compose[3-functions1-8]
========================= 2 failed, 2 passed in 0.09s ==========================
"""