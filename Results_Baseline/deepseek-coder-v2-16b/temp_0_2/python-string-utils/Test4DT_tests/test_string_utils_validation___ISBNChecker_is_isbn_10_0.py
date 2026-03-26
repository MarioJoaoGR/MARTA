# Module: string_utils.validation
# test_string_utils_validation.py
from string_utils.validation import __ISBNChecker
import pytest

def is_string(input_string):
    # Mock function to check if input is a string
    return isinstance(input_string, str)

class InvalidInputError(Exception):
    pass

# Test cases for __ISBNChecker initialization with normalization and without normalization
@pytest.mark.parametrize("isbn, normalize, expected", [
    ('978-0-13-235088-4', True, '9780132350884'),
    ('978-0-13-235088-4', False, '978-0-13-235088-4'),
    ('0471606957', True, '0471606957'),
    ('0471606957', False, '0471606957')
])
def test_isbn_checker_init(isbn, normalize, expected):
    checker = __ISBNChecker(isbn, normalize=normalize)
    assert checker.input_string == expected

# Test cases for checking ISBN-10 validity
@pytest.mark.parametrize("isbn, normalize, expected", [
    ('1506715214', True, True),
    ('150-6715214', True, True),
    ('150-6715214', False, False),
    ('9780470059029', True, False)  # This should be ISBN-13
])
def test_isbn_checker_is_isbn_10(isbn, normalize, expected):
    checker = __ISBNChecker(isbn, normalize=normalize)
    assert checker.is_isbn_10() == expected

# Test cases for checking ISBN-13 validity (not applicable in this context as the method is specific to ISBN-10)
