
import pytest
from ansible.inventory.data import InventoryData

# Fixture to create an instance of InventoryData for testing
@pytest.fixture
def inventory():
    return InventoryData()

# Test adding a group
def test_add_group(inventory):
    added_group_name = inventory.add_group('webservers')
    assert added_group_name == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding a host to a group
def test_add_host(inventory):
    inventory.add_group('webservers')  # Add the group first
    added_host_name = inventory.add_host('192.168.1.10', group='webservers')
    assert added_host_name == '192.168.1.10'
    assert '192.168.1.10' in inventory.hosts