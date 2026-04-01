
import pytest
from dataclasses import dataclass
from typing import List, Dict, Union
from dataclasses_json.core import asdict

@dataclass
class Person:
    name: str
    age: int
    addresses: List[Dict[str, str]]

def test_valid_input_dataclass():
    person = Person(name="John Doe", age=30, addresses=[{"street": "123 Main St", "city": "Anytown"}])
    result = asdict(person)
    assert isinstance(result, dict)
    assert result == {
        'name': 'John Doe',
        'age': 30,
        'addresses': [{'street': '123 Main St', 'city': 'Anytown'}]
    }

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__asdict_0_test_valid_input_dataclass
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_input_dataclass.py:5:0: E0611: No name 'asdict' in module 'dataclasses_json.core' (no-name-in-module)


"""