
import pytest
from tornado import escape

def recursive_unicode(obj):
    if isinstance(obj, dict):
        return {recursive_unicode(k): recursive_unicode(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [recursive_unicode(i) for i in obj]
    elif isinstance(obj, tuple):
        return tuple(recursive_unicode(i) for i in obj)
    elif isinstance(obj, bytes):
        return escape.to_unicode(obj)
    else:
        return obj

def test_recursive_unicode_with_list():
    input_list = [b"hello", b"world"]
    expected_output = ['hello', 'world']
    assert recursive_unicode(input_list) == expected_output

def test_recursive_unicode_with_dict():
    input_dict = {"key1": b"value1", "key2": b"value2"}
    expected_output = {'key1': 'value1', 'key2': 'value2'}
    assert recursive_unicode(input_dict) == expected_output

def test_recursive_unicode_with_bytes():
    input_bytes = b"this is a test"
    expected_output = escape.to_unicode(input_bytes)
    assert recursive_unicode(input_bytes) == expected_output

def test_recursive_unicode_with_nested_structure():
    nested_structure = {
        "list": [b"item1", b"item2"],
        "tuple": (b"element1", b"element2"),
        "dict": {b"key1": b"value1"}
    }
    expected_output = {
        "list": ['item1', 'item2'],
        "tuple": ('element1', 'element2'),
        "dict": {'key1': 'value1'}
    }
    assert recursive_unicode(nested_structure) == expected_output

def test_recursive_unicode_with_non_supported_input():
    non_supported_input = 42
    assert recursive_unicode(non_supported_input) == non_supported_input
