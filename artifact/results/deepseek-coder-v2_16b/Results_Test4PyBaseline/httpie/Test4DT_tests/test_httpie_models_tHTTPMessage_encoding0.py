# Module: httpie.models
import pytest
from httpie.models import HTTPMessage

# Test creating an instance by copying another HTTPMessage instance
def test_http_message_init_with_dict():
    original_message = {
        "headers": {"Content-Type": "application/json"},
        "body": b'{"key": "value"}'
    }
    http_message = HTTPMessage(original_message)
    assert isinstance(http_message._orig, dict), "The original message should be a dictionary."
    assert http_message._orig == original_message, "The copied message should match the original."

# Test creating an instance with a dictionary representing an HTTP request
def test_http_message_init_with_request_dict():
    request_dict = {
        "method": "GET",
        "url": "http://example.com/api",
        "headers": {"User-Agent": "PythonHTTPClient"},
        "body": b""
    }
    http_message = HTTPMessage(request_dict)
    assert isinstance(http_message._orig, dict), "The original message should be a dictionary."
    assert http_message._orig == request_dict, "The copied message should match the original request dictionary."

# Test creating an instance with a list representing an HTTP response
def test_http_message_init_with_response_list():
    response_list = [
        "HTTP/1.1 200 OK",
        {"Content-Type": "application/json"},
        b'{"status": "success"}'
    ]
    http_message = HTTPMessage(response_list)
    assert isinstance(http_message._orig, list), "The original message should be a list."
    assert http_message._orig == response_list, "The copied message should match the original response list."

# Test creating an instance with an invalid type (should raise TypeError)
def test_http_message_init_with_invalid_type():
    try:
        invalid_input = "not a valid HTTP message"
        http_message = HTTPMessage(invalid_input)
    except TypeError as e:
        assert str(e) == "orig must be a dictionary or list representing an HTTP message", "The error message should match the expected error."
