
import pytest
from unittest.mock import patch
from ansible.plugins.inventory.constructed import InventoryModule


def test_verify_no_extension():
    with patch('os.path.splitext', return_value=('', '.config')):
        inventory_module = InventoryModule()
        assert inventory_module.verify_file('/path/to/config') == False

def test_verify_multiple_extensions():
    with patch('os.path.splitext', return_value=('.config.backup', '.yaml')):
        inventory_module = InventoryModule()
        assert inventory_module.verify_file('/path/to/config.config.backup') == False