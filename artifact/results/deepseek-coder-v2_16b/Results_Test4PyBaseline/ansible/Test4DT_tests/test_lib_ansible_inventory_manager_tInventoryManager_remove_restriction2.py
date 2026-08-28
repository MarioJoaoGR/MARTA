
import pytest
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def loader():
    # Create a mock loader for testing purposes
    class MockLoader:
        def load(self):
            return {}
    
    return MockLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader, sources=['path/to/source1', 'path/to/source2'])

# Test case for removing restriction in the InventoryManager
def test_remove_restriction(inventory_manager):
    # Before removal, there should be no restriction
    assert inventory_manager._restriction is None
    
    # Call the remove_restriction method
    inventory_manager.remove_restriction()
    
    # After removal, the restriction should still be None (no change expected)
    assert inventory_manager._restriction is None
