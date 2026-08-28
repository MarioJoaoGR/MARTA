
import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

# Define a custom container class for testing
class MyContainer:
    def __init__(self, data):
        self.data = data

def test_register_custom_container():
    # Test registering a custom container type
    register_no_map_class(MyContainer)
    assert MyContainer in _NO_MAP_TYPES

def test_register_builtin_list():
    # Test registering the built-in list type
    register_no_map_class(list)
    assert list in _NO_MAP_TYPES

def test_register_builtin_dict():
    # Test registering the built-in dict type
    register_no_map_class(dict)
    assert dict in _NO_MAP_TYPES


def test_register_twice():
    # Test registering the same type twice does not raise an error and only adds once
    register_no_map_class(MyContainer)
    initial_length = len(_NO_MAP_TYPES)
    register_no_map_class(MyContainer)
    assert len(_NO_MAP_TYPES) == initial_length

def test_unregister_type():
    # Test unregistering a type by removing it from _NO_MAP_TYPES
    register_no_map_class(MyContainer)
    _NO_MAP_TYPES.remove(MyContainer)
    assert MyContainer not in _NO_MAP_TYPES