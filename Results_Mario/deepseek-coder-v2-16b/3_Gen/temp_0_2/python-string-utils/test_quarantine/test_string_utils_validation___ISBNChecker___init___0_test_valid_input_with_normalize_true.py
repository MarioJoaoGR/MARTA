
import pytest
from string_utils.validation import is_string
from custom_exceptions import InvalidInputError

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string.replace('-', '') if normalize else input_string

def test_valid_input_with_normalize_true():
    checker = __ISBNChecker("978-0-13-235088-4", normalize=True)
    assert checker.input_string == "9780132350884"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""