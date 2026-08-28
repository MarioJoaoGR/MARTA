
import pytest
from ansible.inventory.host import Host

# Test creating a new Host instance with only its name
def test_create_host_with_name():
    host = Host(name='example_host')
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert 'ansible_port' not in host.vars
    assert host._uuid is not None  # UUID should be generated

# Test creating a Host instance with name and port
def test_create_host_with_name_and_port():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert host.vars['ansible_port'] == 22
    assert host._uuid is not None  # UUID should be generated

# Test setting an additional variable on the host
def test_set_variable():
    host = Host(name='example_host')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test removing a group from the host that exists
def test_remove_group_existing():
    # Assuming there is an existing group to remove
    host = Host(name='example_host')
    group = "webservers"  # Example group name
    host.groups.append(group)