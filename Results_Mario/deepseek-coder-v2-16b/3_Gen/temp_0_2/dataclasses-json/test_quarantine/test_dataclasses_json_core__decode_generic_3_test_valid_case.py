
import pytest
from dataclasses_json.core import _decode_generic
from dataclasses import dataclass
from typing import List, Optional, Union
from enum import Enum

@dataclass
class Person:
    name: str
    age: int

def test_valid_case():
    person_data = {"name": "John Doe", "age": 30}
    decoded_person = _decode_generic(Person, person_data, infer_missing=False)
    assert isinstance(decoded_person, Person), "The decoded object should be an instance of Person"
    assert decoded_person.name == "John Doe", "The name field should match the input data"
    assert decoded_person.age == 30, "The age field should match the input data"

    list_of_numbers = [1, 2, 3]
    decoded_list = _decode_generic(List[int], list_of_numbers, infer_missing=False)
    assert isinstance(decoded_list, list), "The decoded object should be a list"
    assert all(isinstance(n, int) for n in decoded_list), "All elements in the list should be integers"
