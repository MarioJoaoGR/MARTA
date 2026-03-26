
import pytest
from typing import List, Dict, Set, Tuple
from dataclasses_json.core import _resolve_collection_type_to_decode_to

def test_resolve_list():
    my_list = [1, 2, 3]
    resolved_type = _resolve_collection_type_to_decode_to(my_list.__class__)
    assert isinstance(resolved_type, type) and issubclass(resolved_type, list), f"Expected a subclass of list but got {resolved_type}"

def test_resolve_dict():
    my_dict = {'key': 'value'}
    resolved_type = _resolve_collection_type_to_decode_to(my_dict.__class__)
    assert isinstance(resolved_type, type) and issubclass(resolved_type, dict), f"Expected a subclass of dict but got {resolved_type}"

def test_resolve_set():
    my_set = {1, 2, 3}
    resolved_type = _resolve_collection_type_to_decode_to(my_set.__class__)
    assert isinstance(resolved_type, type) and issubclass(resolved_type, set), f"Expected a subclass of set but got {resolved_type}"

def test_resolve_tuple():
    my_tuple = (1, 2, 3)
    resolved_type = _resolve_collection_type_to_decode_to(my_tuple.__class__)
    assert isinstance(resolved_type, type) and issubclass(resolved_type, tuple), f"Expected a subclass of tuple but got {resolved_type}"

def test_resolve_custom_class():
    class MyCustomList(list):
        pass
    
    my_custom_list = MyCustomList([1, 2, 3])
    resolved_type = _resolve_collection_type_to_decode_to(my_custom_list.__class__)
    assert resolved_type == MyCustomList, f"Expected MyCustomList but got {resolved_type}"

def test_resolve_unknown_type():
    class UnknownType:
        pass
    
    unknown = UnknownType()
    resolved_type = _resolve_collection_type_to_decode_to(unknown.__class__)
    assert resolved_type == UnknownType, f"Expected UnknownType but got {resolved_type}"
