
import pytest
import base64
from ansible.plugins.filter.core import b64encode

def to_bytes(text, encoding='utf-8', errors='surrogate_or_strict'):
    return text.encode(encoding, errors)

def to_text(bytes_or_str, encoding='utf-8', errors='surrogate_or_strict'):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode(encoding, errors)
    return bytes_or_str

def test_valid_input_default_encoding():
    string = "Hello, World!"
    expected_output = 'SGVsbG8sIFdvcmxkIQ=='
    encoded_string = b64encode(string)
    assert to_text(base64.b64encode(to_bytes(string))) == expected_output

def test_valid_input_custom_encoding():
    string = "Hello, World!"
    encoding = 'utf-8'
    expected_output = 'SGVsbG8sIFdvcmxkIQ=='
    encoded_string = b64encode(string, encoding)
    assert to_text(base64.b64encode(to_bytes(string, encoding))) == expected_output
