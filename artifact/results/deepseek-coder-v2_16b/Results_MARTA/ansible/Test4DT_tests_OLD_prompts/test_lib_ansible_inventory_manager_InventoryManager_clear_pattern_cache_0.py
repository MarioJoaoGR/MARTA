
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock, patch

def test_clear_pattern_cache_invalid_input():
    loader = MagicMock()
    manager = InventoryManager(loader=loader)
    
    with pytest.raises(AttributeError):
        manager.clear_pattern_cach('invalid_input')
