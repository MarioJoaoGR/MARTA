
# Test case  

import pytest
from dataclasses_json.undefined import _UndefinedParameterAction
from dataclasses import dataclass  # Importing the dataclass decorator

class Example:
    def __init__(self, value):
        self.value = value

class AnotherExample:
    def __init__(self, name):
        self.name = name

@dataclass
class DataClassExample:
    id: int
    description: str

def test_create_init_with_class():
    example_init = _UndefinedParameterAction.create_init(Example)
    instance = Example.__new__(Example)
    example_init(instance, 10)
    assert instance.value == 10

def test_create_init_with_instance():
    another_instance = AnotherExample("Test")
    another_init = _UndefinedParameterAction.create_init(type(another_instance))
    another_init(another_instance, "New Name")
    assert another_instance.name == "New Name"

def test_create_init_with_dataclass():
    data_init = _UndefinedParameterAction.create_init(DataClassExample)
    data_instance = DataClassExample.__new__(DataClassExample)
    data_init(data_instance, 1, "Sample Description")
    assert data_instance.id == 1