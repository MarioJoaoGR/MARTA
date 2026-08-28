
import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    hostvars = HostVars(inventory, variable_manager, loader)
    return hostvars, inventory, variable_manager, loader

def test_hostvars_initialization(setup_hostvars):
    hostvars, _, _, _ = setup_hostvars
    assert hasattr(hostvars, '_inventory')
    assert hasattr(hostvars, '_loader')
    assert hasattr(hostvars, '_variable_manager')
    assert hostvars._variable_manager._hostvars is hostvars



def test_contains(setup_hostvars):
    hostvars, inventory, _, _ = setup_hostvars
    host_name = 'existing-host'
    host = MagicMock()
    inventory.get_host.return_value = host
    
    assert host_name in hostvars