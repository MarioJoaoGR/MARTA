
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Mocking a simple loader for testing purposes
class SimpleLoader:
    def load(self):
        return {'hosts': ['host1', 'host2'], 'vars': {}}

@pytest.fixture
def my_loader():
    return SimpleLoader()

# Test cases
def test_valid_input(my_loader):
    manager = InventoryManager(loader=my_loader, sources=['source1', 'source2'], parse=True)
    assert isinstance(manager._sources, list) and len(manager._sources) == 2
    assert manager._restriction is None

def test_edge_case_none(my_loader):
    manager = InventoryManager(loader=my_loader, sources=['source1', 'source2'], parse=True)
    manager.restrict_to_hosts(None)
    assert manager._restriction is None

def test_invalid_input(my_loader):
    with pytest.raises(TypeError):
        InventoryManager(loader=my_loader, sources=['source1', 'source2'], parse=True, restriction='invalid')
