
import pytest
from dataclasses import dataclass, fields
from typing import Collection, Dict, List, Mapping, Union
import copy
from dataclasses_json.core import _asdict, is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config
from dataclasses import asdict  # Importing from standard library for comparison

@dataclass
class Person:
    name: str
    age: int

def test_valid_inputs():
    person = Person(name="John", age=30)
    result = _asdict(person)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert result == {'name': 'John', 'age': 30}, f"Expected {{'name': 'John', 'age': 30}} but got {result}"
    
    data = [{"key": "value"}, {"another_key": "another_value"}]
    encoded_data = _asdict(data, encode_json=True)
    assert isinstance(encoded_data, List), f"Expected a list but got {type(encoded_data)}"
    for item in encoded_data:
        assert isinstance(item, Dict), f"Expected each item to be a dictionary but got {type(item)}"
        if 'key' in item:
            assert isinstance(item['key'], str), f"Expected the value of 'key' to be a string but got {type(item['key'])}"
