
import pytest
from flutes.iterator import scanr

def test_valid_case():
    assert list(scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['abcd', 'bcd', 'cd', 'd']
    assert list(scanr(operator.add, [1, 2, 3, 4], 0)) == [10, 9, 7, 4, 0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_0_test_valid_case
flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py:7:22: E0602: Undefined variable 'operator' (undefined-variable)


"""