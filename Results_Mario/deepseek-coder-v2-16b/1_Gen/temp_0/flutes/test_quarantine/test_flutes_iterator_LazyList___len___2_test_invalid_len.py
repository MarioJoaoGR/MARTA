
import pytest
from lazy_list import LazyList

def test_invalid_len():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___len___2_test_invalid_len
flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_invalid_len.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""