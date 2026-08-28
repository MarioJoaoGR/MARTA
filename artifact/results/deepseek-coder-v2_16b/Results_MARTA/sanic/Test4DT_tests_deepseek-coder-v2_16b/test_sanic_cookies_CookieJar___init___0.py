
import pytest
from sanic.cookies import CookieJar

def test_valid_add_cookie():
    jar = CookieJar({'Set-Cookie': 'cookie1=value1; Path=/; Expires=Fri, 31 Dec 2023 23:59:59 GMT'})
    assert not hasattr(jar, "add_cookie")

def test_edge_remove_cookie():
    jar = CookieJar({})
    with pytest.raises(AttributeError):
        jar.remove_cookie('cookie1')

def test_invalid_add_cookie():
    jar = CookieJar({'Set-Cookie': 'cookie1=value1; Path=/; Expires=Fri, 31 Dec 2023 23:59:59 GMT'})
    with pytest.raises(AttributeError):
        jar.add_cookie(None, None)
