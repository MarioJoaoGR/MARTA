
import pytest
from superstring.superstring import SuperStringConcatenation

def test_error_case():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.concatenate() == "HelloWorld"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_error_case
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_error_case.py:7:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)


"""