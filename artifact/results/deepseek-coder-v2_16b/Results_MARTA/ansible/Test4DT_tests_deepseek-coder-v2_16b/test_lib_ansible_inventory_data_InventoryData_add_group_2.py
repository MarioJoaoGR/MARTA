
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

# Test adding a valid group to the inventory
def test_valid_input():
    inventory = InventoryData()
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding a group with empty string as input
def test_edge_case():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_group('')

# Test adding a group with invalid type input
def test_invalid_input():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_group(123)  # Invalid type, should raise AnsibleError
