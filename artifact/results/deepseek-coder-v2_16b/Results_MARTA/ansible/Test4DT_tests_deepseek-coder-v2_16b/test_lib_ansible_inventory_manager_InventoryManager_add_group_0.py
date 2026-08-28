
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from unittest.mock import patch

# Test for valid input to add_group method
def test_valid_input_add_group():
    class RealLoaderClass:
        pass
    
    loader = RealLoaderClass()
    manager = InventoryManager(loader=loader, sources=['source1', 'source2'], parse=True)
    
    # Add a valid group to the inventory
    with pytest.raises(AnsibleError):
        result = manager.add_group({'name': 'example_group'})
