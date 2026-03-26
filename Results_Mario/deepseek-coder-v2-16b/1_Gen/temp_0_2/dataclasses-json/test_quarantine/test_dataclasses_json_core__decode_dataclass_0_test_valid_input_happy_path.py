
import pytest
from dataclasses import dataclass, fields
from typing import Optional
from dataclasses_json.core import _decode_dataclass

@dataclass
class ExampleDataclass:
    name: str
    age: int
    email: Optional[str] = None

def test_valid_input_happy_path():
    # Define a valid input dictionary
    kvs = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}
    
    # Call the function with the dataclass and the input dictionary
    result = _decode_dataclass(ExampleDataclass, kvs, infer_missing=True)
    
    # Assert that the result is an instance of ExampleDataclass
    assert isinstance(result, ExampleDataclass)
    
    # Assert that the fields are correctly populated
    assert result.name == "John Doe"
    assert result.age == 30
    assert result.email == "john.doe@example.com"
