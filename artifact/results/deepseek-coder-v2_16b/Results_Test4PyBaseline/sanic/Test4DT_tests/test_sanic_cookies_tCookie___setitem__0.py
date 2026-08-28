
import pytest
from datetime import datetime
from sanic.cookies import Cookie

# Test creating a valid cookie instance
def test_valid_cookie_creation():
    key = 'my_cookie'
    value = 'my_value'
    cookie = Cookie(key, value)
    assert cookie.key == key