
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

# Test initialization with sources and no parse

# Test initialization with default settings

# Test parsing sources immediately upon initialization
def test_initialization_with_parse():
    loader = DataLoader()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    assert hasattr(manager, '_loader')
    assert hasattr(manager, '_inventory')  # inventory should be parsed after initialization

# Test clearing caches