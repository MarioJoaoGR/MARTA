
import pytest
from ansible.inventory.host import Host

# Test case for initializing a Host instance without raising an error
def test_init_host():
    host = Host(name='testHost', port=22)
    assert host.name == 'testHost'
    assert host.vars['ansible_port'] == 22

# Test case for initializing a Host instance with UUID generation disabled
def test_init_host_no_uuid():
    host = Host(name='testHost', port=22, gen_uuid=False)
    assert host._uuid is None

# Test case for setting a variable in the Host instance
def test_set_variable():
    host = Host(name='testHost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test case for creating a Host instance with specific name and port
def test_init_host_specific():
    host = Host(name='specificHost', port=80)
    assert host.name == 'specificHost'
    assert host.vars['ansible_port'] == 80

# Test case for checking inequality between two Host instances
def test_ne_operator():
    host1 = Host(name='host1', port=22)
    host2 = Host(name='host2', port=22)
    assert host1 != host2
