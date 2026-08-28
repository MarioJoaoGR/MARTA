
import pytest
from ansible.inventory.host import Host

# Test case 1: Creating a Host instance without specifying a port (the name will be used as the address)
def test_create_host_without_port():
    host = Host(name='example-host')
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert hasattr(host, 'ansible_port') is False
    assert hasattr(host, '_uuid') is True

# Test case 2: Creating a Host instance with both a name and a specified port
def test_create_host_with_port():
    host = Host(name='example-host', port=22)
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert host.vars['ansible_port'] == 22
    assert hasattr(host, '_uuid') is True

# Test case 3: Creating a Host instance with a specific UUID (since `gen_uuid` is set to False)
def test_create_host_without_generating_uuid():
    host = Host(name='example-host', gen_uuid=False)
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert hasattr(host, '_uuid') is True
    assert host._uuid is None

# Test case 4: Setting an additional variable on the created host
def test_set_variable():
    host = Host(name='example-host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test case 5: Creating a Host instance and immediately setting multiple variables (using `set_variable` method)
def test_set_multiple_variables():
    host = Host(name='example-host', port=22)
    host.set_variable('ansible_user', 'admin')
    host.set_variable('ansible_become', True)
    assert host.vars['ansible_user'] == 'admin'