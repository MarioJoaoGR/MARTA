
# Module: ansible.inventory.data
# test_inventory_data.py
from ansible.errors import AnsibleError  # Importing the correct module and class for the error
import pytest
from ansible.inventory.data import InventoryData  # Assuming this is part of the same module or correctly imported

@pytest.fixture
def inventory():
    return InventoryData()

def test_add_group_valid(inventory):
    """Test adding a valid group to the inventory."""
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

def test_add_group_invalid_type(inventory):
    """Test adding a group with an invalid type (non-string)."""
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_group(12345)
    assert "Invalid group name supplied, expected a string but got <class 'int'> for 12345" in str(excinfo.value)

def test_add_group_empty_or_false(inventory):
    """Test adding a group with empty or false input."""
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_group(False)
    assert "Invalid empty/false group name provided: False" in str(excinfo.value)

def test_add_existing_group(inventory):
    """Test adding an already existing group."""
    inventory.add_group('dbservers')  # Add 'dbservers' group to the inventory
    same_group_name = inventory.add_group('dbservers')  # Attempt to add the same group again
    assert same_group_name == 'dbservers'
