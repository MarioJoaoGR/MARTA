
import pytest
from superstring import SuperStringConcatenation

def test_invalid_input():
    with pytest.raises(TypeError):
        ssc = SuperStringConcatenation("Hello", 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_invalid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_invalid_input.py:3:0: E0611: No name 'SuperStringConcatenation' in module 'superstring' (no-name-in-module)


"""