
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

# Define a simple dataclass for testing
@dataclass
class MyClass:
    param1: int
    param2: str

def test_valid_input():
    kvs = {'param1': 10, 'param2': 'value'}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert known_params == {'param1': 10, 'param2': 'value'}

def test_empty_dict_input():
    kvs = {}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert known_params == {}

def test_undefined_parameters():
    kvs = {'param1': 10}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert known_params == {'param1': 10}
