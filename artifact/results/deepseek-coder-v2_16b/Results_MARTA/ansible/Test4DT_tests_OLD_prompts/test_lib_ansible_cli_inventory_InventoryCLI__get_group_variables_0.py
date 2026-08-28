
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.inventory import InventoryCLI


def test_invalid_inputs():
    args = {'host': 'invalid_host', 'group': 'example_group'}
    with patch('ansible.cli.inventory.InventoryCLI.__init__', return_value=None):
        inventory_cli = InventoryCLI(args)
        with pytest.raises(Exception):
            assert inventory_cli.vm is None