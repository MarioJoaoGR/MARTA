# Module: ansible.inventory.host
import pytest
from ansible.inventory.host import Host

# Test creating a Host instance with default values
def test_host_creation_with_default_values():
    host = Host(name='example_host')
    assert host.name == 'example_host'
    assert host._uuid is not None  # Check that UUID was generated

# Test creating a Host instance with specified port
def test_host_creation_with_specified_port():
    host = Host(name='example_host', port=22)
    assert host.vars['ansible_port'] == 22

# Test setting a custom variable on the host
def test_set_custom_variable():
    host = Host(name='example_host')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test comparing two Host instances (UUIDs)
def test_compare_hosts_by_uuid():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='another_host', port=22, gen_uuid=False)
    assert not host1 == host2  # UUIDs are different

# Test creating a Host instance with generation of UUID disabled
def test_host_creation_with_no_uuid():
    host = Host(name='example_host', port=22, gen_uuid=False)
    assert host._uuid is None  # Check that UUID was not generated

# Test deserializing a Host instance from data
def test_deserialize_host():
    data = {
        'name': 'example_host',
        'vars': {'ansible_port': 22},
        'groups': [],
        '_uuid': 'some_unique_id'
    }
    host = Host()
    host.deserialize(data)
    assert host.name == 'example_host'
    assert host.vars['ansible_port'] == 22

if __name__ == "__main__":
    pytest.main()
