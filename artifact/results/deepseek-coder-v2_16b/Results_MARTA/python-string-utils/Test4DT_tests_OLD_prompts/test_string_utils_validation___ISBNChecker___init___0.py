
import pytest
from unittest.mock import patch
from string_utils.validation import __ISBNChecker, InvalidInputError

# Test for valid input with hyphens and normalization enabled
def test_valid_input_with_hyphens():
    checker = __ISBNChecker('978-0-13-235088-4', normalize=True)
    assert checker.input_string == '9780132350884'

# Test for valid input without normalization enabled
def test_valid_input_without_hyphens():
    checker = __ISBNChecker('9780132350884', normalize=False)
    assert checker.input_string == '9780132350884'

# Test for invalid input raising InvalidInputError
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker(None, normalize=True)
