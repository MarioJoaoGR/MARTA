
import pytest
from ansible.module_utils.splitter import _get_quote_state

# Test for valid input with happy path scenario
def test_valid_input_happy_path():
    token = 'hello "world"'
    result = _get_quote_state(token, None)
    assert result == '"'

# Test for unterminated quote scenario
def test_unterminated_quote():
    token = 'hello \'world'
    result = _get_quote_state(token, None)
    assert result == "'"

# Test when no quotes are present scenario
def test_no_quotes():
    token = 'hello world'
    result = _get_quote_state(token, None)
    assert result is None
