
import pytest
from lazy_list import LazyList  # Assuming the class is defined in a module named 'lazy_list'

def test_valid_input_single_index():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___getitem___0_test_valid_input_single_index
flutes/Test4DT_tests/test_flutes_iterator_LazyList___getitem___0_test_valid_input_single_index.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""