
import pytest
from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json.core import _decode_dataclass

@dataclass
class Person:
    name: str
    age: int = 30

@dataclass
class Address:
    city: str
    zip_code: str

@dataclass
class Employee:
    name: str
    address: Address

def test_invalid_inputs():
    # Test with incorrect data types
    person_incorrect_type = _decode_dataclass(Person, {'name': 'Alice', 'age': 'thirty'}, infer_missing=False)
    assert isinstance(person_incorrect_type.age, str)  # Ensure age is still a string as no conversion happens

def test_invalid_inputs_with_infer_missing():
    # Test with incorrect data types and infer_missing set to True
    person_incorrect_type = _decode_dataclass(Person, {'name': 'Alice', 'age': 'thirty'}, infer_missing=True)
    assert isinstance(person_incorrect_type.age, str)  # Ensure age is still a string as no conversion happens

def test_missing_field_with_default():
    # Test with missing field and default value
    person_missing_age = _decode_dataclass(Person, {'name': 'Alice'}, infer_missing=False)
    assert person_missing_age.age == 30  # Default value should be used

def test_missing_field_without_infer_missing():
    # Test with missing field and infer_missing set to False
    person_missing_age = _decode_dataclass(Person, {'name': 'Alice'}, infer_missing=True)
    assert person_missing_age.age == 30  # Default value should be used

def test_nested_dataclasses():
    # Test with nested dataclasses
    employee_dict = {'name': 'Bob', 'address': {'city': 'New York', 'zip_code': '10001'}}
    employee_instance = _decode_dataclass(Employee, employee_dict, infer_missing=False)
    assert employee_instance.name == 'Bob'
    assert isinstance(employee_instance.address, Address)

def test_existing_instance():
    # Test with an already instantiated object
    existing_person = Person(name='David', age=25)
    same_person_instance = _decode_dataclass(Person, existing_person, infer_missing=True)
    assert same_person_instance.name == 'David'
    assert same_person_instance.age == 25

def test_optional_field():
    # Test with an optional field
    @dataclass
    class OptionalPerson:
        name: str
        age: Optional[int] = None

    person_with_none_age = _decode_dataclass(OptionalPerson, {'name': 'Alice', 'age': None}, infer_missing=False)
    assert person_with_none_age.age is None  # Age should be None as it's optional
