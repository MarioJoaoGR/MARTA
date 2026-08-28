
import pytest
from sanic.cookies import Cookie
from datetime import datetime

# Test creating a valid Cookie instance
def test_valid_cookie():
    cookie = Cookie('my_cookie', 'my_value')
    assert cookie.key == 'my_cookie'
    assert cookie.value == 'my_value'

# Test handling an invalid key (reserved word)
def test_invalid_key():
    with pytest.raises(KeyError):
        Cookie('expires', 'bad_value')

# Test setting properties of the Cookie
def test_set_properties():
    cookie = Cookie('name', 'value')