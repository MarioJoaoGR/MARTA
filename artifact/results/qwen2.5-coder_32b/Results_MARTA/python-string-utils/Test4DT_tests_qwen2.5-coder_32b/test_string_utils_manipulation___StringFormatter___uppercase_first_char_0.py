
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError



def test_uppercase_first_char_empty_string():
    formatter = __StringFormatter('')
    match = re.match(r'\w*', '')
    result = formatter._StringFormatter__uppercase_first_char(match)
    assert result == ''

def test_uppercase_first_char_single_character():
    formatter = __StringFormatter('a')
    match = re.match(r'\w+', 'a')
    result = formatter._StringFormatter__uppercase_first_char(match)
    assert result == 'A'