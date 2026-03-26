
import pytest
from string_utils.errors import InvalidInputError

def process_string(input_data):
    if not isinstance(input_data, str):
        raise InvalidInputError(input_data)
    return True

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        process_string([1, 2, 3])  # List is an invalid input type expected to raise the error
