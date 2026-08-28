
import pytest
from ansible.inventory.data import InventoryData, Host



def test_add_to_non_existing_group():
    inventory = InventoryData()
    with pytest.raises(Exception) as e:
        inventory.add_host('web1', group='nonexistent_group')
    assert str(e.value) == "Could not find group nonexistent_group in inventory"