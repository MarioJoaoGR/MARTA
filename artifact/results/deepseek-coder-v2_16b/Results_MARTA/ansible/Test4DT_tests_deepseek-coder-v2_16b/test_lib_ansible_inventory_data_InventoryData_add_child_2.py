
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError



def test_add_child_invalid_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        success = inventory.add_child('nonexistent_group', 'host1')