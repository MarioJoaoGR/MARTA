
from python_string_utils.string_utils.validation import __ISBNChecker
import pytest

def test_valid_input_with_normalize_true():
    checker = __ISBNChecker("978-0-13-235088-4", normalize=True)
    assert checker.input_string == "9780132350884"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true.py:2:0: E0401: Unable to import 'python_string_utils.string_utils.validation' (import-error)


"""