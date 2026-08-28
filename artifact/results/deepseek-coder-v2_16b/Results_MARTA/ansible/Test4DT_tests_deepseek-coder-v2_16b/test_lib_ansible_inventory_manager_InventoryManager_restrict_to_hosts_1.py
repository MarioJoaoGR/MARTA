
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Fixture to create a mock loader and inventory manager for testing
@pytest.fixture
def setup_manager():
    class MockLoader:
        pass
    
    return InventoryManager(loader=MockLoader(), sources=['source1', 'source2'], parse=True)

# Test scenario 1: test_valid_input
def test_valid_input(setup_manager):
    manager = setup_manager
    hosts = ['host1', 'host2']
    manager.restrict_to_hosts(hosts)
    assert set(manager._restriction) == {'host1', 'host2'}

# Test scenario 2: test_edge_case_none
def test_edge_case_none(setup_manager):
    manager = setup_manager
    manager.restrict_to_hosts(None)
    assert manager._restriction is None

# Test scenario 3: test_invalid_input
def test_invalid_input(setup_manager):
    manager = setup_manager
    with pytest.raises(TypeError):
        manager.restrict_to_hosts("not a list")
