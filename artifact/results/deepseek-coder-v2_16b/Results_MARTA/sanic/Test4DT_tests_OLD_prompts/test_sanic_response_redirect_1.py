
import pytest
from unittest.mock import patch
from sanic import HTTPResponse
from sanic.response import redirect

def test_redirect_with_full_url():
    with patch('urllib.parse.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com")
        assert response is not None
        assert response.status == 302
        assert response.headers['Location'] == 'https://example.com'


def test_redirect_with_custom_headers():
    custom_headers = {"X-Custom-Header": "Value"}
    with patch('urllib.parse.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com", headers=custom_headers)
        assert response is not None
        assert response.status == 302
        assert response.headers['Location'] == 'https://example.com'
        assert response.headers['X-Custom-Header'] == 'Value'

def test_redirect_with_custom_status():
    with patch('urllib.parse.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com", status=301)
        assert response is not None
        assert response.status == 301
        assert response.headers['Location'] == 'https://example.com'

def test_redirect_with_custom_content_type():
    with patch('urllib.parse.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com", content_type="application/json")
        assert response is not None
        assert response.status == 302
        assert response.headers['Location'] == 'https://example.com'
        assert response.content_type == "application/json"