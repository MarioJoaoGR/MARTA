
# Module: typesystem.json_schema
import pytest
from typesystem.json_schema import all_of_from_json_schema, from_json_schema, Field, AllOf

# Define a sample schema for testing
sample_definitions = {
    "stringSchema": {"type": "string"},
    "numberSchema": {"minimum": 10, "maximum": 100}
}

def test_all_of_from_json_schema_basic():
    data = {
        "allOf": [{"type": "string"}, {"minimum": 10, "maximum": 100}]
    }
    field_instance = all_of_from_json_schema(data, sample_definitions)
    assert isinstance(field_instance, AllOf)
    assert len(field_instance.all_of) == 2
    assert all(isinstance(f, Field) for f in field_instance.all_of)

def test_all_of_from_json_schema_default():
    data = {
        "allOf": [{"type": "string"}, {"minimum": 10, "maximum": 100}],
        "default": "default_value"
    }
    field_instance = all_of_from_json_schema(data, sample_definitions)
    assert isinstance(field_instance, AllOf)
    assert len(field_instance.all_of) == 2
    assert all(isinstance(f, Field) for f in field_instance.all_of)
    assert field_instance.default == "default_value"

def test_all_of_from_json_schema_different_definitions():
    data = {
        "allOf": [{"type": "integer"}, {"minimum": 100}]
    }
    field_instance = all_of_from_json_schema(data, sample_definitions)
    assert isinstance(field_instance, AllOf)
    assert len(field_instance.all_of) == 2
    assert all(isinstance(f, Field) for f in field_instance.all_of)

def test_all_of_from_json_schema_edge_cases():
    data = {
        "allOf": [{"type": "number"}, {"minimum": -100, "maximum": 0}]
    }
    field_instance = all_of_from_json_schema(data, sample_definitions)
    assert isinstance(field_instance, AllOf)
    assert len(field_instance.all_of) == 2
    assert all(isinstance(f, Field) for f in field_instance.all_of)

def test_all_of_from_json_schema_default_and_definitions():
    data = {
        "allOf": [{"type": "boolean"}, {"minimum": 1}]
    }
    field_instance = all_of_from_json_schema(data, sample_definitions)
    assert isinstance(field_instance, AllOf)
    assert len(field_instance.all_of) == 2
    assert all(isinstance(f, Field) for f in field_instance.all_of)
