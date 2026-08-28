
import pytest
from ansible.inventory.data import InventoryData, Host

def test_remove_host():
    inventory = InventoryData()
    host1 = Host('host1')
    inventory.hosts['host1'] = host1
    
    # Test removing an existing host
    inventory.remove_host(host1)
    assert 'host1' not in inventory.hosts
    assert len(inventory.hosts) == 0

def test_remove_nonexistent_host():
    inventory = InventoryData()
    
    # Test removing a None host, which should raise an AttributeError
    with pytest.raises(AttributeError):
        inventory.remove_host(None)

def test_remove_invalid_input():
    inventory = InventoryData()
    
    # Test removing a non-existent string input, which should raise an AttributeError
    with pytest.raises(AttributeError):
        inventory.remove_host('nonExistentHost')
