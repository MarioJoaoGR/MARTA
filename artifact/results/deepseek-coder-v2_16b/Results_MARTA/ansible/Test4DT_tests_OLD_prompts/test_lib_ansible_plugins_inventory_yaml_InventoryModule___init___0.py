
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.inventory.yaml import InventoryModule



def test_invalid_input():
    with patch('ansible.plugins.inventory.yaml.InventoryModule.__init__', return_value=None):
        inv = InventoryModule()
        with pytest.raises(TypeError):
            inv.parse('non_existent_file.yaml', None)