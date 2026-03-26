
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
    assert person_inferred.email == "jane@example.com"

# Additional test cases for uncovered lines
def test_decode_dataclass_with_none_value():
    # Test when a field value is None and should be inferred as missing
    kvs = {"name": "John Doe", "age": 30, "email": None}
    person = Person.from_dict(kvs, infer_missing=True)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

def test_decode_dataclass_with_default_value():
    # Test when a field has a default value and should not be inferred as missing
    kvs = {"name": "John Doe", "age": 30, "email": "john@example.com"}
    person = Person.from_dict(kvs)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email == "john@example.com"

def test_decode_dataclass_with_missing_default_factory():
    # Test when a field has a default factory and should be created if missing
    kvs = {"name": "John Doe", "age": 30}
    person = Person.from_dict(kvs, infer_missing=True)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

def test_decode_dataclass_with_undefined_parameters():
    # Test handling of undefined parameters with a custom dictionary
    kvs = {"name": "John Doe", "age": 30, "extra_key": "value"}
    person = Person.from_dict(kvs)