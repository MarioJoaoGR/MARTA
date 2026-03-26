
import pytest
from lazylist import LazyList  # Assuming 'lazylist' is the module name where LazyList is defined

def test_valid_inputs():
    lst = LazyList([1, 2, 3, 4])
    
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert lst[3] == 4
    
    with pytest.raises(IndexError):
        lst[4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList__fetch_until_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_0_test_valid_inputs.py:3:0: E0401: Unable to import 'lazylist' (import-error)


"""