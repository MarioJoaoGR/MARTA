
# Test case  
import pytest
from dataclasses_json.mm import SchemaF
from dataclasses_json import DataClassJsonMixin
import dataclasses

def test_schemaf_instantiation_raises_notimplementederror():
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

def test_schemaf_subclass_can_be_instantiated():
    class MySchema(SchemaF):
        def __init__(self, *args, **kwargs):
            pass  # Avoid calling the parent class's __init__

    # This should not raise an error because we are not calling the parent class's __init__
    my_schema_instance = MySchema()

def test_schemaf_subclass_methods_can_be_defined():
    @dataclasses.dataclass
    class Person(DataClassJsonMixin):
        name: str
        age: int

    class MySchema(SchemaF):
        def __init__(self, *args, **kwargs):
            pass  # Avoid calling the parent class's __init__

        def dump(self, obj: Person, many: bool = None) -> dict:
            if many is True:
                return [person.to_json() for person in obj]
            else:
                return obj.to_json()

        def dumps(self, obj: Person, many: bool = None, *args, **kwargs) -> str:
            if many is True:
                return '[' + ','.join([person.to_json(indent=2) for person in obj]) + ']'
            else:
                return obj.to_json(*args, **kwargs)

        def load(self, data: dict, many: bool = None, partial: bool = None, unknown: str = None) -> Person:
            if many is True:
                return [Person.from_json(person_data) for person_data in data]
            else:
                return Person.from_json(data)

        def loads(self, json_data: str, many: bool = None, partial: bool = None, unknown: str = None, **kwargs) -> Person:
            if many is True:
                import json
                data_list = json.loads(json_data)
                return [Person.from_json(person_data) for person_data in data_list]
            else:
                return Person.from_json(json_data)

    # Create an instance of MySchema
    schema = MySchema()

    # Serialize a single object
    person = Person(name="John", age=30)
    serialized_person = schema.dumps(person)
    assert serialized_person == '{"name": "John", "age": 30}'

    # Deserialize a JSON string into an object
    json_data = '{"name": "Jane", "age": 25}'
    deserialized_person = schema.loads(json_data)
    assert deserialized_person.name == "Jane" and deserialized_person.age == 25

    # Serialize multiple objects
    people = [Person(name="Alice", age=30), Person(name="Bob", age=25)]
    serialized_people = schema.dumps(people, many=True)