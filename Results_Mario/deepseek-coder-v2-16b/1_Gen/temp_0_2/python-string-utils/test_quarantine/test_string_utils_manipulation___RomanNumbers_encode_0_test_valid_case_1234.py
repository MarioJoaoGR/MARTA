
import pytest
from roman_numerals import __RomanNumbers

def test_valid_case_1234():
    instance = __RomanNumbers()
    result = instance.encode(1234)
    assert result == 'MCCXXXIV'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___RomanNumbers_encode_0_test_valid_case_1234
python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_encode_0_test_valid_case_1234.py:3:0: E0401: Unable to import 'roman_numerals' (import-error)


"""