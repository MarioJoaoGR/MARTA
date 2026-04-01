
import pytest
from string_utils.manipulation import InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(123)
