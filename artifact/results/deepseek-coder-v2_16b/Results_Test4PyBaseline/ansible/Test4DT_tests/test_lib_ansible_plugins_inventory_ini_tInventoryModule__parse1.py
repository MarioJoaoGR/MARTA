
import pytest
from ansible.plugins.inventory import ini

# Fixture to create an instance of InventoryModule for testing
@pytest.fixture
def inventory_module():
    inventory_module = ini.InventoryModule()
    return inventory_module

# Test initialization of the InventoryModule class
def test_inventory_module_initialization(inventory_module):
    assert isinstance(inventory_module, ini.InventoryModule)
    assert inventory_module._filename is None