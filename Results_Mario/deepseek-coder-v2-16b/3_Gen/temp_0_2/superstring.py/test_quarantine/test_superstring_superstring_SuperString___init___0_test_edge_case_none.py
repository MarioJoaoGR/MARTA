
import pytest
from superstring.superstring import SuperString

def test_edge_case_none():
    s = SuperString(None)
    assert s.split() == []
    assert s.split(previous=1) == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperString___init___0_test_edge_case_none
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_edge_case_none.py:8:11: E1123: Unexpected keyword argument 'previous' in method call (unexpected-keyword-arg)


"""