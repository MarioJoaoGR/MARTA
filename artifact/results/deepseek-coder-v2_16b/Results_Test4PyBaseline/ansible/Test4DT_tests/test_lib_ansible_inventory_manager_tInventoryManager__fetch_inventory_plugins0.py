
import pytest
from ansible.inventory.manager import InventoryManager

# Assuming the loader is already defined and properly configured for testing purposes
loader = None  # Replace with actual loader object if available

def test_default_initialization():
    manager = InventoryManager(loader)
    assert isinstance(manager, InventoryManager)
    assert not hasattr(manager, '_sources') or manager._sources == []
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}

def test_initialization_with_specified_sources():
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}

def test_initialization_with_specified_sources_and_parsing():
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources, parse=True)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}