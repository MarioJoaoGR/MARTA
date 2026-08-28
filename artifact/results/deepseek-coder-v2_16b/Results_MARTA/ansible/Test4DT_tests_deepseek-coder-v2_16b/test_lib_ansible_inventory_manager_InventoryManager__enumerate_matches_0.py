
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch, MagicMock

# Test valid input scenario
def test_valid_input():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['hosts.yml'])
    assert len(manager._sources) == 1
    assert 'hosts.yml' in manager._sources

# Test edge case scenario with None for pattern
def test_edge_case():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=None)
    assert len(manager._sources) == 0

# Test invalid input scenario with non-existent file
def test_invalid_input():
    loader = MagicMock()
    with pytest.raises(FileNotFoundError):
        manager = InventoryManager(loader=loader, sources=['non_existent.yml'])
