# Module: sanic.helpers
import pytest
from sanic.helpers import remove_entity_headers

# Test cases for remove_entity_headers function

def test_remove_entity_headers_basic():
    headers = {'Content-Type': 'text/html', 'Expires': 'Thu, 01 Dec 2023 16:00:00 GMT', 'Last-Modified': 'Wed, 28 Nov 2023 00:00:00 GMT'}
    result = remove_entity_headers(headers)
    assert result == {'Content-Type': 'text/html'}

def test_remove_entity_headers_custom_allowed():
    headers = {'Cache-Control': 'max-age=604800', 'Expires': 'Thu, 01 Dec 2023 16:00:00 GMT', 'Set-Cookie': 'session_id=abc123; expires=Thu, 01-Jan-2024 00:00:00 GMT'}
    allowed = ("content-location", "expires")
    result = remove_entity_headers(headers, allowed)
    assert result == {'Cache-Control': 'max-age=604800', 'Set-Cookie': 'session_id=abc123; expires=Thu, 01-Jan-2024 00:00:00 GMT'}

def test_remove_entity_headers_no_allowed():
    headers = {'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=20'}
    result = remove_entity_headers(headers)
    assert result == {'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=20'}

def test_remove_entity_headers_empty():
    headers = {}
    result = remove_entity_headers(headers)
    assert result == {}

# Additional edge cases can be added to ensure robustness
