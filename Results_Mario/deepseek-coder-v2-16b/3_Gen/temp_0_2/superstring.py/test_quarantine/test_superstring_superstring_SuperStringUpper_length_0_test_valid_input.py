
import pytest
from superstring.superstring import SuperString

def test_valid_input():
    s = SuperString('Hello, World!')
    upper_str = SuperStringUpper(s)
    assert upper_str.length() == len("HELLO, WORLD!")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringUpper_length_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_length_0_test_valid_input.py:7:16: E0602: Undefined variable 'SuperStringUpper' (undefined-variable)


"""