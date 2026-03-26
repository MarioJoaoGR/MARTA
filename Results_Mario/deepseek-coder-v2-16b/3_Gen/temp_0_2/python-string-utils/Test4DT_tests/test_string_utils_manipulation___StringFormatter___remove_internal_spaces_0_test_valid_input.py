
import re
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

    def format_string(self):
        return re.sub(r'\s+', ' ', self.input_string).strip()

def test_valid_input():
    formatter = __StringFormatter("  Hello   World!  ")
    assert formatter.format_string() == "Hello World!"
