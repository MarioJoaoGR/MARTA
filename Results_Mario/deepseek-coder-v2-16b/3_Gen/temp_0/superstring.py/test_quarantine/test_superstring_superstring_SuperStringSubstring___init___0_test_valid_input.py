
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_input():
    ss = SuperStringSubstring("Hello, World!", 7, 12)
    assert ss.get_substring() == 'World'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring___init___0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring___init___0_test_valid_input.py:7:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""