
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test___ISBNChecker_is_isbn_13_basic():
    # Test basic functionality of is_isbn_13 method
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() == True

def test___ISBNChecker_invalid_input_type():
    # Test that InvalidInputError is raised for non-string input
    with pytest.raises(InvalidInputError):
        __ISBNChecker(1234567890)

def test___ISBNChecker_no_normalization_valid_isbn_13():
    # Test valid ISBN-13 without normalization
    checker = __ISBNChecker('9783161484100', normalize=False)
    assert checker.is_isbn_13() == True

def test___ISBNChecker_no_normalization_invalid_isbn_13():
    # Test invalid ISBN-13 without normalization
    checker = __ISBNChecker('9783161484101', normalize=False)
    assert checker.is_isbn_13() == False

def test___ISBNChecker_valid_isbn_13_with_hyphens():
    # Test valid ISBN-13 with hyphens
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() == True

def test___ISBNChecker_invalid_length():
    # Test invalid length input
    checker = __ISBNChecker('978316148410')
    assert checker.is_isbn_13() == False

def test___ISBNChecker_non_digit_characters():
    # Test input with non-digit characters (excluding hyphens)
    checker = __ISBNChecker('978-3-16-1A410-0')
    assert checker.is_isbn_13() == False
