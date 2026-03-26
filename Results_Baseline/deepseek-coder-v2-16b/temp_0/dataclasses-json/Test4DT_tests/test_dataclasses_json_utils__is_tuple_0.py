# Module: dataclasses_json.utils
import pytest
from typing import Tuple, List, Union
from dataclasses_json.utils import _is_tuple as target_function

# Test cases for _is_tuple function
def test_is_tuple_custom_tuple():
    my_tuple = Tuple[int, str]
    assert target_function(my_tuple) is True

def test_is_tuple_list():
    my_list = List[int]
    assert target_function(my_list) is False

def test_is_tuple_union():
    mixed_types = Union[int, str]
    assert target_function(mixed_types) is False

def test_is_tuple_integer():
    integer_type = int
    assert target_function(integer_type) is False
