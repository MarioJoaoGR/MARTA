
import pytest
from ansible.inventory.manager import InventoryManager

# Assuming SomeLoaderClass is a valid loader class for the inventory data
class SomeLoaderClass:
    pass

@pytest.fixture
def setup_inventory_manager():
    loader = SomeLoaderClass()
    return InventoryManager(loader)

def test_list_hosts_default_pattern(setup_inventory_manager):
    manager = setup_inventory_manager
    result = manager.list_hosts()
    assert isinstance(result, list), f"Expected a list but got {type(result)}"