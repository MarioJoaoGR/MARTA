# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass, field
from typing import Dict, Any, Tuple

# Import the function from the provided module
from dataclasses_json.undefined import _UndefinedParameterAction

# Define a simple dataclass that inherits from _UndefinedParameterAction for testing
@dataclass
class MyClass(_UndefinedParameterAction):
    param1: int = field(default=0)
    param2: str = field(default='default')

# Type aliases for clarity
KnownParameters = Dict[str, Any]
UnknownParameters = Dict[str, Any]

def test_separate_defined_undefined_kvs():
    # Example dictionary with both defined and undefined keys
    kvs = {'param1': 10, 'param3': 'extra', 'param2': 'value'}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs)
    assert known_params == {'param1': 10, 'param2': 'value'}, "Known parameters do not match expected output"
    assert unknown_params == {'param3': 'extra'}, "Unknown parameters do not match expected output"

def test_separate_defined_undefined_kvs_only_defined():
    # Example dictionary with only defined keys
    kvs_only_defined = {'param1': 5, 'param2': 'test'}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_only_defined)
    assert known_params == {'param1': 5, 'param2': 'test'}, "Known parameters do not match expected output"
    assert unknown_params == {}, "Unknown parameters should be empty"

def test_separate_defined_undefined_kvs_only_undefined():
    # Example dictionary with only undefined keys
    kvs_only_undefined = {'param4': 7, 'param5': 'another'}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_only_undefined)
    assert known_params == {}, "Known parameters should be empty"
    assert unknown_params == {'param4': 7, 'param5': 'another'}, "Unknown parameters do not match expected output"

def test_separate_defined_undefined_kvs_empty_dict():
    # Example with an empty dictionary
    kvs_empty = {}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_empty)
    assert known_params == {}, "Known parameters should be empty"
    assert unknown_params == {}, "Unknown parameters should be empty"

def test_separate_defined_undefined_kvs_no_overlap():
    # Example with no overlap between defined and provided keys
    kvs_no_overlap = {'param3': 'extra', 'param4': 7}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_no_overlap)
    assert known_params == {}, "Known parameters should be empty"
    assert unknown_params == {'param3': 'extra', 'param4': 7}, "Unknown parameters do not match expected output"

def test_separate_defined_undefined_kvs_all_same():
    # Example where all provided keys are the same as defined keys with different values
    kvs_all_same = {'param1': 10, 'param2': 'value'}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_all_same)
    assert known_params == {'param1': 10, 'param2': 'value'}, "Known parameters do not match expected output"
    assert unknown_params == {}, "Unknown parameters should be empty"

def test_separate_defined_undefined_kvs_case_sensitive():
    # Example with case-sensitive keys
    kvs_case_sensitive = {'Param1': 10, 'param2': 'value'}
    known_params, unknown_params = MyClass._separate_defined_undefined_kvs(MyClass, kvs_case_sensitive)
    assert known_params == {'param2': 'value'}, "Known parameters do not match expected output"
    assert unknown_params == {'Param1': 10}, "Unknown parameters do not match expected output"
