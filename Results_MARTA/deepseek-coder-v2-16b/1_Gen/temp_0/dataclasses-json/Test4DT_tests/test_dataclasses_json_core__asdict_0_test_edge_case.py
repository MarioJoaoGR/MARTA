
import pytest
from dataclasses import dataclass, fields
from typing import Union, Mapping, Collection, Dict, List, Any
import copy
from dataclasses_json.core import _asdict, is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config
from dataclasses import asdict  # Importing from standard library for comparison

@dataclass
class SimpleTestDataClass:
    name: str
    age: int

def test_asdict():
    data = SimpleTestDataClass(name="John Doe", age=30)
    result = _asdict(data)
    assert isinstance(result, dict)
    assert result == {'name': 'John Doe', 'age': 30}

def test_asdict_with_encode_json():
    data = SimpleTestDataClass(name="John Doe", age=30)
    result = _asdict(data, encode_json=True)
    assert isinstance(result, dict)
    assert result == {'name': 'John Doe', 'age': 30}

def test_asdict_with_mapping():
    data_mapping = {"key": [1, "string", {"nestedKey": None}]}
    result = _asdict(data_mapping, encode_json=True)
    assert isinstance(result, dict)
    assert result == {'key': [1, 'string', {'nestedKey': None}]}

def test_asdict_with_collection():
    data_collection = [SimpleTestDataClass(name="John Doe", age=30), SimpleTestDataClass(name="Jane Doe", age=25)]
    result = _asdict(data_collection, encode_json=True)
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
    assert result == [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
