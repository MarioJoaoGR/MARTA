
import re
from unittest.mock import patch
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(f"Expected a string but got {type(input_string).__name__}")
        
        self.input_string = input_string

    def format(self):
        import re
        formatted_string = re.sub(r'\s*(.*?)\s*', self.__remove_internal_spaces, self.input_string)
        return formatted_string

    def __remove_internal_spaces(self, regex_match):
        return regex_match.group(1).strip()

def test_valid_input():
    with patch('string_utils.manipulation.is_string', return_value=True):
        formatter = __StringFormatter("Hello, World!")
        assert formatter.input_string == "Hello, World!"
        formatted_result = formatter.format()
        assert formatted_result == "Hello,World!"
