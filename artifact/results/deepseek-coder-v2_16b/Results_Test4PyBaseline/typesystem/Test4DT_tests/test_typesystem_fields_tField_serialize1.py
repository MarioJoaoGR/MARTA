
import pytest
from typesystem.fields import Field, NO_DEFAULT
import typing

def test_field_creation():
    field = Field(title="Name", description="The name of the person")
    assert isinstance(field.title, str)
    assert field.title == "Name"
    assert isinstance(field.description, str)
    assert field.description == "The name of the person"

def test_serialize_returns_input():
    field = Field()
    # Test with different types of input objects
    assert field.serialize("string") == "string"
    assert field.serialize(123) == 123
    assert field.serialize([1, 2, 3]) == [1, 2, 3]
    assert field.serialize({"key": "value"}) == {"key": "value"}
    assert field.serialize(None) is None
    # Test with complex nested structures
    nested_obj = {"list": [1, 2, 3], "dict": {"nested_key": "nested_value"}}
    assert field.serialize(nested_obj) == nested_obj

def test_serialize_with_subclass():
    class CustomFormat(Field):
        def serialize(self, obj: typing.Any) -> typing.Any:
            return {"custom": obj}
    
    custom_field = CustomFormat()
    assert custom_field.serialize("string") == {"custom": "string"}