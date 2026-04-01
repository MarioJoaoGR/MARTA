
import pytest
from flutes.iterator import scanl

def test_edge_case_none():
    # Test when the iterable is empty and no initial value is provided
    assert scanr(lambda x, y: x + y, []) == []

    # Test with a non-empty list and no initial value
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]

    # Test with a string iterable
    result = scanr(lambda x, y: x + y, "abcd")
    assert result == ["abcd", "bcd", "cd", "d"]

    # Test with a list and an initial value
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_1_test_edge_case_none
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case_none.py:7:11: E0602: Undefined variable 'scanr' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case_none.py:10:13: E0602: Undefined variable 'scanr' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case_none.py:14:13: E0602: Undefined variable 'scanr' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case_none.py:18:13: E0602: Undefined variable 'scanr' (undefined-variable)

"""