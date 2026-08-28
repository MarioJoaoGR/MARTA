# Module: string_utils.validation
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_isbn_checker_initialization_with_normalization():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.input_string == '9783161484100'

def test_isbn_checker_initialization_without_normalization():
    checker = __ISBNChecker('9783161484100', normalize=False)
    assert checker.input_string == '9783161484100'

def test_isbn_checker_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __ISBNChecker(1234567890)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_isbn_checker_valid_isbn_13():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.is_isbn_13() is True

def test_isbn_checker_invalid_isbn_13():
    checker = __ISBNChecker('9783161484101', normalize=False)
    assert checker.is_isbn_13() is False

def test_isbn_checker_valid_isbn_13_no_hyphens():
    checker = __ISBNChecker('9783161484100')
    assert checker.is_isbn_13() is True

def test_isbn_checker_invalid_length():
    checker = __ISBNChecker('978-3-16-148410', normalize=False)
    assert checker.is_isbn_13() is False

def test_isbn_checker_non_numeric_input():
    checker = __ISBNChecker('978-3-16-1A410-0')
    assert checker.is_isbn_13() is False
