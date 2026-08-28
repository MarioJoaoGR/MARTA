
import pytest
from sanic.cookies import Cookie

def _is_legal_key(key):
    # This is a placeholder for the actual implementation of key validation
    # For simplicity, let's assume it checks if the key contains only legal characters (alphanumeric and underscore)
    return all(c.isalnum() or c == '_' for c in key)



def test_valid_key():
    cookie = Cookie('valid_key', 'admin')
    assert cookie.key == 'valid_key'
    assert cookie.value == 'admin'