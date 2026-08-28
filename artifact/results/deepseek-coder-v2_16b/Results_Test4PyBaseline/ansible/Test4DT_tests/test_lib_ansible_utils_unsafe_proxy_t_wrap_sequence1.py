
import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence, wrap_var

# Test cases for _wrap_sequence function

def test_wrap_sequence_with_tuple():
    original_tuple = (1, 2, "unsafe", [3, 4])
    wrapped_tuple = _wrap_sequence(original_tuple)
    assert isinstance(wrapped_tuple, tuple), "The result should be a tuple"
    for item in wrapped_tuple:
        assert isinstance(item, wrap_var(type(item))), f"Item {item} should be of type {type(item)}"

def test_wrap_sequence_with_list():
    original_list = [1, 2, "unsafe", [3, 4]]
    wrapped_list = _wrap_sequence(original_list)
    assert isinstance(wrapped_list, list), "The result should be a list"
    for item in wrapped_list:
        assert isinstance(item, wrap_var(type(item))), f"Item {item} should be of type {type(item)}"

def test_wrap_sequence_with_empty():
    original_tuple = (1, 2, "unsafe", [3, 4])  # Define the variable here
    empty_sequence = () if isinstance(original_tuple, tuple) else []  # Use the same type as original_tuple or list
    wrapped_empty = _wrap_sequence(empty_sequence)
    assert isinstance(wrapped_empty, type(empty_sequence)), f"The result should be of type {type(empty_sequence)}"

def test_wrap_sequence_with_nested():
    nested_sequence = (1, [2, "unsafe", [3, 4]], {"key": "value"})
    wrapped_nested = _wrap_sequence(nested_sequence)
    assert isinstance(wrapped_nested, tuple), "The result should be a tuple"
    for item in wrapped_nested:
        if isinstance(item, (tuple, list)):
            assert isinstance(item, type(item)), f"Nested item {item} should be of type {type(item)}"
        elif isinstance(item, dict):
            assert isinstance(item, dict), "The result should be a dictionary"
        else:
            assert isinstance(item, wrap_var(type(item))), f"Item {item} should be of type {type(item)}"
