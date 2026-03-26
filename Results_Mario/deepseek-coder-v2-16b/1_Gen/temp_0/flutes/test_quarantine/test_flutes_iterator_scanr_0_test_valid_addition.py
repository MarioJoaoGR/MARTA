
import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List, TypeVar

A = TypeVar('A')

def add(x: A, y: A) -> A:
    return x + y

@pytest.mark.parametrize("iterable, expected", [
    ([1, 2, 3, 4], [10, 9, 7, 4]),
    ([5, 10, 15], [20, 25, 35]),
    ([0, 0, 0], [0, 0, 0]),
    ([-1, -2, -3, -4], [-1, -3, -6, -10])
])
def test_scanr(iterable, expected):
    result = scanr(add, iterable)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py . [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_scanr[iterable1-expected1] ________________________

iterable = [5, 10, 15], expected = [20, 25, 35]

    @pytest.mark.parametrize("iterable, expected", [
        ([1, 2, 3, 4], [10, 9, 7, 4]),
        ([5, 10, 15], [20, 25, 35]),
        ([0, 0, 0], [0, 0, 0]),
        ([-1, -2, -3, -4], [-1, -3, -6, -10])
    ])
    def test_scanr(iterable, expected):
        result = scanr(add, iterable)
>       assert result == expected
E       assert [30, 25, 15] == [20, 25, 35]
E         
E         At index 0 diff: 30 != 20
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py:19: AssertionError
_______________________ test_scanr[iterable3-expected3] ________________________

iterable = [-1, -2, -3, -4], expected = [-1, -3, -6, -10]

    @pytest.mark.parametrize("iterable, expected", [
        ([1, 2, 3, 4], [10, 9, 7, 4]),
        ([5, 10, 15], [20, 25, 35]),
        ([0, 0, 0], [0, 0, 0]),
        ([-1, -2, -3, -4], [-1, -3, -6, -10])
    ])
    def test_scanr(iterable, expected):
        result = scanr(add, iterable)
>       assert result == expected
E       assert [-10, -9, -7, -4] == [-1, -3, -6, -10]
E         
E         At index 0 diff: -10 != -1
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py::test_scanr[iterable1-expected1]
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py::test_scanr[iterable3-expected3]
========================= 2 failed, 2 passed in 0.09s ==========================
"""