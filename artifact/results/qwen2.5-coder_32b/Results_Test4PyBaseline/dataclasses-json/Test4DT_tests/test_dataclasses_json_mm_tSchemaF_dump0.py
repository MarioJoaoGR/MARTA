
import pytest
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

# Mocking SchemaF since it cannot be imported from schema_module
class SchemaF:
    def dump(self, obj, many=None):
        raise NotImplementedError("This method should be overridden by subclasses")

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

class MySchema(SchemaF):
    def dump(self, obj, many=None):
        if many:
            return [person.to_json() for person in obj]
        else:
            return obj.to_json()

def test_schema_f_instantiation():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()
        schema.dump(None)  # This will raise NotImplementedError

def test_my_schema_dump_single_object():
    schema = MySchema()
    person = Person(name="John", age=30)
    assert schema.dump(person) == '{"name": "John", "age": 30}'

def test_my_schema_dump_multiple_objects():
    schema = MySchema()
    people = [
        Person(name="Alice", age=25),
        Person(name="Bob", age=30)
    ]
    assert schema.dump(people, many=True) == ['{"name": "Alice", "age": 25}', '{"name": "Bob", "age": 30}']
