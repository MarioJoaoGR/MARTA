
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any

# Assuming _UndefinedParameterAction is part of a module named 'dataclasses_json.undefined'
# For this example, we will define it here as per your provided function code.
class _UndefinedParameterAction:
    @classmethod
    def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
        # Example transformation logic: filter out undefined keys
        field_names = {field.name for field in fields(cls)}
        return {k: v for k, v in kvs.items() if isinstance(kvs, dict) and k in field_names}

@dataclass
class MyClass(_UndefinedParameterAction):
    param1: str
    param2: int



def test_valid_case_with_integer_keys():
    kvs = {0: 'value1', 1: 42}
    result = MyClass.handle_from_dict(kvs)
    assert result == {}

def test_valid_case_with_string_keys():
    kvs = {'param1': 'value1', 'param2': 42}
    result = MyClass.handle_from_dict(kvs)
    assert result == {'param1': 'value1', 'param2': 42}

def test_mixed_types_keys():
    kvs = {'param1': 'value1', 2: 42}
    result = MyClass.handle_from_dict(kvs)
    assert result == {'param1': 'value1'}

def test_empty_dict_input():
    kvs = {}
    result = MyClass.handle_from_dict(kvs)
    assert result == {}

def test_partial_keys():
    kvs = {'param1': 'value1'}
    result = MyClass.handle_from_dict(kvs)
    assert result == {'param1': 'value1'}

def test_no_matching_keys():
    kvs = {'unrelated_key': 'value1', 'another_unrelated_key': 42}
    result = MyClass.handle_from_dict(kvs)
    assert result == {}