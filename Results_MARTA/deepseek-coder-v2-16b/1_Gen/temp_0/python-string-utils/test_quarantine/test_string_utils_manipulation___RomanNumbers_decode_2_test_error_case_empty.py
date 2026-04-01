
import pytest
from __RomanNumbers import __RomanNumbers

def test_error_case_empty():
    with pytest.raises(ValueError):
        __RomanNumbers().decode('')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___RomanNumbers_decode_2_test_error_case_empty
python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_2_test_error_case_empty.py:3:0: E0401: Unable to import '__RomanNumbers' (import-error)

"""