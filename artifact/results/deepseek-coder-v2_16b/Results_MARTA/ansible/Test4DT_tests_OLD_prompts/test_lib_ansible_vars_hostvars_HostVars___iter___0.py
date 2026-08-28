
import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def hostvars_instance():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    
    # Set up the mock objects as needed for HostVars initialization
    inventory.hosts = ["host1", "host2"]  # Example hosts in the inventory
    hostvars = HostVars(inventory, variable_manager, loader)
    return hostvars

def test_hostvars_iteration(hostvars_instance):
    expected_hosts = ["host1", "host2"]
    actual_hosts = list(hostvars_instance)
    
    assert actual_hosts == expected_hosts
