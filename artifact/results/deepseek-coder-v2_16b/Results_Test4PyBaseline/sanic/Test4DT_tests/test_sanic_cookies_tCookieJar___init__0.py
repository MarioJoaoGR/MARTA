# Module: sanic.cookies
import pytest
from typing import Dict
from sanic.cookiesclass import CookieJar

# Test initialization with initial headers
def test_init_with_initial_headers():
    headers = {'Set-Cookie': 'session=abc123', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    assert isinstance(cookie_jar, CookieJar)
    assert cookie_jar.headers == headers
    assert cookie_jar.cookie_headers == {'Set-Cookie': 'session=abc123'}
    assert cookie_jar.header_key == "Set-Cookie"

# Test adding a new cookie
def test_add_cookie():
    headers = {}
    cookie_jar = CookieJar(headers)
    cookie_jar.add_cookie('user', 'user_data')
    assert cookie_jar.cookie_headers == {'Set-Cookie': 'user=user_data'}
    assert cookie_jar.headers == {'Set-Cookie': 'user=user_data'}

# Test removing an existing cookie
def test_remove_cookie():
    headers = {'Set-Cookie': 'session=abc123; user=user_data', 'Other-Header': 'value'}
    cookie_jar = CookieJar(headers)
    cookie_jar.remove_cookie('user')
    assert 'user' not in cookie_jar.cookie_headers
    assert 'Set-Cookie' not in cookie_jar.headers

# Test adding and removing cookies multiple times
def test_add_and_remove_cookies():
    headers = {}
    cookie_jar = CookieJar(headers)
    cookie_jar.add_cookie('user1', 'data1')
    cookie_jar.add_cookie('user2', 'data2')
    assert cookie_jar.cookie_headers == {'Set-Cookie': ['user1=data1', 'user2=data2']}
    assert cookie_jar.headers == {'Set-Cookie': ['user1=data1', 'user2=data2']}
    
    cookie_jar.remove_cookie('user1')
    assert 'user1' not in cookie_jar.cookie_headers
    assert 'Set-Cookie' not in cookie_jar.headers
    
    cookie_jar.add_cookie('user3', 'data3')
    assert cookie_jar.cookie_headers == {'Set-Cookie': ['user2=data2', 'user3=data3']}
    assert cookie_jar.headers == {'Set-Cookie': ['user2=data2', 'user3=data3']}
