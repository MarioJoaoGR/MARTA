
import pytest
from dataclasses import dataclass, fields
from typing import Type, Dict, Any
from dataclasses_json.core import _decode_dataclass

@dataclass
class Person:
    name: str
    age: int = 0

def test_decode_dataclass():
    # Test data
    json_data = {"name": "John Doe", "age": 30}
    
    # Expected dataclass instance
    expected_person = Person(name="John Doe", age=30)
    
    # Call the function under test
    result = _decode_dataclass(Person, json_data, False)
    
    # Assert that the result matches the expected dataclass instance
    assert isinstance(result, Person)
    assert result == expected_person
