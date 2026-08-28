
import pytest
from dataclasses import dataclass
from typing import List, Dict, Optional, Union, Any
from enum import Enum
from dataclasses_json.core import _decode_generic

# Example data classes and enums for testing
@dataclass
class Person:
    name: str
    age: int

class Color(Enum):
    RED = 1
    GREEN = 2


def test_decode_generic_list_of_persons():
    people_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    decoded_people = _decode_generic(List[Person], people_dicts, infer_missing=False)
    assert isinstance(decoded_people, list)
    assert len(decoded_people) == 2
    assert all(isinstance(person, Person) for person in decoded_people)
    assert decoded_people[0].name == 'Alice'
    assert decoded_people[1].name == 'Bob'

def test_decode_generic_dict_with_string_keys_to_int():
    xs = {'1': 'Alice', '2': 'Bob'}
    decoded_dict = _decode_generic(Dict[int, str], xs, infer_missing=False)
    assert isinstance(decoded_dict, dict)
    assert decoded_dict[1] == 'Alice'
    assert decoded_dict[2] == 'Bob'

def test_decode_generic_optional_type_none():
    optional_str = _decode_generic(Optional[str], None, infer_missing=False)
    assert optional_str is None

def test_decode_generic_union_string_or_int():
    union_value = "example"
    decoded_union = _decode_generic(Union[str, int], union_value, infer_missing=False)
    assert isinstance(decoded_union, str)
    assert decoded_union == 'example'

def test_decode_generic_enum():
    color_value = 1
    decoded_enum = _decode_generic(Color, color_value, infer_missing=False)
    assert isinstance(decoded_enum, Color)
    assert decoded_enum == Color.RED

def test_decode_generic_any_type():
    any_value = "any"
    decoded_any = _decode_generic(Any, any_value, infer_missing=False)
    assert decoded_any == 'any'