
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError

@dataclass
class MyClass:
    known_param1: int
    known_param2: str

def test_handle_from_dict_with_valid_parameters():
    kvs_valid = {'known_param1': 42, 'known_param2': 'example'}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_valid)
    assert result == {'known_param1': 42, 'known_param2': 'example'}



def test_handle_from_dict_with_empty_dictionary():
    kvs_empty = {}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_empty)
    assert result == {}

def test_handle_from_dict_with_no_invalid_parameters():
    kvs_no_invalid = {'known_param1': 42, 'known_param2': 'example'}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_no_invalid)
    assert result == {'known_param1': 42, 'known_param2': 'example'}