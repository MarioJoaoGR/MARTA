
import pytest
from python_string_utils.manipulation import __RomanNumbers

def test_valid_case_2():
    assert __RomanNumbers.__encode_digit(0, 3) == 'III'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_2
python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_2.py:3:0: E0401: Unable to import 'python_string_utils.manipulation' (import-error)


"""