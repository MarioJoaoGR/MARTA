
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch, MagicMock

# Test 1: Basic Initialization with Default Settings
@pytest.fixture(scope="module")
def manager():
    loader = MagicMock()
    return InventoryManager(loader=loader)

def test_basic_initialization(manager):
    assert isinstance(manager, InventoryManager)
    assert manager._loader is not None
    assert len(manager._sources) == 0
    assert manager._restriction is None
    assert manager._subset is None
    assert len(manager._hosts_patterns_cache) == 0
    assert len(manager._pattern_cache) == 0

# Test 2: Specifying Sources and Enabling Parsing
@pytest.fixture(scope="module")
def manager_with_sources():
    loader = MagicMock()
    return InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)

def test_initialization_with_sources(manager_with_sources):
    assert isinstance(manager_with_sources, InventoryManager)
    assert manager_with_sources._loader is not None
    assert len(manager_with_sources._sources) == 2
    assert manager_with_sources._restriction is None
    assert manager_with_sources._subset is None
    assert len(manager_with_sources._hosts_patterns_cache) == 0
    assert len(manager_with_sources._pattern_cache) == 0

# Test 3: Restricting Operations to Specific Hosts
@pytest.fixture(scope="module")
def manager_restricted():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    hosts = ['host1', 'host2']
    manager.restrict_to_hosts(hosts)
    return manager


# Test 4: Subsetting Inventory Based on Pattern
@pytest.fixture(scope="module")
def manager_subset():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    with patch('ansible.inventory.manager.to_text', return_value='role:webserver'):
        manager.subset('role:webserver')
    return manager


# Test 5: Getting Hosts Matching a Specific Pattern
@pytest.fixture(scope="module")
def matched_hosts():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    with patch('ansible.inventory.manager.to_text', side_effect=['host1', 'host2']):
        return manager.get_hosts('webserver')
