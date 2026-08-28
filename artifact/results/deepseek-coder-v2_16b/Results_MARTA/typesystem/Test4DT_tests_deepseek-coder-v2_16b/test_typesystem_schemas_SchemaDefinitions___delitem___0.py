
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

# Scenario 2: Test invalid input by attempting to delete a None key
def test_invalid_input():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(KeyError):
        del schema_defs[None]

# Scenario 3: Test adding and removing definitions
def test_add_and_remove():
    schema_defs = SchemaDefinitions()
    assert len(schema_defs) == 0
    schema_defs['key1'] = 'value1'
    assert len(schema_defs) == 1
    assert schema_defs['key1'] == 'value1'
    del schema_defs['key1']
    assert len(schema_defs) == 0
