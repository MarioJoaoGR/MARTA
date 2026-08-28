
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

def prettify(input_string: str) -> str:
    formatted = __StringFormatter(input_string).format()
    return formatted

# Test for valid input

# Test for edge case with empty string

# Test for invalid input type
def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        prettify(__StringFormatter("unprettified string"))