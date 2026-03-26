
import pytest
from string_utils.validation import __ISBNChecker
from custom_exceptions import InvalidInputError

def test_invalid_length_isbn_13():
    # Test an ISBN-13 number with invalid length (should be 13 characters)
    isbn_invalid = "978047005902"  # Missing the last digit
    
    checker = __ISBNChecker(isbn_invalid)
    
    assert not checker.is_isbn_13(), "Expected False for an invalid ISBN-13 number with length less than 13"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_invalid_length_isbn_13
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_invalid_length_isbn_13.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""