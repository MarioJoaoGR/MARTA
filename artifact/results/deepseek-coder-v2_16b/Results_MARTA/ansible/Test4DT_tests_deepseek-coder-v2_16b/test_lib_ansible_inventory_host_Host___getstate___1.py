
import pytest
from ansible.inventory.host import Host

def test_host_initialization():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host.vars['ansible_port'] == 22

def test_host_without_uuid():
    host = Host(name='exampleHost', port=22, gen_uuid=False)
    assert host._uuid is None

def test_host_serialization():
    host = Host(name='exampleHost', port=22)
    serialized_host = host.serialize()
    assert isinstance(serialized_host, dict)
    assert 'name' in serialized_host
    assert serialized_host['name'] == 'exampleHost'
    assert 'address' in serialized_host
    assert serialized_host['address'] == 'exampleHost'
    assert 'vars' in serialized_host
    assert serialized_host['vars']['ansible_port'] == 22
    assert '_uuid' not in serialized_host

def test_host_set_variable():
    host = Host(name='exampleHost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

def test_host_getstate():
    host = Host(name='exampleHost', port=22)
    serialized_host = host.__getstate__()
    assert isinstance(serialized_host, dict)
    assert 'name' in serialized_host
    assert serialized_host['name'] == 'exampleHost'
    assert 'address' in serialized_host
    assert serialized_host['address'] == 'exampleHost'
    assert 'vars' in serialized_host
    assert serialized_host['vars']['ansible_port'] == 22
    assert '_uuid' not in serialized_host
