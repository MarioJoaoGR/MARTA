
import pytest
from httpie.models import HTTPMessage

# Test case 1: Creating an instance of HTTPMessage with a valid dictionary representation of an HTTP message
def test_http_message_init_with_dict():
    original_message = {"headers": {}, "body": b"example content"}
    http_message = HTTPMessage(original_message)
    assert hasattr(http_message, '_orig')
    assert http_message._orig == original_message

# Test case 2: Creating an instance of HTTPMessage with a valid list representation of an HTTP message
def test_http_message_init_with_list():
    original_message = [{"headers": {}, "body": b"example content"}]
    http_message = HTTPMessage(original_message)
    assert hasattr(http_message, '_orig')