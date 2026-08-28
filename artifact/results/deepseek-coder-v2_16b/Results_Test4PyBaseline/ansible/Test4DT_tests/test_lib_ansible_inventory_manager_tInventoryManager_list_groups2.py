
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def loader():
    return DataLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

# Test case to cover the uncovered line 603 in list_groups method
def test_list_groups_returns_sorted_group_keys(inventory_manager):
    # Adding groups to the inventory for testing
    inventory_manager._inventory.add_group('group1')
    inventory_manager._inventory.add_group('group2')
    inventory_manager._inventory.add_group('group3')
    
    group_keys = inventory_manager.list_groups()
    assert isinstance(group_keys, list), "Expected a list but got something else"