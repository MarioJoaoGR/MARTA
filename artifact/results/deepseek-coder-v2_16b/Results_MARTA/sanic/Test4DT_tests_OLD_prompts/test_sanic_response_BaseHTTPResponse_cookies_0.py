
import pytest
from unittest.mock import patch, MagicMock
from sanic.response import BaseHTTPResponse

# Test scenario 1: Creating a new instance of BaseHTTPResponse and setting attributes

# Test scenario 2: Using the cookies method to manage cookies in the response
def test_basehttpresponse_cookies():
    response = BaseHTTPResponse()
    with patch('sanic.response.CookieJar', new=MagicMock()) as mock_cookiejar:
        assert isinstance(response.cookies(), MagicMock)
        mock_cookiejar.assert_called_once_with(response.headers)

# Test scenario 3: Adding headers to the response
def test_basehttpresponse_add_headers():
    response = BaseHTTPResponse()
    response.headers['Content-Type'] = 'application/json'
    response.headers['X-Custom-Header'] = 'SomeValue'
    assert response.headers == {'Content-Type': 'application/json', 'X-Custom-Header': 'SomeValue'}

# Test scenario 4: Setting the status code and body content for a response