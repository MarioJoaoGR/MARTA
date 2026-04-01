
import json
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin, dataclass_json
import pytest

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int = 0

def test_valid_input():
    json_string = '{"name": "John Doe", "age": 30}'
    person = Person.from_json(json_string)
    assert person == Person(name='John Doe', age=30)
