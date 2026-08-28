
# Module: ansible.inventory.manager
# test_inventory_manager.py
from ansible.inventory.manager import InventoryManager
import pytest

@pytest.fixture(scope="module")
def loader():
    return None  # Assuming SomeLoaderClass is a valid loader object

@pytest.fixture(scope="module")
def manager(loader):
    return InventoryManager(loader, ['source1', 'source2'])

def test_InventoryManager_initialization(manager):
    assert isinstance(manager, InventoryManager), "Initialization should create an instance of InventoryManager"

def test_InventoryManager_with_specified_sources(manager):
    assert manager._sources == ['source1', 'source2'], "Specified sources should be stored in the instance"

def test_InventoryManager_parsing_sources(manager):
    manager.parse_sources()
    assert len(manager._inventory) > 0, "Parsing sources should populate the inventory"

def test_InventoryManager_matching_hosts(manager):
    matched_hosts = manager.get_hosts('host*')
    assert isinstance(matched_hosts, list), "Matching hosts should return a list"
    assert len(matched_hosts) > 0, "At least one host should match the pattern 'host*'"

def test_InventoryManager_restricting_to_hosts(manager):
    manager.parse_sources()
    manager.restrict_to_hosts(['host1', 'host2'])
    matched_hosts = manager.get_hosts('*')
    assert len(matched_hosts) == 2, "Restricting to specific hosts should limit the matches"

def test_InventoryManager_clearing_pattern_cache(manager):
    initial_cache_size = len(manager._pattern_cache)
    manager.clear_pattern_cache()
    assert len(manager._pattern_cache) == 0, "Clearing the pattern cache should remove all cached patterns"
