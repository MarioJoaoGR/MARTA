
import pytest
from ansible.inventory.host import Host




def test_set_variable():
    host = Host(name='exampleHost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

def test_serialize():
    host = Host(name='exampleHost', port=22)
    serialized_host = host.serialize()
    assert isinstance(serialized_host, dict)
    assert serialized_host['name'] == 'exampleHost'
    assert serialized_host['address'] == 'exampleHost'
    assert serialized_host['vars']['ansible_port'] == 22
