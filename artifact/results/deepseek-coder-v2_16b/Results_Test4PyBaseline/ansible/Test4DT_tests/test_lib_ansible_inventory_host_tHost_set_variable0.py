
import pytest
from ansible.inventory.host import Host
from collections.abc import MutableMapping, Mapping

# Helper function to simulate combining variables
def combine_vars(var1, var2):
    combined = var1.copy()
    for key, value in var2.items():
        if isinstance(value, dict) and key in combined:
            combined[key] = combine_vars(combined[key], value)
        else:
            combined[key] = value
    return combined

# Test cases for Host class initialization
def test_host_initialization():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert hasattr(host, 'vars') and isinstance(host.vars, dict)
    assert hasattr(host, 'groups') and isinstance(host.groups, list)
    assert host._uuid is not None
    assert 'ansible_port' in host.vars
    assert host.vars['ansible_port'] == 22

# Test cases for Host initialization with specific port and no UUID generation
def test_host_initialization_with_specific_port():
    host = Host(name='specific_host', port=80, gen_uuid=False)
    assert host.name == 'specific_host'
    assert host.address == 'specific_host'
    assert hasattr(host, 'vars') and isinstance(host.vars, dict)
    assert hasattr(host, 'groups') and isinstance(host.groups, list)
    assert host._uuid is None
    assert 'ansible_port' in host.vars
    assert host.vars['ansible_port'] == 80

# Test cases for Host initialization with custom variables
def test_host_initialization_with_custom_variables():
    host = Host(name='custom_host', port=443)
    assert host.name == 'custom_host'
    assert host.address == 'custom_host'
    assert hasattr(host, 'vars') and isinstance(host.vars, dict)
    assert hasattr(host, 'groups') and isinstance(host.groups, list)
    assert host._uuid is not None
    assert 'ansible_port' in host.vars
    assert host.vars['ansible_port'] == 443
    host.set_variable('ansible_user', 'admin')
    assert 'ansible_user' in host.vars
    assert host.vars['ansible_user'] == 'admin'

# Test cases for Host initialization with group management
def test_host_initialization_with_group_management():
    from ansible.inventory.group import Group
    group = Group("webservers")
    host = Host(name='webserver1', port=80, gen_uuid=True)
    group.add_host(host)
    assert len(group.hosts) == 1
    assert 'webserver1' in group.hosts

# Test cases for Host initialization from deserialized data
def test_host_initialization_from_deserialized_data():
    data = {
        'name': 'deserialized_host',
        'vars': {'ansible_user': 'root'},
        'groups': ['all']
    }
    host = Host(name=data['name'], port=None, gen_uuid=True)
    for key, value in data['vars'].items():
        host.set_variable(key, value)
    assert host.name == 'deserialized_host'
    assert host.address == 'deserialized_host'
    assert hasattr(host, 'vars') and isinstance(host.vars, dict)
    assert hasattr(host, 'groups') and isinstance(host.groups, list)
    assert host._uuid is not None
    assert 'ansible_user' in host.vars
    assert host.vars['ansible_user'] == 'root'

# Test cases for set_variable method
def test_set_variable():
    host = Host(name='test_host', port=22)
    host.set_variable('new_var', 'value')
    assert 'new_var' in host.vars
    assert host.vars['new_var'] == 'value'
    host.set_variable('existing_var', {'nested': 'value'})
    assert 'existing_var' in host.vars
    assert host.vars['existing_var'] == {'nested': 'value'}
