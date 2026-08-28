
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.data import InventoryData

@pytest.fixture(scope="function")
def inventory():
    return InventoryData()

def test_add_group(inventory):
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

