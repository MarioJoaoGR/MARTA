
import pytest
from httpie.models import HTTPMessage

# Test initialization of HTTPMessage with a valid original message
def test_http_message_initialization():
    orig = "GET /index HTTP/1.1\r\nHost: example.com\r\nContent-Type: text/html\r\n\r\n<html><body>Hello, World!</body></html>"
    http_message = HTTPMessage(orig)
    assert http_message._orig == orig

# Test initialization of HttpRequest with method, path, headers, and body

# Test accessing headers from HttpRequest subclass

# Test raising NotImplementedError when calling headers on HTTPMessage base class
def test_http_message_headers():
    http_message = HTTPMessage("GET /index HTTP/1.1\r\nHost: example.com\r\nContent-Type: text/html\r\n\r\n<html><body>Hello, World!</body></html>")
    with pytest.raises(NotImplementedError):
        http_message.headers()