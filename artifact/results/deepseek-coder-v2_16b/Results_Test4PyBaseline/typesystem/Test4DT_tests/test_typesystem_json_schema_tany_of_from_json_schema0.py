
import pytest
from typesystem.json_schema import any_of_from_json_schema, Field, Union, from_json_schema, NO_DEFAULT

# Define a mock SchemaDefinitions class for testing purposes
class MockSchemaDefinitions:
    def __init__(self):
        self.definitions = {}
    
    def get(self, key):
        return self.definitions.get(key)

def test_any_of_from_json_schema_basic():
    data = {
        "anyOf": [{"type": "integer"}, {"type": "string"}],
        "default": 123
    }
    definitions = MockSchemaDefinitions()
    union_field = any_of_from_json_schema(data, definitions)
    assert isinstance(union_field.any_of[0], Field), f"Expected a list of Field objects but got {type(union_field.any_of[0])}"
    assert not union_field.allow_null, "Expected allow_null to be False"

def test_any_of_from_json_schema_custom():
    data = {
        "anyOf": [{"type": "number"}, {"type": "string"}],
        "default": None
    }
    definitions = MockSchemaDefinitions()
    union_field = any_of_from_json_schema(data, definitions)
    assert isinstance(union_field.any_of[0], Field), f"Expected a list of Field objects but got {type(union_field.any_of[0])}"