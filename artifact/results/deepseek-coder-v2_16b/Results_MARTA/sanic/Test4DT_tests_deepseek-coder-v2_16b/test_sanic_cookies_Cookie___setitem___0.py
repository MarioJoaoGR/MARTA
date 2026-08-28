
import pytest
from datetime import datetime
from sanic.cookies import Cookie

# Test Scenario 1: Test setting valid cookie properties
def test_valid_input():
    my_cookie = Cookie('username', 'admin')
    assert my_cookie.key == 'username'
    assert my_cookie.value == 'admin'

# Test Scenario 2: Test raising KeyError for invalid key characters or reserved words
def test_invalid_key():
    with pytest.raises(KeyError):
        illegal_cookie = Cookie('path', 'illegal')

# Test Scenario 3: Test raising ValueError and TypeError for incorrect property types
def test_error_handling():
    my_cookie = Cookie('username', 'admin')
    with pytest.raises(ValueError):
        my_cookie['max-age'] = "not an integer"
    with pytest.raises(TypeError):
        my_cookie['expires'] = "not a datetime"
