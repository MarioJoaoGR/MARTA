
import pytest
from httpie.models import HTTPMessage
from typing import Iterable

# Test cases for HTTPMessage class initialization
def test_http_message_init_with_valid_dict():
    valid_dict = {"key": "value"}
    http_message = HTTPMessage(valid_dict)
    assert hasattr(http_message, '_orig')
    assert http_message._orig == valid_dict

def test_http_message_init_with_valid_list():
    valid_list = ["item1", "item2"]
    http_message = HTTPMessage(valid_list)
    assert hasattr(http_message, '_orig')