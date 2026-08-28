
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch, MagicMock

# Test Scenario 1: Valid Input
def test_valid_input():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['hosts.yml'])
    assert len(manager._sources) == 1
    assert 'hosts.yml' in manager._sources
    assert isinstance(manager._sources[0], str)

# Test Scenario 2: Edge Case
def test_edge_case():
    with pytest.raises(TypeError):
        InventoryManager()
    
    manager = InventoryManager(loader=MagicMock(), sources=None)
    assert len(manager._sources) == 0

    manager = InventoryManager(loader=MagicMock(), sources=[])
    assert len(manager._sources) == 0

# Test Scenario 3: Invalid Input
def test_invalid_input():
    with pytest.raises(TypeError):
        InventoryManager(loader=MagicMock(), sources=None)
    
    manager = InventoryManager(loader=MagicMock(), sources=['hosts.yml'])
    assert len(manager._sources) == 1
    assert 'hosts.yml' in manager._sources
