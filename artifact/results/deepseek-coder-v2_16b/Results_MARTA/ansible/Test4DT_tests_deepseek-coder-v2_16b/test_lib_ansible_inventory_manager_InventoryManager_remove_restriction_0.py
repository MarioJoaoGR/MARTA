
import pytest
from ansible.inventory.manager import InventoryManager



def test_clear_pattern_cache():
    class SomeLoaderClass:
        pass
    
    loader = SomeLoaderClass()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    # Initially, the cache should be empty
    assert manager._hosts_patterns_cache == {}
    
    # Clear the pattern cache and check if it is now empty
    manager.clear_pattern_cache()
    assert manager._hosts_patterns_cache == {}