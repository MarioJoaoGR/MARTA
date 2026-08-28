
import pytest
from httpie.models import HTTPMessage

# Test case 1: Creating an instance by copying another HTTPMessage instance
def test_http_message_init():
    original_message = {
        'headers': {'Content-Type': b'text/plain'},
        'body': b'Hello, world!'
    }
    http_message = HTTPMessage(original_message)
    assert hasattr(http_message, '_orig'), "The instance should have an '_orig' attribute"
    assert isinstance(http_message._orig, dict), "The '_orig' attribute should be a dictionary"
    assert 'headers' in http_message._orig, "The dictionary should contain 'headers'"
    assert 'body' in http_message._orig, "The dictionary should contain 'body'"

# Test case 2: Content-Type header present as bytes
def test_content_type_bytes():
    original_message = {
        'headers': {'Content-Type': b'text/plain'},
        'body': b'Hello, world!'
    }
    http_message = HTTPMessage(original_message)