
import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleError



def test_none_restriction():
    mock_loader = MagicMock()
    
    with patch('ansible.inventory.manager.InventoryManager', return_value=MagicMock()):
        manager = InventoryManager(loader=mock_loader, sources=['source1'], parse=True)
        
        # Case 3: No restriction (None)
        manager.restrict_to_hosts(None)
        assert manager._restriction is None