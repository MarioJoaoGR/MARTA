
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError


def test_invalid_group_name():
    inventory = InventoryData()
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_group('')  # Attempt to add a group with an invalid name (empty string)
    assert "Invalid empty/false group name provided" in str(excinfo.value), "Expected error message not found"

def test_non_string_group_name():
    inventory = InventoryData()
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_group(12345)  # Attempt to add a group with an invalid name (non-string type)
    assert "Invalid group name supplied, expected a string but got <class 'int'> for 12345" in str(excinfo.value), "Expected error message not found"