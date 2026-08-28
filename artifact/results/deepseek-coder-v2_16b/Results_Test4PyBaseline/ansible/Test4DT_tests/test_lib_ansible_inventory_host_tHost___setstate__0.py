# Module: ansible.inventory.host
import pytest
from ansible.inventory.host import Host

# Test initialization with name and port
def test_host_initialization():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert host.vars['ansible_port'] == 22

# Test setting a variable on the host
def test_set_variable():
    host = Host(name='example_host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test comparing two hosts with different UUIDs
def test_compare_hosts():
    host1 = Host(name='example_host', port=22)
    host2 = Host('another.com', port=22, gen_uuid=False)
    assert host1._uuid != host2._uuid  # UUIDs will be different in this example
    assert not (host1 == host2)

# Test deserialization of the host state
def test_deserialize():
    data = {'name': 'example_host', 'vars': {'ansible_port': 22}, 'address': 'example_host'}
    host = Host(name='example_host', port=22)
    assert host.__setstate__(data) == host.deserialize(data)

# Test adding a group to the host
def test_add_group():
    host = Host(name='example_host', port=22)
    host.groups.append("webservers")
    assert "webservers" in host.groups

if __name__ == "__main__":
    pytest.main()
