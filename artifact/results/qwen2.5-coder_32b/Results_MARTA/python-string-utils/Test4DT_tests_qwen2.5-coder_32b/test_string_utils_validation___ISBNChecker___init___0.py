
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def is_string(value):
    return isinstance(value, str)

# Test a valid ISBN-13 number with hyphens and default normalization (True)
def test_valid_isbn_13_with_hyphens():
    checker = __ISBNChecker('978-3-16-148410-0')
    assert checker.input_string == '9783161484100'

# Test a valid ISBN-10 number without hyphens and normalization set to False
def test_valid_isbn_10_without_hyphens():
    checker = __ISBNChecker('0306406152', normalize=False)
    assert checker.input_string == '0306406152'

# Test an invalid input type (integer instead of string)
def test_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __ISBNChecker(1234567890)
    assert str(excinfo.value) == 'Expected "str", received "int"'
