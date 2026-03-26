
import json
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin, dataclass_json
import pytest

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_valid_input():
    json_string = '{"name": "John Doe", "age": 30}'
    person = Person.from_json(json_string)
    assert person == Person(name='John Doe', age=30)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_json_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0_test_valid_input.py:15:13: E1101: Class 'Person' has no 'from_json' member (no-member)

"""