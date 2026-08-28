
import pytest
import typing
from typesystem.json_schema import from_json_schema, Field, Any, NeverMatch

# Test cases for the `from_json_schema` function

def test_simple_boolean():
    field = from_json_schema(True)  # Returns an Any() field
    assert isinstance(field, Any), f"Expected type: <class 'typesystem.fields.Any'> but got {type(field)}"

def test_complex_schema():
    complex_data = {
        "definitions": {
            "address": {"type": "string"},
            "age": {"type": "integer"}
        },
        "properties": {
            "name": {"type": ["string", "null"]},
            "address": {"$ref": "#/definitions/address"},
            "age": {"const": 18}
        }
    }
    field_from_complex = from_json_schema(complex_data)  # Returns a complex Field instance based on the schema constraints