
# Module: dataclasses_json.mm
import pytest
from dataclasses import dataclass

# Mocking necessary components for testing
class Schema:
    @staticmethod
    def dump(obj, *, many=None):
        if isinstance(obj, list):
            return [{field: getattr(item, field) for field in item.__dataclass_fields__} for item in obj]
        else:
            return {field: getattr(obj, field) for field in obj.__dataclass_fields__}

def _handle_undefined_parameters_safe(cls, kvs, usage):
    # Mock implementation that returns an empty dictionary
    return {}

# Define a sample dataclass for testing
@dataclass
class Person:
    name: str
    age: int

# Create instances of the dataclass for testing
person = Person(name="Alice", age=30)
people = [Person(name="Alice", age=30), Person(name="Bob", age=25)]

# Assuming `schema` is an instance of a subclass of Schema that implements the dump method
class MockSchema(Schema):
    pass

schema = MockSchema()

def test_dump_single_object():
    result = schema.dump(person)
    assert isinstance(result, dict)
    assert result == {'name': 'Alice', 'age': 30}

def test_dump_multiple_objects_explicit_many_true():
    result = schema.dump(people, many=True)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {'name': 'Alice', 'age': 30}
    assert result[1] == {'name': 'Bob', 'age': 25}

def test_dump_multiple_objects_inferred_many():
    result = schema.dump(people)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {'name': 'Alice', 'age': 30}
    assert result[1] == {'name': 'Bob', 'age': 25}

def test_dump_single_object_inferred_many():
    result = schema.dump(person)
    assert isinstance(result, dict)
    assert result == {'name': 'Alice', 'age': 30}

def test_dump_empty_list_explicit_many_true():
    result = schema.dump([], many=True)
    assert isinstance(result, list)
    assert len(result) == 0

def test_dump_empty_list_inferred_many():
    result = schema.dump([])
    assert isinstance(result, list)
    assert len(result) == 0
