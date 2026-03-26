
import pytest
from lazy_list import LazyList

def test_error_handling():
    lst = LazyList([1, 2, 3, 4])
    
    # Test accessing a valid index
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert lst[3] == 4
    
    # Test accessing an invalid index that raises IndexError
    with pytest.raises(IndexError):
        lst[4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___getitem___1_test_error_handling
flutes/Test4DT_tests/test_flutes_iterator_LazyList___getitem___1_test_error_handling.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""