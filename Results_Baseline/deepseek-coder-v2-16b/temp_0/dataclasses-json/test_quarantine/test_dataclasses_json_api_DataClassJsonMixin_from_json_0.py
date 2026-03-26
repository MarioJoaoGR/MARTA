
# Module: dataclasses_json.api
# test_dataclass_json_mixin.py
import pytest
from dataclasses import dataclass
from typing import Optional, Type, Any, Callable, JsonData
import json
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class Person:
    name: str
    age: int = 0

def test_from_json():
    # Test case where JSON string is successfully parsed into a dataclass instance
    json_string = '{"name": "John Doe", "age": 30}'
    person = DataClassJsonMixin.from_json(Person, json_string)
    assert isinstance(person, Person), "Expected an instance of the dataclass"
    assert person.name == "John Doe", "Name should be 'John Doe'"
    assert person.age == 30, "Age should be 30"

def test_from_json_with_parse_float():
    # Test case where a custom parse function for floats is provided
    json_string = '{"name": "John Doe", "age": 30.5}'
    person = DataClassJsonMixin.from_json(Person, json_string, parse_float=lambda x: float(x))
    assert isinstance(person, Person), "Expected an instance of the dataclass"
    assert person.name == "John Doe", "Name should be 'John Doe'"
    assert person.age == 30.5, "Age should be 30.5 with custom parse_float"

def test_from_json_with_parse_int():
    # Test case where a custom parse function for ints is provided
    json_string = '{"name": "John Doe", "age": "30"}'
    person = DataClassJsonMixin.from_json(Person, json_string, parse_int=lambda x: int(x))
    assert isinstance(person, Person), "Expected an instance of the dataclass"
    assert person.name == "John Doe", "Name should be 'John Doe'"
    assert person.age == 30, "Age should be 30 with custom parse_int"

def test_from_json_with_parse_constant():
    # Test case where a custom parse function for constants is provided
    json_string = '{"name": "John Doe", "age": "Infinity"}'
    person = DataClassJsonMixin.from_json(Person, json_string, parse_constant=lambda x: float(x) if x == "Infinity" else None)
    assert isinstance(person, Person), "Expected an instance of the dataclass"
    assert person.name == "John Doe", "Name should be 'John Doe'"
    assert person.age == float('inf'), "Age should be Infinity with custom parse_constant"

def test_from_json_with_infer_missing():
    # Test case where infer_missing is set to True and some fields are missing in the JSON string
    json_string = '{"name": "John Doe"}'
    person = DataClassJsonMixin.from_json(Person, json_string, infer_missing=True)
    assert isinstance(person, Person), "Expected an instance of the dataclass"
    assert person.name == "John Doe", "Name should be 'John Doe'"
    assert person.age == 0, "Age should default to 0 when inferred from the dataclass"

def test_from_json_invalid_dataclass():
    # Test case where a non-dataclass type is provided as the first argument
    with pytest.raises(TypeError):
        DataClassJsonMixin.from_json(int, '{"name": "John Doe", "age": 30}')

def test_from_json_invalid_json():
    # Test case where an invalid JSON string is provided
    json_string = '{invalid}'
    with pytest.raises(json.JSONDecodeError):
        DataClassJsonMixin.from_json(Person, json_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_json_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:6:0: E0611: No name 'JsonData' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:18:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:26:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:34:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:42:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:50:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:58:8: E1121: Too many positional arguments for classmethod call (too-many-function-args)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_0.py:64:8: E1121: Too many positional arguments for classmethod call (too-many-function-args)

"""