
# Module: ansible.inventory.data
# test_inventory_data.py
from ansible.errors import AnsibleError
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory():
    return InventoryData()

def test_add_host_invalid_host(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_host(12345)  # Invalid host type (int)
    assert "Invalid host name supplied, expected a string but got" in str(excinfo.value)

def test_add_host_empty_host(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_host('')  # Empty host name
    assert "Invalid empty host name provided:" in str(excinfo.value)

def test_add_host_none_host(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.add_host(None)  # None host name