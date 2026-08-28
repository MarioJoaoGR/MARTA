
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

# Test case for initializing the InventoryManager with default settings
def test_initialization_with_default_settings(loader):
    manager = InventoryManager(loader)
    assert manager._sources == []

# Test case for initializing the InventoryManager with specified sources and parsing them
def test_initialization_with_specified_sources(loader):
    manager = InventoryManager(loader, sources=['path/to/source1', 'path/to/source2'])
    assert manager._sources == ['path/to/source1', 'path/to/source2']

# Test case for removing restriction in the InventoryManager
def test_remove_restriction():
    manager = InventoryManager(None)  # Passing None as loader since it's not used in this function
    assert manager._restriction is None
    manager.remove_restriction()
    assert manager._restriction is None

# Test case for removing restriction multiple times
def test_remove_restriction_multiple_calls():
    manager = InventoryManager(None)  # Passing None as loader since it's not used in this function
    assert manager._restriction is None
    manager.remove_restriction()
    assert manager._restriction is None
    manager.remove_restriction()
    assert manager._restriction is None
