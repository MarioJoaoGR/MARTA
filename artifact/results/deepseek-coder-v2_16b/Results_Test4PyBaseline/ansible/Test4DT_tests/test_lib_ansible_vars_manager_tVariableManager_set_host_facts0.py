# Module: ansible.vars.manager
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from collections import defaultdict, MutableMapping
from sha import sha1
import os
from ansible.errors import AnsibleAssertionError, AnsibleError
from ansible.utils import display, to_text

# Fixture for creating a VariableManager instance with default parameters
@pytest.fixture
def variable_manager():
    loader = DataLoader()  # Create a data loader instance
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')  # Load the inventory
    return VariableManager(loader=loader, inventory=inventory)  # Initialize the VariableManager

# Test initialization with default parameters
def test_variable_manager_init():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict)
    assert isinstance(variable_manager._vars_cache, defaultdict)
    assert isinstance(variable_manager._extra_vars, defaultdict)
    assert isinstance(variable_manager._host_vars_files, defaultdict)
    assert isinstance(variable_manager._group_vars_files, defaultdict)
    assert variable_manager._inventory == inventory
    assert variable_manager._loader == loader
    assert variable_manager._omit_token is not None

# Test setting host facts with valid data
def test_set_host_facts_valid(variable_manager):
    host = 'example_host'
    facts = {'os': 'Linux', 'kernel': '3.10'}
    variable_manager.set_host_facts(host, facts)
    assert host in variable_manager._fact_cache
    assert isinstance(variable_manager._fact_cache[host], dict)
    assert variable_manager._fact_cache[host] == facts

# Test setting host facts with invalid data type
def test_set_host_facts_invalid_type():
    vm = VariableManager()
    with pytest.raises(AnsibleAssertionError):
        vm.set_host_facts('example_host', 'not a dict')

# Test setting host facts for a non-existent host
def test_set_host_facts_non_existent_host(variable_manager):
    host = 'nonexistent_host'
    facts = {'os': 'Linux', 'kernel': '3.10'}
    variable_manager.set_host_facts(host, facts)
    assert host in variable_manager._fact_cache
    assert isinstance(variable_manager._fact_cache[host], dict)
    assert variable_manager._fact_cache[host] == facts

# Test setting inventory with valid data
def test_set_inventory(variable_manager):
    new_inventory = {
        'hosts': {'host1': {}, 'host2': {}},
        'vars': {'all': {'ansible_user': 'admin'}}
    }
    variable_manager.set_inventory(new_inventory)
    assert variable_manager._inventory is not None
    assert isinstance(variable_manager._inventory, dict)
    assert new_inventory == variable_manager._inventory
