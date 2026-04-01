
from dataclasses_json.api import DataClassJsonMixin
import pytest
import json
from typing import Optional, Union, Tuple, Callable
import dataclasses

@dataclasses.dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_case():
    data = MyDataClass(name="John Doe", age=30)
    json_string = data.to_json()
    
    expected_output = '{"name": "John Doe", "age": 30}'
    assert json_string == expected_output
