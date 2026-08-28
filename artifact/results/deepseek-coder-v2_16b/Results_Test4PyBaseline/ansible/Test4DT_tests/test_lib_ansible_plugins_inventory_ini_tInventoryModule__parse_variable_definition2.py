
# Module: ansible.plugins.inventory.ini
# test_inventory_module.py
from ansible.plugins.inventory.ini import InventoryModule
import pytest

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_variable_definition_valid(inventory_module):
    line = "key=value"
    key, value = inventory_module._parse_variable_definition(line)
    assert key == "key"
    assert value == "value"

def test_parse_variable_definition_invalid(inventory_module):
    with pytest.raises(Exception) as e:
        line = "noequal"
        inventory_module._parse_variable_definition(line)