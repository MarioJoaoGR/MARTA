
# Module: ansible.inventory.data
# test_inventory_data.py
from ansible.errors import AnsibleError  # Corrected import statement for AnsibleError
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory():
    return InventoryData()

def test_initialization(inventory):
    assert isinstance(inventory, InventoryData)
    assert 'all' in inventory.groups
    assert 'ungrouped' in inventory.groups

def test_add_group(inventory):
    group_name = 'webservers'
    added_group_name = inventory.add_group(group_name)
    assert added_group_name == group_name