
from typing import Callable, Iterable, List
import pytest
from flutes.iterator import scanr

# Example usage with addition function
def add(x, y):
    return x + y

# Example usage with multiplication function
def multiply(x, y):
    return x * y

@pytest.mark.parametrize("func, iterable, expected", [
    (add, [1, 2, 3, 4], [10, 9, 7, 4]),
    (multiply, [1, 2, 3, 4], [1, 2, 6, 24])
])
def test_valid_addition(func, iterable, expected):
    result = scanr(func, iterable)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________ test_valid_addition[multiply-iterable1-expected1] _______________

func = <function multiply at 0x7f141831f060>, iterable = [1, 2, 3, 4]
expected = [1, 2, 6, 24]

    @pytest.mark.parametrize("func, iterable, expected", [
        (add, [1, 2, 3, 4], [10, 9, 7, 4]),
        (multiply, [1, 2, 3, 4], [1, 2, 6, 24])
    ])
    def test_valid_addition(func, iterable, expected):
        result = scanr(func, iterable)
>       assert result == expected
E       assert [24, 24, 12, 4] == [1, 2, 6, 24]
E         
E         At index 0 diff: 24 != 1
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_addition.py::test_valid_addition[multiply-iterable1-expected1]
========================= 1 failed, 1 passed in 0.10s ==========================
"""