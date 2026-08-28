
import pytest
from ansible.inventory.host import Host

# Test Scenario 1: Test standard input for Host.set_variable method
def test_valid_input():
    host = Host(name='exampleHost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'
    assert host.vars['ansible_port'] == 22

# Test Scenario 2: Test edge cases for Host.set_variable method with None, empty lists, and boundary values
def test_edge_case():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', None)
    assert host.vars['ansible_user'] is None
    
    host.set_variable('ansible_port', 0)
    assert host.vars['ansible_port'] == 0

# Test Scenario 3: Test invalid inputs and error handling for Host.set_variable method
def test_invalid_input():
    host = Host(name='exampleHost')
    with pytest.raises(KeyError):
        host.set_variable('non_existent_key', 'value')
