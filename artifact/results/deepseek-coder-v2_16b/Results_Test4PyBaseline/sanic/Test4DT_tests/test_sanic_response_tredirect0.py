
import pytest
from sanic.response import redirect
from urllib.parse import quote_plus
from typing import Dict, Optional

# Test cases for the redirect function
def test_redirect_basic():
    response = redirect(to="https://example.com")
    assert response.status == 302
    assert response.headers["Location"] == "https://example.com"
    assert response.content_type == "text/html; charset=utf-8"

def test_redirect_with_custom_headers():
    headers_dict: Dict[str, str] = {"X-Custom-Header": "Value"}
    response = redirect(to="https://example.com", headers=headers_dict)
    assert response.status == 302
    assert response.headers["Location"] == "https://example.com"
    assert response.headers["X-Custom-Header"] == "Value"
    assert response.content_type == "text/html; charset=utf-8"

def test_redirect_with_different_status_and_content_type():
    response = redirect(to="https://example.com", status=301, content_type="text/plain")
    assert response.status == 301
    assert response.headers["Location"] == "https://example.com"