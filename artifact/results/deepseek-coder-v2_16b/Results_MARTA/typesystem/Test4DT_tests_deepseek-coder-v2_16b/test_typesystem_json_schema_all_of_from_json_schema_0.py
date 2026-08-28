
import pytest
from typesystem.json_schema import all_of_from_json_schema, Field, SchemaDefinitions, NO_DEFAULT, AllOf

# Test data for basic functionality
data = {
    "allOf": [{"type": "string"}, {"minimum": 10}],
    "default": None
}
definitions = {}

def test_all_of_from_json_schema_basic():
    schema_instance = all_of_from_json_schema(data, definitions)
    
    # Assert that the returned instance is of type AllOf
    assert isinstance(schema_instance, AllOf), "Expected an instance of AllOf"
    
    # Assert that the all_of field contains the correct fields
    assert len(schema_instance.all_of) == 2, "Expected two fields in all_of"
    assert all(isinstance(field, Field) for field in schema_instance.all_of), "All items in all_of should be instances of Field"
    
    # Assert that the default value is set correctly
    assert schema_instance.default == data["default"], "Expected default value to match the provided default key in data"
