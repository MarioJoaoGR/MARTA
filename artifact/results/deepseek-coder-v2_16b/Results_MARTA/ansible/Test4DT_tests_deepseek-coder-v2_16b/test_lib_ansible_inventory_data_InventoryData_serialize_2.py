
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

# Test adding a group
def test_add_group():
    inventory = InventoryData()
    added_group_name = inventory.add_group('webservers')
    assert 'webservers' in inventory.groups
    assert added_group_name == 'webservers'

# Test adding an existing group should raise an exception

# Test adding a child (host) to a group

# Test adding a child (sub-group) to an existing group

# Test adding a child to a non-existing group should raise an exception
def test_add_child_to_non_existing_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('nonexistent_group', 'host1')