
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

# Test adding a group to the inventory

# Test adding a child (host or sub-group) to an existing group

# Test adding a child (sub-group) to an existing group

# Test adding a child to a non-existing group, which should raise an AnsibleError
def test_add_child_to_non_existing_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('non_existing_group', 'host1')