
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase, Undefined
import json

@dataclass_json
@dataclass
class Person:
    name: str
    age: int

def test_valid_inputs():
    person = Person(name="John Doe", age=30)
    json_str = json.dumps(person, cls=dataclass_json)  # Serializes the dataclass to JSON
    deserialized_person = json.loads(json_str, object_hook=Person.from_json)  # Deserializes the JSON back to a dataclass
    
    assert person == deserialized_person

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_valid_inputs.py:16:59: E1101: Class 'Person' has no 'from_json' member (no-member)


"""