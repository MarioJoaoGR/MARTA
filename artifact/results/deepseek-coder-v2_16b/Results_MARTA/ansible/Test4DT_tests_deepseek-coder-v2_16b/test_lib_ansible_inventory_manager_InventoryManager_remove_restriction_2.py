
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch, MagicMock

# Test fixture to create an InventoryManager instance for testing
@pytest.fixture(scope="module")
def inventory_manager():
    loader = MagicMock()
    sources = "invalid_source"
    manager = InventoryManager(loader=loader, sources=sources)
    return manager

# Test that checks if remove_restriction method sets _restriction to None
def test_remove_restriction(inventory_manager):
    inventory_manager.remove_restriction()
    assert inventory_manager._restriction is None
