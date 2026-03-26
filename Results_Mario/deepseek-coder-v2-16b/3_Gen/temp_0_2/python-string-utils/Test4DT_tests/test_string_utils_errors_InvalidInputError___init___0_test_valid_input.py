
from string_utils.errors import InvalidInputError
import pytest

def process_string(input_data):
    if not isinstance(input_data, str):
        raise InvalidInputError(input_data)
    return input_data

def test_valid_input():
    # Test with a valid string input
    assert process_string("valid_string") == "valid_string"

def test_invalid_input():
    # Test with an invalid input type (e.g., list)
    with pytest.raises(InvalidInputError):
        process_string([1, 2, 3])
