
import pytest
import base64
from ansible.plugins.filter.core import b64decode

def to_bytes(string, errors='surrogate_or_strict'):
    return string.encode('utf-8') if isinstance(string, str) else string

def to_text(bytes_obj, encoding='utf-8', errors='surrogate_or_strict'):
    return bytes_obj.decode(encoding) if isinstance(bytes_obj, bytes) else bytes_obj

# Test case for normal base64 decoding
def test_normal_b64decode():
    assert b64decode('SGVsbG8gV29ybGQ=') == 'Hello World'

# Test case for specifying encoding during decoding
def test_encoding_b64decode():
    assert b64decode('SGVsbG8gV29ybGQ=', encoding='ascii') == 'Hello World'.encode('ascii').decode()

# Test case for handling non-base64 input gracefully