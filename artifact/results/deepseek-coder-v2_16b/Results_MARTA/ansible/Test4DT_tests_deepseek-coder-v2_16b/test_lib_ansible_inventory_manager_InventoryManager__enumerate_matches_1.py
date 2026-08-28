
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock
from ansible.inventory.data import InventoryData
import os

# Test for valid input initialization
def test_valid_input():
    loader = MagicMock()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources)
    
    assert len(manager._sources) == 2
    assert manager._sources == ['source1', 'source2']
    assert isinstance(manager._inventory, InventoryData)

# Test for invalid input initialization