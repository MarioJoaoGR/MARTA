
import re
import pytest
from string_utils.validation import is_string, InvalidInputError
from your_module_name.__ISBNChecker import __ISBNChecker  # Replace with actual module path

def test_invalid_isbn_10():
    checker = __ISBNChecker("0471606958")
    assert not checker.is_isbn_10(), "Expected False for invalid ISBN-10 number"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_isbn_10
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_isbn_10.py:5:0: E0401: Unable to import 'your_module_name.__ISBNChecker' (import-error)


"""