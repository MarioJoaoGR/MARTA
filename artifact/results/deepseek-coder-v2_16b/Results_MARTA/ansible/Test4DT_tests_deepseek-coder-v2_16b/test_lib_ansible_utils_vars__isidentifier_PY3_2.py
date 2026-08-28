
import pytest
from ansible.utils.vars import _isidentifier_PY3
import keyword

# Test valid identifier
def test_valid_identifier():
    ident = 'my_variable'
    assert _isidentifier_PY3(ident) is True, f"Expected '{ident}' to be a valid identifier"

# Test invalid identifier starting with a digit
def test_invalid_starts_with_digit():
    ident = '123abc'
    assert _isidentifier_PY3(ident) is False, f"Expected '{ident}' to be an invalid identifier"

# Test invalid identifier being a keyword
def test_invalid_keyword():
    ident = 'if'
    assert _isidentifier_PY3(ident) is False, f"Expected '{ident}' to be an invalid identifier due to being a keyword"
