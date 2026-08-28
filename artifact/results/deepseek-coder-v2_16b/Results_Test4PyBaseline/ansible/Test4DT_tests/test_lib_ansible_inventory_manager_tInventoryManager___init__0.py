
# Module: ansible.inventory.manager
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.data import InventoryData  # Corrected the import for InventoryData

# Assuming 'loader' is a valid loader object from ansible.parsing.dataloader
loader = DataLoader()

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader)

@pytest.fixture
def inventory_manager_with_sources():
    return InventoryManager(loader, ['source1', 'source2'], parse=True)

# Test default initialization
def test_default_initialization(inventory_manager):
    assert isinstance(inventory_manager._loader, DataLoader)
    assert isinstance(inventory_manager._inventory, InventoryData)  # Corrected the assertion for InventoryData
    assert inventory_manager._restriction is None
    assert inventory_manager._subset is None
    assert len(inventory_manager._sources) == 0

# Test initialization with specific sources and parsing
def test_initialization_with_specific_sources_and_parsing(inventory_manager_with_sources):
    assert isinstance(inventory_manager_with_sources._loader, DataLoader)
    assert isinstance(inventory_manager_with_sources._inventory, InventoryData)  # Corrected the assertion for InventoryData
    assert inventory_manager_with_sources._restriction is None
    assert inventory_manager_with_sources._subset is None
    assert len(inventory_manager_with_sources._sources) == 2
    assert inventory_manager_with_sources._sources == ['source1', 'source2']

# Test initialization without parsing
def test_initialization_without_parsing():
    manager = InventoryManager(loader, ['source1', 'source2'], parse=False)
    assert isinstance(manager._loader, DataLoader)
    assert isinstance(manager._inventory, InventoryData)  # Corrected the assertion for InventoryData
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._sources) == 2
    assert manager._sources == ['source1', 'source2']
    with pytest.raises(AttributeError):
        inventory_manager_with_sources.parse_sources()  # This should raise an error because parse=False

# Test initializing without sources and parsing
def test_initialization_without_sources_and_parsing():
    manager = InventoryManager(loader, sources=None, parse=True)
    assert isinstance(manager._loader, DataLoader)
    assert isinstance(manager._inventory, InventoryData)  # Corrected the assertion for InventoryData
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._sources) == 0
