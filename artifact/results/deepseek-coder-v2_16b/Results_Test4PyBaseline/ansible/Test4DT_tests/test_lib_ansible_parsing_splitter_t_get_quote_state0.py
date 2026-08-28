
import pytest
from ansible.parsing.splitter import _get_quote_state

# Test cases for _get_quote_state function

def test_no_quote():
    result = _get_quote_state('hello world', None)
    assert result is None, f"Expected None but got {result}"

def test_single_quoted_string():
    result = _get_quote_state("hello 'world'", None)
    assert result == "'", f"Expected single quote ('') but got {result}"

def test_double_quoted_string():
    result = _get_quote_state('he"llo "world"', None)
    assert result == '"', f"Expected double quote (\") but got {result}"

def test_escaped_quote_character():
    result = _get_quote_state('he\"llo \"world\"', '"')
    assert result == '"', f"Expected double quote (\") but got {result}"

def test_unterminated_double_quoted_string():
    result = _get_quote_state('hello world', None)
    assert result is None, f"Expected None but got {result}"

def test_escaped_escaped_quote_character():
    result = _get_quote_state('he\\"llo \\"world\\"', '"')
    assert result == '"', f"Expected double quote (\") but got {result}"
