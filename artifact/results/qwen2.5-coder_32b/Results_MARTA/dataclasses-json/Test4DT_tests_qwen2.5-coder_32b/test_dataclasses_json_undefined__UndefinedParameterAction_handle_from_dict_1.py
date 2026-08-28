
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

def test_handle_from_dict_with_integer_keys():
    """Test handle_from_dict with integer keys."""
    kvs = {0: 'value1', 1: 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {}

def test_handle_from_dict_with_string_keys():
    """Test handle_from_dict with string keys."""
    kvs = {'param1': 'value1', 'param2': 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1', 'param2': 42}

def test_handle_from_dict_with_mixed_types():
    """Test handle_from_dict with mixed types."""
    kvs = {'param1': 'value1', 2: 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1'}

def test_handle_from_dict_with_no_matching_keys():
    """Test handle_from_dict with no matching keys."""
    kvs = {3: 'value1', 4: 42}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {}

def test_handle_from_dict_with_extra_keys():
    """Test handle_from_dict with extra keys."""
    kvs = {'param1': 'value1', 'param2': 42, 'extra_key': 'extra_value'}
    params = MyParameterAction.handle_from_dict(kvs)
    assert params == {'param1': 'value1', 'param2': 42}
