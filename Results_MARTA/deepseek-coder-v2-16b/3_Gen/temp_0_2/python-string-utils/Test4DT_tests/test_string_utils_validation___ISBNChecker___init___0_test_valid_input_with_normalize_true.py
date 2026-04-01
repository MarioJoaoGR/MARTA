
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_valid_input_with_normalize_true():
    # Test with valid input and normalize=True
    checker = __ISBNChecker("978-0-13-235088-4")
    assert checker.input_string == "9780132350884"

    # Test with valid input and normalize=False
    checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert checker.input_string == "978-0-13-235088-4"
