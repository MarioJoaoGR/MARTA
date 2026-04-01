
import pytest
from superstring import SuperStringUpper, SuperStringBase

def test_valid_input():
    base_string = SuperStringBase('hello, world!')
    upper_string = SuperStringUpper(base_string)
    assert upper_string.length() == len('HELLO, WORLD!')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringUpper_length_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_length_0_test_valid_input.py:3:0: E0611: No name 'SuperStringUpper' in module 'superstring' (no-name-in-module)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_length_0_test_valid_input.py:3:0: E0611: No name 'SuperStringBase' in module 'superstring' (no-name-in-module)


"""