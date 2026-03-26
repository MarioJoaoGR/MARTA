
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringConcatenation

def test_valid_inputs():
    s1 = SuperStringBase()
    s2 = s1 + "Hello"
    assert str(s2) == "Hello", "Expected 'Hello' but got something else."
    
    s3 = SuperStringBase()
    s4 = s3 + SuperString("World")
    assert s4.concatenate() == "World", "Expected 'World' but got something else."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___add___0_test_valid_inputs
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_inputs.py:12:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)


"""