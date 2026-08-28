
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

# Scenario 2: Test adding a new key-value pair to the schema definitions
def test_add_new_key():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    schema_defs['new_key'] = 'new_value'
    assert len(schema_defs) == 3
    assert schema_defs['new_key'] == 'new_value'

# Scenario 3: Test retrieving a value from the schema definitions
def test_get_item():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert schema_defs['key1'] == 'value1'
    assert schema_defs['key2'] == 'value2'

# Scenario 4: Test checking if a key exists in the schema definitions
def test_contains():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert 'key1' in schema_defs
    assert 'key3' not in schema_defs

# Scenario 5: Test removing a key-value pair from the schema definitions
def test_remove_item():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    del schema_defs['key1']
    assert len(schema_defs) == 1
    with pytest.raises(KeyError):
        print(schema_defs['key1'])
