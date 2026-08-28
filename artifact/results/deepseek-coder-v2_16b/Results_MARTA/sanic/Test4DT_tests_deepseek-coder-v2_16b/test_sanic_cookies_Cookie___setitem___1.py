
import pytest
from sanic import Sanic
from sanic.cookies import Cookie
from datetime import datetime

# Test for invalid key

# Test for setting max-age with invalid type
def test_set_max_age():
    cookie = Cookie('test_key', 'test_value')
    with pytest.raises(ValueError):
        cookie['max-age'] = 'not_an_integer'

# Test for setting expires with invalid type
def test_set_expires():
    cookie = Cookie('test_key', 'test_value')
    with pytest.raises(TypeError):
        cookie['expires'] = 'not_a_datetime'