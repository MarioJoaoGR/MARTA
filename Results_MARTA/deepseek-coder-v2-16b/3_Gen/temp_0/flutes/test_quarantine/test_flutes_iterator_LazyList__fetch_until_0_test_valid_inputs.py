
import pytest
from lazylist import LazyList  # Assuming the module is named 'lazylist' and contains the LazyList class

def test_valid_inputs():
    lst = LazyList([1, 2, 3, 4])
    
    # Access elements of the lazy list one by one
    for i in range(4):
        assert lst[i] == i + 1
    
    # Check that accessing beyond the end raises an IndexError
    with pytest.raises(IndexError):
        lst[4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList__fetch_until_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_valid_inputs.py:3:0: E0401: Unable to import 'lazylist' (import-error)


"""