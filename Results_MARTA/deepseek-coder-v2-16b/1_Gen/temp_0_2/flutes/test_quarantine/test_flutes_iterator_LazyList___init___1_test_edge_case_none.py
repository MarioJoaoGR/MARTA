
import pytest
from lazy_list import LazyList

def test_edge_case_none():
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyList___init___1_test_edge_case_none
flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___1_test_edge_case_none.py:3:0: E0401: Unable to import 'lazy_list' (import-error)


"""