
# Module: ansible.plugins.inventory.ini
# test_inventory_module.py
from ansible.plugins.inventory import ini as ini_inventory
import pytest

@pytest.fixture
def inventory_module():
    return ini_inventory.InventoryModule()

def test_initialization(inventory_module):
    assert isinstance(inventory_module, ini_inventory.InventoryModule)
    assert inventory_module._filename is None