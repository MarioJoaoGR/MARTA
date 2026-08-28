
import pytest
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def loader():
    return object()  # Placeholder for actual loader object

@pytest.fixture
def sources():
    return ['source1', 'source2']


def test_initialization_without_parsing_sources(loader, sources):
    manager = InventoryManager(loader=loader, sources=sources, parse=False)
    assert isinstance(manager, InventoryManager)
    assert manager._sources == sources
    assert not hasattr(manager, '_parse')


def test_restricting_operations_to_specific_hosts(loader, sources):
    manager = InventoryManager(loader=loader, sources=sources)
    manager.parse_sources(cache=True)
    with pytest.raises(AttributeError):
        manager.restrict_to_hosts(['host1', 'host2'])

def test_getting_localhost_inventory(loader, sources):
    manager = InventoryManager(loader=loader, sources=sources)
    manager.parse_sources(cache=True)
    with pytest.raises(TypeError):
        localhost_inventory = manager.localhost()