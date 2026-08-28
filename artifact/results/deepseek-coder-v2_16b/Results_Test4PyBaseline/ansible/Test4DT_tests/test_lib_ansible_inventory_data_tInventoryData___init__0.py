
import pytest
from ansible.inventory.data import InventoryData

# Test initialization of InventoryData class
def test_initialization():
    inventory = InventoryData()
    assert isinstance(inventory, InventoryData)
    assert 'all' in inventory.groups
    assert 'ungrouped' in inventory.groups

# Test adding a new group
def test_add_group():
    inventory = InventoryData()
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding an existing group should not create a new one
def test_add_existing_group():
    inventory = InventoryData()
    inventory.add_group('webservers')
    original_count = len(inventory.groups)
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'