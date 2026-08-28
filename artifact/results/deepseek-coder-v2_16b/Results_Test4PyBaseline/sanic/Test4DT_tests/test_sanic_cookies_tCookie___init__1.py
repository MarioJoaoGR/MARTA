
import pytest
from sanic.cookies import Cookie

# Test cases for the Cookie class
def test_valid_cookie():
    cookie = Cookie('my_cookie', 'my_value')
    assert cookie.key == 'my_cookie'
    assert cookie.value == 'my_value'

def test_invalid_reserved_word_key():
    with pytest.raises(KeyError) as e:
        Cookie('expires', 'bad_value')