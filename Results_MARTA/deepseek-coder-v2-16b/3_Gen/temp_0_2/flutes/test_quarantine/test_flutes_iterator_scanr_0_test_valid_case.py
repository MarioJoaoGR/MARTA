
import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List

# Assuming add and mul are defined in a module named 'flutes.iterator'
def add(x, y): return x + y
def mul(x, y): return x * y

@pytest.mark.parametrize("func, iterable, initial, expected", [
    (add, [1, 2, 3], 0, [6, 5, 3, 0]),
    (mul, [1, 2, 3], 1, [3, 2, 1])
])
def test_valid_case(func, iterable, initial, expected):
    result = scanr(func, iterable, initial)
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
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py .F  [100%]

=================================== FAILURES ===================================
__________________ test_valid_case[mul-iterable1-1-expected1] __________________

func = <function mul at 0x7efc37c407c0>, iterable = [1, 2, 3], initial = 1
expected = [3, 2, 1]

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (add, [1, 2, 3], 0, [6, 5, 3, 0]),
        (mul, [1, 2, 3], 1, [3, 2, 1])
    ])
    def test_valid_case(func, iterable, initial, expected):
        result = scanr(func, iterable, initial)
>       assert result == expected
E       assert [6, 6, 3, 1] == [3, 2, 1]
E         
E         At index 0 diff: 6 != 3
E         Left contains one more item: 1
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py::test_valid_case[mul-iterable1-1-expected1]
========================= 1 failed, 1 passed in 0.08s ==========================
"""