
import pytest
from ansible.vars.manager import get_vars_from_inventory_sources

def test_valid_input():
    entities = [
        {'source': 'plugin1', 'config': {'key1': 'value1'}},
        {'source': 'plugin2', 'config': {'key2': 'value2'}},
        {'source': 'plugin1', 'config': {'key3': 'value3'}}
    ]
    expected_output = {
        'plugin1': [{'config': {'key1': 'value1', 'key3': 'value3'}}, {'config': {'key3': 'value3'}}],
        'plugin2': [{'config': {'key2': 'value2'}}]
    }
    result = get_vars_from_inventory_sources(None, None, entities, None)
    assert result == expected_output

def test_empty_list():
    entities = []
    expected_output = {}
    result = get_vars_from_inventory_sources(None, None, entities, None)
    assert result == expected_output

def test_missing_source_key():
    entities = [
        {'config': {'key1': 'value1'}},
        {'source': 'plugin2', 'config': {'key2': 'value2'}},
        {'source': 'plugin1', 'config': {'key3': 'value3'}}
    ]
    expected_output = {
        'plugin1': [{'config': {'key3': 'value3'}}],
        'plugin2': [{'config': {'key2': 'value2'}}]
    }
    result = get_vars_from_inventory_sources(None, None, entities, None)
    assert result == expected_output
