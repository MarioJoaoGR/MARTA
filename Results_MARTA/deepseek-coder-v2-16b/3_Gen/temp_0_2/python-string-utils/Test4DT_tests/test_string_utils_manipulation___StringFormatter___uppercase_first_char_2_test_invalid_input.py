
import pytest
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert isinstance(exc_info.value, InvalidInputError)
