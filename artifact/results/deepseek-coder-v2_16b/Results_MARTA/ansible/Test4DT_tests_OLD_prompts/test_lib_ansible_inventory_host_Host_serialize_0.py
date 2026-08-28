
import pytest
from ansible.inventory.host import Host

def test_init_with_name():
    host = Host(name='exampleHost')
    assert host.name == 'exampleHost'

def test_init_with_name_and_port():
    host = Host(name='exampleHost', port=22)
    assert host.vars['ansible_port'] == 22

def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

def test_init_with_uuid():
    host = Host(name='exampleHost', gen_uuid=True)
    assert host._uuid is not None

def test_serialize():
    host = Host(name='exampleHost')
    serialized_host = host.serialize()
    assert isinstance(serialized_host, dict)
    assert serialized_host['name'] == 'exampleHost'

