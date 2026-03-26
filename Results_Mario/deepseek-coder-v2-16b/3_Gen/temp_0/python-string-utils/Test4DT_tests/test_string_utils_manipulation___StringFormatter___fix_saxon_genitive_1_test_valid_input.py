
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    input_string = "valid string"
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

def test_invalid_input():
    invalid_input = 12345
    with pytest.raises(InvalidInputError):
        __StringFormatter(invalid_input)
