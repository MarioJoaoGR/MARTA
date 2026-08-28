
import pytest
from dataclasses import dataclass
import typing
from dataclasses_json.mm import schema

@dataclass
class MyMixin:
    pass

@dataclass
class TestClass(MyMixin):
    name: str = 'John'
    age: int = 30

@dataclass
class EdgeCaseClass(MyMixin):
    name: typing.Optional[str] = None
    age: int = 0

def test_happy_path():
    schema_dict = schema(TestClass, MyMixin, True)
    assert 'name' in schema_dict and 'age' in schema_dict

def test_edge_cases():
    schema_dict = schema(EdgeCaseClass, MyMixin, False)
    assert 'name' in schema_dict and 'age' in schema_dict
    assert schema_dict['name'].allow_none is True

def test_invalid_inputs():
    invalid_class = 'not_a_dataclass'
    with pytest.raises(TypeError):
        schema(invalid_class, MyMixin, True)
