
import pytest
from lib.ansible.inventory.host import Host



def test_init_with_generate_uuid():
    host = Host(name='exampleHost', gen_uuid=True)
    assert isinstance(host._uuid, str)
    assert host.name == 'exampleHost'
    assert 'ansible_port' not in host.vars

def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

