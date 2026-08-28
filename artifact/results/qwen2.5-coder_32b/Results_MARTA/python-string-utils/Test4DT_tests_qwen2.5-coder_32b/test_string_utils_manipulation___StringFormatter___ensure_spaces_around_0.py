
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_case():
    formatter = __StringFormatter('hello world')
    match = re.search(r'(world)', 'hello world')
    result = formatter._StringFormatter__ensure_spaces_around(match)
    assert result == ' world '

def test_edge_case_empty_string():
    formatter = __StringFormatter('')
    match = re.search(r'()', '')
    result = formatter._StringFormatter__ensure_spaces_around(match)
    assert result == '  '

def test_invalid_input_non_match_object():
    formatter = __StringFormatter('hello world')
    invalid_match = 'not a match object'
    try:
        formatter._StringFormatter__ensure_spaces_around(invalid_match)
    except AttributeError as e:
        assert str(e) == "'str' object has no attribute 'group'"

def test_invalid_input_non_string():
    try:
        __StringFormatter(123)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "int"'

def test_match_with_leading_trailing_spaces():
    formatter = __StringFormatter('hello   world')
    match = re.search(r'(world)', 'hello   world')
    result = formatter._StringFormatter__ensure_spaces_around(match)
    assert result == ' world '
