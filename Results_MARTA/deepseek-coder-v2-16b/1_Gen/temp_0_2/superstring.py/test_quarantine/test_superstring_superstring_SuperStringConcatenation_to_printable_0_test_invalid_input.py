
import pytest
from superstring.superstring import SuperStringConcatenation

def test_invalid_input():
    with pytest.raises(TypeError):
        ssc = SuperStringConcatenation("Hello", "World")
        ssc.concat()  # This should raise a TypeError because concat is not defined in the class

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_invalid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_invalid_input.py:8:8: E1101: Instance of 'SuperStringConcatenation' has no 'concat' member (no-member)


"""