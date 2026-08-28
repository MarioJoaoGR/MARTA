
import pytest
from typesystem.json_schema import enum_from_json_schema, SchemaDefinitions
from typesystem.fields import Choice, NO_DEFAULT

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    data = {"enum": ["Option1", "Option2"], "default": "Option1"}
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    field_instance = enum_from_json_schema(data, schema_defs)
    
    assert isinstance(field_instance, Choice)
    assert field_instance.choices == [("Option1", "Option1"), ("Option2", "Option2")]
    assert field_instance.default == "Option1"

# Scenario 2: Test invalid input with an invalid default value