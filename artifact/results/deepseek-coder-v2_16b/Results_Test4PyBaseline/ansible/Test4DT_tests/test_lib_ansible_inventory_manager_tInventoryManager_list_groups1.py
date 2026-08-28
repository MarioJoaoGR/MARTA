
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def loader():
    return DataLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

# Test case to ensure the list_groups method returns a sorted list of group keys
def test_list_groups_returns_sorted_group_keys(inventory_manager):
    group_keys = inventory_manager.list_groups()
    assert isinstance(group_keys, list), "Expected list but got {}".format(type(group_keys))
    expected_keys = ['all', 'ungrouped']  # Expected keys after initialization
    sorted_expected_keys = sorted(expected_keys)
    assert group_keys == sorted_expected_keys, "List does not match expected keys: {}".format(group_keys)

# Test case to ensure the list_groups method returns an empty list when there are no groups
def test_list_groups_empty_inventory(loader):
    manager = InventoryManager(loader)
    assert isinstance(manager.list_groups(), list), "Expected list but got {}".format(type(manager.list_groups()))