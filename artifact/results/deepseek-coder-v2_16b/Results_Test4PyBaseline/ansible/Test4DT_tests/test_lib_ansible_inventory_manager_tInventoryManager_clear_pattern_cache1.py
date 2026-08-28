
import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

# Mocking necessary classes and functions for testing
class InventoryData:
    pass

def test_clear_pattern_cache():
    # Arrange
    manager = InventoryManager(MagicMock())
    
    # Act
    manager.clear_pattern_cache()
    
    # Assert
    assert len(manager._pattern_cache) == 0
    assert manager._pattern_cache == {}

def test_clear_pattern_cache_with_existing_data():
    # Arrange
    manager = InventoryManager(MagicMock())
    manager._pattern_cache = {'key1': 'value1', 'key2': 'value2'}
    
    # Act
    manager.clear_pattern_cache()
    
    # Assert
    assert len(manager._pattern_cache) == 0
    assert manager._pattern_cache == {}

def test_clear_pattern_cache_multiple_calls():
    # Arrange
    manager = InventoryManager(MagicMock())
    
    # Act and Assert
    for _ in range(3):
        manager.clear_pattern_cache()
        assert len(manager._pattern_cache) == 0
        assert manager._pattern_cache == {}
