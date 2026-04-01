
import pytest
from string_utils.validation import is_string, InvalidInputError
from __ISBNChecker import __ISBNChecker

def test_valid_input_with_normalize_false():
    # Arrange
    input_string = "978-0-13-235088-4"
    
    # Act
    checker = __ISBNChecker(input_string, normalize=False)
    
    # Assert
    assert checker.input_string == input_string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___1_test_valid_input_with_normalize_false
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_valid_input_with_normalize_false.py:4:0: E0401: Unable to import '__ISBNChecker' (import-error)


"""