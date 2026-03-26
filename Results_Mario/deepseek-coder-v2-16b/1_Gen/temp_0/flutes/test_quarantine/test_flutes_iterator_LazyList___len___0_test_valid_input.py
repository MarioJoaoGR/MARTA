
import pytest
from lazy_list import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___len___0_test_valid_input
flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_valid_input.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""