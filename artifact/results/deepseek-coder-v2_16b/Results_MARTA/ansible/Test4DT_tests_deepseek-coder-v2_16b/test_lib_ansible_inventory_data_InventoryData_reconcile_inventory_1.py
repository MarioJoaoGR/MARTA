
import pytest
from ansible.inventory.data import InventoryData

# Test fixture to create an instance of InventoryData for each test
@pytest.fixture(scope="module")
def inventory_minimal():
    return InventoryData()

# Test case to check invalid group addition raises Exception
def test_invalid_group_addition(inventory_minimal):
    with pytest.raises(Exception):
        inventory_minimal.add_child('nonexistent_group', 'host1')
