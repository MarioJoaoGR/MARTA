
import pytest
from ansible.utils.vars import _isidentifier_PY3
import keyword
from six import string_types

# Test valid identifier
def test_valid_identifier():
    ident = 'my_variable'
    assert _isidentifier_PY3(ident) is True, f"Expected {ident} to be a valid identifier"

# Test invalid identifier starting with a digit
def test_invalid_start_with_digit():
    ident = '123abc'
    assert _isidentifier_PY3(ident) is False, f"Expected {ident} to be an invalid identifier"

# Test invalid identifier being a keyword
def test_invalid_keyword():
    ident = 'if'
    assert _isidentifier_PY3(ident) is False, f"Expected {ident} to be an invalid identifier due to being a keyword"

# Test invalid identifier containing non-ASCII characters
def test_invalid_non_ascii():
    ident = 'ünicode'
    assert _isidentifier_PY3(ident) is False, f"Expected {ident} to be an invalid identifier due to containing non-ASCII characters"

# Test handling None input
def test_none_input():
    ident = None
    assert _isidentifier_PY3(ident) is False, f"Expected None to be considered as an invalid identifier"

# Test handling an empty string
def test_empty_string():
    ident = ''
    assert _isidentifier_PY3(ident) is False, f"Expected an empty string to be considered as an invalid identifier"

# Test handling a non-string type
def test_invalid_type():
    ident = 12345
    assert _isidentifier_PY3(ident) is False, f"Expected a non-string type ({type(ident)}) to be considered as an invalid identifier"
