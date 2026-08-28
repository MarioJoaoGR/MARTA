
import pytest
from unittest.mock import patch
from ansible.inventory.data import InventoryData, AnsibleError



def test_remove_group():
    inventory = InventoryData()
    inventory.add_group('webservers')
    with patch('ansible.inventory.data.display.debug') as mock_debug:
        inventory.remove_group('webservers')
        assert 'webservers' not in inventory.groups, "Expected group to be removed"