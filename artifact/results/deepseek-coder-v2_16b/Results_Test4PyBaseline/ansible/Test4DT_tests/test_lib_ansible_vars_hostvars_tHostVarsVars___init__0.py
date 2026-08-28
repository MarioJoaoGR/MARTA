# Module: ansible.vars.hostvars
import pytest
from ansible.vars import HostVarsVars
from ansible.parsing.dataloader import DataLoader

# Fixture to create a sample HostVarsVars instance for testing
@pytest.fixture
def host_vars():
    variables = {'host1': {'key1': 'value1'}, 'host2': {'key2': 'value2'}}
    loader = DataLoader()
    return HostVarsVars(variables, loader)

# Test case to check if the instance is created correctly
def test_host_vars_instance():
    variables = {'host1': {'key1': 'value1'}, 'host2': {'key2': 'value2'}}
    loader = DataLoader()
    host_vars = HostVarsVars(variables, loader)
    assert isinstance(host_vars, HostVarsVars)

# Test case to check if the instance has the correct variables for a given host
def test_get_host_variables(host_vars):
    assert 'key1' in host_vars['host1']
    assert host_vars['host1']['key1'] == 'value1'
    assert 'key2' in host_vars['host2']
    assert host_vars['host2']['key2'] == 'value2'

# Test case to check if the instance returns undefined object for an undefined host
def test_undefined_host():
    variables = {'host1': {'key1': 'value1'}}
    loader = DataLoader()
    host_vars = HostVarsVars(variables, loader)
    assert not hasattr(host_vars['host2'], '_vars')
    assert not hasattr(host_vars['host2'], '_loader')

# Test case to check the number of hosts in the instance
def test_number_of_hosts(host_vars):
    assert len(host_vars) == 2

# Test case to set a nonpersistent fact for a host and check if it is set correctly
def test_set_nonpersistent_fact(host_vars):
    host_vars.set_nonpersistent_facts('host1', {'new_fact': 'new_value'})
    assert 'new_fact' in host_vars['host1']
    assert host_vars['host1']['new_fact'] == 'new_value'
