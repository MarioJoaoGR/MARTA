
import pytest
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(f"Expected a string but got {type(input_string).__name__}")
        
        self.input_string = input_string

    def format(self):
        import re
        
        def __ensure_spaces_around(self, regex_match):
            return ' ' + regex_match.group(1).strip() + ' '
        
        formatted_string = re.sub(r'(?<!\s)(\w+)(?!\s)', lambda m: __ensure_spaces_around(self, m), self.input_string)
        return formatted_string.strip()

def test_edge_case():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)
