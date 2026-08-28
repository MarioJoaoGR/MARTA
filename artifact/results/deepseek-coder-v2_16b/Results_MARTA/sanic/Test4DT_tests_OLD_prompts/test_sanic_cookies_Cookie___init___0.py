
import pytest
from sanic.cookies import Cookie



def test_valid_cookie():
    cookie = Cookie('valid_key', 'valid_value')
    assert cookie.key == 'valid_key'
    assert cookie.value == 'valid_value'