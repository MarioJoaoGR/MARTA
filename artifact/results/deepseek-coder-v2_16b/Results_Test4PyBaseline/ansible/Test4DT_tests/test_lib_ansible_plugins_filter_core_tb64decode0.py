
import base64
from ansible.plugins.filter.core import b64decode

def test_b64decode_basic():
    result = b64decode('SGVsbG8gV29ybGQ=')
    assert result == 'Hello World'

def test_b64decode_specified_encoding():
    result = b64decode('SGVsbG8gV29ybGQ=', encoding='ascii')
    assert result == 'Hello World'

def test_b64decode_invalid_input():
    try:
        result = b64decode('invalid-base64-string')
    except ValueError as e:
        assert str(e) == "Error decoding base64 string: 'invalid-base64-string' is not a valid Base64 string."
