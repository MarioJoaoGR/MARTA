
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError, _RaiseUndefinedParameters

@dataclass
class MyClass:
    known_param1: int
    known_param2: str

def test_handle_from_dict_valid_parameters():
    kvs_valid = {'known_param1': 42, 'known_param2': 'example'}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_valid)
    assert result == {'known_param1': 42, 'known_param2': 'example'}



def test_handle_from_dict_empty_parameters():
    kvs_empty = {}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_empty)
    assert result == {}

def test_handle_from_dict_partial_valid_parameters():
    kvs_partial = {'known_param1': 42}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_partial)
    assert result == {'known_param1': 42}
