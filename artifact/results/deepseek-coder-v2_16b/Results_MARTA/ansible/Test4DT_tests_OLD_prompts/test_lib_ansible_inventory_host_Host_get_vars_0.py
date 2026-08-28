
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host



def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert 'ansible_user' in host.vars, "Variable ansible_user should be set in vars dictionary"
    assert host.vars['ansible_user'] == 'admin', "Variable value should match the provided value"

def test_get_magic_vars():
    host = Host(name='exampleHost')
    magic_vars = host.get_magic_vars()
    assert 'inventory_hostname' in magic_vars, "Magic variable inventory_hostname should be present"
    assert magic_vars['inventory_hostname'] == 'exampleHost', "Inventory hostname should match the provided name"

def test_get_vars():
    host = Host(name='exampleHost')
    combined_vars = host.get_vars()
    assert 'inventory_hostname' in combined_vars, "Combined vars should include inventory_hostname"
    assert combined_vars['inventory_hostname'] == 'exampleHost', "Inventory hostname should match the provided name"