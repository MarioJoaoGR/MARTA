
import pytest
from ansible.inventory.manager import InventoryManager, InventoryData  # Corrected the import and added InventoryData

# Assuming SomeLoaderClass is a valid loader class for the inventory data
class SomeLoaderClass:
    pass

@pytest.fixture
def loader():
    return SomeLoaderClass()

@pytest.fixture
def manager(loader):
    return InventoryManager(loader, sources=['path/to/source1', 'path/to/source2'], parse=True)

def test_initialization_with_parsing(manager):
    assert isinstance(manager._inventory, InventoryData), "Inventory should be an instance of InventoryData"
    assert manager._sources == ['path/to/source1', 'path/to/source2']