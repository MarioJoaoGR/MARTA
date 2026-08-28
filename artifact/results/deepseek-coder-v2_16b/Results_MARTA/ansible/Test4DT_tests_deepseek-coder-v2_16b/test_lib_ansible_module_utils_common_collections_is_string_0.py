
import pytest
from ansible.module_utils.common.collections import text_type, binary_type

def is_string(seq):
    """Identify whether the input has a string-like type (including bytes)."""
    return isinstance(seq, (text_type, binary_type)) or getattr(seq, '__ENCRYPTED__', False)

# Test cases for is_string function

def test_valid_string():
    assert is_string("Hello, World!") == True

def test_valid_bytes():
    assert is_string(b"Hello, World!") == True

def test_invalid_types():
    assert is_string([1, 2, 3]) == False
    assert is_string({"key": "value"}) == False
