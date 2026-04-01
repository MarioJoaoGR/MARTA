
import pytest
from lazy_list import LazyList

def test_error_case_invalid_index():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        lazy_list[10]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___getitem___2_test_error_case_invalid_index
flutes/Test4DT_tests/test_flutes_iterator_LazyList___getitem___2_test_error_case_invalid_index.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""