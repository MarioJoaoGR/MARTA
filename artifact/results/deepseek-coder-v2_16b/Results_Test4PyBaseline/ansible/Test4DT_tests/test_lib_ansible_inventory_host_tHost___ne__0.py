
import pytest
from ansible.inventory.host import Host

# Test creating a Host instance with name and port
def test_host_creation_with_name_and_port():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.vars['ansible_port'] == 22
    assert host._uuid is not None

# Test creating a Host instance without name but with port
def test_host_creation_without_name():
    with pytest.raises(TypeError):
        Host(port=22)

# Test setting a custom variable on the host
def test_set_variable():
    host = Host(name='example_host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test comparing two hosts based on UUID
def test_compare_hosts():
    host1 = Host(name='host1', port=22)
    host2 = Host('host2', port=22, gen_uuid=False)
    assert not (host1 == host2)
    assert host1 != host2

# Test comparing hosts with the same UUID
def test_compare_hosts_same_uuid():
    host1 = Host(name='host1', port=22)
    host2 = Host('host2', port=22, gen_uuid=False)
    assert not (host1 == host2)
    assert host1 != host2
