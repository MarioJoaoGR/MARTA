
# Module: dataclasses_json.undefined
import pytest
from typing import Dict, Any
from dataclasses_json.undefined import handle_from_dict, UndefinedParameterError

# Define a sample class for testing
class SampleClass:
    def __init__(self, param1: int, param2: str = None):
        self.param1 = param1
        self.param2 = param2

# Test cases for handle_from_dict function
def test_handle_from_dict_known_parameters():
    kvs = {'param1': 1, 'param2': 'value'}
    cls = SampleClass
    result = handle_from_dict(cls, kvs)
    assert result == {'param1': 1, 'param2': 'value'}

def test_handle_from_dict_unknown_parameters():
    kvs = {'param1': 1, 'extra_param': 2}
    cls = SampleClass
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(cls, kvs)

def test_handle_from_dict_catch_all():
    kvs = {'param1': 1, 'param2': 'value', 'extra_param': 3}
    cls = SampleClass
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(cls, kvs)

def test_handle_from_dict_default_value():
    kvs = {'param1': 1}
    cls = SampleClass
    result = handle_from_dict(cls, kvs)
    assert result == {'param1': 1, 'param2': None}

def test_handle_from_dict_already_parsed():
    kvs = {'param1': 1, 'param2': {'nested_key': 'nested_value'}}
    cls = SampleClass
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(cls, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0.py:5:0: E0611: No name 'handle_from_dict' in module 'dataclasses_json.undefined' (no-name-in-module)

"""