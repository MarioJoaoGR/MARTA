
import pytest
from flutes.iterator import scanl

def test_valid_case():
    # Test with operator.add and a list of numbers, starting with 0
    assert scanr(lambda s, x: s + x, [1, 2, 3, 4], 0) == [10, 9, 7, 4, 0]
    
    # Test with a lambda function and a list of characters
    assert scanr(lambda s, x: s + x, ['a', 'b', 'c', 'd']) == ['abcd', 'bcd', 'cd', 'd']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_0_test_valid_case
flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py:7:11: E0602: Undefined variable 'scanr' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanr_0_test_valid_case.py:10:11: E0602: Undefined variable 'scanr' (undefined-variable)


"""