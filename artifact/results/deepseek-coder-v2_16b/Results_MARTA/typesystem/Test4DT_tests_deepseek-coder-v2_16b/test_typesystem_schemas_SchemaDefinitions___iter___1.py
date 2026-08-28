
import pytest
from typesystem.schemas import SchemaDefinitions

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert len(schema_defs) == 2
    assert schema_defs['key1'] == 'value1'
    assert schema_defs['key2'] == 'value2'
    schema_defs['new_key'] = 'new_value'
    assert len(schema_defs) == 3
    assert schema_defs['new_key'] == 'new_value'

# Scenario 2: Test invalid inputs to raise TypeError when initializing SchemaDefinitions
def test_invalid_inputs():
    with pytest.raises(TypeError):
        SchemaDefinitions({1, 2, 3})  # Invalid input type (set) should raise TypeError

# Scenario 3: Test iteration over schema definitions
def test_iteration():
    schema_defs = SchemaDefinitions({'schema1': {'key1': 'value1'}, 'schema2': {'key2': 'value2'}})
    iterated_schemas = [schema for schema in schema_defs]
    assert len(iterated_schemas) == 2
    assert 'schema1' in iterated_schemas
    assert 'schema2' in iterated_schemas
