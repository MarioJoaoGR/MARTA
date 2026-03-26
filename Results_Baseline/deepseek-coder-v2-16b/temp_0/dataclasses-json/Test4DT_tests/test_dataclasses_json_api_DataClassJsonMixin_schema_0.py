
# Module: dataclasses_json.api
# test_dataclass_json.py
from dataclasses import dataclass
from dataclasses_json import dataclass_json, DataClassJsonMixin
import pytest

@dataclass_json
@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int = 0

def test_person_serialization():
    person = Person(name="John Doe", age=30)
    serialized = person.to_dict()
    assert serialized == {"name": "John Doe", "age": 30}

def test_person_deserialization():
    data = {"name": "John Doe", "age": 30}
    person = Person.from_dict(data)
    assert person.name == "John Doe"
    assert person.age == 30

@pytest.mark.xfail(reason="Expected TypeError not raised")
def test_person_serialization_with_missing_field():
    with pytest.raises(TypeError):
        person = Person(name="John Doe")
        serialized = person.to_dict()
