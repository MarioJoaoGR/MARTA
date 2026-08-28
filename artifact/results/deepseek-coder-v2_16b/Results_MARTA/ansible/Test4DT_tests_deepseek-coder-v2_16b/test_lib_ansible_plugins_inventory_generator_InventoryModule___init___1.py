
import pytest
from ansible.plugins.inventory.generator import InventoryModule

def test_invalid_input():
    with pytest.raises(AttributeError):
        inventory_module = InventoryModule()
        inventory_module.setup('incorrect_params')
