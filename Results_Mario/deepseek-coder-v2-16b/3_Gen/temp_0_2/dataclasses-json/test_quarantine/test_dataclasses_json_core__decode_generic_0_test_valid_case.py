
import pytest
from dataclasses import dataclass
from typing import List
from dataclasses_json.core import _decode_generic

@dataclass
class Person:
    name: str
    age: int

def test_valid_case():
    person_data = {"name": "John Doe", "age": 30}
    decoded_person = _decode_generic(Person, person_data, infer_missing=False)
    assert isinstance(decoded_person, Person)
    assert decoded_person.name == "John Doe"
    assert decoded_person.age == 30

    list_of_numbers = [1, 2, 3]
    decoded_list = _decode_generic(List[int], list_of_numbers, infer_missing=False)
    assert isinstance(decoded_list, list)
    assert all(isinstance(num, int) for num in decoded_list)
