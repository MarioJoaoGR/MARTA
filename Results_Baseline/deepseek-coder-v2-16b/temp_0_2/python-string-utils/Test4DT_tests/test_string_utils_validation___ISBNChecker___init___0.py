
# Module: string_utils.validation
import pytest
from string_utils.errors import InvalidInputError
from string_utils.validation import __ISBNChecker

# Test cases for __ISBNChecker class initialization
def test_init_with_valid_isbn():
    checker = __ISBNChecker('978-0-13-235088-4')
    assert checker.input_string == '9780132350884'

def test_init_with_invalid_type():
    with pytest.raises(InvalidInputError) as e:
        __ISBNChecker(12345)