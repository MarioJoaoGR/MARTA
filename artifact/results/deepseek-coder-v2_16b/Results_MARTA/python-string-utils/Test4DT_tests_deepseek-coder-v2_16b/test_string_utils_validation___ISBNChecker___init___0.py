
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

# Test for valid input with hyphens
def test_valid_input_with_hyphens():
    checker = __ISBNChecker('978-0-13-235088-4', normalize=True)
    assert checker.input_string == '9780132350884'

# Test for valid input without hyphens
def test_valid_input_without_hyphens():
    checker = __ISBNChecker('9780132350884', normalize=False)
    assert checker.input_string == '9780132350884'

# Test for invalid input
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(None)
