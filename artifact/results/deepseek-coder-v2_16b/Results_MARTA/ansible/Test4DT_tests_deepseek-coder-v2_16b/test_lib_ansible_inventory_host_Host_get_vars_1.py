
import pytest
from ansible.inventory.host import Host

# Test for valid input scenario
def test_valid_input():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert 'ansible_port' in host.vars
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test for edge case scenario with None initialization parameters
def test_edge_case():
    host = Host()
    assert host.name is None
    assert host.address is None
    assert not hasattr(host, 'vars')
    assert not hasattr(host, '_uuid')

# Test for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        Host(name=123, port='invalid_port')
    with pytest.raises(ValueError):
        Host(name='exampleHost', port=-1)
