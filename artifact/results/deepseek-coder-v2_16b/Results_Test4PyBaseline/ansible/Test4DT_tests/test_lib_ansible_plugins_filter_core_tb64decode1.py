
import base64
from ansible.plugins.filter.core import b64decode
import pytest

def test_b64decode_basic():
    result = b64decode('SGVsbG8gV29ybGQ=')
    assert result == 'Hello World'

def test_b64decode_specified_encoding():
    result = b64decode('SGVsbG8gV29ybGQ=', encoding='ascii')
    assert result == 'Hello World'

def test_b64decode_invalid_input():
    with pytest.raises(ValueError) as e:
        b64decode('invalid-base64-string')