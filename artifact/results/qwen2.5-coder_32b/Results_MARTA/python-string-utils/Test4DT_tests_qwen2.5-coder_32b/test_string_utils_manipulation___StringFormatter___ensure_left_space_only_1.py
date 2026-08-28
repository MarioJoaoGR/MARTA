
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_case():
    formatter = __StringFormatter('example string')
    match = re.search(r'(\w+)', ' example ')
    result = formatter._StringFormatter__ensure_left_space_only(match)
    assert result == ' example'

def test_edge_case_empty_string():
    formatter = __StringFormatter('empty test')
    match = re.search(r'(\w*)', '')
    result = formatter._StringFormatter__ensure_left_space_only(match)
    assert result == ' '

def test_invalid_input_error_handling():
    with pytest.raises(InvalidInputError):
        __StringFormatter(123)

# Ensure pytest is imported if not already
import pytest
