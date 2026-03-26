
import pytest
from typing import Callable, Iterable, List, TypeVar

# Import the function from its module
from flutes.iterator import scanr

# Define type variables for generic types in the function signature
A = TypeVar('A')

# Test cases for scanr function
def test_scanr_sum():
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
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

flutes/Test4DT_tests/test_flutes_iterator_scanr_0.py F.                  [100%]

=================================== FAILURES ===================================
________________________________ test_scanr_sum ________________________________

    def test_scanr_sum():
        result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
>       assert result == [7, 5, 3, 1]
E       assert [10, 9, 7, 4] == [7, 5, 3, 1]
E         
E         At index 0 diff: 10 != 7
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanr_0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanr_0.py::test_scanr_sum
========================= 1 failed, 1 passed in 0.10s ==========================
"""