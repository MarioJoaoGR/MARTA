
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.headers import HeaderBytesIterable

# Define a dictionary to mock _HTTP1_STATUSLINES for testing
_HTTP1_STATUSLINES = {
    200: b"HTTP/1.1 200 OK\r\n",
    404: b"HTTP/1.1 404 Not Found\r\n"
}

def format_http1_response(status: int, headers: HeaderBytesIterable) -> bytes:
    """Format a HTTP/1.1 response header."""
    ret = _HTTP1_STATUSLINES[status]
    for h in headers:
        ret += b"%b: %b\r\n" % h
    ret += b"\r\n"
    return ret

# Test cases
def test_valid_http_response():
    status = 200
    headers = [(b"Content-Type", b"text/html"), (b"Server", b"MyServer")]
    expected_output = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nServer: MyServer\r\n\r\n'
    assert format_http1_response(status, headers) == expected_output

