
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

    def format_string(self):
        pass

def test_edge_case():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)
