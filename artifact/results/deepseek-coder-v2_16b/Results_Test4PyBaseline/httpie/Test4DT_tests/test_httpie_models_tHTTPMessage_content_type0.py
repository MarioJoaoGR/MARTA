
# Module: httpie.models
import pytest
from httpie.models import HTTPMessage
from typing import Iterable

# Test case 1: Creating an instance by copying another HTTPMessage instance
def test_http_message_init():
    original_message = {
        'headers': {'Content-Type': b'text/plain'},
        'body': b'Hello, world!'
    }
    http_message = HTTPMessage(original_message)
    assert isinstance(http_message._orig, dict), "The orig should be a dictionary"
    assert 'headers' in http_message._orig, "The original message should contain headers"