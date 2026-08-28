# Module: string_utils.validation
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_isbn_checker_with_hyphens():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.input_string == '9783161484100'

def test_isbn_checker_without_normalization():
    checker = __ISBNChecker('978-3-16-148410-0', normalize=False)
    assert checker.input_string == '978-3-16-148410-0'

def test_isbn_checker_no_hyphens():
    checker = __ISBNChecker('9783161484100')
    assert checker.input_string == '9783161484100'

def test_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __ISBNChecker(1234567890)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_empty_string():
    checker = __ISBNChecker('')
    assert checker.input_string == ''

def test_only_hyphens():
    checker = __ISBNChecker('---')
    assert checker.input_string == ''
