# Module: dataclasses_json.mm
import pytest
from dataclasses import dataclass
from typing import Dict, Any
import inspect
import functools

class _UnionField:
    def __init__(self, desc, cls, field, *args, **kwargs):
        self.desc = desc
        self.cls = cls
        self.field = field
        super().__init__(*args, **kwargs)

class _IgnoreUndefinedParameters:
    @staticmethod
    def handle_from_dict(cls, kvs: Dict[str, Any]) -> Dict[str, Any]:
        known_params = {}
        for key, value in kvs.items():
            if hasattr(cls, key):
                known_params[key] = value
        return known_params

# Test cases for _UnionField class
def test__UnionField_init():
    desc = "A union field"
    cls = type('SomeClass', (), {})
    field = "some_field"
    union_field = _UnionField(desc, cls, field)
    
    assert union_field.desc == desc
    assert union_field.cls is cls
    assert union_field.field == field

# Test cases for _IgnoreUndefinedParameters class
def test__IgnoreUndefinedParameters_handle_from_dict():
    @dataclass
    class MyClass:
        param1: int = 1
        param2: int = 2
    
    kvs = {'param1': 10, 'param3': 30, 'param4': 40}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    
    assert len(known_params) == 1
    assert list(known_params.keys())[0] == 'param1'
    assert list(known_params.values())[0] == 10

def test__IgnoreUndefinedParameters_handle_from_dict_no_match():
    @dataclass
    class MyClass:
        param1: int = 1
        param2: int = 2
    
    kvs = {'param3': 30, 'param4': 40}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    
    assert len(known_params) == 0

def test__IgnoreUndefinedParameters_handle_from_dict_all_match():
    @dataclass
    class MyClass:
        param1: int = 1
        param2: int = 2
    
    kvs = {'param1': 10, 'param2': 20}
    known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    
    assert len(known_params) == 2
    assert list(known_params.keys())[0] == 'param1'
    assert list(known_params.values())[0] == 10
    assert list(known_params.keys())[1] == 'param2'
    assert list(known_params.values())[1] == 20
