
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture(scope="module")
def inventory():
    return InventoryData()

# Test for valid input to deserialize method
def test_valid_input(inventory):
    data = {
        'hosts': {'host1': {}, 'host2': {}},
        'groups': {'group1': {}, 'group2': {}},
        'local': None,
        'source': 'file:/path/to/inventory',
        'processed_sources': []
    }
    inventory.deserialize(data)
    assert len(inventory.hosts) == 2
    assert len(inventory.groups) == 2
    assert inventory.localhost is None
    assert inventory.current_source == 'file:/path/to/inventory'
    assert inventory.processed_sources == []

# Test for edge cases with None, empty lists and boundary values
def test_edge_case(inventory):
    # Test with None input
    with pytest.raises(TypeError):
        inventory.deserialize(None)
    
    # Test with empty hosts and groups
    data = {
        'hosts': {},
        'groups': {},
        'local': None,
        'source': 'file:/path/to/inventory',
        'processed_sources': []
    }
    inventory.deserialize(data)
    assert len(inventory.hosts) == 0
    assert len(inventory.groups) == 2  # all and ungrouped are always present
    assert inventory.localhost is None
    assert inventory.current_source == 'file:/path/to/inventory'
    assert inventory.processed_sources == []
    
    # Test with boundary values for hosts and groups
    data = {
        'hosts': {'host1': {}, 'host2': {}},
        'groups': {'group1': {}, 'group2': {}},
        'local': None,
        'source': '',
        'processed_sources': ['initial']
    }
    inventory.deserialize(data)
    assert len(inventory.hosts) == 2
    assert len(inventory.groups) == 4  # now including all and ungrouped twice
    assert inventory.localhost is None
    assert inventory.current_source == ''
    assert inventory.processed_sources == ['initial']

# Test for invalid inputs to check error handling in deserialize method
def test_invalid_input(inventory):
    # Test with non-dict input
    with pytest.raises(TypeError):
        inventory.deserialize("not a dictionary")
    
    # Test with dict missing required keys
    data = {
        'hosts': {'host1': {}},
        'groups': {},
        'local': None,
        'source': 'file:/path/to/inventory',
        'processed_sources': []
    }
    with pytest.raises(KeyError):
        inventory.deserialize(data)
    
    # Test with dict containing invalid data types
    data = {
        'hosts': {'host1': {}},
        'groups': {'group1': {}},
        'local': None,
        'source': 12345,  # Invalid type for source
        'processed_sources': []
    }
    with pytest.raises(TypeError):
        inventory.deserialize(data)
