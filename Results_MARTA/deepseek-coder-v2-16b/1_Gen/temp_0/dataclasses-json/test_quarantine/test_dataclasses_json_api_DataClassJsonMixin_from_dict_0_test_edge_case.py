
from dataclasses import dataclass
from typing import Optional, Type, Dict, Any
import pytest
from dataclasses_json.api import DataClassJsonMixin

# Mocking _decode_dataclass function
def mock_decode_dataclass(cls: Type[Any], kvs: Dict[str, Any], infer_missing: bool) -> Any:
    return cls(**kvs)

DataClassJsonMixin._decode_dataclass = mock_decode_dataclass

@dataclass
class Person:
    name: str
    age: int

def test_edge_case():
    person_dict = {"name": "John Doe", "age": 30}
    person = DataClassJsonMixin.from_dict(Person, person_dict)
    assert isinstance(person, Person)
    assert person.name == "John Doe"
    assert person.age == 30

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_dict_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_dict_0_test_edge_case.py:20:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)

"""