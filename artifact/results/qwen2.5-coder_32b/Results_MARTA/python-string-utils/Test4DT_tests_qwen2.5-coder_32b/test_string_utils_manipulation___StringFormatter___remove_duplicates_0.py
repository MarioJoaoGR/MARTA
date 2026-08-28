
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_string_initialization():
    input_string = "hello world"
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

def test_invalid_input_non_string():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_remove_duplicates():
    formatter = __StringFormatter("aaabbbcc")
    import re
    match = re.search(r'(.)\1*', "aaabbbcc")
    result = formatter._StringFormatter__remove_duplicates(match)
    assert result == 'a'
