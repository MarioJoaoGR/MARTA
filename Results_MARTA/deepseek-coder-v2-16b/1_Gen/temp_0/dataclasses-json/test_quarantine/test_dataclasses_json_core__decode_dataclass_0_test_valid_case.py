
import pytest
from dataclasses import dataclass, fields
from typing import Type, Dict, Any
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_valid_case():
    # Define a valid JSON string that can be deserialized into the Person dataclass
    json_string = '{"name": "John Doe", "age": 30}'
    
    # Deserialize the JSON string to an instance of Person
    person = Person.from_dict(json_string)
    
    # Assert that the deserialized object has the correct attributes and values
    assert person.name == "John Doe"
    assert person.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_valid_case.py:18:13: E1101: Class 'Person' has no 'from_dict' member (no-member)

"""