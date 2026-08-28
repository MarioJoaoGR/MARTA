
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass:
    known_param1: int
    known_param2: str

@dataclass
class EmptyClass:
    pass

@dataclass
class DetailedClass:
    id: int
    name: str
    is_active: bool

@dataclass
class Address:
    street: str
    city: str

@dataclass
class Person:
    name: str
    address: Address

def test_handle_from_dict_with_known_parameters():
    kvs = {'known_param1': 42, 'unknown_param': 'value', 'known_param2': 'example'}
    result = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
    assert result == {'known_param1': 42, 'known_param2': 'example'}

def test_handle_from_dict_with_no_fields():
    kvs = {'param1': 10, 'param2': 'test'}
    result = _IgnoreUndefinedParameters.handle_from_dict(EmptyClass, kvs)
    assert result == {}

def test_handle_from_dict_with_multiple_fields_of_different_types():
    kvs = {'id': 101, 'name': 'John Doe', 'is_active': True, 'extra_field': 'ignore'}
    result = _IgnoreUndefinedParameters.handle_from_dict(DetailedClass, kvs)
    assert result == {'id': 101, 'name': 'John Doe', 'is_active': True}

def test_handle_from_dict_with_nested_dataclasses():
    kvs = {'name': 'Jane Doe', 'address': {'street': '123 Elm St', 'city': 'Somewhere'}, 'extra_field': 456}
    result = _IgnoreUndefinedParameters.handle_from_dict(Person, kvs)
    assert result == {'name': 'Jane Doe', 'address': {'street': '123 Elm St', 'city': 'Somewhere'}}
