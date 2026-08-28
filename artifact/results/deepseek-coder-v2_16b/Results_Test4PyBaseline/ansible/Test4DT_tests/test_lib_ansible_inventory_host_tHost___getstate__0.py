
import pytest
from ansible.inventory.host import Host

# Test initialization with default values
def test_host_initialization_with_default_values():
    host = Host(name="example_host")
    assert host.name == "example_host"
    assert host.address == "example_host"
    assert 'ansible_port' not in host.vars
    assert host._uuid is not None
    assert host.implicit is False

# Test initialization with specified port
def test_host_initialization_with_specified_port():
    host = Host(name="example_host", port=22)
    assert host.name == "example_host"
    assert host.address == "example_host"
    assert host.vars['ansible_port'] == 22
    assert host._uuid is not None
    assert host.implicit is False

# Test initialization without generating UUID
def test_host_initialization_without_generating_uuid():
    host = Host(name="example_host", gen_uuid=False)
    assert host.name == "example_host"
    assert host.address == "example_host"
    assert 'ansible_port' not in host.vars
    assert host._uuid is None
    assert host.implicit is False

# Test setting a variable on the host
def test_set_variable():
    host = Host(name="example_host", port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test serialization method
def test_serialize():
    host = Host(name="example_host", port=22)
    serialized_data = host.__getstate__()
    expected_data = {
        'name': 'example_host',
        'address': 'example_host',
        'vars': {'ansible_port': 22},
        'groups': [],
        '_uuid': host._uuid,
        'implicit': False
    }