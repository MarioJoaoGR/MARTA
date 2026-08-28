
import pytest
from ansible.inventory.host import Host

def test_valid_init():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22

def test_invalid_port_value():
    with pytest.raises(ValueError):
        host = Host(name='exampleHost', port='invalid')
