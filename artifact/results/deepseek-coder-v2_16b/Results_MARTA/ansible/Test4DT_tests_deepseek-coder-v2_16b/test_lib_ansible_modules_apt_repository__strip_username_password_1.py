
import pytest

def _strip_username_password(s):
    if '@' in s:
        s = s.split('@', 1)
        s = s[-1]
    return s

# Test cases for the function _strip_username_password

def test_valid_input():
    s = 'user@example.com'
    assert _strip_username_password(s) == 'example.com'

def test_missing_at_symbol():
    s = 'example.com'
    assert _strip_username_password(s) == 'example.com'

def test_invalid_input():
    s = None
    with pytest.raises(TypeError):  # Since the function expects a string and does not handle NoneType well, it should raise a TypeError
        _strip_username_password(s)
