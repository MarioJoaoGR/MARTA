
import pytest
from dataclasses import dataclass
from typing import Optional, Type, Dict, Any as Json
from dataclasses_json.api import DataClassJsonMixin

# Mocking _decode_dataclass function for the test
@pytest.fixture
def mock_decode_dataclass(mocker):
    return mocker.patch('dataclasses_json.api._decode_dataclass')

@dataclass
class Person:
    name: str
    age: int

# Test case for valid input
def test_valid_input(mock_decode_dataclass):
    person_dict = {"name": "John Doe", "age": 30}
    DataClassJsonMixin.from_dict(Person, person_dict)
    mock_decode_dataclass.assert_called_once_with(Person, person_dict, infer_missing=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_dict_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_dict_0_test_valid_input.py:20:4: E1121: Too many positional arguments for classmethod call (too-many-function-args)

"""