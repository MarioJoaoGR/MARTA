
import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import Mock

def test_initialization():
    inventory = Mock()
    variable_manager = Mock()
    loader = Mock()
    
    hostvars = HostVars(inventory, variable_manager, loader)
    
    assert hostvars._inventory == inventory
    assert hostvars._variable_manager == variable_manager
    assert hostvars._loader == loader
    assert hostvars._variable_manager._hostvars is hostvars
