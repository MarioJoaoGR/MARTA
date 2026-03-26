
import pytest
from superstring import SuperString

def test_split_default():
    s = SuperString("Hello, World!")
    assert s.split() == ['Hello,', 'World!']

def test_split_non_zero_previous():
    s = SuperString("Hello, World!")
    assert s.split(previous=1) == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperString_to_printable_0_test_edge_cases
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0_test_edge_cases.py:11:11: E1123: Unexpected keyword argument 'previous' in method call (unexpected-keyword-arg)


"""