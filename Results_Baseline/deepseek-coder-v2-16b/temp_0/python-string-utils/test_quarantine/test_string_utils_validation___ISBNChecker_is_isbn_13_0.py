
# Module: string_utils.validation
import pytest
from string_utils.validation import __ISBNChecker

# Test cases for __ISBNChecker class initialization and normalization
def test_init_with_default_normalize():
    checker = __ISBNChecker("978-0-13-235088-4")
    assert checker.input_string == "9780132350884"

def test_init_without_normalize():
    checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert checker.input_string == "978-0-13-235088-4"

def test_init_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(123456)

# Test cases for is_isbn_13 method
def test_valid_isbn_13():
    checker = __ISBNChecker("9780470059029")
    assert checker.is_isbn_13() == True

def test_invalid_isbn_13():
    checker = __ISBNChecker("978-0-470-05902-9", normalize=False)
    assert checker.is_isbn_13() == False

# Additional edge cases and invalid inputs can be added to ensure robustness

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_0
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py:16:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)

"""