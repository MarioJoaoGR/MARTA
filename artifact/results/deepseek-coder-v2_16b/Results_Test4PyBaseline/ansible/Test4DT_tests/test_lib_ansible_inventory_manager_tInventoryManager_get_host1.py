
# Module: ansible.inventory.manager
# test_inventory_manager.py
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
import pytest

@pytest.fixture
def loader():
    return DataLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

# Test to check the get_host method with an existing host
def test_inventory_manager_get_host_existing(inventory_manager):
    # Assuming there is a host 'host1' in the inventory for this test
    hostname = 'host1'
    host = inventory_manager._inventory.get_host(hostname)
    retrieved_host = inventory_manager.get_host(hostname)
    assert retrieved_host == host, f"Expected host with hostname '{hostname}' to be retrieved correctly."

# Test to check the get_host method with a non-existing host
def test_inventory_manager_get_host_non_existing(inventory_manager):
    # Assuming there is no host 'nonexistent' in the inventory for this test
    hostname = 'nonexistent'
    retrieved_host = inventory_manager.get_host(hostname)
    assert retrieved_host is None, f"Expected get_host to return None for a non-existing host."

# Test to check the get_host method with an empty string as hostname
def test_inventory_manager_get_host_empty_string(inventory_manager):
    hostname = ''
    retrieved_host = inventory_manager.get_host(hostname)