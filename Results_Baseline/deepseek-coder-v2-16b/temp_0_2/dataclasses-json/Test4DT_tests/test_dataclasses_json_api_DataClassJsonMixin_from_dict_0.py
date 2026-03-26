
# Module: dataclasses_json.api
# test_dataclasses_json.py
from dataclasses import dataclass
import pytest
from dataclasses_json import DataClassJsonMixin
from typing import Optional  # Corrected the import statement for Optional

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int
    email: Optional[str] = None

# Test case for initializing a Person instance from a dictionary without inferring missing fields
def test_from_dict_without_infer_missing():
    person_dict = {"name": "John Doe", "age": 30}
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

# Test case for initializing a Person instance from a dictionary with inferring missing fields
def test_from_dict_with_infer_missing():
    person_dict_with_extra = {"name": "Jane Doe", "age": 25, "email": "jane@example.com"}
    person_inferred = Person.from_dict(person_dict_with_extra, infer_missing=True)
    assert person_inferred.name == "Jane Doe"
    assert person_inferred.age == 25
    assert person_inferred.email == "jane@example.com"

# Test case for handling undefined parameters in the dictionary during deserialization
def test_from_dict_with_undefined_parameters():
    person_dict_with_extra = {"name": "Jane Doe", "age": 25, "email": "jane@example.com", "undefined_param": "extra"}
    person_inferred = Person.from_dict(person_dict_with_extra, infer_missing=True)
    assert person_inferred.name == "Jane Doe"
    assert person_inferred.age == 25
    assert person_inferred.email == "jane@example.com"