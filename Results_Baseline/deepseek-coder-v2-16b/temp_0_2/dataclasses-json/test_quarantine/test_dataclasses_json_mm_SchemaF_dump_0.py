
# Module: dataclasses_json.mm
import pytest
from dataclasses_json import DataClassJsonMixin
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int
    email: Optional[str] = None

def test_person_creation_from_dict():
    person_dict = {"name": "John Doe", "age": 30}
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

def test_person_creation_with_inferred_fields():
    person_dict_with_extra = {"name": "Jane Doe", "age": 25, "email": "jane@example.com"}
    person_inferred = Person.from_dict(person_dict_with_extra, infer_missing=True)
    assert person_inferred.name == "Jane Doe"
    assert person_inferred.age == 25
    assert person_inferred.email == "jane@example.com"

def test_person_creation_without_infer_missing():
    person_dict = {"name": "John Doe", "age": 30}
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email is None

def test_person_creation_with_invalid_input():
    with pytest.raises(TypeError):
        Person()  # This should raise a TypeError because the class should not be instantiated directly.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_dump_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dump_0.py:37:8: E1120: No value for argument 'name' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dump_0.py:37:8: E1120: No value for argument 'age' in constructor call (no-value-for-parameter)

"""