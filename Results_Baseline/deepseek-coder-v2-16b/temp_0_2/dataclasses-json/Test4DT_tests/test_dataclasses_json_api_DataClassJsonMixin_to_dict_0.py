
# Module: dataclasses_json.api
from dataclasses_json.api import DataClassJsonMixin
import pytest
from typing import Dict, Optional

# Define a sample dataclass for testing
from dataclasses import dataclass

@dataclass
class SampleDataclass(DataClassJsonMixin):
    name: str
    age: int

def test_to_dict_without_json():
    # Test the to_dict method without JSON encoding
    sample = SampleDataclass(name="John", age=30)
    result = sample.to_dict()
    assert isinstance(result, dict), "Expected a dictionary as output"
    assert result == {'name': 'John', 'age': 30}, "Unexpected dictionary representation"

def test_to_dict_with_json():
    # Test the to_dict method with JSON encoding
    sample = SampleDataclass(name="Jane", age=25)
    result = sample.to_dict(encode_json=True)
    assert isinstance(result, dict), "Expected a dictionary as output"