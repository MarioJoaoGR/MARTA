
# Module: ansible.inventory.host
import pytest
from ansible.inventory.host import Host

# Test initialization with only the required parameter 'name'
def test_init_with_only_name():
    host = Host(name='example-host')
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert host._uuid is not None  # UUID should be generated automatically
    assert 'ansible_port' not in host.vars

# Test initialization with both 'name' and 'port' parameters
def test_init_with_name_and_port():
    host = Host(name='example-host', port=22)
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert host._uuid is not None  # UUID should be generated automatically
    assert host.vars['ansible_port'] == 22

# Test initialization without generating a new UUID
def test_init_without_gen_uuid():
    host = Host(name='example-host', gen_uuid=False)
    assert host.name == 'example-host'
    assert host.address == 'example-host'
    assert host._uuid is None  # UUID should not be generated if gen_uuid is False
    assert 'ansible_port' not in host.vars

# Test setting an additional variable on the host
def test_set_variable():
    host = Host(name='example-host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

# Test getting the name of the host
def test_get_name():
    host = Host(name='example-host')
    assert host.get_name() == 'example-host'

# Additional test case to cover uncovered line (103) directly
def test_get_name_method():
    host = Host(name='example-host')
    assert host.get_name() == 'example-host'  # Ensure the method returns the correct name
