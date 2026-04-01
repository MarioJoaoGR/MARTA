
import pytest
from dataclasses_json.utils import _issubclass_safe, _get_type_origin
from typing import Tuple, List, Union

def test_is_tuple():
    my_tuple = Tuple[int, str]
    assert _is_tuple(my_tuple) == True
    
    my_list = List[int]
    assert _is_tuple(my_list) == False
    
    mixed_types = Union[int, str]
    assert _is_tuple(mixed_types) == False

def _is_tuple(type_):
    return _issubclass_safe(_get_type_origin(type_), Tuple)
