
import pytest
from ansible.inventory.data import InventoryData

# Fixture to create an instance of InventoryData for testing
@pytest.fixture
def inventory():
    return InventoryData()

# Test removing a host from the inventory
def test_remove_host(inventory):
    # Add a group and a host to the inventory
    inventory.add_group('webservers')
    added_host_name = inventory.add_host('192.168.1.10', group='webservers')
    assert added_host_name == '192.168.1.10'