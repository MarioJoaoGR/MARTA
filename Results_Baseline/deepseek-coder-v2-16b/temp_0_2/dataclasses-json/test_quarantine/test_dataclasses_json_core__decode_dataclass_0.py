
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str

def test_decode_dataclass_with_missing_fields():
    person_dict = {"name": "John Doe"}
    with pytest.raises(ValueError):
        Person.from_dict(person_dict)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_0.py:14:8: E1101: Class 'Person' has no 'from_dict' member (no-member)

"""