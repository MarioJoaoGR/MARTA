# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass, field
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass(_IgnoreUndefinedParameters):
    param1: int = field(default=0)
    param2: str = field(default='default')

def test_handle_from_dict_with_defined_parameters():
    kvs = {'param1': 10, 'param2': 'value'}
    result = MyClass.handle_from_dict(MyClass, kvs)
    assert result == {'param1': 10, 'param2': 'value'}

def test_handle_from_dict_with_extra_undefined_parameters():
    kvs_with_extra = {'param1': 10, 'param3': 'extra', 'param2': 'value'}
    result_with_extra = MyClass.handle_from_dict(MyClass, kvs_with_extra)
    assert result_with_extra == {'param1': 10, 'param2': 'value'}

def test_handle_from_dict_with_no_parameters():
    empty_kvs = {}
    result_empty = MyClass.handle_from_dict(MyClass, empty_kvs)
    assert result_empty == {}

def test_handle_from_dict_with_only_undefined_parameters():
    undefined_kvs = {'param3': 'extra', 'param4': 'another_extra'}
    result_undefined = MyClass.handle_from_dict(MyClass, undefined_kvs)
    assert result_undefined == {}

def test_handle_from_dict_with_mixed_data_types_for_values():
    mixed_kvs = {'param1': 20, 'param2': [1, 2, 3], 'param3': 'extra'}
    result_mixed = MyClass.handle_from_dict(MyClass, mixed_kvs)
    assert result_mixed == {'param1': 20, 'param2': [1, 2, 3]}

def test_handle_from_dict_with_none_values():
    none_kvs = {'param1': None, 'param2': None}
    result_none = MyClass.handle_from_dict(MyClass, none_kvs)
    assert result_none == {'param1': None, 'param2': None}

def test_handle_from_dict_with_nested_dataclass():
    @dataclass
    class NestedClass(_IgnoreUndefinedParameters):
        nested_param: int

    @dataclass
    class OuterClass(_IgnoreUndefinedParameters):
        param1: int
        nested: NestedClass

    kvs = {'param1': 10, 'nested': {'nested_param': 5}}
    result_nested = OuterClass.handle_from_dict(OuterClass, kvs)
    assert result_nested == {'param1': 10, 'nested': {'nested_param': 5}}

def test_handle_from_dict_with_non_matching_types():
    non_matching_kvs = {'param1': 'not an int', 'param2': 123}
    result_non_matching = MyClass.handle_from_dict(MyClass, non_matching_kvs)
    assert result_non_matching == {'param1': 'not an int', 'param2': 123}

def test_handle_from_dict_with_empty_string_keys():
    empty_string_key_kvs = {'': 'value', 'param1': 10}
    result_empty_string_key = MyClass.handle_from_dict(MyClass, empty_string_key_kvs)
    assert result_empty_string_key == {'param1': 10}
