
import pytest
from typesystem.json_schema import SchemaDefinitions, Field, ref_from_json_schema
from unittest.mock import patch

# Test case 1: Valid $ref with supported style
def test_valid_ref():
    schema_data = {"$ref": "#/definitions/exampleSchema"}
    definitions = SchemaDefinitions({"exampleSchema": {"type": "object", "properties": {}}})
    
    with patch('typesystem.json_schema.Reference', autospec=True) as mock_reference:
        ref_from_json_schema(schema_data, definitions)
        assert mock_reference.called

# Test case 2: Invalid $ref without supported style
def test_invalid_ref():
    schema_data = {"$ref": "https://example.com/schema"}
    definitions = SchemaDefinitions({"exampleSchema": {"type": "object", "properties": {}}})
    
    with pytest.raises(AssertionError):
        ref_from_json_schema(schema_data, definitions)

# Test case 3: No $ref in schema data
def test_no_ref():
    schema_data = {"type": "object", "properties": {}}
    definitions = SchemaDefinitions({"exampleSchema": {"type": "object", "properties": {}}})
    
    with pytest.raises(KeyError):
        ref_from_json_schema(schema_data, definitions)
