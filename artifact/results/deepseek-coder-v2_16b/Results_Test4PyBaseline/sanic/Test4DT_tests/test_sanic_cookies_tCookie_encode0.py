
import pytest
from sanic.cookies import Cookie

# Test cases for Cookie class
def test_cookie_valid():
    cookie = Cookie('my_cookie', 'my_value')
    assert cookie.key == 'my_cookie'
    assert cookie.value == 'my_value'

def test_cookie_reserved_key():
    with pytest.raises(KeyError) as e:
        Cookie('expires', 'bad_value')