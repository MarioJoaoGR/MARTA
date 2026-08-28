
import pytest
from dataclasses import dataclass, fields, MISSING
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

def test_decode_dataclass_with_default_values():
    person_dict = {'name': 'Alice'}
    person_instance = _decode_dataclass(Person, person_dict, infer_missing=True)
    assert person_instance == Person(name='Alice', age=30)

def test_decode_dataclass_nested_dataclasses():
    employee_dict = {'name': 'Bob', 'address': {'city': 'New York', 'zip_code': '10001'}}
    employee_instance = _decode_dataclass(Employee, employee_dict, infer_missing=False)
    assert employee_instance == Employee(name='Bob', address=Address(city='New York', zip_code='10001'))

def test_decode_dataclass_missing_fields_with_infer_missing():
    person_dict = {'name': 'Charlie'}
    person_instance = _decode_dataclass(Person, person_dict, infer_missing=True)
    assert person_instance == Person(name='Charlie', age=30)

def test_decode_dataclass_existing_instance():
    existing_person = Person(name='David', age=25)
    same_person_instance = _decode_dataclass(Person, existing_person, infer_missing=True)
    assert same_person_instance == existing_person

def test_decode_dataclass_none_value_with_infer_missing():
    person_dict = {'name': 'Eve', 'age': None}
    person_instance = _decode_dataclass(Person, person_dict, infer_missing=True)
    assert person_instance == Person(name='Eve', age=None)


def test_decode_dataclass_with_none_value_without_infer_missing():
    person_dict = {'name': 'Grace', 'age': None}
    with pytest.warns(RuntimeWarning):
        person_instance = _decode_dataclass(Person, person_dict, infer_missing=False)
    assert person_instance.age is None