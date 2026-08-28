
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import build_schema

@dataclass
class MyDataClass:
    name: str = 'default_name'
    age: int = 0

class MyMixin:
    pass

@dataclass
class EmptyDataClass:
    pass

class InvalidType:
    pass

def test_happy_path():
    CustomSchema = build_schema(MyDataClass, MyMixin, True, True)
    instance = MyDataClass(name="John Doe", age=30)
    schema_instance = CustomSchema()
    serialized_data = schema_instance.dumps(instance)
    assert serialized_data == '{"name": "John Doe", "age": 30}'

def test_edge_cases():
    CustomSchema = build_schema(EmptyDataClass, MyMixin, False, False)
    instance = EmptyDataClass()
    schema_instance = CustomSchema()
    serialized_data = schema_instance.dumps(instance)
    assert serialized_data == '{}'

def test_invalid_inputs():
    with pytest.raises(TypeError):
        CustomSchema = build_schema(InvalidType, MyMixin, 'not_a_bool', 'also_not_a_bool')
