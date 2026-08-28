
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleOptionsError

# Fixture to create an instance of InventoryManager for testing
@pytest.fixture(scope="module")
def inventory_manager():
    loader = None  # Assuming a pre-defined loader object is available
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    return manager

# Test for invalid input error handling in get_hosts method
def test_invalid_input_error_handling(inventory_manager):
    pattern = "webserver"
    ignore_limits = False
    ignore_restrictions = False
    order = 'unsupported_order'
    
    with pytest.raises(AnsibleOptionsError):
        inventory_manager.get_hosts(pattern, ignore_limits, ignore_restrictions, order)
