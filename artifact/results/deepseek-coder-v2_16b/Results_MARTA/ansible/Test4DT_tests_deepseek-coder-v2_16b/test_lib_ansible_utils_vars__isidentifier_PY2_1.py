
import pytest
from ansible.utils.vars import _isidentifier_PY2

# Test valid identifier
def test_valid_identifier():
    ident = 'my_variable'
    assert _isidentifier_PY2(ident) is True, f"Expected {ident} to be a valid Python identifier."

# Test invalid identifier starting with a digit
def test_invalid_start_with_digit():
    ident = '123abc'
    assert _isidentifier_PY2(ident) is False, f"Expected {ident} to be an invalid Python identifier."

# Test empty string as an identifier
def test_empty_string():
    ident = ''
    assert _isidentifier_PY2(ident) is False, f"Expected {ident} to be an invalid Python identifier."
