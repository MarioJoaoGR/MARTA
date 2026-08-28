
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
    assert inventory_module.patterns == {}

def test_parse_group_name_valid(inventory_module):
    valid_line = "[test_group]"
    group_name = inventory_module._parse_group_name(valid_line)
    assert group_name == "test_group"

def test_parse_group_name_invalid(inventory_module):
    invalid_line = "not a valid group name"
    with pytest.raises(Exception, match=r"Expected group name, got: .*"):
        inventory_module._parse_group_name(invalid_line)
