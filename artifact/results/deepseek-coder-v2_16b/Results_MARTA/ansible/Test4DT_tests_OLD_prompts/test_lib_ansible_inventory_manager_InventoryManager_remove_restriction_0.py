
import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager

# Test case for initializing the InventoryManager with specific sources and parsing enabled
def test_initialize_with_specific_sources():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    assert manager._sources == ['source1', 'source2']
    assert manager._restriction is None

# Test case for initializing the InventoryManager without parsing initially
def test_initialize_without_parsing():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=False)
    assert manager._sources == ['source1', 'source2']
    assert manager._restriction is None

# Test case for initializing the InventoryManager and immediately parsing the sources
def test_initialize_and_parse():
    loader = MagicMock()
    with patch('ansible.inventory.manager.InventoryData') as mock_inventory:
        manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
        assert manager._sources == ['source1', 'source2']
        assert manager._restriction is None
        mock_inventory.assert_called_once()

# Test case for restricting operations to specific hosts

# Test case for removing the restriction on list operations