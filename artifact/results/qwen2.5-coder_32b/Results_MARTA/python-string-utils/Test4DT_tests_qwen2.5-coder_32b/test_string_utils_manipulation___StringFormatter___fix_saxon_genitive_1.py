
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_saxon_genitive():
    input_string = 'John s car'
    regex_match = re.search(r"(\b\w+)' s\b", f"{input_string} extra text")
    if regex_match:
        formatter = __StringFormatter(input_string)
        result = formatter._StringFormatter__fix_saxon_genitive(regex_match)
        assert result == "John's "




def test_valid_string_initialization():
    formatter = __StringFormatter('hello world')
    assert formatter.input_string == 'hello world'