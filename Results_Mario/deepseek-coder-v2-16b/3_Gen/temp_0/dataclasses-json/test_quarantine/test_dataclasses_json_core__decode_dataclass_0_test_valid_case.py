
from dataclasses import dataclass, fields
from typing import Type, Dict, Any
from dataclasses_json import dataclass_json
import pytest

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_valid_case():
    # Test data
    json_data = {"name": "John Doe", "age": 30}
    
    # Call the function with the dataclass and JSON data
    person = Person.from_dict(json_data)
    
    # Assertions to verify the output
    assert person.name == "John Doe"
    assert person.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0_test_valid_case.py:18:13: E1101: Class 'Person' has no 'from_dict' member (no-member)


"""