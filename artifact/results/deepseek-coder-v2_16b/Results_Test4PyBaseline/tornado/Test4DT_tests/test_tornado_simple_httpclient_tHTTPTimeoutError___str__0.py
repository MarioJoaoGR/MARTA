# Module: tornado.simple_httpclient
import pytest
from tornado.simple_httpclient import HTTPTimeoutError

# Test cases for HTTPTimeoutError class
def test_http_timeout_error_basic():
    with pytest.raises(HTTPTimeoutError) as exc_info:
        raise HTTPTimeoutError("Request timed out")
    assert str(exc_info.value) == "Request timed out"

def test_http_timeout_error_custom_message():
    custom_message = "Custom timeout message"
    with pytest.raises(HTTPTimeoutError) as exc_info:
        raise HTTPTimeoutError(custom_message)
    assert str(exc_info.value) == custom_message

def test_http_timeout_error_in_function():
    def make_request():
        raise HTTPTimeoutError("Request timed out")
    
    with pytest.raises(HTTPTimeoutError) as exc_info:
        make_request()
    assert str(exc_info.value) == "Request timed out"
