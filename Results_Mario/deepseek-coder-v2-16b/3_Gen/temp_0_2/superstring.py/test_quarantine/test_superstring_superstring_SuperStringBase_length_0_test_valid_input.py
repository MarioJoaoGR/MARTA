
from superstring.superstring import MyString  # Importing MyString from the correct module
import pytest

def test_valid_input():
    my_string = MyString("Hello, World!")
    assert my_string.length() == 13

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase_length_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_length_0_test_valid_input.py:2:0: E0611: No name 'MyString' in module 'superstring.superstring' (no-name-in-module)


"""