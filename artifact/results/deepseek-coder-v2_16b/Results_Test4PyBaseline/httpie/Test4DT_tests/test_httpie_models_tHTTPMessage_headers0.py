
import pytest
from httpie.models import HTTPMessage

def test_init_with_valid_dict():
    original_message = {
        'headers': {'Content-Type': 'application/json'},
        'body': b'{"key": "value"}'
    }
    http_message = HTTPMessage(original_message)
    assert isinstance(http_message._orig, dict), "Expected _orig to be a dictionary"
    assert http_message._orig == original_message, "_orig should match the provided dictionary"

def test_init_with_valid_list():
    original_message = [
        {'headers': {'Content-Type': 'application/json'}},
        b'{"key": "value"}'
    ]
    http_message = HTTPMessage(original_message)
    assert isinstance(http_message._orig, list), "Expected _orig to be a list"