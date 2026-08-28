
import pytest
from ansible.inventory.manager import InventoryManager
import re
import fnmatch
from ansible.errors import AnsibleError

@pytest.fixture(scope="module")
def inventory_manager():
    loader = None  # Assuming a default loader is available or can be provided
    sources = ['host1', 'host2']
    manager = InventoryManager(loader=loader, sources=sources)
    return manager


def test_invalid_pattern(inventory_manager):
    matched_hosts = inventory_manager._match_list(['host1', 'host2'], 'invalid*')
    assert matched_hosts == []