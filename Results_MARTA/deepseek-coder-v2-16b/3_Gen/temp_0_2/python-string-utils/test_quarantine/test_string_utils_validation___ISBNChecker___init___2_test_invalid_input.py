
import pytest
from python_string_utils.__ISBNChecker import __ISBNChecker
from string_utils.validation import InvalidInputError, is_string

def test_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert str(excinfo.value) == "978-0-13-235088-4"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___2_test_invalid_input.py:3:0: E0401: Unable to import 'python_string_utils.__ISBNChecker' (import-error)


"""