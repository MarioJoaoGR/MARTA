
import pytest
from dataclasses import dataclass, fields
from typing import Type, Optional, Any
from dataclasses_json.core import _decode_dataclass

@dataclass
class Person:
    name: str
    age: int = 0

def test_decode_dataclass():
    # Test case for decoding a valid dataclass from a dictionary
    data = {"name": "John Doe", "age": 30}
    person = _decode_dataclass(Person, data, infer_missing=False)
    assert isinstance(person, Person)
    assert person.name == "John Doe"
    assert person.age == 30

def test_decode_dataclass_with_infer_missing():
    # Test case for decoding a dataclass with infer_missing set to True
    data = {"name": "John Doe"}
    person = _decode_dataclass(Person, data, infer_missing=True)
    assert isinstance(person, Person)
    assert person.name == "John Doe"
    assert person.age == 0  # Default value should be used since age is not in the dictionary

def test_decode_dataclass_with_invalid_data():
    # Test case for handling invalid data that cannot be decoded into a dataclass
    data = {"name": "John Doe", "age": "thirty"}  # Invalid value for age field
    with pytest.raises(ValueError):
        _decode_dataclass(Person, data, infer_missing=False)
