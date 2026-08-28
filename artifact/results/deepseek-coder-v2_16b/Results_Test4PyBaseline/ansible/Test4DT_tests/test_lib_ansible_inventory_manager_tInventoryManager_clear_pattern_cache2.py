
import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

# Mocking necessary classes and functions for testing
class InventoryData:
    pass

def test_clear_pattern_cache():
    # Arrange
    loader = MagicMock()
    manager = InventoryManager(loader)
    
    # Act
    manager.clear_pattern_cache()
    
    # Assert
    assert len(manager._pattern_cache) == 0
    assert isinstance(manager._pattern_cache, dict)
    assert manager._pattern_cache == {}

def test_clear_pattern_cache_multiple_calls():
    # Arrange
    loader = MagicMock()
    manager = InventoryManager(loader)
    
    # Act
    manager.clear_pattern_cache()
    manager.clear_pattern_cache()
    
    # Assert
    assert len(manager._pattern_cache) == 0
    assert isinstance(manager._pattern_cache, dict)
    assert manager._pattern_cache == {}

def test_clear_pattern_cache_with_existing_data():
    # Arrange
    loader = MagicMock()
    manager = InventoryManager(loader)
    manager._pattern_cache['test_key'] = 'test_value'
    
    # Act
    manager.clear_pattern_cache()
    
    # Assert
    assert len(manager._pattern_cache) == 0
    assert isinstance(manager._pattern_cache, dict)
    assert manager._pattern_cache == {}
