# Module: dataclasses_json.core
import pytest
from typing import List
import collections

# Import the function from its module
from dataclasses_json.core import _resolve_collection_type_to_decode_to as resolve_func

def test_resolve_generic_type():
    my_list = [1, 2, 3]
    resolved_type = resolve_func(my_list.__class__)
    assert resolved_type == list, f"Expected {list}, but got {resolved_type}"

def test_resolve_builtin_type():
    resolved_type = resolve_func([1, 2, 3].__class__)
    assert resolved_type == list, f"Expected {list}, but got {resolved_type}"

def test_resolve_non_generic_type():
    resolved_type = resolve_func(int)
    assert resolved_type == int, f"Expected {int}, but got {resolved_type}"

def test_resolve_none_input():
    resolved_type = resolve_func(None)
    assert resolved_type is None, f"Expected None, but got {resolved_type}"

# Additional edge cases can be added here to ensure robustness
