
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

# Scenario 2: Test adding a new definition to the schema definitions
def test_add_definition():
    schema_defs = SchemaDefinitions({'key1': 'value1'})
    schema_defs['key2'] = 'value2'
    assert len(schema_defs) == 2
    assert schema_defs['key1'] == 'value1'
    assert schema_defs['key2'] == 'value2'

# Scenario 3: Test retrieving a definition from the schema definitions
def test_get_definition():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert schema_defs['key1'] == 'value1'
    assert schema_defs.get('key1') == 'value1'
    assert schema_defs.get('key2') == 'value2'

# Scenario 4: Test checking if a definition exists in the schema definitions
def test_definition_exists():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert 'key1' in schema_defs
    assert 'key2' in schema_defs
    assert 'non_existent_key' not in schema_defs
