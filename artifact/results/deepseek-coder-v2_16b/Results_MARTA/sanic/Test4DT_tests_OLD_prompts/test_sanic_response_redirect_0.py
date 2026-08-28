
import pytest
from unittest.mock import patch
from sanic import Sanic, HTTPResponse
from sanic.response import redirect as sanic_redirect
from urllib.parse import quote_plus
from typing import Dict, Optional

# Define the function to be tested
def redirect(
    to: str,
    headers: Optional[Dict[str, str]] = None,
    status: int = 302,
    content_type: str = "text/html; charset=utf-8",
) -> HTTPResponse:
    """
    Abort execution and cause a redirect to the specified URL or path with optional headers.
    The function sets a `Location` header in the response pointing to the provided URL (`to`), using the default status code of 302.
    It also supports customizing the content type of the response through the `content_type` parameter.
    
    Parameters:
        to (str): The path or fully qualified URL to which the client should be redirected. This string will be percent-encoded for safety in URLs.
        headers (Optional[Dict[str, str]]): A dictionary of additional HTTP headers to include in the response. If not provided, an empty dictionary is used. Note that this function ensures the `Location` header is always included and properly set.
        status (int): The HTTP status code for the redirection response. Defaults to 302. Other common values include 301 (Moved Permanently) and 307 (Temporary Redirect).
        content_type (str): The MIME type of the content being sent in the response. This defaults to "text/html; charset=utf-8" but can be adjusted as needed for different content types like "application/json" or custom text formats.
    
    Returns:
        HTTPResponse: An instance of the `HTTPResponse` class, initialized with the provided status code, headers, and content type. The response includes a `Location` header pointing to the specified URL.
    """
    headers = headers or {}
    safe_to = quote_plus(to, safe=":/%#?&=@[]!$&'()*+,;")
    headers["Location"] = safe_to
    return HTTPResponse(status=status, headers=headers, content_type=content_type)

# Test cases for the redirect function
def test_valid_input():
    with patch('sanic.response.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com")
        assert response.status == 302
        assert response.headers['Location'] == 'https://example.com'
        assert response.content_type == "text/html; charset=utf-8"

def test_custom_headers():
    with patch('sanic.response.quote_plus', return_value='https://example.com'):
        custom_headers = {"X-Custom-Header": "Value"}
        response = redirect("https://example.com", headers=custom_headers)
        assert response.status == 302
        assert response.headers['Location'] == 'https://example.com'
        assert response.headers['X-Custom-Header'] == 'Value'
        assert response.content_type == "text/html; charset=utf-8"


def test_custom_status_and_content_type():
    with patch('sanic.response.quote_plus', return_value='https://example.com'):
        response = redirect("https://example.com", status=301, content_type="application/json")
        assert response.status == 301
        assert response.headers['Location'] == 'https://example.com'
        assert response.content_type == "application/json"