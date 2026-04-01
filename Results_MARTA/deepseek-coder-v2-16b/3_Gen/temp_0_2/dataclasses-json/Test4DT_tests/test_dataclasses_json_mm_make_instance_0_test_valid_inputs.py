
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str
    age: int

def make_instance(cls, kvs, **kwargs):
    return cls(**kvs, **kwargs)

def test_valid_inputs():
    # Test with valid key-value pairs and additional keyword arguments
    person = make_instance(Person, {'name': 'John'}, age=30)
    
    assert person.name == 'John'
    assert person.age == 30
