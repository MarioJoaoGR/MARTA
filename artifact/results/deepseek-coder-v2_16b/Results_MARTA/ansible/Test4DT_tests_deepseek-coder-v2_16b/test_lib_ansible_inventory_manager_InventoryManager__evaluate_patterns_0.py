
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.data import InventoryData

def test_default_initialization():
    loader = DataLoader()
    manager = InventoryManager(loader=loader)
    assert len(manager._sources) == 0
    assert isinstance(manager._inventory, InventoryData)
    assert not manager._inventory.hosts

def test_initialization_with_sources():
    loader = DataLoader()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources)
    assert len(manager._sources) == 2
    assert manager._sources == ['source1', 'source2']
    assert isinstance(manager._inventory, InventoryData)
    assert not manager._inventory.hosts


