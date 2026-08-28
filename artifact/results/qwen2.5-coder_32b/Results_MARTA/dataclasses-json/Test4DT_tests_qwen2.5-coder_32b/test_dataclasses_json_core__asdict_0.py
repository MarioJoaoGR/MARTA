
import pytest
from dataclasses import dataclass
from typing import List, Dict, Any
from collections.abc import Mapping, Collection
import copy

# Assuming _asdict is part of a module named `dataclasses_json.core`
from dataclasses_json.core import _asdict, _is_dataclass_instance, fields, _handle_undefined_parameters_safe, _encode_overrides, _user_overrides_or_exts


@dataclass
class Person:
    name: str
    age: int

def test_asdict_with_dataclass():
    person = Person(name="Alice", age=30)
    expected_output = {'name': 'Alice', 'age': 30}
    assert _asdict(person) == expected_output

def test_asdict_with_dataclass_encode_json():
    person = Person(name="Alice", age=30)
    expected_output = {'name': 'Alice', 'age': 30}
    assert _asdict(person, encode_json=True) == expected_output

def test_asdict_with_dict():
    my_dict = {'key1': 'value1', 'key2': [1, 2, 3]}
    expected_output = {'key1': 'value1', 'key2': [1, 2, 3]}
    assert _asdict(my_dict) == expected_output

def test_asdict_with_list():
    my_list = [{'name': 'Alice'}, {'name': 'Bob'}]
    expected_output = [{'name': 'Alice'}, {'name': 'Bob'}]
    assert _asdict(my_list) == expected_output

def test_asdict_with_set():
    my_set = {1, 2, 3}
    expected_output = [1, 2, 3]  # Note: sets are unordered, but the values should be the same
    assert sorted(_asdict(my_set)) == sorted(expected_output)

def test_asdict_with_nested_structure():
    nested_structure = {
        'person': Person(name="Alice", age=30),
        'numbers': [1, 2, {'three': 3}]
    }
    expected_output = {
        'person': {'name': 'Alice', 'age': 30},
        'numbers': [1, 2, {'three': 3}]
    }
    assert _asdict(nested_structure) == expected_output

def test_asdict_with_nested_structure_encode_json():
    nested_structure = {
        'person': Person(name="Alice", age=30),
        'numbers': [1, 2, {'three': 3}]
    }
    expected_output = {
        'person': {'name': 'Alice', 'age': 30},
        'numbers': [1, 2, {'three': 3}]
    }
    assert _asdict(nested_structure, encode_json=True) == expected_output
