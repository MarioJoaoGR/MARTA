# Module: sanic.headers
import pytest
from sanic.headers import format_http1_response, HeaderBytesIterable

# Define a simple fixture for the headers iterable
@pytest.fixture
def headers():
    return [(b"X-Custom-Header", b"Value")]

# Test cases for format_http1_response function
def test_format_http1_response_simple_ok_response(headers):
    response = format_http1_response(200, headers)
    assert response == b'HTTP/1.1 200 OK\r\nX-Custom-Header: Value\r\n\r\n'

def test_format_http1_response_unauthorized_response():
    headers = [(b"WWW-Authenticate", b'Basic realm="Secure Area"')]
    response = format_http1_response(401, headers)
    assert response == b'HTTP/1.1 401 Unauthorized\r\nWWW-Authenticate: Basic realm="Secure Area"\r\n\r\n'

def test_format_http1_response_no_content_response():
    response = format_http1_response(204, [])
    assert response == b'HTTP/1.1 204 No Content\r\n\r\n'

def test_format_http1_response_internal_server_error_response():
    headers = [(b"Retry-After", b"3600")]
    response = format_http1_response(500, headers)
    assert response == b'HTTP/1.1 500 Internal Server Error\r\nRetry-After: 3600\r\n\r\n'

def test_format_http1_response_custom_status_code_with_multiple_headers():
    headers = [(b"X-Custom-Header", b"Value"), (b"Content-Type", b"application/json")]
    response = format_http1_response(409, headers)
    assert response == b'HTTP/1.1 409 Conflict\r\nX-Custom-Header: Value\r\nContent-Type: application/json\r\n\r\n'
