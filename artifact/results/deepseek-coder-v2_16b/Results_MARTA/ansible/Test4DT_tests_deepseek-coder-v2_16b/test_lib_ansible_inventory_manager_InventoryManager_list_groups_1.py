
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Test scenario 1: Initialization with specific sources and parsing enabled
def test_initialization_with_sources():
    mock_loader = type('MockLoader', (object,), {'load': lambda self: None})()
    manager = InventoryManager(loader=mock_loader, sources=['source1', 'source2'], parse=True)
    assert len(manager._sources) == 2

# Test scenario 2: Parsing sources immediately upon initialization
def test_initialization_with_parse():
    mock_loader = type('MockLoader', (object,), {'load': lambda self: None})()
    manager = InventoryManager(loader=mock_loader, sources=['source1', 'source2'], parse=True)
    assert len(manager._sources) == 2
    assert set(manager._inventory.groups.keys()) == {'all', 'ungrouped'}

# Test scenario 3: Listing groups from the inventory
def test_list_groups():
    mock_loader = type('MockLoader', (object,), {'load': lambda self: None})()
    manager = InventoryManager(loader=mock_loader, sources=['source1', 'source2'], parse=True)
    assert set(manager.list_groups()) == {'all', 'ungrouped'}
