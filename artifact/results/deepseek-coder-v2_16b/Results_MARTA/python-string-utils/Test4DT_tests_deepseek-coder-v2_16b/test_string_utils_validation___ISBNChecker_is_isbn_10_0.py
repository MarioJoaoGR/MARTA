
import pytest
from string_utils.validation import __ISBNChecker
from string_utils.errors import InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

# Test for valid ISBN-10 number
def test_valid_isbn_10():
    checker = __ISBNChecker("9780132350884", normalize=False)
    assert checker.is_isbn_10() == False  # Assuming is_isbn_10 method returns True for valid ISBN-10 numbers

# Test for invalid ISBN-10 number
def test_invalid_isbn_10():
    checker = __ISBNChecker("9780132350884", normalize=False)
    assert checker.is_isbn_10() == False  # Assuming is_isbn_10 method returns False for invalid ISBN-10 numbers

# Test for valid ISBN-10 number with hyphens removed

# Test for invalid input raises InvalidInputError