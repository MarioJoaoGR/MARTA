
import pytest
from pymonet.utils import eq  # Assuming this module contains the eq function

@pytest.mark.parametrize("test_input, expected", [
    (5, 5),
    ("hello", "world"),
    ([1, 2], [1, 2]),
    (None, None),
    (None, 1),
    (1, None),
    ([], []),
    ([1, 2], [3, 4]),
])
def test_edge_cases(test_input, expected):
    assert eq(test_input, expected) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py FFFFFFF [ 87%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_cases[5-5] _____________________________

test_input = 5, expected = 5

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert True == 5
E        +  where True = eq(5, 5)

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
_________________________ test_edge_cases[hello-world] _________________________

test_input = 'hello', expected = 'world'

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       AssertionError: assert False == 'world'
E        +  where False = eq('hello', 'world')

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
____________________ test_edge_cases[test_input2-expected2] ____________________

test_input = [1, 2], expected = [1, 2]

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert True == [1, 2]
E        +  where True = eq([1, 2], [1, 2])

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
__________________________ test_edge_cases[None-None] __________________________

test_input = None, expected = None

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert True == None
E        +  where True = eq(None, None)

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
___________________________ test_edge_cases[None-1] ____________________________

test_input = None, expected = 1

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert False == 1
E        +  where False = eq(None, 1)

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
___________________________ test_edge_cases[1-None] ____________________________

test_input = 1, expected = None

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert False == None
E        +  where False = eq(1, None)

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
____________________ test_edge_cases[test_input6-expected6] ____________________

test_input = [], expected = []

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert True == []
E        +  where True = eq([], [])

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
____________________ test_edge_cases[test_input7-expected7] ____________________

test_input = [1, 2], expected = [3, 4]

    @pytest.mark.parametrize("test_input, expected", [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        (None, None),
        (None, 1),
        (1, None),
        ([], []),
        ([1, 2], [3, 4]),
    ])
    def test_edge_cases(test_input, expected):
>       assert eq(test_input, expected) == expected
E       assert False == [3, 4]
E        +  where False = eq([1, 2], [3, 4])

pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[5-5]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[hello-world]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[test_input2-expected2]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[None-None]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[None-1]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[1-None]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[test_input6-expected6]
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_1_test_edge_cases.py::test_edge_cases[test_input7-expected7]
============================== 8 failed in 0.10s ===============================
"""