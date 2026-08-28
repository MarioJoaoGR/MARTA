
import pytest
from your_module import InventoryData  # Replace 'your_module' with the actual module name where InventoryData is defined

# Test cases for InventoryData class methods
def test_valid_input():
    inventory = InventoryData()
    inventory.add_group('webservers')
    inventory.add_child('webservers', 'host1')
    assert 'webservers' in inventory.groups
    assert 'host1' in inventory.hosts
    inventory.remove_group('webservers')
    assert 'webservers' not in inventory.groups
    assert 'host1' not in inventory.hosts

def test_edge_case():
    inventory = InventoryData()
    with pytest.raises(KeyError):
        inventory.remove_group('nonexistent_group')

def test_invalid_input():
    with pytest.raises(TypeError):
        InventoryData().remove_group()
