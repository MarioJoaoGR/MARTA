
import pytest
from lib.ansible.inventory.host import Host
from lib.ansible.inventory.group import Group

# Test 1: Creating a Host Instance with Default Parameters

# Test 2: Creating a Host Instance with Specified Port and UUID
def test_host_creation_with_specified_port_and_uuid():
    host = Host(name='exampleHost', port=22, gen_uuid=True)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host._uuid is not None, "Expected _uuid to be generated"

# Test 3: Setting Variables for the Host
def test_host_setting_variables():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert 'ansible_user' in host.vars, "Expected ansible_user to be set"
    assert host.vars['ansible_user'] == 'admin', "Expected ansible_user value to be 'admin'"

# Test 4: Adding a Group to the Host

# Test 5: Removing a Group from the Host
def test_host_removing_group():
    host = Host(name='exampleHost')
    group1 = Group(name="webservers")
    host.add_group(group1)
    host.remove_group(group1)
    assert "webservers" not in host.groups, "Expected webservers to be removed from the host's groups"