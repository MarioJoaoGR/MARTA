
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable

def add(x: int, y: int) -> int:
    return x + y

# Test data
test_data = [
    (add, [1, 2, 3, 4], 0, [0, 1, 3, 6, 10]),
    (add, [5, -1, 2], 10, [10, 5, 4, 6]),
    (lambda x, y: x * y, [2, 3, 4], 1, [1, 2, 6, 24]),
]

@pytest.mark.parametrize("func, iterable, initial, expected", test_data)
def test_valid_inputs(func, iterable, initial, expected):
    result = list(scanl(func, iterable, initial))
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
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_inputs.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
________________ test_valid_inputs[add-iterable1-10-expected1] _________________

func = <function add at 0x7f19cfa2f380>, iterable = [5, -1, 2], initial = 10
expected = [10, 5, 4, 6]

    @pytest.mark.parametrize("func, iterable, initial, expected", test_data)
    def test_valid_inputs(func, iterable, initial, expected):
        result = list(scanl(func, iterable, initial))
>       assert result == expected
E       assert [10, 15, 14, 16] == [10, 5, 4, 6]
E         
E         At index 1 diff: 15 != 5
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_inputs.py::test_valid_inputs[add-iterable1-10-expected1]
========================= 1 failed, 2 passed in 0.08s ==========================
"""