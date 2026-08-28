
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

# Test for valid ISBN-13 number

# Test for non-normalized ISBN-13 number

# Test for invalid input
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(12345)