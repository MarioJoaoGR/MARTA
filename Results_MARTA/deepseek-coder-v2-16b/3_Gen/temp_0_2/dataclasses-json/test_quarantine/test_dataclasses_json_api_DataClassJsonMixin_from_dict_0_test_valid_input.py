
import pytest
from dataclasses import dataclass
from typing import Optional, Type, Dict, Any as Json
from dataclasses_json import DataClassJsonMixin

# Mocking the Person class with DataClassJsonMixin
@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_valid_input():
    # Valid input dictionary
    valid_dict = {"name": "John Doe", "age": 30}
    
    # Creating an instance of Person from the valid dictionary
    person = Person.from_dict(valid_dict)
    
    # Asserting that the created object matches the expected values
    assert person.name == "John Doe"
    assert person.age == 30
