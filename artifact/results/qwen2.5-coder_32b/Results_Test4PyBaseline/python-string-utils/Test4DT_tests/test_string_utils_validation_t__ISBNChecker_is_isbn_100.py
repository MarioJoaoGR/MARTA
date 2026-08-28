# Module: string_utils.validation
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_isbn_checker_initialization_with_normalization():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.input_string == '9783161484100'

def test_isbn_checker_initialization_without_normalization():
    checker_no_normalize = __ISBNChecker('9783161484100', normalize=False)
    assert checker_no_normalize.input_string == '9783161484100'

def test_isbn_checker_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __ISBNChecker(1234567890)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_isbn_checker_valid_isbn_10():
    isbn_10_checker = __ISBNChecker('0306406152')
    assert isbn_10_checker.is_isbn_10() is True

def test_isbn_checker_invalid_isbn_10():
    invalid_isbn_10_checker = __ISBNChecker('0306406153')
    assert invalid_isbn_10_checker.is_isbn_10() is False

def test_isbn_checker_non_numeric_input():
    non_numeric_checker = __ISBNChecker('0306A06152')
    assert non_numeric_checker.is_isbn_10() is False

def test_isbn_checker_too_short_input():
    short_input_checker = __ISBNChecker('030640615')
    assert short_input_checker.is_isbn_10() is False

def test_isbn_checker_too_long_input():
    long_input_checker = __ISBNChecker('03064061520')
    assert long_input_checker.is_isbn_10() is False
