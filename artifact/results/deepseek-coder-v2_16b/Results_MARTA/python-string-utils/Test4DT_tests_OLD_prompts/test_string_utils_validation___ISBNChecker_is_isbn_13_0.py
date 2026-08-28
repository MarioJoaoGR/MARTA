
import pytest
from string_utils.validation import __ISBNChecker

# Test valid ISBN-13 number

# Test invalid ISBN-13 number length
def test_invalid_length():
    checker = __ISBNChecker("978045145052")
    assert checker.input_string == "978045145052"
    assert checker.is_isbn_13() is False

# Test invalid characters in ISBN-13 number
def test_invalid_characters():
    checker = __ISBNChecker("978045145052a")
    assert checker.input_string == "978045145052a"
    assert checker.is_isbn_13() is False