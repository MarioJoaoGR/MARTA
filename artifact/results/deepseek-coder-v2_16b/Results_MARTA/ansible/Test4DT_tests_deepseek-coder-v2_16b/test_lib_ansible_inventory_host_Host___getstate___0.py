
import pytest
from ansible.inventory.host import Host

# Test valid input scenario
def test_valid_input():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test edge case scenario with None input
def test_edge_case():
    host = Host(name=None, port=None, gen_uuid=False)
    assert host.name is None
    assert host.address is None
    assert 'ansible_port' not in host.vars
    assert host._uuid is None

# Test invalid input scenario raising ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        Host(name='exampleHost', port='invalid_port')
