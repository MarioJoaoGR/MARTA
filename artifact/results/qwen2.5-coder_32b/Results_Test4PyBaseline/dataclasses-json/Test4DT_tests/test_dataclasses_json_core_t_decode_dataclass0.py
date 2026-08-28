
# Test case  
# Module: dataclasses_json.core
import pytest
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from dataclasses_json.core import _decode_dataclass

@dataclass
class Person:
    name: str
    age: int = 30
    email: Optional[str] = None

@dataclass
class Address:
    street: str
    city: str

@dataclass
class PersonWithAddress:
    name: str
    address: Address
    age: int = 30

def test_decode_dataclass_basic_conversion_with_defaults():
    person_dict = {'name': 'Alice'}
    person_instance = _decode_dataclass(Person, person_dict, infer_missing=True)
    assert isinstance(person_instance, Person)
    assert person_instance.name == 'Alice'
    assert person_instance.age == 30
    assert person_instance.email is None

def test_decode_dataclass_all_fields_provided():
    person_dict = {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'}
    person_instance = _decode_dataclass(Person, person_dict, infer_missing=True)
    assert isinstance(person_instance, Person)
    assert person_instance.name == 'Bob'
    assert person_instance.age == 25