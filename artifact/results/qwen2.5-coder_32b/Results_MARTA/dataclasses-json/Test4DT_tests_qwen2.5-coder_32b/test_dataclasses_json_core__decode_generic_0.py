
import pytest
from dataclasses import dataclass
from typing import List, Dict, Optional, Union
from enum import Enum
from dataclasses_json.core import _decode_generic

# Define a simple dataclass for testing
@dataclass
class Person:
    name: str
    age: int

# Define an enum for testing
class Color(Enum):
    RED = 1
    GREEN = 2

# Test decoding a dictionary into a dataclass instance

# Test decoding a list of dictionaries into a list of dataclass instances
def test_decode_list_of_dicts_to_dataclasses():
    people_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    decoded_people = _decode_generic(List[Person], people_dicts, infer_missing=False)
    assert decoded_people == [Person(name='Alice', age=30), Person(name='Bob', age=25)]

# Test decoding a dictionary with string keys to integer keys
def test_decode_dict_with_string_keys_to_int_keys():
    xs = {'1': 'Alice', '2': 'Bob'}
    decoded_dict = _decode_generic(Dict[int, str], xs, infer_missing=False)
    assert decoded_dict == {1: 'Alice', 2: 'Bob'}

# Test handling optional types
def test_handle_optional_types():
    optional_str = _decode_generic(Optional[str], None, infer_missing=False)
    assert optional_str is None

# Test decoding a union type (assuming Union from the typing module)
def test_decode_union_type():
    union_value = "example"
    decoded_union = _decode_generic(Union[str, int], union_value, infer_missing=False)
    assert decoded_union == 'example'

# Test decoding an enum value
def test_decode_enum_value():
    color_value = 1
    decoded_enum = _decode_generic(Color, color_value, infer_missing=False)
    assert decoded_enum == Color.RED