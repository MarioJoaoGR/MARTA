
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory():
    return InventoryData()

# Test adding a valid group to the inventory
def test_valid_input(inventory):
    result = inventory.add_group('webservers')
    assert result == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding an empty string as a group name
def test_edge_case(inventory):
    with pytest.raises(Exception) as e:
        inventory.add_group('')
    assert str(e.value) == "Invalid empty/false group name provided: None"

# Test adding a None type as a group name
def test_invalid_input(inventory):
    with pytest.raises(Exception) as e:
        inventory.add_group(None)
    assert str(e.value) == "Invalid empty/false group name provided: None"
