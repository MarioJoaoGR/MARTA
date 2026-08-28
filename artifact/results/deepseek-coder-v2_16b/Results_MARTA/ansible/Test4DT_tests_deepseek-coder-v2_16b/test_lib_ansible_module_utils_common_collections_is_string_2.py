
import pytest
from ansible.module_utils.common.collections import text_type, binary_type

def is_string(seq):
    """Identify whether the input has a string-like type (including bytes)."""
    return isinstance(seq, (text_type, binary_type)) or getattr(seq, '__ENCRYPTED__', False)

# Test cases

def test_valid_case_standard_string():
    assert is_string("Hello, World!")  # True, as it's a standard str

def test_valid_case_bytes():
    assert is_string(b"Hello, World!")  # True, as it's bytes

def test_invalid_case_none():
    assert not is_string(None)  # False, as None is not string-like

def test_invalid_case_list():
    assert not is_string([1, 2, 3])  # False, as it's a list and not string-like

def test_invalid_case_dict():
    assert not is_string({"key": "value"})  # False, as it's a dict and not string-like
