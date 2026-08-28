
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

@pytest.fixture(scope="module")
def inventory():
    return InventoryData()

# Test adding a valid group to the inventory
def test_valid_group_addition(inventory):
    initial_groups = len(inventory.groups)
    added_group_name = inventory.add_group('test_group')
    assert added_group_name == 'test_group'
    assert 'test_group' in inventory.groups
    assert len(inventory.groups) == initial_groups + 1

# Test adding an invalid child type (e.g., non-existent host or group)
def test_invalid_child_type(inventory):
    with pytest.raises(AnsibleError):
        inventory.add_child('test_group', 'non_existent')

# Test adding a child to a missing group, expecting an AnsibleError
def test_missing_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('missing_group', 'host1')
