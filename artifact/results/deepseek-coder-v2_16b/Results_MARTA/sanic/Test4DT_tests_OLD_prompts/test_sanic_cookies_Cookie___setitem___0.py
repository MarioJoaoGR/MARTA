
import pytest
from sanic import Sanic
from sanic.cookies import Cookie
from datetime import datetime

# Test for invalid key that is a reserved word

# Test for unknown key

# Test for setting max-age to a non-integer value
def test_max_age_non_integer():
    my_cookie = Cookie('username', 'admin')
    with pytest.raises(ValueError) as e:
        my_cookie['max-age'] = "not an integer"
    assert str(e.value) == "Cookie max-age must be an integer"

# Test for setting expires to a non-datetime value
def test_expires_non_datetime():
    my_cookie = Cookie('username', 'admin')
    with pytest.raises(TypeError) as e:
        my_cookie['expires'] = "not a datetime"
    assert str(e.value) == "Cookie 'expires' property must be a datetime"