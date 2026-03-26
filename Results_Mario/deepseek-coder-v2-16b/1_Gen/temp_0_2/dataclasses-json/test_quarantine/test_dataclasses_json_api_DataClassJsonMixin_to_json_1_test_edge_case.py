
import pytest
from dataclasses import dataclass
from typing import Optional, Union, Tuple, Callable
from dataclasses_json.api import DataClassJsonMixin
import json

# Assuming _ExtendedEncoder is defined in your module or context where it should be imported from 'your_module'
class _ExtendedEncoder(json.JSONEncoder):
    pass  # Implement any custom encoding logic if necessary

@dataclass
class YourDataclass(DataClassJsonMixin):
    name: str
    age: int

def test_to_json():
    obj = YourDataclass(name='John Doe', age=30)
    expected_output = '{"name": "John Doe", "age": 30}'
    
    # Call the to_json method and check if it returns the expected JSON string
    json_str = obj.to_json()
    assert json_str == expected_output, f"Expected {expected_output}, but got {json_str}"
