
import pytest
from dataclasses import dataclass, field
from typing import Dict, Any
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError

# Define a sample dataclass for testing
@dataclass
class MyClass(_RaiseUndefinedParameters):
    param1: int = field(default=0)
    param2: str = field(default='default')

def test_handle_from_dict_with_defined_parameters():
    kvs = {'param1': 10, 'param2': 'value'}
    known_params = MyClass.handle_from_dict(MyClass, kvs)
    assert known_params == {'param1': 10, 'param2': 'value'}

def test_handle_from_dict_with_undefined_parameters():
    kvs = {'param1': 10, 'param3': 'extra', 'param2': 'value'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        MyClass.handle_from_dict(MyClass, kvs)
    assert str(excinfo.value) == "Received undefined initialization arguments {'param3': 'extra'}"

def test_handle_from_dict_with_no_parameters():
    kvs = {}
    known_params = MyClass.handle_from_dict(MyClass, kvs)
    assert known_params == {}

def test_handle_from_dict_with_only_undefined_parameters():
    kvs = {'param3': 'extra', 'param4': 'another_extra'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        MyClass.handle_from_dict(MyClass, kvs)
    assert str(excinfo.value) == "Received undefined initialization arguments {'param3': 'extra', 'param4': 'another_extra'}"

def test_handle_from_dict_with_mixed_case_parameters():
    kvs = {'Param1': 10, 'param2': 'value'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        MyClass.handle_from_dict(MyClass, kvs)
    assert str(excinfo.value) == "Received undefined initialization arguments {'Param1': 10}"

def test_handle_from_dict_with_none_value():
    kvs = {'param1': None, 'param2': 'value'}
    known_params = MyClass.handle_from_dict(MyClass, kvs)
    assert known_params == {'param1': None, 'param2': 'value'}
