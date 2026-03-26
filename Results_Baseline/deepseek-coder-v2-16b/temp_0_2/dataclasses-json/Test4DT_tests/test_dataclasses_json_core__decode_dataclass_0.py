
import pytest
from dataclasses import dataclass, fields
from typing import Optional
from dataclasses_json import DataClassJsonMixin
import json

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int
    email: Optional[str] = None

# Example dictionary to initialize a Person instance
person_dict = {"name": "John Doe", "age": 30}
person_dict_with_extra = {"name": "Jane Doe", "age": 25, "email": "jane@example.com"}

def test_decode_dataclass_basic():
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

def test_decode_dataclass_with_infer_missing():
    person_inferred = Person.from_dict(person_dict_with_extra, infer_missing=True)
    assert person_inferred.name == "Jane Doe"
    assert person_inferred.age == 25