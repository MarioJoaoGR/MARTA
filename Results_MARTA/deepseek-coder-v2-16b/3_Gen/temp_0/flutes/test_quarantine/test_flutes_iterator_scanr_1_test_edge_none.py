
import pytest
from flutes.iterator import scanr

# Test cases for scanr function
@pytest.mark.parametrize("func, iterable, expected", [
    (add, [], []),
    (multiply, [], []),
    (add, [1], [1]),
    (multiply, [1], [1]),
    (add, [1, 2, 3, 4], [10, 9, 7, 4]),
    (multiply, [1, 2, 3, 4], [1, 2, 6, 24]),
])
def test_scanr(func, iterable, expected):
    result = scanr(func, iterable)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_1_test_edge_none
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:7:5: E0602: Undefined variable 'add' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:8:5: E0602: Undefined variable 'multiply' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:9:5: E0602: Undefined variable 'add' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:10:5: E0602: Undefined variable 'multiply' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:11:5: E0602: Undefined variable 'add' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_none.py:12:5: E0602: Undefined variable 'multiply' (undefined-variable)

"""