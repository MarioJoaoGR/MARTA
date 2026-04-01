
import pytest
from dataclasses import dataclass
from dataclasses_json.api import DataClassJsonMixin
import json

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_from_json():
    person_json = '{"name": "Alice", "age": 30}'
    person = Person.from_json(person_json)
    assert isinstance(person, Person)
    assert person.name == "Alice"
    assert person.age == 30
