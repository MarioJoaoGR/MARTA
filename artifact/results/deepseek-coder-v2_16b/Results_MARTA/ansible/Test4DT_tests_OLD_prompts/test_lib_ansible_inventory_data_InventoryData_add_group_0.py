
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.data import InventoryData, Group
from ansible.errors import AnsibleError




def test_add_invalid_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_group(None)

def test_add_child_to_nonexistent_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('nonexistent_group', 'host1')