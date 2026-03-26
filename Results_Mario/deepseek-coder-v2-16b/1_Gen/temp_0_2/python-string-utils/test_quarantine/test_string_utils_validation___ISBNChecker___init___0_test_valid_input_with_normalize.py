
# Import necessary modules
from string_utils.validation import InvalidInputError
import pytest

# Define test case for valid input with normalization
def test_valid_input_with_normalize():
    # Test a valid ISBN-13 number that includes hyphens
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.input_string == "9783161484100"

    # Test a valid ISBN-10 number that includes hyphens
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.input_string == "9783161484100"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize.py:9:14: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize.py:13:14: E0602: Undefined variable '__ISBNChecker' (undefined-variable)


"""