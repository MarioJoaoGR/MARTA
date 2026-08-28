
import pytest
from ansible.inventory.manager import InventoryManager

# Assuming SomeLoaderClass is a valid loader class used in the InventoryManager initialization
class SomeLoaderClass:
    pass

def test_initialization_with_default_settings():
    loader = SomeLoaderClass()
    manager = InventoryManager(loader)
    assert isinstance(manager, InventoryManager)
    assert not manager._sources

def test_initialization_with_specific_sources():
    loader = SomeLoaderClass()
    sources = ['path/to/source1', 'path/to/source2']
    manager = InventoryManager(loader, sources)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources

def test_initialization_with_specific_sources_and_parsing():
    loader = SomeLoaderClass()
    sources = ['path/to/source1', 'path/to/source2']
    manager = InventoryManager(loader, sources, parse=True)
    assert isinstance(manager, InventoryManager)