
import pytest
from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json
from dataclasses_json.core import _decode_generic
from dataclasses_json.core import is_dataclass

# Define a sample dataclass for testing
@dataclass_json
@dataclass
class SampleDataClass:
    name: str
    age: Optional[int] = None
    score: Union[float, int] = 0.0

def test_valid_inputs():
    # Valid JSON data for the dataclass
    valid_json = {
        "name": "John Doe",
        "age": 30,
        "score": 85.5
    }
    
    # Decode the JSON to the dataclass instance
    decoded_instance = _decode_generic(SampleDataClass, valid_json, False)
    
    # Assert that the decoding was successful and matches the expected values
    assert isinstance(decoded_instance, SampleDataClass), "The decoded object is not an instance of the dataclass"
    assert decoded_instance.name == "John Doe", "Name does not match the expected value"
    assert decoded_instance.age == 30, "Age does not match the expected value"
    assert decoded_instance.score == 85.5, "Score does not match the expected value"
