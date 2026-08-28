
import pytest
from unittest.mock import patch

def _get_quote_state(token, current_quote_state):
    '''
    the goal of this block is to determine if the quoted string
    is unterminated in which case it needs to be put back together
    '''
    # the char before the current one, used to see if
    # the current character is escaped
    prev_char = None
    for idx, cur_char in enumerate(token):
        if idx > 0:
            prev_char = token[idx - 1]
        if cur_char in '"\'' and prev_char != '\\':
            if current_quote_state:
                if cur_char == current_quote_state:
                    return None
            else:
                return cur_char
    return current_quote_state

# Test cases
def test_valid_case_1():
    result = _get_quote_state('hello "world"', None)
    assert result == '"'

def test_valid_case_2():
    result = _get_quote_state("hello 'world", None)
    assert result == "'"

def test_error_case():
    with pytest.raises(TypeError):
        _get_quote_state(42, None)  # Invalid input type (non-string)
