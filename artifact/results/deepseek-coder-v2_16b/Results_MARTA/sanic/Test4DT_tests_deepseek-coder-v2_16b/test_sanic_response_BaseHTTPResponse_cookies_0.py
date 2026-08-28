
import pytest
from sanic.response import BaseHTTPResponse

def test_valid_cookies_creation():
    response = BaseHTTPResponse()
    response.cookies["test"] = "It worked!"
    assert response.cookies["test"].value == "It worked!"
    response.cookies["test"]["domain"] = ".yummy-yummy-cookie.com"
    response.cookies["test"]["httponly"] = True
    cookies_dict = dict(response.cookies)  # Convert the cookie jar to a dictionary for comparison
    assert cookies_dict["test"].value == "It worked!"
    assert cookies_dict["test"]["domain"] == ".yummy-yummy-cookie.com"
    assert cookies_dict["test"]["httponly"] is True

def test_missing_lines_to_cover():
    response = BaseHTTPResponse()
    response.cookies['test'] = 'It worked!'
    assert hasattr(response, '_cookies')
    assert isinstance(response._cookies, dict)  # Sanic's CookieJar is internally a dictionary-like object
