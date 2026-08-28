
import pytest
from typing import Any

def recursive_unicode(obj: Any) -> Any:
    """Walks a simple data structure, converting byte strings to unicode.

    Supports lists, tuples, and dictionaries.
    """
    if isinstance(obj, dict):
        return dict(
            (recursive_unicode(k), recursive_unicode(v)) for (k, v) in obj.items()
        )
    elif isinstance(obj, list):
        return list(recursive_unicode(i) for i in obj)
    elif isinstance(obj, tuple):
        return tuple(recursive_unicode(i) for i in obj)
    elif isinstance(obj, bytes):
        return to_unicode(obj)
    else:
        return obj

def to_unicode(byte_string: bytes) -> str:
    """Converts a byte string to a Unicode string."""
    return byte_string.decode('utf-8')

# Test cases for recursive_unicode function

def test_valid_case_list():
    input_list = [b'hello', b'world']
    expected_output = ['hello', 'world']
    assert recursive_unicode(input_list) == expected_output

def test_valid_case_dict():
    input_dict = {'key1': b'value1', 'key2': b'value2'}
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    assert recursive_unicode(input_dict) == expected_output

def test_invalid_input():
    invalid_input = 42
    assert recursive_unicode(invalid_input) == invalid_input
