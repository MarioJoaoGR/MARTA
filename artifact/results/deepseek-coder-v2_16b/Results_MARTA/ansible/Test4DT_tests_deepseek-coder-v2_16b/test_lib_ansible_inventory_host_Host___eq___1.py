
import pytest
from ansible.inventory.host import Host

# Test valid case scenario
def test_valid_case():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test edge case scenario with None arguments
def test_edge_case_none():
    host = Host(name=None, port=None, gen_uuid=False)
    assert host.name is None
    assert host.vars == {}
    assert host._uuid is None

# Test invalid input scenario with incorrect argument types
def test_invalid_input():
    with pytest.raises(TypeError):
        Host(name='exampleHost', port='invalid_port')
