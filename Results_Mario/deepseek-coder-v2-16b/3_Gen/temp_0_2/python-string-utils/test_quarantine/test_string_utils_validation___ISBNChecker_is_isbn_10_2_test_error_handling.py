
import pytest
from string_utils.validation import __ISBNChecker
from custom_exceptions import InvalidInputError

def test_isbn_10_valid():
    checker = __ISBNChecker("0471606957")
    assert checker.is_isbn_10() is True

def test_isbn_10_invalid_length():
    checker = __ISBNChecker("123456789X")  # Length is correct but invalid checksum
    assert checker.is_isbn_10() is False

def test_isbn_10_invalid_characters():
    with pytest.raises(InvalidInputError):
        __ISBNChecker("047160695A")  # Contains an invalid character 'A'

def test_isbn_10_valid_with_hyphens():
    checker = __ISBNChecker("0-471-60695-7")
    assert checker.is_isbn_10() is True

def test_isbn_10_invalid_checksum():
    checker = __ISBNChecker("0471606957")  # Valid length but incorrect checksum
    assert checker.is_isbn_10() is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_2_test_error_handling
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_2_test_error_handling.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""