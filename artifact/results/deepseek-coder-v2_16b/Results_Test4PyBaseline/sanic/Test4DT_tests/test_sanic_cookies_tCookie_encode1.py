
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
    assert str(e.value) == "Cookie name is a reserved word"

# New test cases for encode method
def test_encode_method_with_valid_encoding():
    cookie = Cookie('my_cookie', 'my_value')
    encoded_cookie = cookie.encode('utf-8')
    assert isinstance(encoded_cookie, bytes)
    assert encoded_cookie == b'my_value'

def test_encode_method_with_invalid_encoding():
    cookie = Cookie('my_cookie', 'my_value')
    with pytest.raises(UnicodeEncodeError):
        cookie.encode('ascii')  # ascii does not support all characters in 'my_value'
