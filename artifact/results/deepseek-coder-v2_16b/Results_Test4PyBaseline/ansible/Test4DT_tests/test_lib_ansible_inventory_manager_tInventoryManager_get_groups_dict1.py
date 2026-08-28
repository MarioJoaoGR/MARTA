
import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

# Mocking the necessary classes and methods for testing
class InventoryData:
    def get_groups_dict(self):
        return {'group1': {}, 'group2': {}}

class SomeLoaderClass:
    pass

@pytest.fixture
def loader():
    return SomeLoaderClass()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

# Test cases for InventoryManager class
def test_initialization_with_default_settings(loader, inventory_manager):
    assert isinstance(inventory_manager, InventoryManager)
    assert inventory_manager._sources == []
    assert inventory_manager._restriction is None
    assert inventory_manager._subset is None

# New test case for get_groups_dict method
def test_get_groups_dict_returns_correct_dictionary(inventory_manager):
    # Mock the _inventory to return a mock InventoryData object
    inventory_manager._inventory = MagicMock()
    inventory_manager._inventory.get_groups_dict.return_value = {'group1': {}, 'group2': {}}
    
    # Call the method and check the result
    groups_dict = inventory_manager.get_groups_dict()
    assert groups_dict == {'group1': {}, 'group2': {}}
