
import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError

def test_valid_inputs():
    loader = MagicMock()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader=loader, sources=sources, parse=True)

    assert manager._loader == loader
    assert manager._sources == sources
    assert len(manager._sources) == 2
    assert hasattr(manager, 'parse_sources')
    assert callable(getattr(manager, 'parse_sources', None))

