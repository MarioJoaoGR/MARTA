
# Module: ansible.inventory.data
# test_inventory_data.py
from ansible.errors import AnsibleError
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory():
    return InventoryData()

def test_add_host_without_group(inventory):
    added_host = inventory.add_host('192.168.1.10')
    assert added_host == '192.168.1.10'
    assert '192.168.1.10' in inventory.hosts

def test_add_host_to_existing_group(inventory):
    inventory.add_group('webservers')
    added_host = inventory.add_host('192.168.1.10', group='webservers')
    assert added_host == '192.168.1.10'
    assert '192.168.1.10' in inventory.hosts
    assert 'webservers' in inventory.groups
    # Simplified assertion to check the group membership of the host