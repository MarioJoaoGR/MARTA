
import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List

# Assuming the function definitions are in a separate file or module named 'flutes.iterator'
# and contains the definition of `scanr` as per the provided documentation.

def add(x: int, y: int) -> int:
    return x + y

def mul(x: int, y: int) -> int:
    return x * y

@pytest.mark.parametrize("func, iterable, initial, expected", [
    (add, [], 0, []),
    (mul, [], 1, []),
])
def test_scanr_edge_cases(func, iterable, initial, expected):
    result = scanr(func, iterable, initial)
    assert result == expected, f"Expected {expected}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py FF   [100%]

=================================== FAILURES ===================================
_______________ test_scanr_edge_cases[add-iterable0-0-expected0] _______________

func = <function add at 0x7fda8fef68e0>, iterable = [], initial = 0
expected = []

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
    ])
    def test_scanr_edge_cases(func, iterable, initial, expected):
        result = scanr(func, iterable, initial)
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected [], but got [0]
E       assert [0] == []
E         
E         Left contains one more item: 0
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py:21: AssertionError
_______________ test_scanr_edge_cases[mul-iterable1-1-expected1] _______________

func = <function mul at 0x7fda8fef6fc0>, iterable = [], initial = 1
expected = []

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [], 0, []),
        (mul, [], 1, []),
    ])
    def test_scanr_edge_cases(func, iterable, initial, expected):
        result = scanr(func, iterable, initial)
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected [], but got [1]
E       assert [1] == []
E         
E         Left contains one more item: 1
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py::test_scanr_edge_cases[add-iterable0-0-expected0]
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py::test_scanr_edge_cases[mul-iterable1-1-expected1]
============================== 2 failed in 0.08s ===============================
"""