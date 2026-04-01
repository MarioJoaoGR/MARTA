
import pytest
from string_utils.manipulation import InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)
