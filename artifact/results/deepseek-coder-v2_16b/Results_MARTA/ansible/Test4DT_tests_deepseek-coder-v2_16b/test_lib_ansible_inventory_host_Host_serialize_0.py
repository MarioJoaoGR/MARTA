
import pytest
from ansible.inventory.host import Host

def test_init_with_name():
    host = Host(name='exampleHost')
    assert hasattr(host, 'name'), "Host should have a name attribute"
    assert host.name == 'exampleHost', f"Expected host name to be 'exampleHost' but got {host.name}"

def test_init_with_port():
    host = Host(name='exampleHost', port=22)
    assert hasattr(host, 'vars'), "Host should have a vars attribute"
    assert host.vars['ansible_port'] == 22, f"Expected ansible_port to be 22 but got {host.vars['ansible_port']}"

def test_init_with_uuid():
    host = Host(name='exampleHost', gen_uuid=True)
    assert hasattr(host, '_uuid'), "Host should have a _uuid attribute"
    assert isinstance(host._uuid, str), f"_uuid should be a string but got {type(host._uuid)}"

def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert 'ansible_user' in host.vars, "Expected ansible_user to be set in vars"
    assert host.vars['ansible_user'] == 'admin', f"Expected ansible_user to be 'admin' but got {host.vars['ansible_user']}"

def test_serialize():
    host = Host(name='exampleHost')
    serialized_host = host.serialize()
    assert isinstance(serialized_host, dict), "Expected serialize method to return a dictionary"
    assert serialized_host['name'] == 'exampleHost', f"Expected name in serialized host to be 'exampleHost' but got {serialized_host['name']}"
