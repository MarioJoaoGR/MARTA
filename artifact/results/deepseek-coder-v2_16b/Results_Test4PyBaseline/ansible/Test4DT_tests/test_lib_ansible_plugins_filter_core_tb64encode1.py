
import base64
from ansible.plugins.filter.core import b64encode
import pytest

def test_b64encode_default_encoding():
    encoded_string = b64encode("Hello, World!")
    assert encoded_string == 'SGVsbG8sIFdvcmxkIQ=='

def test_b64encode_explicit_utf_8():
    encoded_string = b64encode("Hello, World!", encoding='utf-8')