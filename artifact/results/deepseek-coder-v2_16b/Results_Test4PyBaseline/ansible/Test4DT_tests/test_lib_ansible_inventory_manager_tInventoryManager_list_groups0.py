
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def loader():
    return DataLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader)

def test_default_initialization(loader):
    manager = InventoryManager(loader)
    assert isinstance(manager, InventoryManager)
    assert not manager._sources
    assert not manager._restriction
    assert not manager._subset
    assert not manager._hosts_patterns_cache
    assert not manager._pattern_cache

def test_initialization_with_specific_sources(loader):
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources=sources)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert not manager._restriction
    assert not manager._subset
    assert not manager._hosts_patterns_cache
    assert not manager._pattern_cache

def test_initialization_with_specific_sources_and_parsing(loader):
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources=sources, parse=True)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert not manager._restriction
    assert not manager._subset
    assert not manager._hosts_patterns_cache
    assert not manager._pattern_cache

def test_list_groups(inventory_manager):
    group_keys = inventory_manager.list_groups()
    assert isinstance(group_keys, list)
    assert sorted(group_keys) == group_keys  # Ensure the list is sorted

def test_list_groups_empty(loader):
    manager = InventoryManager(loader)
    group_keys = manager.list_groups()
    assert isinstance(group_keys, list)
    assert len(group_keys) == 2  # Should be ['all', 'ungrouped'] if no sources are provided
