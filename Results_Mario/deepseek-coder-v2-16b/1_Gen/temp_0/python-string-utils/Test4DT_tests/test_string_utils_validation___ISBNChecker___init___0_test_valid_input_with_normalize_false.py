
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_valid_input_with_normalize_false():
    # Test that an ISBN-13 number is correctly normalized when initialize with normalize=False
    checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert checker.input_string == "978-0-13-235088-4"
