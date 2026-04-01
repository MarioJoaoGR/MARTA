
import dataclasses
from typing import Optional, Union, Type, Callable, TypeVar
from dataclasses_json import dataclass_json, LetterCase, Undefined
import json

T = TypeVar('T')

@dataclass_json
@dataclasses.dataclass
class Person:
    name: str
    age: int

# Example test case to ensure the functionality works correctly
def test_valid_inputs_happy_path():
    person_dict = {"name": "John Doe", "age": 30}
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_0_test_valid_inputs_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_valid_inputs_happy_path.py:18:13: E1101: Class 'Person' has no 'from_dict' member (no-member)


"""