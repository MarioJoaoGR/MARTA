
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class MyClass:
    param1: str
    param2: int

class MyParameterAction(_UndefinedParameterAction):
    @classmethod
    def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
        # Example transformation logic: filter out undefined keys
        field_names = {field.name for field in fields(MyClass)}
        return {k: v for k, v in kvs.items() if k in field_names}

# Test cases

def test_handle_from_dict_with_integer_keys():
    kvs = {0: 'value1', 1: 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {}

def test_handle_from_dict_with_string_keys():
    kvs = {'param1': 'value1', 'param2': 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1', 'param2': 42}

def test_handle_from_dict_with_mixed_types():
    kvs = {'param1': 'value1', 2: 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1'}

def test_handle_from_dict_with_no_matching_keys():
    kvs = {'unrelated_key': 'value'}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {}

def test_handle_from_dict_with_all_matching_keys():
    kvs = {'param1': 'value1', 'param2': 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1', 'param2': 42}

def test_handle_from_dict_with_extra_keys():
    kvs = {'param1': 'value1', 'param2': 42, 'extra_key': 'extra_value'}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1', 'param2': 42}
