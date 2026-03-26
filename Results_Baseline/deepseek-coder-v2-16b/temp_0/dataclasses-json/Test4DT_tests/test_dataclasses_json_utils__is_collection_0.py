
import pytest
from collections import deque, abc as Collection
from dataclasses_json.utils import _is_collection, _get_type_origin, _issubclass_safe

# Test cases for _is_collection function
def test_is_collection_list():
    my_list = [1, 2, 3]
    assert _is_collection(my_list.__class__) == True

def test_is_collection_set():
    my_set = {1, 2, 3}
    assert _is_collection(my_set.__class__) == True

def test_is_collection_dict():
    my_dict = {'a': 1, 'b': 2}
    assert _is_collection(my_dict.__class__) == True

def test_is_collection_int():
    int_value = 42
    assert _is_collection(int_value.__class__) == False

def test_is_collection_str():
    str_value = "hello"