
import pytest
from typesystem.json_schema import from_json_schema_type, Field
from typesystem import Float, Integer, String, Boolean, Array, Object

def test_from_json_schema_type_number():
    data = {"minimum": 0, "maximum": 10, "exclusiveMinimum": True, "default": 3.14}
    field = from_json_schema_type(data, "number", allow_null=True, definitions={})
    assert isinstance(field, Float)
    assert field.minimum == 0
    assert field.maximum == 10
    assert field.exclusive_minimum is True
    assert field.default == 3.14

def test_from_json_schema_type_integer():
    data = {"minimum": 0, "maximum": 10, "exclusiveMinimum": True, "default": 5}
    field = from_json_schema_type(data, "integer", allow_null=True, definitions={})
    assert isinstance(field, Integer)
    assert field.minimum == 0
    assert field.maximum == 10
    assert field.exclusive_minimum is True
    assert field.default == 5

def test_from_json_schema_type_string():
    data = {"minLength": 5, "maxLength": 20, "format": "email", "default": "example@example.com"}
    field = from_json_schema_type(data, "string", allow_null=False, definitions={})
    assert isinstance(field, String)
    assert field.min_length == 5
    assert field.max_length == 20
    assert field.format == "email"
    assert field.default == "example@example.com"

def test_from_json_schema_type_boolean():
    data = {"default": True}
    field = from_json_schema_type(data, "boolean", allow_null=True, definitions={})
    assert isinstance(field, Boolean)
    assert field.default is True

def test_from_json_schema_type_array():
    data = {"items": [{"type": "string"}, {"type": "integer"}], "minItems": 2}
    field = from_json_schema_type(data, "array", allow_null=False, definitions={})
    assert isinstance(field, Array)
    assert len(field.items) == 2
    assert all(isinstance(item, (String, Integer)) for item in field.items)
    assert field.min_items == 2

def test_from_json_schema_type_object():
    data = {"properties": {"name": {"type": "string"}, "age": {"type": "integer"}}, "required": ["name"]}
    field = from_json_schema_type(data, "object", allow_null=False, definitions={})
    assert isinstance(field, Object)
    assert len(field.properties) == 2
    assert all(isinstance(prop, (String, Integer)) for prop in field.properties.values())
    assert list(field.properties.keys()) == ["name", "age"]
    assert field.required == ["name"]

# Additional test cases to cover uncovered lines
def test_from_json_schema_type_array_nested():
    data = {"items": [{"type": "string"}, {"$ref": "#/definitions/integerDef"}], "minItems": 2}
    definitions = {
        "integerDef": {"type": "integer", "minimum": 0, "maximum": 10, "exclusiveMinimum": True, "default": 5}
    }
    field = from_json_schema_type(data, "array", allow_null=False, definitions=definitions)