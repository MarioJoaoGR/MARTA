
import pytest
from lazy_list import LazyList

def test_none_input():
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___len___1_test_none_input
flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_none_input.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""