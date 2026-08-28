
import pytest
from ansible.vars.hostvars import HostVars

# Test scenarios
def test_valid_input():
    inventory = {'hosts': ['host1', 'host2', 'host3']}
    hostvars = HostVars(inventory, None, None)
    assert len(hostvars) == 3

def test_edge_case():
    inventory = {'hosts': []}
    hostvars = HostVars(inventory, None, None)
    assert len(hostvars) == 0

def test_invalid_input():
    with pytest.raises(TypeError):
        inventory = None
        hostvars = HostVars(inventory, None, None)
