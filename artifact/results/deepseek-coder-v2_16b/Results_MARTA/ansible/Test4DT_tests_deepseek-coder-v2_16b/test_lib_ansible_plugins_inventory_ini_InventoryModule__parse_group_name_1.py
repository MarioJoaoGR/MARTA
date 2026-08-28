
import pytest
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture(scope="module")
def inventory_module():
    return InventoryModule()

# Test Scenario 1: Valid Case
def test_valid_case(inventory_module):
    line = "[groupname]"
    group_name = inventory_module._parse_group_name(line)
    assert group_name == "groupname"

# Test Scenario 2: Edge Case
def test_edge_case(inventory_module):
    line = None
    with pytest.raises(Exception) as e_info:
        inventory_module._parse_group_name(line)
    assert str(e_info.value) == "Expected group name, got: None"

# Test Scenario 3: Error Case
def test_error_case(inventory_module):
    line = "[invalid-group-name]"
    with pytest.raises(Exception) as e_info:
        inventory_module._parse_group_name(line)
    assert str(e_info.value) == "Expected group name, got: [invalid-group-name]"
