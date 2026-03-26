
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker(12345)  # Test invalid input type (int)
