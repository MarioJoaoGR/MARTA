
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

# Test case to cover the initialization of InventoryManager with default parameters
def test_inventory_manager_initialization_default(loader):
    manager = InventoryManager(loader)
    assert isinstance(manager, InventoryManager)
    assert not manager._sources
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._hosts_patterns_cache) == 0
    assert len(manager._pattern_cache) == 0

# Test case to cover the initialization of InventoryManager with specified sources
def test_inventory_manager_initialization_with_sources(loader):
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._hosts_patterns_cache) == 0
    assert len(manager._pattern_cache) == 0

# Test case to cover the initialization of InventoryManager with specified sources and parse parameter
def test_inventory_manager_initialization_with_parse(loader):
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources, parse=True)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._hosts_patterns_cache) == 0