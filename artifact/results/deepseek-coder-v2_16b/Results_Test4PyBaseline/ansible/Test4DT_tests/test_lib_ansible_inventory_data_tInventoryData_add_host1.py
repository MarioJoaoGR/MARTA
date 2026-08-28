
# Module: ansible.inventory.data
# test_inventory_data.py
from ansible.errors import AnsibleError
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory():
    return InventoryData()

# Test case to cover line 194-196: Check if the function raises an error for a non-string host name
def test_add_host_invalid_host_type(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_host(host=123)
    assert "Invalid host name supplied, expected a string but got <class 'int'> for 123" in str(excinfo.value)

# Test case to cover line 199-202: Check if the function raises an error when the group does not exist
def test_add_host_group_not_found(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_host('192.168.1.10', group='non_existent_group')