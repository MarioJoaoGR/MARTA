
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_valid_isbn_10():
    checker = __ISBNChecker('0-306-40615-2')
    assert checker.is_isbn_10() is True

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(1234567890)

def test_edge_cases():
    # Test None input
    with pytest.raises(InvalidInputError):
        __ISBNChecker(None)
    
    # Test empty string
    checker = __ISBNChecker('')
    assert checker.is_isbn_10() is False
    
    # Test incorrect length
    checker = __ISBNChecker('123456789')
    assert checker.is_isbn_10() is False
