# Module: sanic.cookies
import pytest
from sanic.cookies import CookieJar

# Test initialization with initial headers
def test_init_with_initial_headers():
    headers = {'Set-Cookie': 'session=abc123', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    assert cookie_jar.headers == headers
    assert cookie_jar.cookie_headers == {}
    assert cookie_jar.header_key == "Set-Cookie"

# Test adding a new cookie
def test_add_cookie():
    headers = {'Set-Cookie': 'session=abc123', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    cookie_jar.add_cookie('user', 'user_data')
    assert "user" in cookie_jar.cookie_headers
    assert cookie_jar.cookie_headers["user"] == "user_data"
    assert cookie_jar.headers["Set-Cookie"] == "session=abc123; user=user_data"

# Test removing an existing cookie
def test_remove_cookie():
    headers = {'Set-Cookie': 'session=abc123; user=user_data', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    cookie_jar.remove_cookie('user')
    assert "user" not in cookie_jar.cookie_headers
    assert cookie_jar.headers["Set-Cookie"] == "session=abc123"

# Test removing a non-existing cookie
def test_remove_non_existing_cookie():
    headers = {'Set-Cookie': 'session=abc123', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    cookie_jar.remove_cookie('nonexistent')
    assert "nonexistent" not in cookie_jar.cookie_headers
    assert cookie_jar.headers["Set-Cookie"] == "session=abc123"

# Test deleting an item from the cookie jar
def test_delitem():
    headers = {'Set-Cookie': 'session=abc123; user=user_data', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    del cookie_jar['user']
    assert "user" not in cookie_jar.cookie_headers
    assert cookie_jar.headers["Set-Cookie"] == "session=abc123"
