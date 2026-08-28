
# Module: sanic.response
# test_basehttpresponse.py
from sanic.response import BaseHTTPResponse, Header, CookieJar
import pytest

@pytest.fixture
def base_http_response():
    response = BaseHTTPResponse()
    yield response

def test_initialization(base_http_response):
    assert base_http_response.asgi == False
    assert base_http_response.body is None
    assert base_http_response.content_type is None
    assert base_http_response.stream is None
    assert base_http_response.status is None
    assert isinstance(base_http_response.headers, Header)
    assert base_http_response._cookies is None

def test_setting_properties(base_http_response):
    base_http_response.status = 200
    base_http_response.content_type = 'application/json'
    base_http_response.body = b'{"message": "Hello, World!"}'
    
    assert base_http_response.status == 200
    assert base_http_response.content_type == 'application/json'
    assert base_http_response.body == b'{"message": "Hello, World!"}'

def test_cookies(base_http_response):
    cookies = base_http_response.cookies()
    assert isinstance(cookies, CookieJar)
    
    # Adding a cookie and checking if it is set correctly
    base_http_response.cookies["test"] = "It worked!"
    base_http_response.cookies["test"]["domain"] = ".yummy-yummy-cookie.com"
    base_http_response.cookies["test"]["httponly"] = True
    
    cookies = base_http_response.cookies()
    assert len(cookies) == 1
    assert cookies["test"].value == "It worked!"
    assert cookies["test"]["domain"] == ".yummy-yummy-cookie.com"
    assert cookies["test"]["httponly"] is True
