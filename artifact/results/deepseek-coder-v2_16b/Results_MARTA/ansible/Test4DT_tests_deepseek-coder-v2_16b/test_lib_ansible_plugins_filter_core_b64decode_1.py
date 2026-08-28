
import pytest
import base64
from unittest.mock import patch

# Assuming to_text and to_bytes are defined as follows:
def to_text(data, encoding='utf-8', errors='strict'):
    return data.decode(encoding, errors)

def to_bytes(string, encoding='utf-8', errors='strict'):
    if string is None:
        return None
    return string.encode(encoding, errors)

# Function under test
def b64decode(string, encoding='utf-8'):
    return to_text(base64.b64decode(to_bytes(string, errors='surrogate_or_strict')), encoding=encoding)

# Test cases
@pytest.mark.parametrize("input_string, expected", [('SGVsbG8gV29ybGQ=', 'Hello World')])
def test_valid_input_happy_path(input_string, expected):
    assert b64decode(input_string) == expected

def test_edge_case_none():
    with pytest.raises(TypeError):
        b64decode(None)

def test_invalid_input_error_handling():
    with pytest.raises(base64.binascii.Error):
        b64decode('invalid-base64')
