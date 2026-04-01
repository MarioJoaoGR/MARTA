
from string_utils.validation import __ISBNChecker
import pytest

def test_valid_input_with_normalize_false():
    # Test with valid input and normalize set to False
    checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert checker.input_string == "978-0-13-235088-4"
