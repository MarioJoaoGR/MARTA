
import pytest
from ansible.inventory.host import Host

# Test cases for Host class initialization and method calls

def test_init_basic():
    host = Host(name='example_host')
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert 'ansible_port' not in host.vars
    assert host._uuid is None or isinstance(host._uuid, str)  # Allow for UUID to be either None or a string

def test_init_with_port():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert host.vars['ansible_port'] == 22
    assert host._uuid is None or isinstance(host._uuid, str)  # Allow for UUID to be either None or a string

def test_init_without_uuid():
    host = Host(name='example_host', gen_uuid=False)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert host._uuid is None

def test_set_variable():
    host = Host(name='example_host')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

def test_init_with_port_and_set_variable():
    host = Host(name='example_host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'
    assert host.vars['ansible_port'] == 22

def test_hash():
    host1 = Host(name='example_host')
    host2 = Host(name='example_host')
    assert hash(host1) == hash(host2)

# New test case to cover the uncovered line (49)
def test_hash_method():
    host = Host(name='test_host')
    expected_hash = hash('test_host')  # Using Python's built-in hash function as a reference
    assert host.__hash__() == expected_hash
