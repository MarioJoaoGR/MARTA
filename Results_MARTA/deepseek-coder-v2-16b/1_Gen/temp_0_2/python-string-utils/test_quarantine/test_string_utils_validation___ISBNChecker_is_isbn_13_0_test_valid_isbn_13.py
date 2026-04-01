
import pytest
from string_utils.validation import is_string
from your_module_containing_isbn_checker import __ISBNChecker

def test_valid_isbn_13():
    # Test a valid ISBN-13 number
    checker = __ISBNChecker("9780470059028")
    assert checker.is_isbn_13() is True

    # Test an invalid ISBN-13 number
    checker = __ISBNChecker("978-0-470-05902-8", normalize=False)
    assert checker.is_isbn_13() is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_valid_isbn_13
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_valid_isbn_13.py:4:0: E0401: Unable to import 'your_module_containing_isbn_checker' (import-error)


"""