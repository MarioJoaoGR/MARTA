
import pytest
from ansible.utils.vars import _isidentifier_PY2

# Test valid identifier
def test_valid_identifier():
    ident = 'my_variable'
    assert _isidentifier_PY2(ident) is True, f"Expected True for valid identifier '{ident}', but got False."

# Test invalid empty string
def test_invalid_empty_string():
    ident = ''
    assert _isidentifier_PY2(ident) is False, f"Expected False for empty string '{ident}', but got True."

# Test invalid reserved keyword
def test_invalid_reserved_keyword():
    ident = 'if'
    assert _isidentifier_PY2(ident) is False, f"Expected False for reserved keyword '{ident}', but got True."
