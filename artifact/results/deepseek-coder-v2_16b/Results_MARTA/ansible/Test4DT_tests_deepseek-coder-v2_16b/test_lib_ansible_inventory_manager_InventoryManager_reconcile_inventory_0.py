
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

def test_edge_case():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=None, parse=True)
    
    assert isinstance(manager._sources, list)
    assert len(manager._sources) == 0
    assert not hasattr(manager.parse_sources, 'called')
