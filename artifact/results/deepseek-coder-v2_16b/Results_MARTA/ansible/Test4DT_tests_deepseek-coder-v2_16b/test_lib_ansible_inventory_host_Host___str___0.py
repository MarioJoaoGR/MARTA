
import pytest
from ansible.inventory.host import Host

def test_valid_creation():
    host = Host(name='exampleHost', port=22, gen_uuid=True)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Host(name=123, port='string', gen_uuid=True)

def test_setting_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'
