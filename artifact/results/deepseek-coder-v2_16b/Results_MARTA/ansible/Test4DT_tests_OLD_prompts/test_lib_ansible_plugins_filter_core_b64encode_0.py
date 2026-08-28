
import pytest
from ansible.plugins.filter.core import b64encode

def test_valid_encoding():
    input_string = "Hello, World!"
    encoded_string = b64encode(input_string)
    assert encoded_string == 'SGVsbG8sIFdvcmxkIQ=='
