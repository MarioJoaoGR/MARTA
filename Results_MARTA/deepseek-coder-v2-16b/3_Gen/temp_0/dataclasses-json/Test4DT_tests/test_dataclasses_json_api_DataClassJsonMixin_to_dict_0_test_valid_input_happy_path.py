
import pytest
from dataclasses import dataclass
from typing import Dict, Optional
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_input_happy_path():
    data = MyDataClass(name="John Doe", age=30)
    result = data.to_dict()
    assert isinstance(result, dict), "The result should be a dictionary"
    assert set(result.keys()) == {'name', 'age'}, "The keys in the dictionary should match the dataclass fields"
    assert result['name'] == 'John Doe', "The value for name should be 'John Doe'"
    assert result['age'] == 30, "The value for age should be 30"

    encoded_data = data.to_dict(encode_json=True)
    assert isinstance(encoded_data, dict), "The encoded result should be a dictionary"
    assert set(encoded_data.keys()) == {'name', 'age'}, "The keys in the encoded dictionary should match the dataclass fields"
    assert encoded_data['name'] == 'John Doe', "The value for name should still be 'John Doe' after encoding"
    assert encoded_data['age'] == 30, "The value for age should still be 30 after encoding"
