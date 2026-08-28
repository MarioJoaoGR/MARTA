
import pytest
from string_utils.validation import __ISBNChecker

# Test valid ISBN-10 number

# Test invalid ISBN-10 number with incorrect length
def test_invalid_length_isbn_10():
    checker = __ISBNChecker('978013235088', normalize=False)
    assert checker.is_isbn_10() is False

# Test invalid ISBN-10 number with non-numeric characters
def test_invalid_characters_isbn_10():
    checker = __ISBNChecker('978013235088a', normalize=False)
    assert checker.is_isbn_10() is False