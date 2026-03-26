
import pytest
from typing import Tuple, List, Union
from dataclasses_json.utils import _is_tuple

def test_invalid_input():
    # Test with a list type
    my_list = List[int]
    assert not _is_tuple(my_list), "Expected _is_tuple to return False for list types"
    
    # Test with an int type
    my_int = int
    assert not _is_tuple(my_int), "Expected _is_tuple to return False for int types"
    
    # Test with a union of int and str
    mixed_types = Union[int, str]
    assert not _is_tuple(mixed_types), "Expected _is_tuple to return False for union types"
    
    # Additional test cases can be added here to cover more invalid input scenarios.
