
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

# Test case for iter_body method when it is not implemented
def test_iter_body_not_implemented():
    http_message = HTTPMessage({})  # Initialize with an empty dictionary to trigger the NotImplementedError
    chunk_size = 1024  # Specify a chunk size, though this should not matter since the method raises an error
    with pytest.raises(NotImplementedError):
        for _ in http_message.iter_body(chunk_size):
            pass
