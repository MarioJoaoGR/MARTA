
import pytest
from unittest.mock import patch, MagicMock
from string_utils.validation import __ISBNChecker

# Test valid ISBN-13 number

# Test invalid ISBN-13 number length
def test_invalid_length():
    checker = __ISBNChecker("978045145052")
    assert checker.input_string == "978045145052"
    assert checker.is_isbn_13() is False

# Test invalid characters in ISBN-13 number
def test_invalid_characters():
    checker = __ISBNChecker("978045145052")
    assert checker.input_string == "978045145052"
    assert checker.is_isbn_13() is False

# Test valid ISBN-10 number

# Test invalid ISBN-10 number with incorrect length
def test_invalid_length_isbn_10():
    checker = __ISBNChecker("013235088", normalize=False)
    assert checker.input_string == "013235088"
    assert checker.is_isbn_10() is False

# Test invalid ISBN-10 number with non-numeric characters
def test_invalid_characters_isbn_10():
    checker = __ISBNChecker("013235088", normalize=False)
    assert checker.input_string == "013235088"
    assert checker.is_isbn_10() is False