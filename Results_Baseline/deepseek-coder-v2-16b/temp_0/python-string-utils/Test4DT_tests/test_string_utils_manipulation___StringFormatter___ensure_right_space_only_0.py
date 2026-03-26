
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Helper function to simulate InvalidInputError for testing purposes
def is_string(input_data):
    return isinstance(input_data, str)

def test_valid_string():
    input_string = "valid string"
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)  # This should raise InvalidInputError since 12345 is not a string
