# Module: sanic.response
import pytest
from your_http_response_module import BaseHTTPResponse
from typing import Iterator, Tuple

# Fixture to create a new instance of BaseHTTPResponse for each test
@pytest.fixture
def base_http_response():
    return BaseHTTPResponse()

def test_processed_headers_default(base_http_response):
    # Test default headers when no properties are set
    assert list(base_http_response.processed_headers()) == []

def test_processed_headers_with_status_and_content_type(base_http_response):
    base_http_response.status = 200
    base_http_response.content_type = 'text/html'
    base_http_response.headers['Content-Type'] = 'text/html'
    expected_headers = [(b'Content-Type', b'text/html')]
    assert list(base_http_response.processed_headers()) == expected_headers

def test_processed_headers_with_status_304(base_http_response):
    base_http_response.status = 304
    expected_headers = []
    assert list(base_http_response.processed_headers()) == expected_headers

def test_processed_headers_with_no_content_type_set(base_http_response):
    base_http_response.status = 200
    # Ensure content-type is set even if not explicitly provided
    headers = list(base_http_response.processed_headers())
    assert len(headers) == 1
    assert b'content-type' in {name for name, _ in headers}

def test_processed_headers_with_entity_headers_removed(base_http_response):
    base_http_response.status = 412
    expected_headers = []
    assert list(base_http_response.processed_headers()) == expected_headers

def test_processed_headers_with_message_body(base_http_response):
    base_http_response.status = 200
    base_http_response.content_type = 'application/json'
    headers = list(base_http_response.processed_headers())
    assert len(headers) == 1
    assert b'content-type' in {name for name, _ in headers}
