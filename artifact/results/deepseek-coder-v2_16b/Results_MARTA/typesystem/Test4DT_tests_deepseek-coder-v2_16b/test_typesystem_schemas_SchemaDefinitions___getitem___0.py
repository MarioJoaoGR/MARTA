
import pytest
from typesystem.schemas import SchemaDefinitions

# Scenario 1: Test standard input for __getitem__ method with valid key
def test_valid_input():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    assert schema_defs['key1'] == 'value1'
    assert schema_defs['key2'] == 'value2'

# Scenario 2: Test edge case for __getitem__ method with None key
def test_edge_case():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(KeyError):
        assert schema_defs[None]

# Scenario 3: Test invalid input for __getitem__ method with non-existent key
def test_invalid_input():
    schema_defs = SchemaDefinitions({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(KeyError):
        assert schema_defs['non_existent_key']
