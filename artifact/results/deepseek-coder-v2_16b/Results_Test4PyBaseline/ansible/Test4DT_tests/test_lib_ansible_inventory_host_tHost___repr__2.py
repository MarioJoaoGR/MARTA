
import pytest
from ansible.inventory.host import Host

# Test creating a Host instance with only the required parameter 'name'
def test_create_host_with_only_required_parameter():
    host = Host(name='example-host')
    assert host.name == 'example-host', "Expected name to be 'example-host'"
    assert host.address == 'example-host', "Expected address to be 'example-host'"
    assert not hasattr(host, 'port'), "Expected no port attribute"
    assert '_uuid' in host.__dict__, "_uuid should be generated automatically"
    assert host.implicit is False, "Expected implicit to be False"

# Test creating a Host instance with both 'name' and 'port' parameters
def test_create_host_with_both_parameters():
    host = Host(name='example-host', port=22)
    assert host.name == 'example-host', "Expected name to be 'example-host'"
    assert host.address == 'example-host', "Expected address to be 'example-host'"
    assert host.vars['ansible_port'] == 22, "Expected ansible_port to be set"
    assert '_uuid' in host.__dict__, "_uuid should be generated automatically"
    assert host.implicit is False, "Expected implicit to be False"

# Test creating a Host instance without generating a new UUID (UUID will be generated automatically)
def test_create_host_without_generating_uuid():
    host = Host(name='example-host', gen_uuid=False)
    assert host.name == 'example-host', "Expected name to be 'example-host'"
    assert host.address == 'example-host', "Expected address to be 'example-host'"