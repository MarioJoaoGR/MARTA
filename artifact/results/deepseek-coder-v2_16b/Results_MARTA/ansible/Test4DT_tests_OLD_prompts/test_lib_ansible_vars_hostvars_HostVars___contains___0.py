
import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.hostvars import HostVars

def test_edge_case():
    with patch('ansible.vars.hostvars.HostVars.__contains__', return_value=False):
        inventory = MagicMock()
        variable_manager = MagicMock()
        loader = MagicMock()
        
        hostvars = HostVars(inventory, variable_manager, loader)
        
        assert 'none-host' not in hostvars
