
import pytest
from ansible.inventory.data import InventoryData

# Test adding a group to the inventory
def test_add_group():
    inventory = InventoryData()
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding a host to an existing group

# Test adding a sub-group to an existing group

# Test serialization of the InventoryData object