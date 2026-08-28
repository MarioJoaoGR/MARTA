
import pytest
from dataclasses import dataclass
from typing import List, Dict, Optional, Union, Any
from enum import Enum
from dataclasses_json.core import _decode_generic

# Example Dataclass for testing
@dataclass
class Person:
    name: str
    age: int

# Example Enum for testing
class Color(Enum):
    RED = 1
    GREEN = 2


def test_decode_generic_list_of_dataclasses():
    """Test decoding a list of dictionaries into a list of dataclass instances."""
    people_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    decoded_people = _decode_generic(List[Person], people_dicts, infer_missing=False)
    assert decoded_people == [Person(name='Alice', age=30), Person(name='Bob', age=25)]

def test_decode_generic_dict_with_string_keys_to_int_keys():
    """Test decoding a dictionary with string keys to integer keys."""
    xs = {'1': 'Alice', '2': 'Bob'}
    decoded_dict = _decode_generic(Dict[int, str], xs, infer_missing=False)
    assert decoded_dict == {1: 'Alice', 2: 'Bob'}

def test_decode_generic_optional_type():
    """Test handling optional types."""
    optional_str = _decode_generic(Optional[str], None, infer_missing=False)
    assert optional_str is None

def test_decode_generic_union_type_string():
    """Test decoding a union type with string value."""
    union_value = "example"
    decoded_union = _decode_generic(Union[str, int], union_value, infer_missing=False)
    assert decoded_union == "example"

def test_decode_generic_union_type_int():
    """Test decoding a union type with integer value."""
    union_value = 123
    decoded_union = _decode_generic(Union[str, int], union_value, infer_missing=False)
    assert decoded_union == 123

def test_decode_generic_enum():
    """Test decoding an enum value."""
    color_value = 1
    decoded_enum = _decode_generic(Color, color_value, infer_missing=False)
    assert decoded_enum == Color.RED