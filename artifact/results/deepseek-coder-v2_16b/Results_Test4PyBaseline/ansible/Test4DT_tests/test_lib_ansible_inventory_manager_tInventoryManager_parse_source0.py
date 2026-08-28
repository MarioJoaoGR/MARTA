
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData  # Assuming 'InventoryData' is defined here

# Assuming 'loader' is already instantiated and properly configured
@pytest.fixture
def loader():
    # Create a mock loader for testing purposes
    class MockLoader:
        pass
    return MockLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

# Test default initialization
def test_default_initialization(loader):
    manager = InventoryManager(loader)
    assert manager._sources == []
    assert isinstance(manager._inventory, InventoryData)

# Test specifying a single source
def test_single_source(loader):
    manager = InventoryManager(loader, ['/path/to/source1'])
    assert manager._sources == ['/path/to/source1']
    assert isinstance(manager._inventory, InventoryData)

# Test specifying multiple sources
def test_multiple_sources(loader):
    manager = InventoryManager(loader, ['/path/to/source1', '/path/to/source2'])
    assert manager._sources == ['/path/to/source1', '/path/to/source2']
    assert isinstance(manager._inventory, InventoryData)

# Test initializing without parsing
def test_initialize_without_parsing(loader):
    manager = InventoryManager(loader, ['/path/to/source1', '/path/to/source2'], parse=False)
    assert manager._sources == ['/path/to/source1', '/path/to/source2']