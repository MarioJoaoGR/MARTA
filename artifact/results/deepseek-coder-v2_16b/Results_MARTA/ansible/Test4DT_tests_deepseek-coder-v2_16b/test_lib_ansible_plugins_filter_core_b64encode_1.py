
import pytest
from ansible.plugins.filter.core import b64encode

def test_b64encode_default_encoding():
    string = "Hello, World!"
    encoded_string = b64encode(string)
    assert encoded_string == 'SGVsbG8sIFdvcmxkIQ=='
