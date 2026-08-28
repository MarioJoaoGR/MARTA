
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch
import os

@pytest.fixture(scope="module")
def inventory_manager():
    loader = None  # Assuming a suitable loader object is available or can be mocked
    sources = ['invalid-source']  # Providing an invalid source to trigger the warning
    manager = InventoryManager(loader=loader, sources=sources)
    return manager


def test_clear_pattern_cache_after_parsing(inventory_manager):
    # Parse the sources to populate the cache
    inventory_manager.parse_sources()
    
    # Clear the pattern cache
    inventory_manager.clear_pattern_cache()
    
    # Check that the pattern cache is now empty
    assert not inventory_manager._pattern_cache