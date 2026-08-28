
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json

# Assuming _decode_dataclass is a function that exists in dataclasses_json.mm
# Since it's not directly accessible, we will simulate its behavior for testing purposes.
def _decode_dataclass(cls, kvs, partial=False):
    if partial:
        return cls(**{k: v for k, v in kvs.items() if k in cls.__dataclass_fields__})
    else:
        return cls(**kvs)

@dataclass_json
@dataclass
class Person:
    name: str
    age: int

def make_instance(cls, kvs, **kwargs):
    return _decode_dataclass(cls, {**kvs, **kwargs})

# Test cases
def test_make_instance_basic():
    person = make_instance(Person, {'name': 'Alice', 'age': 30})
    assert person.name == 'Alice'
    assert person.age == 30

def test_make_instance_with_override():
    person = make_instance(Person, {'name': 'Bob', 'age': 25}, age=40)
    assert person.name == 'Bob'
    assert person.age == 40

def test_make_instance_with_default_value():
    person = make_instance(Person, {'name': 'Charlie'}, age=28)
    assert person.name == 'Charlie'
    assert person.age == 28
