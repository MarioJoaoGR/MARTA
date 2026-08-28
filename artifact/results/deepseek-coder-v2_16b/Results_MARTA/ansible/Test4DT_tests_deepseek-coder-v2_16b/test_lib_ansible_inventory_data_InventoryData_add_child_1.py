
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

@pytest.fixture(scope="module")
def inventory():
    return InventoryData()

# Test adding a valid child to an existing group
def test_valid_input_add_child(inventory):
    inventory.add_group('webservers')
    inventory.add_group('parent_group')
    assert inventory.add_child('parent_group', 'host1') is True
    assert 'host1' in inventory.groups['parent_group'].get_hosts()

# Test adding a child with None value, should raise AnsibleError
def test_invalid_input_none_value(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_child('webservers', None)
    assert str(excinfo.value) == 'None is not a known host nor group'

# Test adding a child to a non-existent group, should raise AnsibleError
def test_invalid_input_non_existent_group(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_child('nonexistent_group', 'host1')
    assert str(excinfo.value) == 'nonexistent_group is not a known group'
