
import pytest
from lazy_list import LazyList  # Assuming the module is named 'lazy_list' and contains the LazyList class

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    
    assert list(lazy_list) == [1, 2, 3, 4]
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    
    with pytest.raises(IndexError):
        lazy_list[4]  # Ensure accessing beyond the list raises an IndexError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___getitem___0_test_valid_input
flutes/Test4DT_tests/test_flutes_iterator_LazyList___getitem___0_test_valid_input.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""