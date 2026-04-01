
import pytest
from dataclasses_json.utils import _is_tuple
from typing import Tuple, List, Union

def test_is_tuple():
    # Test when type is a tuple
    my_tuple = Tuple[int, str]
    assert _is_tuple(my_tuple) == True
    
    # Test when type is not a tuple
    my_list = List[int]
    assert _is_tuple(my_list) == False
    
    # Test when type is a union of types (not a tuple)
    mixed_types = Union[int, str]
    assert _is_tuple(mixed_types) == False
