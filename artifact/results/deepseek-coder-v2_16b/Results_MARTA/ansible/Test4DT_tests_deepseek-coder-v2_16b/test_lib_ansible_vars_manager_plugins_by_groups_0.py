
import pytest
from unittest.mock import patch, MagicMock

# Assuming host_groups is defined somewhere in this scope or imported from another module
host_groups = ['group1', 'group2']  # Example host groups

def _combine_and_track(existing, new, description):
    """Helper function to combine and track data."""
    return {**existing, **new}

def _plugins_inventory(group):
    """Mocked function to simulate fetching inventory group variables for a given group."""
    if group == 'group1':
        return {'key1': 'value1', 'key2': 'value2'}
    elif group == 'group2':
        return {'key3': 'value3'}
    return {}

def _plugins_play(group):
    """Mocked function to simulate fetching playbook group variables for a given group."""
    if group == 'group1':
        return {'key4': 'value4', 'key5': 'value5'}
    elif group == 'group2':
        return {'key6': 'value6'}
    return {}

def plugins_by_groups():
    """Merges all plugin sources by group."""
    data = {}
    for group in host_groups:
        data[group] = _combine_and_track(data.get(group, {}), _plugins_inventory(group), "inventory group_vars for '%s'" % group)
        data[group] = _combine_and_track(data[group], _plugins_play(group), "playbook group_vars for '%s'" % group)
    return data

# Test functions
def test_valid_input():
    result = plugins_by_groups()
    assert isinstance(result, dict)
    assert len(result) == 2
    assert 'group1' in result and 'group2' in result
    assert result['group1'] == {'key1': 'value1', 'key2': 'value2', 'key4': 'value4', 'key5': 'value5'}
    assert result['group2'] == {'key3': 'value3', 'key6': 'value6'}

def test_edge_case_none():
    with patch('__main__.host_groups', None):
        with pytest.raises(TypeError):
            plugins_by_groups()

def test_error_handling():
    with patch('__main__._plugins_inventory', MagicMock(side_effect=Exception("Mocked error"))):
        with patch('__main__._plugins_play', MagicMock(side_effect=Exception("Mocked error"))):
            with pytest.raises(Exception):
                plugins_by_groups()
