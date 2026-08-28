
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

# Fixture to create an instance of InventoryData for testing
@pytest.fixture(scope="module")
def inventory():
    return InventoryData()

# Test case for setting a valid variable in the inventory

# Test case for attempting to set a variable in an invalid group, which should raise AnsibleError
def test_invalid_group(inventory):
    with pytest.raises(AnsibleError):
        inventory.set_variable('nonexistent_group', 'ansible_host', '192.168.1.100')

# Test case for attempting to set a variable in an invalid entity, which should raise AnsibleError
def test_invalid_entity(inventory):
    with pytest.raises(AnsibleError):
        inventory.set_variable('webservers', 'nonexistent_varname', '192.168.1.100')