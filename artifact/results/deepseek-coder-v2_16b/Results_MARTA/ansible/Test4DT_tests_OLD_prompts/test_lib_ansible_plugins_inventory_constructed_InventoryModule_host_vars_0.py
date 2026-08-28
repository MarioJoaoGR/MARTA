
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.constructed import InventoryModule


def test_edge_case_none():
    inventory = InventoryModule()
    host = None
    loader = None
    sources = []
    
    with patch('ansible.plugins.inventory.constructed.InventoryModule', return_value=inventory):
        with pytest.raises(AttributeError):
            vars = inventory.host_vars(host, loader, sources)