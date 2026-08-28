
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Test 1: Valid subset pattern
def test_valid_subset_pattern():
    class MockLoader:
        pass
    
    class MockInventoryData:
        pass
    
    loader = MockLoader()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources, parse=True)
    
    subset_pattern = 'role:webserver'
    manager.subset(subset_pattern)
    
    assert isinstance(manager._subset, list), "Subset should be a list"
    assert len(manager._subset) > 0, "Subset should not be empty"

# Test 2: None subset pattern
def test_none_subset_pattern():
    class MockLoader:
        pass
    
    class MockInventoryData:
        pass
    
    loader = MockLoader()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources, parse=True)
    
    subset_pattern = None
    manager.subset(subset_pattern)
    
    assert manager._subset is None, "Subset should be None"

# Test 3: Invalid subset pattern raises ValueError
def test_invalid_subset_pattern():
    class MockLoader:
        pass
    
    class MockInventoryData:
        pass
    
    loader = MockLoader()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources, parse=True)
    
    subset_pattern = 'invalid_pattern'
    with pytest.raises(ValueError):
        manager.subset(subset_pattern)
