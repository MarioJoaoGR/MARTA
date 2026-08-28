
import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleOptionsError



def test_invalid_pattern():
    my_loader = MagicMock()
    manager = InventoryManager(loader=my_loader, sources=['source1', 'source2'], parse=True)
    
    with patch('ansible.inventory.manager.InventoryData') as mock_inventory:
        hosts = manager.get_hosts('invalidpattern')
        
        assert isinstance(hosts, list), "Expected a list of hosts"
        assert len(hosts) == 0, "No hosts should match the invalid pattern"