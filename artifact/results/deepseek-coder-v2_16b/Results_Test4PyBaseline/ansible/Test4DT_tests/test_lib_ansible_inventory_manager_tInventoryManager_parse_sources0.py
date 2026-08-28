
import pytest
from ansible.inventory.manager import InventoryManager

# Example loader object for testing purposes
class DummyLoader:
    pass

loader = DummyLoader()

def test_default_initialization():
    manager = InventoryManager(loader)
    assert isinstance(manager, InventoryManager)
    assert not hasattr(manager, '_sources')  # Default sources should be empty
    assert not hasattr(manager, '_restriction')  # Default restrictions should be None
    assert not hasattr(manager, '_subset')  # Default subset should be None

def test_initialization_with_specified_sources():
    manager = InventoryManager(loader, ['source1', 'source2'], parse=True)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == ['source1', 'source2']  # Sources should be set correctly

def test_parsing_sources_immediately():
    manager = InventoryManager(loader)
    manager.parse_sources()
    assert hasattr(manager, '_inventory')  # Inventory should be populated after parsing

def test_initialization_with_specified_sources_and_parsing():
    manager = InventoryManager(loader, ['source1', 'source2'], parse=True)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == ['source1', 'source2']  # Sources should be set correctly
    assert hasattr(manager, '_inventory')  # Inventory should be populated after parsing

def test_parsing_sources_with_caching():
    manager = InventoryManager(loader, ['source1', 'source2'])
    manager.parse_sources(cache=True)
    assert hasattr(manager, '_inventory')  # Inventory should be populated after parsing with caching

def test_restricting_operations_to_specific_hosts():
    manager = InventoryManager(loader, ['source1', 'source2'], parse=True)
    with pytest.raises(AttributeError):
        manager.restrict_to_hosts(['host1', 'host2'])
