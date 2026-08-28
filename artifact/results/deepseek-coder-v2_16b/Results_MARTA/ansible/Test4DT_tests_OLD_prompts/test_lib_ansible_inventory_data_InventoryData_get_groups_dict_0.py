
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

# Test for adding a group and then adding a child (host) to it
def test_valid_input_get_groups_dict():
    inventory = InventoryData()
    # Add a group for testing
    inventory.add_group('webservers')
    # Add a host to the group
    with pytest.raises(AnsibleError):
        inventory.add_child('webservers', 'host1')
