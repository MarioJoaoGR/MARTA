
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_case():
    formatter = __StringFormatter('example  string')
    match = re.search(r'(\w+)', 'example  string')
    result = formatter._StringFormatter__ensure_right_space_only(match)
    assert result == "example "

def test_edge_case_empty_string():
    formatter = __StringFormatter('')
    match = re.search(r'(\w*)', '')
    result = formatter._StringFormatter__ensure_right_space_only(match)
    assert result == " "

def test_invalid_input_error_handling():
    formatter = __StringFormatter('example string')
    match = None
    try:
        formatter._StringFormatter__ensure_right_space_only(match)
    except AttributeError as e:
        assert str(e) == "'NoneType' object has no attribute 'group'"
